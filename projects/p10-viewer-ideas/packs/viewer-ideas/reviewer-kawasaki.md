---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`R` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`、`P` = `R/projects/p10-viewer-ideas`、`T` = `P/teams/viewer-ideas`、`O` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/org`（雛形。読むだけ）。

1. `T/charter.md` 全体 — 照らす完了条件。指摘は番号で書く。
2. `P/charter.md` の「材料」 — 叩き台 8 件の原文。判定の表に 8 件全部があるか突き合わせる。
3. `P/report.md`（作業者が書く）と、そこから貼られた `T/screenshots/`・リンクされた `T/evidence.md` — 見る成果物。
4. `T/research.md` — report.md の外の出典の裏取りに使う（出典の URL は report.md から抜き取りで開く）。
5. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md` の「画面ごとの指摘」「UI 全体の指摘」 — 川崎さんが何を嫌うか・何に困ったかの原文。案の「価値」がこれに接地しているか。

## 事業の文脈の要約

事業の案件ではない。読み手は川崎さん 1 人（あなたに付く `kawasaki` のペルソナそのもの）。**画面は作らないチーム**なので、`design.md` と screen-probe での判定は対象外。ペルソナの判定の問いは、**レポートそのもの**に当てる。

- 見ること:
  1. **読み手として（完了条件 6）:** report.md を頭から開いて、Summary と上位 3〜5 件だけで「何を改善できるか・なぜか・どれからやるか」が 1 分で掴めるか。案の本文を開いて回らないと結論が分からない、文が長い、同じことが繰り返される、は指摘する。画像が表示され、どこを変えるかが分かるか。
  2. **根拠（完了条件 2）:** 案ごとの問題に、どのプロジェクトのどの記録か（ファイルか hash）が付いているか。**10 件以上を抜き取りで開き**、書いてあることがそこにあるかを確かめる（記録は `R/projects/p*/log/`・`reports/sessions/`）。根拠の無い案に「根拠なし（推測）」が付いているか。数字にスクリプト（`T/scripts/`）があるか。
  3. **叩き台（完了条件 3）:** 8 件全部に 採る／採らない／形を変える と理由があるか。叩き台に無い案があるか。
  4. **出典（完了条件 4）:** 外の考え方に URL が付いているか。3 件以上開いて、書いた内容がそこにあるか。
  5. **範囲:** 実装していないか（`R/viewer/`・dev-tools・job が変わっていないか。`git -C /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org status` で見る）。監査の指摘・unclear の一覧そのものを作っていないか（それは p11 の仕事。こちらは見せ方まで）。
- 承認の本文に、抜き取りで開いた根拠・出典の一覧と、ペルソナの判定の問いごとの判定を書く。

## これまでの経緯

- p5 のレビュアーは、記録の形から作った画面を承認し、川崎さんに届かなかった。p8 で「ペルソナで見るレビュアー」が初めて画面を判定し、川崎さんに通った。あなたは今回、画面ではなくレポートをその目線で見る。
