#!/usr/bin/env python3
"""叩き台 2・4・5 の根拠を、記録と snapshot.json から確かめる（標準ライブラリだけ）。

1. 写しの古さ: snapshot.json の generated_at より後に、動いているプロジェクトの events.log に何行増えたか
2. 結果の報告（PM → 川崎さん）の本文に、完了条件ごとの表・PR・worktree の言及があるか
3. snapshot にあって画面のコード（viewer/src）が読んでいない項目

使い方: python3 checks.py <ai-org のパス>
"""
import json
import re
import sys
from datetime import datetime
from pathlib import Path

A = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[5]
NOISE = {"ack", "notify_sent", "notify_recv", "notify_skipped", "patrol"}
snap = json.loads((A / "viewer/data/snapshot.json").read_text())
gen = datetime.fromisoformat(snap["generated_at"])
print(f"## 1. 写しの古さ（snapshot の書き出し {snap['generated_at']}・確かめた時刻 {datetime.now().astimezone():%Y-%m-%dT%H:%M:%S}）")
for p in snap["projects"]:
    if p["status"] != "open":
        continue
    rows = [l.split() for l in (A / "projects" / p["id"] / "log/events.log").read_text().splitlines()]
    rows = [r for r in rows if len(r) >= 5 and r[3] not in NOISE]
    after = [r for r in rows if datetime.fromisoformat(r[0]) > gen]
    members_now = {r[5] for r in rows if r[3] == "assign" and len(r) > 5}
    members_snap = set()
    def walk(c):
        for m in c["members"]:
            members_snap.add(m["id"])
        for ch in c["children"]:
            walk(ch)
    walk(p["tree"])
    print(f"- {p['id']}: 写しの後に増えた行 {len(after)}（全 {len(rows)} 行）・写しのメンバー {len(members_snap)} 人／記録のメンバー {len(members_now)} 人"
          + (f"・最後の行 {after[-1][0][11:19]} {after[-1][3]}" if after else ""))

print("\n## 2. 結果の報告（PM → 川崎さん）の本文")
for d in sorted((A / "projects").glob("p[1-9]-*"), key=lambda d: int(d.name.split("-")[0][1:])):
    ev = [l.split() for l in (d / "log/events.log").read_text().splitlines()]
    rep = [r for r in ev if len(r) >= 6 and r[3] == "report" and r[4] == "user" and r[2].endswith("/pm")]
    if not rep:
        print(f"- {d.name}: 結果の報告なし")
        continue
    body = (d / rep[0][5].removeprefix("msg=")).read_text()
    has_cc = bool(re.search(r"完了条件", body))
    cc_table = bool(re.search(r"^\|\s*#?\s*\|\s*(条件|完了条件)", body, re.M))
    pr = sorted(set(re.findall(r"PR\s*#?\d+|PR", body)))
    wt = "worktree" in body
    partial = bool(re.search(r"未確認|確かめる|残り|まだ|閉じるときに", body.split("\n## ")[1] if "\n## " in body else body))
    print(f"- {d.name}（{rep[0][1]}）: 完了条件の言及 {has_cc}・完了条件ごとの表 {cc_table}・PR の言及 {bool(pr)}・worktree の言及 {wt}・Summary に保留の語 {partial}・本文 {len(body)} 字")

print("\n## 3. snapshot にあって画面が読んでいない項目")
src = "".join(p.read_text() for p in (A / "viewer/src").rglob("*") if p.is_file())
for k in snap:
    if k not in src:
        v = snap[k]
        n = len(v) if isinstance(v, (list, dict)) else v
        print(f"- {k}: 画面のコードに出てこない（件数・値 {n}）")
print(f"- totals: {snap['totals']}")
