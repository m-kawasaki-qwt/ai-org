---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild`、`T` = `P/teams/viewer`、`D` = `/Users/maka343noshi/orca/workspaces/dev-tools/viewer-v2`（あなたの workdir。書くのは `D/org/scripts/orgctl.py` の export と `D/org/schema/snapshot.schema.json` だけ）、`A` = `/Users/maka343noshi/orca/workspaces/ai-org/viewer-v2`（ビューアの worktree。書くのは `A/viewer/data/snapshot.json` の書き出しだけ）、`R` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects`（export の元。読むだけ）。

1. `T/charter.md` 全体 — 完了条件（とくに 5）。
2. `D/CLAUDE.md` 全体 — dev-tools の決まり。
3. `D/org/scripts/orgctl.py` の export の節（`# ---- export` から `cmd_export` まで）と、そこから呼ぶ `read_events`・`member_state`・`NOISE_KINDS` — 直す所。
4. `D/org/schema/snapshot.schema.json` — 形の機械の正。項目を足したらここも足す。
5. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/schema.md` の「決めたこと」 — 前回の決めごと（数え方）。
6. `T/design.md` の「snapshot に要るもの」 — リーダーが `start` で渡す。直すのはこれが来てから。

## 事業の文脈の要約

事業の案件ではない（組織の内部の道具）。ビューアは `snapshot.json` だけを読むので、画面に要るのに snapshot に無い項目は、export とスキーマを直して足す。

- 最初（`design.md` が通る前）にやること: `python3 D/org/scripts/orgctl.py export --projects R --out A/viewer/data/snapshot.json --check` で p1〜p8 を書き出して通るか確かめ、時系列の図（メンバーごとの帯・誰から誰への線・入れ子・入れ替え）に要りそうで今は無いもの・あやしいもの（例: 入れ替えたメンバーの前後のつながり、チームの中のメンバーの並び、ペルソナ、開いているプロジェクトの扱い）をリーダーへ `report` で出す。**直すのは `design.md` の要るものが来てから。**
- 直すとき: export は読むだけ（`R` に何も書かない。前後で `R` の中に新しくなったファイルが無いことを確かめる）。既存の関数の振る舞いを変えない（足すのはよい）。標準ライブラリだけ。足した項目はスキーマにも足し、`--check` が通ること。壊した写しで `--check` が落ちることも見る。
- 書き出した `A/viewer/data/snapshot.json` で、p1〜p8 のプロジェクト数・イベント数が記録を直接数えた値と合うことを確かめる。
- `review_request` は `reviewer-export` へ。本文に、足した項目・スキーマの差分・`--check` の結果・読むだけの確かめ方。

## これまでの経緯

- p5 で export とスキーマを足した（+409 行、既存の関数は変えず）。そのあと根っこのセッションがビューアのつなぎの直しを入れている（snapshot の形が p5 の `schema.md` から動いている可能性があるので、`D` のスキーマを正とする）。
