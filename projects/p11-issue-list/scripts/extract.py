#!/usr/bin/env python3
"""p11 の 1 段目: 閉じた p1〜p9 の記録から、問題・課題の候補を 1 行 1 件で抜き出す。

読むだけ。書き出し先は teams/issues/work/ だけ。
  python3 projects/p11-issue-list/scripts/extract.py

出力:
  work/extract.tsv  1 行 1 件（id・プロジェクト・材料・節・参照元 file:line・hash・events の行・送り手・本文）
  work/counts.tsv   材料ごと（ファイルごと）の抜いた件数と、0 件ならその理由
  work/counts.md    counts.tsv を読み物にしたもの（材料の種類ごとの小計つき）
"""
import csv
import datetime as dt
import glob
import hashlib
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.dirname(HERE)  # projects/p11-issue-list
AO = os.path.dirname(os.path.dirname(P))  # ai-org
PROJECTS = os.path.join(AO, "projects")
WORK = os.path.join(P, "teams", "issues", "work")
JOB_README_VERSION = ""
JOB_README = "/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/README.md"

# 材料にするプロジェクト（閉じているもの。p10 は読まない）
PROJ_RE = re.compile(r"^p[1-9]-")

# 1 行報告で本文を抜く種類（pack の 4 種に、根っこの見張りの促し nudge を足す）
EVENT_KINDS = {"review_ng", "rework", "blocked", "escalate", "nudge"}

# msgs の節の見出しで抜くもの
# A: うまくいかなかったこと系（材料の指定どおり）
SEC_A = re.compile(r"うまくいかなかった|試走で|試走として|気づき|気づいた|食い違|unclear")
# B: 残ったこと・申し送り・上げること系（網羅のため候補として抜く。まとめで問題かどうかを決める）
SEC_B = re.compile(r"残る不明点|残ること|残った|申し送り|〔仮〕|上げること|未確認")
# 地の文の札（見出しでない行の先頭）。札だけの行なら続く箇条書き、札のあとに本文があればその本文と続く箇条書き
INLINE_RE = re.compile(r"^(?:\*\*)?(申し送り|うまくいかなかったこと|残る不明点)([^:：]*?)(?:\*\*)?\s*[:：]?\s*(.*)$")

HEAD_RE = re.compile(r"^(#{1,6})\s+(.*)$")
ITEM_RE = re.compile(r"^(?:[-*]|\d+[.)])\s+")


def rel(path):
    """ai-org の root からの相対パス（job の README は job からの相対に印をつける）"""
    if path.startswith(AO + "/"):
        return path[len(AO) + 1:]
    if path.startswith("/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/"):
        return "job:" + path[len("/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/"):]
    return path


def clean(s):
    s = s.strip()
    s = re.sub(r"\s+", " ", s)
    return s.replace("\t", " ")


