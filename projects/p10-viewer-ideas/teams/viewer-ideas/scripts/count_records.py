#!/usr/bin/env python3
"""p1〜p9 の記録から、report.md に載せる数を数える（標準ライブラリだけ）。

読むもの（ai-org/projects/<p>/ の中だけ）:
  - log/events.log            1 行報告（時刻 id 送り手 種類 宛先 ...）
  - component.json            created_at / closed_at
  - reports/sessions/*.yaml   tokens_total・span_min・self の unclear（正規表現で拾う。yaml は入っていない）

使い方: python3 count_records.py [ai-org の projects のパス]
出力: プロジェクトごとの表（Markdown）と、案の根拠に使う個別の数
"""
import json
import re
import statistics
import sys
from datetime import datetime
from pathlib import Path

PROJ = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[5] / "projects"
TARGET = [f"p{i}-" for i in range(1, 10)]
NOISE = {"ack", "notify_sent", "notify_recv", "notify_skipped", "patrol"}
LIFE = {"component_new", "component_closed", "assign", "launch", "teardown"}


def ts(s):
    return datetime.fromisoformat(s)


def events(p):
    out = []
    for line in (p / "log/events.log").read_text().splitlines():
        f = line.split()
        if len(f) < 5:
            continue
        out.append({"ts": ts(f[0]), "id": f[1], "from": f[2], "kind": f[3], "to": f[4], "raw": line})
    return out


def sessions(p):
    rows = []
    for y in sorted((p / "reports/sessions").glob("*.yaml")):
        t = y.read_text()
        tok = re.search(r"^\s*tokens_total:\s*(\d+)", t, re.M)
        span = re.search(r"^\s*span_min:\s*([\d.]+)", t, re.M)
        # self: | の中の unclear: の箇条（次のキーまで）
        unclear = []
        m = re.search(r"^\s+unclear:\s*\n((?:\s+- .*\n?|\s{6,}.*\n?)*)", t, re.M)
        if m:
            unclear = [l for l in m.group(1).splitlines() if re.match(r"^\s+- ", l)]
        rows.append({"file": y.name, "tokens": int(tok.group(1)) if tok else None,
                     "span": float(span.group(1)) if span else None, "unclear": len(unclear)})
    return rows


