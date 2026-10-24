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

1. `T/charter.md` 全体 — 照らす完了条件。
2. `P/charter.md` の「材料」 — 叩き台 8 件。リサーチは、この 8 件と「ほかに無いか」に効く考え方を探す。
3. `O/personas/kawasaki.md` の「何をしに開くか」「嫌うこと」 — 取り入れる考え方を選ぶ基準（全部並べる道具の真似はしない）。
4. `R/projects/p8-viewer-rebuild/log/msgs/b20186.md` の「Summary」 — いまのビューアの 3 画面（いま／プロジェクト／決まりの直し候補）が何か。
5. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/claude/plugins/dev-tools/skills/gemini-api/SKILL.md` — Web 検索の道具 `gemini-api` の使い方。

## 事業の文脈の要約

事業の案件ではない。読み手は川崎さん 1 人（組織の持ち主・IT エンジニア）。ビューアは、AI の組織（PM・リーダー・作業者・レビュアーのセッションが 1 行報告でやりとりする）の中で何が起きているか・自分が何を判断すればよいかを、短い時間で掴むための画面。

- 書くもの: **`T/research.md`**。`worker-records` がこれを読んで、レポートの「外のリサーチから取り入れた考え方」に使う（あなたが直接 report.md を書くことはない）。
- 調べる相手の例: マルチエージェント・LLM の観測やトレースのビューア、CI のダッシュボード、分散トレースの UI、インシデント・オンコールの画面、変更の差分を先に見せる画面など。網羅は要らない。**この組織に効く考え方**を 8〜15 件。
- 1 件ごとの形: 考え方の名前（10 字程度）／どの道具が何をどう見せているか（2〜3 行）／出典（URL。公式のドキュメント・製品ページ・設計の記事を優先）／叩き台の何番に効くか、または叩き台に無い新しい案か／この組織に持ち込むときの注意（1 行）。
- 出典は実在を確かめる（開いて、書いた内容がそのページにあること）。確かめられなかったものは入れないか「未確認」と書く。
- 書いてよい場所は `T` の中だけ。git は触らない。
- できたら、リーダーへ `event report`（本文に research.md のパスと件数）。レビュアーへの review_request は出さない（report.md の中でまとめて見る）。

## これまでの経緯

- ビューアは p5 で作ったが、記録の形をそのまま画面にしたため川崎さんに届かず、p8 で作り直して「わかりやすい。時系列と往復が分かりやすい」と判定された。p10 はその次の改善案を探す。外の道具の「見せる量の多さ」より、「要点を先に・詳細は辿れる」に効くものを選ぶ。
