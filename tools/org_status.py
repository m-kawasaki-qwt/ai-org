#!/usr/bin/env python3
"""org_status — 根っこのプロジェクトを渡すと、コンポーネントの木とメンバーごとの最後の 1 行報告・状態を出す。

  python3 tools/org_status.py projects/p1-org-status [--json]

形と状態の決め方は dev-tools/org/scripts/orgctl.py に合わせてある（標準ライブラリだけ）。
  状態: 片づけ済み = member.json の status が closed、または member.json が無い（teardown が消した）
        未起動     = session_id が無い
        終わった   = 本人が送った最後の 1 行報告（NOISE_KINDS を除く）が done
        動いている = 上のどれでもない
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys

NOISE_KINDS = {"ack", "notify_sent", "notify_recv"}   # orgctl と同じ（読み物ではない行）


def load(p: pathlib.Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def parse_ts(s: str) -> dt.datetime:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))


def read_events(root: pathlib.Path) -> list[dict]:
    """events.log の 1 行: <ts> <hash> <from> <kind> <to> [detail]（orgctl の read_events と同じ分け方）。"""
    p = root / "log/events.log"
    out = []
    if not p.exists():
        return out
    for line in p.read_text(encoding="utf-8").splitlines():
        parts = line.split(" ", 5)
        if len(parts) < 5:
            continue
        out.append({"ts": parts[0], "id": parts[1], "from": parts[2], "kind": parts[3], "to": parts[4],
                    "detail": parts[5] if len(parts) > 5 else "-"})
    return out


def member_state(m: dict | None, last: dict | None) -> str:
    if m is None or m.get("status") == "closed":
        return "片づけ済み"
    if not m.get("session_id"):
        return "未起動"
    if last and last["kind"] == "done":
        return "終わった"
    return "動いている"


def build_member(root: pathlib.Path, name: str, mid: str, evts: list[dict], now: dt.datetime) -> dict:
    mp = root.parent / mid / "member.json"
    m = load(mp) if mp.exists() else None
    mine = [e for e in evts if e["from"] == mid and e["kind"] not in NOISE_KINDS]
    last = mine[-1] if mine else None
    report = None
    if last:
        mins = round((now - parse_ts(last["ts"])).total_seconds() / 60, 1)
        report = {"kind": last["kind"], "ts": last["ts"], "minutes_ago": mins, "to": last["to"]}
    return {"name": name, "id": mid, "position": m.get("position") if m else None,
            "model": m.get("model") if m else None, "state": member_state(m, last), "last_report": report}


def build_component(root: pathlib.Path, cid: str, evts: list[dict], now: dt.datetime) -> dict:
    comp = load(root.parent / cid / "component.json")
    return {"id": comp["id"], "kind": comp["kind"], "status": comp.get("status"),
            "members": [build_member(root, n, mid, evts, now) for n, mid in comp.get("members", {}).items()],
            "children": [build_component(root, c, evts, now) for c in comp.get("children", [])]}


def build_status(root: pathlib.Path, now: dt.datetime | None = None) -> dict:
    root = pathlib.Path(root).resolve()
    now = now or dt.datetime.now().astimezone()
    cj = root / "component.json"
    if not cj.exists():
        raise SystemExit(f"org_status: {root} に component.json が無い")
    return build_component(root, load(cj)["id"], read_events(root), now)


def render(tree: dict, indent: int = 0) -> str:
    pad = "  " * indent
    lines = [f"{pad}{tree['id']}（{tree['kind']}・{tree['status']}）"]
    for m in tree["members"]:
        r = m["last_report"]
        rep = f"最後の報告: {r['kind']} {r['ts']}（{r['minutes_ago']} 分前）" if r else "最後の報告: なし"
        who = f"{m['position']}・{m['model']}" if m["position"] else "ディレクトリなし"
        lines.append(f"{pad}  - {m['name']}（{who}）[{m['state']}]  {rep}")
    for c in tree["children"]:
        lines.append(render(c, indent + 1))
    return "\n".join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("root", help="根っこのプロジェクトのディレクトリ")
    p.add_argument("--json", action="store_true")
    a = p.parse_args(argv)
    tree = build_status(pathlib.Path(a.root))
    print(json.dumps(tree, ensure_ascii=False, indent=2) if a.json else render(tree))


if __name__ == "__main__":
    main()
