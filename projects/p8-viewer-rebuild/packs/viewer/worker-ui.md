---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild`、`T` = `P/teams/viewer`（`design.md`・`screenshots/`・`thread.md` を置く所）、`A` = `/Users/maka343noshi/orca/workspaces/ai-org/viewer-v2`（あなたの workdir。書くのは `A/viewer/` と、要れば `A/tools/`）、`D` = `/Users/maka343noshi/orca/workspaces/dev-tools/viewer-v2`（orgctl の worktree。読むだけ）、`O` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/org`（雛形。読むだけ）。

1. `T/charter.md` 全体 — 完了条件。
2. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md` の「画面ごとの指摘」「UI 全体の指摘」 — 全部潰す。対応表の元。
3. `O/personas/kawasaki.md` 全体 — 使う人。`design.md` の「誰が・何を判断するか」はここから取る。
4. `O/common/ui/principles.md` 全体と `O/common/ui/checklist.md` の「B」「C」 — `design.md` は B-01〜B-09 に答える形で書く。出す前に C を当てる。
5. `O/common/screen-check.md` 全体 — 撮る道具（`O/common/ui/tools/screen-probe.mjs`）と撮り方の注意。
6. `A/tools/org_timeline.py` 全体 — 川崎さんが「はるかによかった」と言った帯の図。時系列の図はこれを発展させる。一度 `python3 A/tools/org_timeline.py <プロジェクト>` で HTML を出して見てよい（出力は scratchpad へ写して見る。本体の `projects/` に書かない）。
7. `D/org/schema/snapshot.schema.json` — いま snapshot にある項目（`Project.timeline` の `Event` に `from`・`to`・`component`・`kind`、`tree` の `Component`・`Member`）。
8. `A/viewer/src/lib/snap.ts` — snapshot の読み込み。使い回してよい。**ほかの `A/viewer/src/` は作り直す対象で、設計の出発点にしない**（p5 の、記録の形から作った画面）。

## 事業の文脈の要約

事業の案件ではない。使う人は川崎さん 1 人（ペルソナ `kawasaki`）。PC、幅 900〜1800px、ダーク。

- 何をしに開くか: AI 組織で「何が起きているか・何が止まっているか・自分が何を判断すればよいか」を数秒で掴み、気になった所だけ深掘りして元の記録（本文）まで辿る。ログ・YAML は自分で読める人なので、ログを HTML にしただけの画面には価値が無い。
- **順番: `design.md` が先。** `T/design.md` に B-01〜B-09 の答えを画面ごと・要素ごとに書き、`reviewer-kawasaki` へ `review_request`。通るまで画面を組み立てない（調べるための試し描きは scratchpad でよい）。
- `design.md` に必ず置く節:
  - 画面ごとに、何を判断する画面か。パフォーマンス・監査の画面も、言えなければ外す（外す理由を書く）。監査のまとめ方（要点 → 元の記録の 2 段）の設計は範囲外。いまあるデータで何を判断する画面かまで。
  - 一覧の列ごとに「なぜ詳細ではなく一覧に載せるか」。
  - 時系列の図: メンバーごとの帯・時刻順・誰から誰への線・入れ子（プロジェクト → チーム → メンバー）。イベントが 200 前後（p6）でも読めるか。見る例: p7（コーディネーターと PM の相談 → 返し → 合意）、p6（チーム 2 つが並行、コーディネーター 2 人）、p5・p3・p2（`review_ng` → 直し → `rework`）、p1（PM の入れ替え）。
  - **snapshot に要るもの**: 図・画面に要る項目のうち、いまの snapshot に無いもの。リーダー経由で `worker-export` が export を直す。あなたは `D` を書き換えない。
  - フィードバックの指摘ごとの対応（どの画面のどの要素で潰すか）。
- 組み立て: 技術（Astro のまま・図を SVG で自前で描く・ライブラリ）は決めてよい。`snapshot.json` だけを読む形は変えない。依存を足すなら理由を書く。
- データ: `python3 D/org/scripts/orgctl.py export --projects /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects --out A/viewer/data/snapshot.json --check` で書き出す（元は読むだけ）。p1〜p8 全部で崩れないこと。
- 動かし方: 最初に `npm ci --prefix A/viewer`（`~/.npm` の権限で落ちたら `--cache $TMPDIR/npm-cache`）。待ち受けは **4391 番**、サンドボックスの外。Playwright は scratchpad に入れる（repo の依存に入れない）。撮った画像と json は `T/screenshots/`。
- `review_request` の本文に: `design.md` のパス、撮った画像と json のパス（900・1800 の全画面）、C の いいえ が 0 になったこと（対象外の番号と理由）、フィードバックの対応表。

## これまでの経緯

- p5 で組織が作ったビューアは、川崎さんに「YAML・ログをそのまま HTML にした形」「時系列はログを縦に並べただけ」「一覧の列の理由が無い」と判定された（上の 2）。根っこのセッションのつなぎの直しで、ダーク・幅・短い名前・帯の図の下書き・Markdown の整形・ポインタは一部入っているが、作り直しの出発点にはしない。
- p6 で UI デザイナーの職種と `O/common/ui/` ができた。あなたがその最初の使い手。
