#!/usr/bin/env python3
"""プロジェクトの events.log・本文・セッション報告から、1 枚の静的 HTML（timeline.html）を書く。

使い方: python3 tools/org_timeline.py projects/<slug>   → projects/<slug>/timeline.html

出すもの: 人の報告（start・report・review_* など）は時刻順の列に置き、送り手の帯に印を付ける。
まとめるもの: assign・launch・teardown は帯の頭の「起動〜終了」に畳む。component_new・component_closed は出さない。
落とすもの: ack・notify_* は件数だけ数えて下に 1 行出す。
"""
import html
import json
import pathlib
import re
import sys
import datetime as dt

LIFECYCLE = {"assign", "launch", "teardown", "component_new", "component_closed"}


def is_noise(kind):
    """通知の配送記録（ack と notify_ で始まる種類すべて）。"""
    return kind == "ack" or kind.startswith("notify_")

POS_RANK = {"user": 0, "pm": 1, "leader": 2, "worker": 3, "reviewer": 4}
KIND_STYLE = {  # 種類: (色, 記号)
    "start": ("#2563eb", "▶"),
    "report": ("#0891b2", "●"),
    "review_request": ("#7c3aed", "?"),
    "review_ng": ("#dc2626", "✕"),
    "review_ok": ("#16a34a", "✓"),
    "rework": ("#ea580c", "↺"),
    "reassign": ("#c026d3", "⇄"),
    "blocked": ("#b91c1c", "■"),
    "escalate": ("#d97706", "▲"),
    "wrap_up": ("#64748b", "◼"),
    "done": ("#475569", "◆"),
}
OTHER_STYLE = ("#9ca3af", "·")
GAP_SEC = 300


def parse_events(path):
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        p = line.split(" ", 5)
        if len(p) < 5:
            continue
        rest = p[5] if len(p) > 5 else ""
        kv = dict(t.split("=", 1) for t in rest.split() if "=" in t)
        out.append({"ts": dt.datetime.fromisoformat(p[0]), "hash": p[1], "frm": p[2],
                    "kind": p[3], "to": p[4], "rest": rest, "kv": kv})
    return out


def read_yaml_machine(path):
    """`machine:` 配下の必要な項目だけ読む。"""
    want = {"id", "position", "occupation", "model_requested", "launched_at", "closed_at",
            "span_min", "tokens_total", "api_messages", "review_ng_count"}
    got, in_m = {}, False
    for line in path.read_text(encoding="utf-8").splitlines():
        if re.match(r"^\S", line):
            in_m = line.startswith("machine:")
            continue
        m = re.match(r"^  (\w+):\s*(.*)$", line) if in_m else None
        if m and m.group(1) in want:
            v = m.group(2).strip().strip('"')
            got[m.group(1)] = None if v in ("null", "") else v
    return got


def collect_components(root):
    """component.json を上から辿り、メンバー id の並び（組織の上から）と position を返す。"""
    order, pos = [], {}

    def walk(d):
        cj = d / "component.json"
        if not cj.exists():
            return
        c = json.loads(cj.read_text(encoding="utf-8"))
        members = c.get("members", {})
        for k in sorted(members, key=lambda k: (POS_RANK.get(re.sub(r"-\d+$", "", k), 5), k)):
            order.append(members[k])
            pos[members[k]] = re.sub(r"-\d+$", "", k)
        for child in c.get("children", []):
            walk(root / child.split("/", 1)[1] if "/" in child else root / child)

    walk(root)
    return order, pos


def short(mid):
    return mid if mid == "user" else mid.split("/", 1)[-1] if "/" in mid else mid


def fmt_tokens(n):
    n = int(n)
    return f"{n / 1e6:.2f}M" if n >= 1e6 else f"{n / 1e3:.0f}k"


def e(s):
    return html.escape(str(s), quote=True)


def build(root):
    events = parse_events(root / "log" / "events.log")
    order, pos = collect_components(root)
    sessions = {}
    for f in sorted((root / "reports" / "sessions").glob("*.yaml")):
        m = read_yaml_machine(f)
        if m.get("id"):
            sessions[m["id"]] = m
    lanes = ["user"] + [m for m in order if m != "user"]
    for ev in events:
        for who in (ev["frm"], ev["to"]):
            if who != "-" and who not in lanes:
                lanes.append(who)
    for s in sessions:
        if s not in lanes:
            lanes.append(s)
    for s, m in sessions.items():
        pos.setdefault(s, m.get("position") or s.rsplit("/", 1)[-1])
    pos["user"] = "user"

    shown = [x for x in events if x["kind"] not in LIFECYCLE and not is_noise(x["kind"])]
    life = {}
    for x in events:
        if x["kind"] in ("launch", "teardown", "assign"):
            who = x["to"] if x["to"] != "-" else x["rest"].split()[0]
            life.setdefault(who, {}).setdefault(x["kind"], []).append(x["ts"])
    noise = {k: sum(1 for x in events if x["kind"] == k) for k in sorted({x["kind"] for x in events if is_noise(x["kind"])})}
    return events, lanes, pos, sessions, shown, life, noise


