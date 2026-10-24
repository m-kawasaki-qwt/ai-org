#!/usr/bin/env python3
"""p1〜p9 の events.log から、プロジェクト全体で 5 分以上だれも何も出さなかった間（静かな間）を拾う。

叩き台 3（誰が誰を待っているか）の根拠に使う。間の直前の行と、間を破った行を出す。
数えるのは配送記録（ack・notify_*・patrol）を除いた行。ライフサイクルの行（assign・launch・teardown）も「出した」に数える。

使い方: python3 gaps.py [ai-org の projects のパス] [分（既定 5）]
"""
import sys
from datetime import datetime
from pathlib import Path

PROJ = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[5] / "projects"
TH = float(sys.argv[2]) if len(sys.argv) > 2 else 5.0
NOISE = {"ack", "notify_sent", "notify_recv", "notify_skipped", "patrol"}

dirs = sorted([d for d in PROJ.iterdir() if d.is_dir() and d.name[:3] in {f"p{i}-" for i in range(1, 10)}],
              key=lambda d: int(d.name.split("-")[0][1:]))
total = 0
for p in dirs:
    rows = []
    for line in (p / "log/events.log").read_text().splitlines():
        f = line.split()
        if len(f) >= 5 and f[3] not in NOISE:
            rows.append((datetime.fromisoformat(f[0]), f))
    for (t0, a), (t1, b) in zip(rows, rows[1:]):
        gap = (t1 - t0).total_seconds() / 60
        if gap >= TH:
            total += 1
            short = lambda f: f"{f[0][11:19]} {f[2].replace(p.name + '/', '')} {f[3]} {f[4].replace(p.name + '/', '')}"
            print(f"{p.name}\t{gap:5.1f} 分\t前: {short(a)}\t破った: {short(b)}")
print(f"\n{TH:g} 分以上の静かな間: {total} 件")
