---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild`、`T` = `P/teams/viewer`、`A` = `/Users/maka343noshi/orca/workspaces/ai-org/viewer-v2`（ビューア。読むだけ・動かすだけ）、`O` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/org`（雛形。読むだけ）。

1. `T/charter.md` 全体 — 照らす完了条件。指摘は番号で書く。
2. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md` の「画面ごとの指摘」「UI 全体の指摘」 — 作業者の対応表が全部を拾っているかを、こちらの原文で突き合わせる。
3. `O/common/ui/checklist.md` の「B」「C」と「p5 の 5 枚に当てた結果」 — 判定の番号と、前回どこが いいえ だったか。
4. `O/common/screen-check.md` 全体 — 自分で撮る手順と、通らないときの書き方。
5. `A/tools/org_timeline.py` の docstring と `KIND_STYLE` — 時系列の図が、これより構造が読めるかの比べる相手。

## 事業の文脈の要約

事業の案件ではない。使う人は川崎さん 1 人（あなたに付く `kawasaki` のペルソナそのもの）。PC・900〜1800px・ダーク。

- 見る順は 2 段:
  1. **`design.md`（`T/design.md`）を B-01〜B-09 に照らす。** 画面・要素・一覧の列ごとに「何を判断するために、なぜここに出すか」が書けているか。パフォーマンス・監査の画面が「何を判断する画面か」を言えているか（言えないなら外していてよい）。時系列の図の節に、帯・線・入れ子・200 前後のイベントでの読みやすさがあるか。通る前に作業者は組み立てない決まり。
  2. **画面を自分で撮り（待ち受けは 4392 番、サンドボックスの外）、C-01〜C-27 とペルソナの判定の問いに照らす。** 900 と 1800 の両方、全画面。`design.md` に理由の無い要素が出ていないか。
- 時系列の図で読めるか確かめる例（どれも本体の記録にある）: p7（PM → コーディネーターの相談 → 返し → 合意 → チームを作る）、p6（チーム 2 つが並行・コーディネーター 2 人）、p5・p3・p2（`review_ng` → 直し → リーダーの `rework`）、p1（PM の入れ替え）。図だけを見て、その流れを言葉で言えるか。言えなければ C-10 で いいえ。
- フィードバックの対応表に、原文の指摘が 1 つでも抜けていたら完了条件 2 で `review_ng`。
- データは `A/viewer/data/snapshot.json`（作業者が書き出したもの）。古いと思えば、作業者の `review_request` にある export の 1 行で自分で書き出し直してよい（書き出し先は scratchpad にして、`A` は書き換えない）。

## これまでの経緯

- p5 のレビュアーは、記録の形から作った画面を承認し、川崎さんに届かなかった（上の 2。checklist の「p5 の 5 枚に当てた結果」に いいえ の並びがある）。あなたは p6 で足した「ペルソナで見るレビュアー」の最初の実例。