def render(root):
    events, lanes, pos, sessions, shown, life, noise = build(root)
    # 列: 1 件 1 列。5 分以上空いたら間隔の列を挟む
    cols, prev = [], None
    for x in shown:
        if prev and (x["ts"] - prev).total_seconds() >= GAP_SEC:
            cols.append(("gap", round((x["ts"] - prev).total_seconds() / 60)))
        cols.append(("ev", x))
        prev = x["ts"]
    max_tok = max([float(s["tokens_total"]) for s in sessions.values() if s.get("tokens_total")] or [1])
    max_span = max([float(s["span_min"]) for s in sessions.values() if s.get("span_min")] or [1])

    css = """
body{font:13px/1.5 -apple-system,'Hiragino Sans',sans-serif;margin:16px;color:#1f2937;background:#fafafa}
h1{font-size:18px;margin:0 0 4px}h2{font-size:15px;margin:24px 0 8px}
.sub{color:#6b7280;margin-bottom:12px}
.wrap{overflow-x:auto;border:1px solid #e5e7eb;background:#fff}
table.tl{border-collapse:collapse}
table.tl td,table.tl th{border-bottom:1px solid #f1f5f9;padding:2px 0;text-align:center;min-width:46px}
table.tl th.t{font-weight:normal;font-size:10px;color:#6b7280;padding:4px 2px;vertical-align:bottom;border-bottom:1px solid #cbd5e1}
th.gap,td.gap{min-width:30px;background:repeating-linear-gradient(135deg,#f8fafc,#f8fafc 4px,#eef2f7 4px,#eef2f7 8px);font-size:10px;color:#94a3b8}
td.head{position:sticky;left:0;z-index:2;background:#fff;text-align:left;min-width:230px;max-width:230px;padding:4px 8px;border-right:2px solid #cbd5e1}
.head b{font-size:12px}.head .pos{color:#6b7280;font-size:11px}
.head .stat{font-size:11px;color:#374151}.bar{height:4px;background:#93c5fd;margin-top:1px}.bar.tok{background:#fcd34d}
a.mark{display:inline-block;min-width:34px;padding:1px 3px;border-radius:4px;color:#fff;text-decoration:none;font-size:10px;line-height:1.3}
a.mark b{font-size:12px;display:block}
.rcv{display:inline-block;width:14px;height:14px;border:2px solid;border-radius:50%;box-sizing:border-box;opacity:.55}
tr.row:hover td{background:#f8fafc}
.ev{border:1px solid #e5e7eb;background:#fff;border-left:5px solid;margin:4px 0;padding:4px 8px}
.ev:target{background:#fffbeb;outline:2px solid #f59e0b}
.ev summary{cursor:pointer}.ev .k{font-weight:bold}
pre{white-space:pre-wrap;background:#f8fafc;padding:8px;margin:6px 0;font-size:12px}
.legend span{display:inline-block;margin-right:10px}.legend i{display:inline-block;width:12px;height:12px;border-radius:3px;vertical-align:-2px;margin-right:3px}
table.ss{border-collapse:collapse}table.ss td,table.ss th{border:1px solid #e5e7eb;padding:3px 8px;text-align:right}
table.ss td:first-child,table.ss th:first-child{text-align:left}
"""
    out = [f"<!doctype html><html lang=ja><meta charset=utf-8><title>{e(root.name)} timeline</title><style>{css}</style><body>"]
    t0 = events[0]["ts"] if events else None
    t1 = events[-1]["ts"] if events else None
    out.append(f"<h1>{e(root.name)} — 誰が・いつ・誰に・何を出したか</h1>")
    if t0:
        out.append(f"<div class=sub>{t0:%Y-%m-%d %H:%M:%S} 〜 {t1:%H:%M:%S}（{(t1 - t0).total_seconds() / 60:.1f} 分）・"
                   f"人の報告 {len(shown)} 件・メンバー {len(lanes)} 人</div>")
    kinds = list(KIND_STYLE) + sorted({x["kind"] for x in shown} - set(KIND_STYLE))
    out.append("<div class=legend>" + "".join(
        f"<span><i style='background:{(KIND_STYLE.get(k) or OTHER_STYLE)[0]}'></i>{e(k)}</span>"
        for k in kinds if k in KIND_STYLE or k in {x['kind'] for x in shown}) +
        "<span><i style='background:none;border:2px solid #888;border-radius:50%'></i>宛先（受け手の帯）</span></div>")

    out.append("<h2>タイムライン（左→右が時刻順。印を押すと下の本文へ）</h2><div class=wrap><table class=tl>")
    out.append("<tr><td class=head></td>")
    last_day = None
    for kind, v in cols:
        if kind == "gap":
            out.append(f"<th class=gap>⋯<br>{v}分</th>")
        else:
            day = ""
            if v["ts"].date() != last_day:
                day = f"{v['ts']:%m-%d}<br>"
                last_day = v["ts"].date()
            out.append(f"<th class=t>{day}{v['ts']:%H:%M:%S}</th>")
    out.append("</tr>")
    for lane in lanes:
        s = sessions.get(lane, {})
        lf = life.get(lane, {})
        out.append(f"<tr class=row><td class=head><b>{e(short(lane))}</b> <span class=pos>{e(pos.get(lane, ''))}"
                   f"{' / ' + e(s['model_requested']) if s.get('model_requested') else ''}</span>")
        if s.get("span_min") or s.get("tokens_total"):
            sp = float(s.get("span_min") or 0)
            tk = float(s.get("tokens_total") or 0)
            last = "（最後の起動分のみ）" if len(lf.get("launch", [])) > 1 else ""
            out.append(f"<div class=stat>⏱ {sp:g} 分 ・ tokens {fmt_tokens(tk)}{last}"
                       f"{' ・ review_ng ' + s['review_ng_count'] if s.get('review_ng_count') not in (None, '0') else ''}</div>"
                       f"<div class=bar style='width:{sp / max_span * 100:.0f}%'></div>"
                       f"<div class='bar tok' style='width:{tk / max_tok * 100:.0f}%'></div>")
        elif lane != "user":
            out.append("<div class=stat>セッション報告なし</div>")
        if lf.get("launch"):
            end = lf["teardown"][-1] if lf.get("teardown") else None
            out.append(f"<div class=stat>起動 {lf['launch'][0]:%H:%M:%S}"
                       f"{' → 終了 ' + format(end, '%H:%M:%S') if end else ''}"
                       f"{' ・起動 ' + str(len(lf['launch'])) + ' 回' if len(lf['launch']) > 1 else ''}</div>")
        out.append("</td>")
        for kind, v in cols:
            if kind == "gap":
                out.append("<td class=gap></td>")
                continue
            color, sym = KIND_STYLE.get(v["kind"], OTHER_STYLE)
            if v["frm"] == lane:
                to = short(v["to"]) if v["to"] != "-" else ""
                out.append(f"<td><a class=mark href='#e-{e(v['hash'])}' style='background:{color}' "
                           f"title='{e(v['kind'])} → {e(to)}'><b>{sym}</b>{e(v['kind'].replace('review_', 'r_'))}</a></td>")
            elif v["to"] == lane:
                out.append(f"<td><span class=rcv style='color:{(KIND_STYLE.get(v['kind']) or OTHER_STYLE)[0]}' "
                           f"title='{e(short(v['frm']))} から {e(v['kind'])}'></span></td>")
            else:
                out.append("<td></td>")
        out.append("</tr>")
    out.append("</table></div>")

    out.append("<h2>セッションごとの時間とトークン</h2><table class=ss><tr><th>メンバー<th>職<th>時間(分)<th>tokens_total<th>備考<th>API 回数<th>review_ng")
    for lane in lanes:
        s = sessions.get(lane)
        if s:
            tk = f"{int(float(s['tokens_total'])):,}" if s.get("tokens_total") else "-"
            out.append(f"<tr><td>{e(short(lane))}<td>{e(pos.get(lane, ''))}<td>{e(s.get('span_min') or '-')}<td>{tk}<td>{'最後の起動分のみ（起動 ' + str(len(life.get(lane, {}).get('launch', []))) + ' 回）' if len(life.get(lane, {}).get('launch', [])) > 1 else ''}")
            out.append(f"<td>{e(s.get('api_messages') or '-')}<td>{e(s.get('review_ng_count') or '0')}")
    out.append("</table>")

    out.append("<h2>報告の一覧（時刻順。クリックで本文）</h2>")
    for x in shown:
        color, sym = KIND_STYLE.get(x["kind"], OTHER_STYLE)
        body = ""
        mp = x["kv"].get("msg")
        if mp:
            f = root / mp
            body = f.read_text(encoding="utf-8") if f.exists() else "(本文ファイルが見つからない)"
        head = (f"<span style='color:{color}'>{sym}</span> {x['ts']:%H:%M:%S} "
                f"<span class=k>{e(x['kind'])}</span> {e(short(x['frm']))} → {e(short(x['to']) if x['to'] != '-' else '-')}")
        if body:
            out.append(f"<details class=ev id='e-{e(x['hash'])}' style='border-left-color:{color}'><summary>{head}</summary><pre>{e(body)}</pre></details>")
        else:
            extra = f" <small>{e(x['rest'])}</small>" if x["rest"] not in ("", "-") else ""
            out.append(f"<div class=ev id='e-{e(x['hash'])}' style='border-left-color:{color}'>{head}{extra}</div>")

    out.append("<h2>畳んだもの</h2><div class=sub>" + "・".join(
        f"{k} {v} 件" for k, v in noise.items()) + "（ack・notify_* の配送記録は件数のみ）。"
        "assign・launch・teardown は各帯の頭の「起動〜終了」に畳んだ。component_new・component_closed は出していない。</div>")
    out.append("</body></html>")
    return "\n".join(out)


def main(argv):
    if len(argv) != 2:
        print("usage: org_timeline.py <project dir>", file=sys.stderr)
        return 2
    root = pathlib.Path(argv[1]).resolve()
    dest = root / "timeline.html"
    dest.write_text(render(root), encoding="utf-8")
    print(dest)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
