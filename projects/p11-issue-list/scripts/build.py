#!/usr/bin/env python3
"""p11 の 4 段目: issues_def.py（判断）と work/extract.tsv（抜き出し）を突き合わせ、数えて並べ、issues.md と対応表を書く。

  python3 projects/p11-issue-list/scripts/extract.py   # 先に抜き出し
  python3 projects/p11-issue-list/scripts/build.py

書くもの:
  issues.md                 一覧（Summary・表・件ごと・作り方）
  teams/issues/work/mapping.tsv / mapping.md   抜き出しの各行 → 件、または入れなかった理由

止まるとき: 抜き出しの行が issues_def.py のどこにも入っていない・2 か所に入っている・無い id を指している。
"""
import csv
import hashlib
import os
import re
import sys
from collections import Counter, OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
P = os.path.dirname(HERE)
WORK = os.path.join(P, "teams", "issues", "work")
sys.path.insert(0, HERE)
from issues_def import ISSUES, EXCLUDE, SECONDARY_SOURCES  # noqa: E402

STATUS_LABEL = {"fixed": "直った", "unknown": "不明", "": "印なし"}
STATUS_ORDER = ["", "unknown", "fixed"]


def load_extract():
    with open(os.path.join(WORK, "extract.tsv"), encoding="utf-8") as f:
        r = csv.reader(f, delimiter="\t", quoting=csv.QUOTE_NONE, quotechar="\x07", escapechar="\\")
        head = next(r)
        rows = OrderedDict()
        for line in r:
            d = dict(zip(head, line))
            rows[d["id"]] = d
    return rows


def pnum(project):
    m = re.match(r"p(\d+)-", project)
    return int(m.group(1)) if m else 0


def anchor(n, title):
    return f"i{n:02d}"


