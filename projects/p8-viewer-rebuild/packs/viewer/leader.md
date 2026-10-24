---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild`、`T` = `P/teams/viewer`（チームのディレクトリ。`design.md`・`screenshots/`・`thread.md` はここ）、`A` = `/Users/maka343noshi/orca/workspaces/ai-org/viewer-v2`（ビューアの worktree）、`D` = `/Users/maka343noshi/orca/workspaces/dev-tools/viewer-v2`（orgctl の worktree）、`O` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/org`（雛形。読むだけ）。

1. `T/charter.md` 全体 — 照らす完了条件。
2. `P/charter.md` の「目的」「範囲」 — 川崎さんの言葉と、書いてよい場所・ポート。
3. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md` の「画面ごとの指摘」「UI 全体の指摘」 — 対応表の行の元。指摘は全部で 1 行ずつにする。
4. `O/personas/kawasaki.md` 全体 — あなたが PM へ出す前に問う「判定の問い」。
5. `O/common/screen-check.md` 全体 — 撮る道具・撮り方の注意（サンドボックスの外・scratchpad に Playwright）。
6. `O/common/ui/checklist.md` の「B」「C」 — `design.md` と画面を照らす番号。
7. `A/tools/org_timeline.py` の冒頭の docstring と `KIND_STYLE` — 川崎さんが「はるかによかった」と言った帯の図の元。時系列の図の出来をこれと比べる。

## 事業の文脈の要約

事業の案件ではない（組織の内部の道具。使う人は川崎さん 1 人、PC で 900〜1800px）。

- p5 の失敗の筋: 記録の形（YAML の木・ログの行）から画面を作り、レビュアーは承認、リーダーが後から rework、それでも川崎さんは「ログを見るのと変わらない」と判定した。今回は **`design.md` を先に通してから組み立てる**。`design.md` がレビュアーに通る前に、作業者（UI）に画面の組み立てを始めさせない。
- 編成（コーディネーターの案）:
  - `worker-ui`（職種 `ui-designer`・opus・`--workdir A`）: `design.md` を書き、`A/viewer/` を組み立て、撮る。
  - `worker-export`（職種 `engineer`・sonnet・`--workdir D`）: `D/org/scripts/orgctl.py` の export と `D/org/schema/snapshot.schema.json` を直す。
  - `reviewer-kawasaki`（職種 `ui-designer`・ペルソナ `kawasaki`・opus）: `design.md` と画面を見る。
  - `reviewer-export`（職種 `engineer`・sonnet）: export・スキーマを見る（読むだけか・既存を壊さないか・`--check` が通るか）。
  - パックは `P/packs/viewer/<名前>.md`（`worker-ui.md`・`worker-export.md`・`reviewer-kawasaki.md`・`reviewer-export.md`）。
- 回し方の順:
  1. `worker-ui` に `design.md` を書かせる。同時に `worker-export` には「いまの snapshot で p1〜p8 を書き出し、`--check` を通し、項目の一覧と、時系列の図に要りそうで無いもの」の洗い出しをさせる（直すのはまだ）。
  2. `design.md` を `reviewer-kawasaki` が B に照らして通す。`design.md` の「snapshot に要るもの」の節を、あなたが `worker-export` へ `start` で渡す（作業者どうしは直接やりとりしない）。
  3. `worker-export` が直して `reviewer-export` が通す → `worker-ui` が実データで組み立て、撮って `reviewer-kawasaki` へ。
  4. あなたが撮り直して判定し、PM へ。
- 割れやすい所: 時系列の図。`design.md` の時系列の節が B で 2 回通らなければ、ヒントを変えた UI デザイナーをもう 1 人並べてよい（同じヒントで並べない）。
- 作業者の「既存がこうなっていたので」「snapshot に無いので」は取り合わない。snapshot に無いなら export を直す（範囲の中）。
- ポート: `worker-ui` 4391・`reviewer-kawasaki` 4392・あなた 4393・PM 4394。4390 は川崎さんの本体のビューアなので使わない。
- export の元は本体の `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects`（読むだけ。p8 自身も入る）。書き出し先は `A/viewer/data/snapshot.json`。

## これまでの経緯

- 2026-10-24 p5 で組織がビューアを作り、川崎さんが「出せる水準に届いていない」と判定（上の 3）。根っこのセッションがつなぎの直し（ダーク・幅・短い名前・帯の図・Markdown の整形・ポインタ）を入れたが、時系列の図の作り込み（入れ子・やりとりの構造）、パフォーマンスと監査の「何を判断する画面か」は残っている。
- 2026-10-24 p6 で UI デザイナー・ペルソナのレビュアー・撮って確かめる基準を足し、p7 でコーディネーターの役割を改めた。p8 はそれを使う最初の画面の案件。
- 2026-10-24 PM がコーディネーターに相談し、チーム 1 つ（このチーム）で合意した。