def unquote(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        s = s[1:-1].replace('\\"', '"')
    return s


def split_items(lines, start_lineno):
    """md の本文の行（見出しの下）を、上の階層の箇条書き 1 つ＝1 件、地の文の段落 1 つ＝1 件に分ける。
    子の箇条書き・続きの行は親に足す。返り値は (行番号, 本文) のリスト。"""
    items = []
    cur = None
    for i, raw in enumerate(lines):
        ln = start_lineno + i
        line = raw.rstrip("\n")
        if not line.strip():
            if cur and not cur[2]:  # 段落は空行で切る（箇条書きは子が続くことがあるので切らない）
                items.append(cur)
                cur = None
            continue
        if line.lstrip().startswith("<!--") or line.strip().startswith("[↑"):
            continue
        top = (not line.startswith((" ", "\t"))) and ITEM_RE.match(line)
        if top:
            if cur:
                items.append(cur)
            cur = [ln, ITEM_RE.sub("", line, count=1), True]
        else:
            if cur is None:
                cur = [ln, line.strip(), False]
            else:
                cur[1] += " " + line.strip()
    if cur:
        items.append(cur)
    return [(a, clean(b)) for a, b, _ in items if clean(b)]


def inline_blocks(lines):
    """地の文の札で始まる塊を拾う。返り値は (行番号, 札, 本文)。
    札の行に本文があれば 1 件、続く箇条書き（空行か見出しまで）は 1 つ 1 件。"""
    out = []
    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")
        m = INLINE_RE.match(line) if not HEAD_RE.match(line) else None
        if not m:
            i += 1
            continue
        label = (m.group(1) + m.group(2)).strip()
        rest = m.group(3).strip()
        # 札の続き（「（軽微。直さなくてよい）」「の 2 つ:」のように、中身でなく札の言い足しだけのもの）は札に寄せる
        if re.match(r"^（[^）]*）\s*[:：]?$", rest) or rest.endswith((":", "：")):
            label += rest.rstrip(":：")
            rest = ""
        if rest:
            out.append((i + 1, label, clean(rest)))
        j = i + 1
        block = []
        while j < len(lines) and lines[j].strip() and not HEAD_RE.match(lines[j]):
            block.append(lines[j])
            j += 1
        for ln, text in split_items(block, i + 2):
            out.append((ln, label, text))
        i = j
    return out


def sections(lines):
    """md を見出しで区切る。返り値は (見出しの行番号, 見出しの深さ, 見出し, 本文の行, 本文の最初の行番号)"""
    out = []
    heads = [(i, HEAD_RE.match(l)) for i, l in enumerate(lines)]
    heads = [(i, m) for i, m in heads if m]
    for k, (i, m) in enumerate(heads):
        depth = len(m.group(1))
        end = len(lines)
        for j, m2 in heads[k + 1:]:
            if len(m2.group(1)) <= depth:
                end = j
                break
        # 子の見出しも本文として含める（子の見出しの行は抜く対象から外す）
        body = [l if not HEAD_RE.match(l) else "" for l in lines[i + 1:end]]
        out.append((i + 1, depth, m.group(2).strip(), body, i + 2))
    return out


def load_events():
    """プロジェクトごとに events.log を読み、本文の hash → (行番号, 種類, 送り手, 宛先)"""
    ev = {}
    lines_by_proj = {}
    for d in sorted(glob.glob(os.path.join(PROJECTS, "p*"))):
        name = os.path.basename(d)
        if not PROJ_RE.match(name):
            continue
        path = os.path.join(d, "log", "events.log")
        lines_by_proj[name] = []
        with open(path, encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                parts = line.rstrip("\n").split(" ")
                if len(parts) < 5:
                    continue
                ts, h, frm, kind, to = parts[:5]
                lines_by_proj[name].append((n, ts, h, frm, kind, to))
                m = re.search(r"msg=log/msgs/([0-9a-f]+)\.md", line)
                if m:
                    ev[(name, m.group(1))] = (n, kind, frm, to)
    return ev, lines_by_proj


rows = []  # 抜いた 1 件
counts = []  # (材料, ファイル, 件数, 理由)


def add(proj, source, section, path, lineno, text, h="", evline="", frm=""):
    rows.append({
        "project": proj, "source": source, "section": section,
        "ref": f"{rel(path)}:{lineno}", "hash": h, "events_line": evline,
        "from": frm, "text": text,
    })


def do_sessions():
    files = sorted(f for f in glob.glob(os.path.join(PROJECTS, "p*", "reports", "sessions", "*.yaml"))
                   if PROJ_RE.match(f.split("/projects/")[1]))
    for path in files:
        proj = path.split("/projects/")[1].split("/")[0]
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        try:
            s = next(i for i, l in enumerate(lines) if l.startswith("self:"))
        except StopIteration:
            counts.append(("sessions", rel(path), 0, "self が無い"))
            continue
        n = 0
        empty = []
        for key in ("not_done", "unclear"):
            k = None
            for i in range(s + 1, len(lines)):
                if re.match(rf"^  {key}:", lines[i]):
                    k = i
                    break
            if k is None:
                empty.append(f"{key} の欄が無い")
                continue
            if lines[k].split(":", 1)[1].strip() == "[]":
                empty.append(f"{key}: []")
                continue
            cur = None
            for i in range(k + 1, len(lines)):
                l = lines[i].rstrip("\n")
                if re.match(r"^  \S", l) or not l.startswith("  "):
                    break
                if l.startswith("    - "):
                    if cur:
                        add(proj, "session", key, path, cur[0] + 1, clean(unquote(cur[1])), frm=os.path.basename(path))
                        n += 1
                    cur = [i, l[6:]]
                elif cur and l.strip():
                    cur[1] += " " + l.strip()
            if cur:
                add(proj, "session", key, path, cur[0] + 1, clean(unquote(cur[1])), frm=os.path.basename(path))
                n += 1
        counts.append(("sessions", rel(path), n, "・".join(empty) if n == 0 else ""))


def do_msgs(ev):
    files = sorted(f for f in glob.glob(os.path.join(PROJECTS, "p*", "log", "msgs", "*.md"))
                   if PROJ_RE.match(f.split("/projects/")[1]))
    for path in files:
        proj = path.split("/projects/")[1].split("/")[0]
        h = os.path.basename(path)[:-3]
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        evinfo = ev.get((proj, h))
        evline, kind, frm = (evinfo[0], evinfo[1], evinfo[2]) if evinfo else ("", "", "")
        if not evinfo:
            m = re.match(r"<!-- (\S+) → (\S+) (\S+)", lines[0]) if lines else None
            if m:
                frm, kind = m.group(1), m.group(3)
        n = 0
        why = []
        is_auditor = frm.endswith("/auditor")
        if kind in EVENT_KINDS:
            # 本文全体を件に分ける（見出しは外す）
            body = [l if not HEAD_RE.match(l) else "" for l in lines[1:]]
            for ln, text in split_items(body, 2):
                add(proj, f"event:{kind}", "本文", path, ln, text, h, evline, frm)
                n += 1
        elif is_auditor:
            secs = sections(lines)
            for hl, depth, title, body, bstart in secs:
                if depth != 2:
                    continue
                for ln, text in split_items(body, bstart):
                    add(proj, "auditor", title, path, ln, text, h, evline, frm)
                    n += 1
            if not secs:
                for ln, text in split_items(lines[1:], 2):
                    add(proj, "auditor", "本文", path, ln, text, h, evline, frm)
                    n += 1
        else:
            for hl, depth, title, body, bstart in sections(lines):
                if SEC_A.search(title):
                    cls = "節A"
                elif SEC_B.search(title):
                    cls = "節B"
                else:
                    continue
                # 子の見出しが同じ型なら、親の側で数えない（二重を避ける）
                for ln, text in split_items(body, bstart):
                    if any(r["ref"] == f"{rel(path)}:{ln}" for r in rows):
                        continue
                    add(proj, f"msg:{cls}", title, path, ln, text, h, evline, frm)
                    n += 1
            # 見出しでなく地の文の札（「申し送り:」「うまくいかなかったこと（…）」）で始まる塊
            for ln, label, text in inline_blocks(lines):
                if any(r["ref"] == f"{rel(path)}:{ln}" for r in rows):
                    continue
                cls = "札A" if SEC_A.search(label) else "札B"
                add(proj, f"msg:{cls}", label, path, ln, text, h, evline, frm)
                n += 1
        if n == 0:
            if kind in EVENT_KINDS:
                why.append(f"{kind} だが本文が空")
            else:
                why.append(f"種類 {kind or '不明'}・該当の節なし")
        counts.append(("msgs", rel(path), n, "・".join(why)))


def do_user_inbox():
    """log/user-inbox.yaml（見張りと orgctl が根っこ宛てに置く受け箱）。
    kind が report の項は log/msgs と同じ本文を指すので抜かない。それ以外（stuck など見張りの記録）を 1 項＝1 件"""
    files = sorted(f for f in glob.glob(os.path.join(PROJECTS, "p*", "log", "user-inbox.yaml"))
                   if PROJ_RE.match(f.split("/projects/")[1]))
    for path in files:
        proj = path.split("/projects/")[1].split("/")[0]
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        items = []
        for i, l in enumerate(lines):
            m = re.match(r'^- kind:\s*"?([^"\s]+)"?', l)
            if m:
                items.append([i + 1, m.group(1), {}])
            elif items:
                m2 = re.match(r'^  (\w+):\s*(.*)$', l)
                if m2:
                    items[-1][2][m2.group(1)] = unquote(m2.group(2))
        n = 0
        n_report = 0
        for ln, kind, kv in items:
            if kind == "report":
                n_report += 1
                continue
            text = f"[{kind}] from={kv.get('from', '')} at={kv.get('at', '')} {kv.get('summary', '')}"
            add(proj, f"user_inbox:{kind}", "受け箱", path, ln, clean(text), frm=kv.get("from", ""))
            n += 1
        why = f"report {n_report} 項だけ（log/msgs と同じ本文を指すので抜かない）" if n == 0 else (f"ほかに report {n_report} 項は抜かない（log/msgs と同じ本文）" if n_report else "")
        counts.append(("user_inbox", rel(path), n, why))
    for path in sorted(glob.glob(os.path.join(PROJECTS, "p*", "log", "notify-outbox.log"))):
        if not PROJ_RE.match(path.split("/projects/")[1]):
            continue
        with open(path, encoding="utf-8") as f:
            first = f.readline()
        m = re.search(r"（([0-9a-f]{6})）", first)
        counts.append(("notify_outbox", rel(path), 0,
                       f"根っこへの知らせの写し。本文は log/msgs/{m.group(1) if m else '?'}.md と同じなので抜かない"))


def do_audit_p9():
    path = os.path.join(PROJECTS, "p9-org-watch", "reports", "audit", "p9-org-watch.md")
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    n = 0
    for ln, text in split_items(lines, 1):
        if not re.match(r"^\*\*", text):
            continue  # 範囲の段落は外す（件は太字の題で始まる番号つきの項）
        add("p9-org-watch", "audit", "監査", path, ln, text, frm="p9-org-watch/auditor")
        n += 1
    counts.append(("audit", rel(path), n, ""))


def do_job_readme():
    path = JOB_README
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    n = 0
    skipped = []
    for hl, depth, title, body, bstart in sections(lines):
        if "組織の直し待ち" in title:
            for ln, text in split_items(body, bstart):
                if ITEM_RE.match(lines[ln - 1]):
                    m = re.match(r"^\d{4}-\d{2}-\d{2} p(\d+)", text)
                    if m and int(m.group(1)) >= 10:  # p10 以降（材料の外。動いている・閉じていない）
                        skipped.append(f"{ln} 行目（p{m.group(1)}）")
                        continue
                    add("job", "job_readme", title, path, ln, text, frm="根っこ")
                    n += 1
        elif "の時点" in title:
            for ln, text in split_items(body, bstart):
                if re.match(r"^\*\*(残ったこと|残っている課題|p\d+ の申し送り|申し送り)", text):
                    add("job", "job_readme", title, path, ln, text, frm="根っこ")
                    n += 1
    raw = open(path, "rb").read()
    st = os.stat(path)
    global JOB_README_VERSION
    JOB_README_VERSION = (f"sha1 {hashlib.sha1(raw).hexdigest()[:12]}・更新 {dt.datetime.fromtimestamp(st.st_mtime).strftime('%Y-%m-%d %H:%M')}"
                          "（job の git の管理外なので、読んだ時点の中身の指紋）")
    counts.append(("job_readme", rel(path), n, ("p10 以降の行は材料の外なので抜かない: " + "・".join(skipped)) if skipped else ""))


def do_events_audit():
    """events.log で、監査役（position=auditor）の assign が無いまま閉じたプロジェクトを 1 件ずつ（参照元は根っこの component_closed の行）。"""
    for d in sorted(glob.glob(os.path.join(PROJECTS, "p*"))):
        name = os.path.basename(d)
        if not PROJ_RE.match(name):
            continue
        path = os.path.join(d, "log", "events.log")
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        has_auditor = any("position=auditor" in l for l in lines)
        closed = [i + 1 for i, l in enumerate(lines) if l.rstrip("\n").endswith(f" component_closed - {name}")]
        if not has_auditor and closed:
            add(name, "events:no_auditor", "events.log", path, closed[-1],
                "events.log に監査役（position=auditor）の assign が無いまま、根っこが閉じた（component_closed）", frm="orgctl")
            counts.append(("events_audit", rel(path), 1, ""))
        else:
            counts.append(("events_audit", rel(path), 0, "監査役の assign がある" if has_auditor else "閉じた行が無い"))


def main():
    ev, _ = load_events()
    do_sessions()
    do_msgs(ev)
    do_user_inbox()
    do_audit_p9()
    do_job_readme()
    do_events_audit()
    os.makedirs(WORK, exist_ok=True)
    cols = ["id", "project", "source", "section", "ref", "hash", "events_line", "from", "text"]
    with open(os.path.join(WORK, "extract.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar="\x07", escapechar="\\")
        w.writerow(cols)
        for i, r in enumerate(rows, 1):
            r["id"] = f"E{i:03d}"
            w.writerow([r[c] for c in cols])
    with open(os.path.join(WORK, "counts.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["material", "file", "extracted", "zero_reason"])
        for c in counts:
            w.writerow(c)
    # 読み物
    by = {}
    for m, fpath, n, _ in counts:
        a = by.setdefault(m, [0, 0, 0])
        a[0] += 1
        a[1] += n
        a[2] += (n == 0)
    by_src = {}
    for r in rows:
        by_src[r["source"]] = by_src.get(r["source"], 0) + 1
    out = ["# 抜き出しの件数表（scripts/extract.py が書いた。手で直さない）", "",
           f"抜いた件数の合計: {len(rows)}", "",
           "## 材料ごとの小計", "", "| 材料 | ファイル数 | 抜いた件数 | 0 件のファイル |", "|---|---|---|---|"]
    for m, (nf, nr, nz) in by.items():
        out.append(f"| {m} | {nf} | {nr} | {nz} |")
    out += ["", "## 抜いた件の出どころ（source）ごと", "", "| source | 件数 |", "|---|---|"]
    for k in sorted(by_src):
        out.append(f"| {k} | {by_src[k]} |")
    out += ["", "## 抜き方（source の意味）", "",
            "- `session`: セッション報告の `self` の `unclear`・`not_done` の 1 項目＝1 件（`machine` は読まない）",
            "- `msg:節A`: msgs の見出しが「うまくいかなかった・試走で・試走として・気づき・気づいた・食い違・unclear」の節。上の階層の箇条書き 1 つ（子は親に足す）か地の文の段落 1 つ＝1 件",
            "- `user_inbox:<kind>`: `log/user-inbox.yaml` の項のうち kind が report でないもの（見張りの stuck など）。report の項は log/msgs と同じ本文を指すので抜かない。`log/notify-outbox.log`（p3 だけ）は根っこへの知らせの写しで、本文は log/msgs と同じなので抜かない",
            "- `msg:節B`: 同じく見出しが「残る不明点・残ること・残った・申し送り・〔仮〕・上げること・未確認」の節（網羅のための候補。問題かどうかはまとめで決める）",
            "- `msg:札B`: 見出しでなく地の文の行頭の札（「申し送り:」など）で始まる塊。札の行の本文と、続く箇条書き（空行まで）を 1 つ 1 件",
            "- `event:<種類>`: events.log で種類が review_ng・rework・blocked・escalate・nudge の行が指す本文の全体を、箇条書き・段落ごとに 1 件（blocked・escalate は p1〜p9 に 0 行。nudge は根っこの見張りの促しで、pack の 4 種に足した）",
            "- `auditor`: 送り手が監査役の本文（p3 の 95df09・p9 の 63bb4d）の `##` 節の項目ごと",
            "- `audit`: p9 の `reports/audit/p9-org-watch.md` の番号つきの項 1 つ＝1 件",
            "- `job_readme`: job の README の「組織の直し待ち」の箇条書き（p10 以降の行は除く）と、「〜の時点」の節の「残ったこと・残っている課題・申し送り」で始まる行。読んだ版: " + JOB_README_VERSION,
            "- `events:no_auditor`: 各プロジェクトの events.log に監査役（position=auditor）の assign が無いまま閉じたもの 1 つ＝1 件（参照元は根っこの component_closed の行。レビュー第1回の指摘で足した）",
            "", "## 読まなかったもの（材料の外）", "",
            "- セッション報告の `machine`（会話ログ由来）と `~/.claude/projects/` の会話ログ",
            "- `teams/*/msgs/`（5 本。作業者の版の写し。往復の本文は log/msgs にある）・`teams/*/thread.md`・`teams/*/result.md`（材料の指定に無い。結果は PM・リーダーの report の本文として log/msgs で読んでいる）",
            "- p10-viewer-ideas・p11-issue-list",
            "", "## ファイルごと", "", "| 材料 | ファイル | 抜いた件数 | 0 件の理由 |", "|---|---|---|---|"]
    for m, fpath, n, why in counts:
        out.append(f"| {m} | `{fpath}` | {n} | {why} |")
    with open(os.path.join(WORK, "counts.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(f"rows={len(rows)} files={len(counts)}", file=sys.stderr)
    for m, (nf, nr, nz) in by.items():
        print(f"{m}: files={nf} rows={nr} zero={nz}", file=sys.stderr)
    for k in sorted(by_src):
        print(f"  {k}: {by_src[k]}", file=sys.stderr)


if __name__ == "__main__":
    main()