def main():
    rows = load_extract()
    fp = hashlib.sha1("\n".join(f"{k}\t{v['ref']}" for k, v in rows.items()).encode()).hexdigest()[:12]

    owner = {}
    errors = []

    def claim(i, who):
        if i not in rows:
            errors.append(f"{who}: {i} は extract.tsv に無い")
        elif i in owner:
            errors.append(f"{i} が 2 か所に入っている（{owner[i]} と {who}）")
        else:
            owner[i] = who

    for it in ISSUES:
        for i in it["ids"].split():
            claim(i, it["key"])
    for reason, ids in EXCLUDE.items():
        for i in ids.split():
            claim(i, "除外: " + reason)
    for i in rows:
        if i not in owner:
            errors.append(f"{i} がどこにも入っていない（{rows[i]['ref']}）")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)

    # 数える
    issues = []
    for it in ISSUES:
        rs = [rows[i] for i in it["ids"].split()]
        primary = [r for r in rs if r["source"] not in SECONDARY_SOURCES]
        counted = primary or rs  # ほかの出どころが無いときだけ、監査・job の控えを数える
        projs = sorted({r["project"] for r in counted if pnum(r["project"])}, key=pnum)
        newest = max([pnum(r["project"]) for r in counted] + [0])
        issues.append(dict(it, rows=rs, counted=counted, projects=projs, n_proj=len(projs),
                           n_rec=len(counted), newest=newest, only_secondary=not primary))
    # 並び: プロジェクト数の多い順 → 記録の数の多い順 → 新しい順（数えた行の中で一番新しいプロジェクト）→ 定義の順
    order = {it["key"]: k for k, it in enumerate(ISSUES)}
    issues.sort(key=lambda x: (-x["n_proj"], -x["n_rec"], -x["newest"], order[x["key"]]))
    for n, it in enumerate(issues, 1):
        it["n"] = n

    n_ex = sum(1 for v in owner.values() if v.startswith("除外"))
    n_in = len(rows) - n_ex
    st = Counter(it["status"] for it in issues)
    cats = Counter(it["cat"] for it in issues)
    cat_proj = Counter()
    for it in issues:
        cat_proj[it["cat"]] += it["n_rec"]

    def ref_text(r):
        s = f"`{r['ref']}`"
        if r["hash"]:
            s += f"（{r['hash']}" + (f"・`log/events.log:{r['events_line']}`" if r["events_line"] else "") + "）"
        return s

    def plist(ps):
        return "・".join(p.split("-")[0] for p in ps) or "—"

    readme_version = ""
    with open(os.path.join(WORK, "counts.md"), encoding="utf-8") as f:
        m = re.search(r"読んだ版: (sha1 [0-9a-f]+・更新 [0-9-]+ [0-9:]+)", f.read())
        readme_version = m.group(1) if m else "不明"
    out = []
    out.append("# AI 組織の問題・課題の一覧（閉じた p1〜p9 の記録から）")
    out.append("")
    out.append("書いてあるのは起きたこと（問題・課題）と参照元だけ。直し方は書かない（直し方は着手の直前に考える。dev-tools の `docs/todo/ai-org-plan.md` の決定ログ 2026-10-24）。数はすべて `scripts/build.py` が数えた値。")
    out.append("")
    out.append("## Summary")
    out.append("")
    out.append(f"- **{len(issues)} 件**（印なし＝まだ起きている {st['']}・不明 {st['unknown']}・直った {st['fixed']}）。材料から抜いた {len(rows)} 行のうち {n_in} 行をこの {len(issues)} 件に寄せ、{n_ex} 行は入れなかった（理由は対応表）。")
    out.append("- 分類ごとの件数（記録の数の合計）: " + "・".join(f"{c} {cats[c]} 件（{cat_proj[c]}）" for c, _ in cats.most_common()))
    top = issues[:5]
    out.append("- 何度も起きているもの（プロジェクト数の多い順の上位 5）:")
    for it in top:
        out.append(f"  - [{it['title']}](#{anchor(it['n'], it['title'])}) — {it['n_proj']} プロジェクト・記録 {it['n_rec']}・{STATUS_LABEL[it['status']]}")
    out.append("")
    out.append("## 目次")
    out.append("")
    out.append("- [Summary](#summary)")
    out.append("- [一覧](#一覧)")
    out.append("- [件ごと](#件ごと)")
    out.append("- [作り方](#作り方)")
    out.append("")
    out.append("## 一覧")
    out.append("")
    out.append("並びはプロジェクト数の多い順（同じなら記録の数の多い順、それも同じなら新しい順）。状態の「印なし」はまだ起きているもの。")
    out.append("")
    out.append("| # | 題 | 分類 | プロジェクト数 | 記録の数 | 状態 |")
    out.append("|---|---|---|---|---|---|")
    for it in issues:
        mark = "" if it["status"] == "" else STATUS_LABEL[it["status"]]
        cell = it["title"].replace("|", "\\|")  # 表のセルの区切りと見分ける
        out.append(f"| {it['n']} | [{cell}](#{anchor(it['n'], it['title'])}) | {it['cat']} | {it['n_proj']}（{plist(it['projects'])}） | {it['n_rec']} | {mark} |")
    out.append("")
    out.append("[↑ 目次へ](#目次)")
    out.append("")
    out.append("## 件ごと")
    out.append("")
    for it in issues:
        out.append(f'<a id="{anchor(it["n"], it["title"])}"></a>')
        out.append("")
        out.append(f"### {it['n']}. {it['title']}")
        out.append("")
        out.append(f"- 分類: {it['cat']}")
        sec_note = "（監査・job の控えだけが書いているので、それを数えた）" if it["only_secondary"] else ""
        out.append(f"- 回数: {it['n_proj']} プロジェクト（{plist(it['projects'])}）・記録 {it['n_rec']}{sec_note}")
        out.append(f"- 状態: {STATUS_LABEL[it['status']]} — {it['basis']}")
        out.append(f"- 起きたこと: {it['what']}")
        out.append("- 参照元:")
        counted_ids = {r["id"] for r in it["counted"]}
        for r in it["rows"]:
            tag = "" if r["id"] in counted_ids else "（別の出どころ。数えない）"
            out.append(f"  - {ref_text(r)}{tag}")
        out.append("")
        out.append("[↑ 目次へ](#目次)")
        out.append("")
    out.append("## 作り方")
    out.append("")
    out.append(f"- 読んだ場所: 閉じた p1〜p9 の `reports/sessions/*.yaml` の `self` の `unclear`・`not_done`、`log/msgs/*.md` の「うまくいかなかったこと」系・「申し送り」「残る不明点」「未確認」系の節と見出しでない「申し送り:」の札、`log/events.log` で種類が review_ng・rework・blocked・escalate・nudge の本文（blocked・escalate は 0 行）、`log/user-inbox.yaml` の report でない項、監査役の出力（p3 の `log/msgs/95df09.md`・p9 の `reports/audit/p9-org-watch.md`）、events.log の監査役の assign の有無（無いまま閉じたプロジェクトを 1 件ずつ）、job の `company/system/ai-org/README.md` の「組織の直し待ち」（p10 以降の行は除く）と「の時点」の残ったこと・申し送り（job の README は git の管理外で外の人が書き足すので、読んだ版の指紋を `counts.md` に残した: " + readme_version + "）。p10 と会話ログは読まない。抜き出しは `scripts/extract.py`（1 行 1 件、`teams/issues/work/extract.tsv`・件数表 `counts.md`）。")
    out.append("- まとめ方: 言い方でなく中身（誰が・何をして・どうなったか）が同じものを 1 件にした。成果物の中身への指摘、何も起きなかった行、直し方の選択肢、これからの段取り、未実施・〔仮〕の申告は入れなかった。各行の行き先と入れなかった理由は `teams/issues/work/mapping.md`。判断は `scripts/issues_def.py`。")
    out.append("- 回数: 「プロジェクト数」はその件の記録があるプロジェクトの数、「記録の数」は寄せた抜き出しの行の数（同じ人の unclear と報告の節は別に数える）。監査役の出力と job の控えは、同じ出来事を別の出どころが書いたものなので参照元に足すが数えない（その件にほかの出どころが無いときだけ数える）。")
    out.append("- 並び: **プロジェクト数**の多い順。同じなら記録の数の多い順、それも同じなら新しい順（数えた記録のうち一番新しいプロジェクト）。")
    out.append("- 状態: 「直った」は dev-tools の main にマージ済みの直した記録があり、かつそのマージより後に始まって閉じたプロジェクトの記録に同じ申告が無いもの。片方しか無いものは「不明」（何が足りないかを書いた）。直した記録が無く最後のプロジェクトまで起きているもの、直したあとにも起きているものは印なし。照合に使ったのは `git -C dev-tools log main` の PR のマージ時刻と、各プロジェクトの events.log の最初と最後の時刻。")
    out.append(f"- 数え直し: `python3 projects/p11-issue-list/scripts/extract.py && python3 projects/p11-issue-list/scripts/build.py`（抜き出しの指紋 {fp}）。")
    out.append("")
    out.append("[↑ 目次へ](#目次)")
    with open(os.path.join(P, "issues.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

    # 対応表
    num = {it["key"]: it["n"] for it in issues}
    title = {it["key"]: it["title"] for it in issues}
    with open(os.path.join(WORK, "mapping.tsv"), "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["id", "ref", "source", "issue_no", "issue_key", "excluded_reason"])
        for i, r in rows.items():
            o = owner[i]
            if o.startswith("除外: "):
                w.writerow([i, r["ref"], r["source"], "", "", o[4:]])
            else:
                w.writerow([i, r["ref"], r["source"], num[o], o, ""])
    md = ["# 対応表（scripts/build.py が書いた。手で直さない）", "",
          f"抜き出し {len(rows)} 行の行き先。件に入れた {n_in} 行・入れなかった {n_ex} 行。件の番号は `issues.md` の番号。", "",
          "## 入れなかった理由ごとの行数", "", "| 理由 | 行数 |", "|---|---|"]
    exc = Counter(o[4:] for o in owner.values() if o.startswith("除外: "))
    for reason in EXCLUDE:
        md.append(f"| {reason} | {exc[reason]} |")
    md += ["", "## 行ごと", "", "| id | 参照元 | 行き先 |", "|---|---|---|"]
    for i, r in rows.items():
        o = owner[i]
        dest = f"入れない: {o[4:]}" if o.startswith("除外: ") else f"{num[o]}. {title[o]}"
        md.append(f"| {i} | `{r['ref']}` | {dest} |")
    with open(os.path.join(WORK, "mapping.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(f"issues={len(issues)} fixed={st['fixed']} unknown={st['unknown']} open={st['']} rows={len(rows)} in={n_in} excluded={n_ex} fingerprint={fp}", file=sys.stderr)
    for it in issues[:10]:
        print(f"  {it['n']:2d} p={it['n_proj']} r={it['n_rec']} {STATUS_LABEL[it['status']]} {it['title'][:50]}", file=sys.stderr)


if __name__ == "__main__":
    main()