def main():
    projects = sorted([d for d in PROJ.iterdir() if d.is_dir() and any(d.name.startswith(t) for t in TARGET)],
                      key=lambda d: int(d.name.split("-")[0][1:]))
    table = []
    for p in projects:
        comp = json.loads((p / "component.json").read_text())
        ev = events(p)
        msg = [e for e in ev if e["kind"] not in NOISE and e["kind"] not in LIFE]
        kinds = {}
        for e in msg:
            kinds[e["kind"]] = kinds.get(e["kind"], 0) + 1
        remakes = kinds.get("review_ng", 0) + kinds.get("rework", 0) + kinds.get("reassign", 0)
        # 人（根っこ＝user）の手: 依頼・終わりの指示（決まった手続き）と、自分が立てた PM・監査役の起動と片づけ以外
        root_pm = {f"{p.name}/pm", f"{p.name}/auditor"}
        user_ev = [e for e in ev if e["from"] == "user" and e["kind"] not in NOISE and e["kind"] != "component_new"
                   and e["kind"] != "component_closed"]
        routine = []
        extra = []
        seen_launch = set()
        for e in user_ev:
            tgt = e["to"] if e["to"] != "-" else e["raw"].split()[5]
            if e["kind"] in ("start", "wrap_up") and tgt in root_pm:
                routine.append(e)
            elif e["kind"] in ("assign", "launch") and tgt in root_pm and (tgt, e["kind"]) not in seen_launch:
                seen_launch.add((tgt, e["kind"]))
                routine.append(e)
            elif e["kind"] == "teardown" and tgt in root_pm:
                # 閉じるとき（閉じた時刻の 10 分以内）の片づけは手続き。途中の片づけ（入れ替え）は手として数える
                closing = (ts(comp["closed_at"]) - e["ts"]).total_seconds() < 600 if comp.get("closed_at") else False
                (routine if closing else extra).append(e)
            else:
                extra.append(e)
        # 途中の入れ替え（同じ PM の 2 回目の assign・launch）も手として数える
        extra_desc = sorted({f'{e["ts"]:%H:%M} {e["kind"]} {e["to"] if e["to"] != "-" else e["raw"].split()[5]}' for e in extra})
        ss = sessions(p)
        tokens = sum(s["tokens"] for s in ss if s["tokens"])
        dur = (ts(comp["closed_at"]) - ts(comp["created_at"])).total_seconds() / 60 if comp.get("closed_at") else None
        # 川崎さん宛ての最後の report から wrap_up までの分（根っこが結果を受けるまで）
        to_user = [e for e in msg if e["to"] == "user" and e["kind"] == "report"]
        wraps = [e for e in msg if e["from"] == "user" and e["kind"] == "wrap_up"]
        lag = None
        if to_user and wraps:
            r = to_user[0]
            w = [x for x in wraps if x["ts"] >= r["ts"]]
            if w:
                lag = (w[0]["ts"] - r["ts"]).total_seconds() / 60
        table.append({
            "p": p.name, "title": comp.get("title"), "dur": dur, "tokens": tokens, "sessions": len(ss),
            "sess_missing_tokens": sum(1 for s in ss if s["tokens"] is None),
            "msgs": len(msg), "review_ng": kinds.get("review_ng", 0), "rework": kinds.get("rework", 0),
            "reassign": kinds.get("reassign", 0), "remakes": remakes, "escalate": kinds.get("escalate", 0),
            "blocked": kinds.get("blocked", 0), "nudge": kinds.get("nudge", 0),
            "unknown_kinds": sorted(k for k in kinds if k not in {"start", "report", "review_request", "review_ok", "review_ng", "rework", "reassign", "escalate", "blocked", "wrap_up", "done"}),
            "root_extra": extra_desc, "unclear": sum(s["unclear"] for s in ss), "report_to_wrap_min": lag,
        })

    print("| プロジェクト | 名前 | 時間(分) | トークン(M) | セッション | やりとり | 差し戻し | やり直し | 入れ替え | 直し計 | 判断の依頼 | 止まっている | 人の手（手続き以外） | 迷った点 | 結果→終わりの指示(分) |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r in table:
        print(f'| {r["p"]} | {r["title"]} | {r["dur"]:.1f} | {r["tokens"]/1e6:.1f} | {r["sessions"]} | {r["msgs"]} | {r["review_ng"]} | {r["rework"]} | {r["reassign"]} | {r["remakes"]} | {r["escalate"]} | {r["blocked"]} | {len(r["root_extra"])} | {r["unclear"]} | {r["report_to_wrap_min"]:.1f} |')
    print()
    for r in table:
        if r["root_extra"] or r["unknown_kinds"] or r["sess_missing_tokens"]:
            print(f'- {r["p"]}: 人の手={r["root_extra"]} 画面に定義の無い種類={r["unknown_kinds"]} トークン欠け={r["sess_missing_tokens"]}')
    durs = [r["dur"] for r in table]
    toks = [r["tokens"] for r in table]
    print()
    print(f"時間: 中央値 {statistics.median(durs):.1f} 分・最小 {min(durs):.1f}・最大 {max(durs):.1f}")
    print(f"トークン: 中央値 {statistics.median(toks)/1e6:.1f}M・最小 {min(toks)/1e6:.1f}M・最大 {max(toks)/1e6:.1f}M・合計 {sum(toks)/1e6:.1f}M")
    md, mt = statistics.median(durs), statistics.median(toks)
    print("中央値との比（時間・トークン）: " + "・".join(f'{r["p"].split("-")[0]} {r["dur"]/md:.1f}倍/{r["tokens"]/mt:.1f}倍' for r in table))
    print(f"直しの回数の種類: {sorted({r['remakes'] for r in table})}")
    print(f"直し: 合計 {sum(r['remakes'] for r in table)}・あったプロジェクト {sum(1 for r in table if r['remakes'])}/{len(table)}")
    print(f"判断の依頼（escalate）: 合計 {sum(r['escalate'] for r in table)}・止まっている（blocked）: 合計 {sum(r['blocked'] for r in table)}")
    print(f"迷った点: 合計 {sum(r['unclear'] for r in table)}")
    print(f"人の手（手続き以外）: 合計 {sum(len(r['root_extra']) for r in table)}・あったプロジェクト {sum(1 for r in table if r['root_extra'])}/{len(table)}")


if __name__ == "__main__":
    main()
