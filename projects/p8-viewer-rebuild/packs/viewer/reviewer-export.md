---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild`、`T` = `P/teams/viewer`、`D` = `/Users/maka343noshi/orca/workspaces/dev-tools/viewer-v2`（作業者が書く場所。読むだけ）、`B` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`（本体。比較用。読むだけ）、`R` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects`（export の元。読むだけ）。

1. `T/charter.md` の完了条件 5 — 照らす所。
2. `T/design.md` の「snapshot に要るもの」 — 足すべき項目の一覧。全部が snapshot に入ったか。
3. `D/CLAUDE.md` 全体 — dev-tools の決まり。
4. `D/org/scripts/orgctl.py` の export の節と `D/org/schema/snapshot.schema.json` — 差分は `git -C D diff` で見る（読むだけ）。

## 事業の文脈の要約

事業の案件ではない（組織の内部の道具）。見るのは export とスキーマだけ（画面は `reviewer-kawasaki` が見る）。

- 先に見る: 読むだけか（export の前後で `R` の中に新しくなったファイルが無い）・既存の関数の振る舞いを変えていないか（足すのはよい）・標準ライブラリだけか・`--check` が通るか・壊した写しで落ちるか。
- 自分でも打つ: `python3 D/org/scripts/orgctl.py export --projects R --out <scratchpad>/snapshot.json --check`。p1〜p8 のプロジェクト数・イベント数を記録を直接数えた値と突き合わせる。
- 足した項目の意味がスキーマの説明と合っているか（例: 入れ替えたメンバーの前後のつながりなら、p1 の PM の 2 回の assign で確かめる）。
- 書き方の好みは指摘にしない。

## これまでの経緯

- p5 で export とスキーマを足した（既存の関数は変えず +409 行）。今回はそこへの追加。
