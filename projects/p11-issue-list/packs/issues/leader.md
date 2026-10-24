---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p10-viewer-ideas/**
  - ~/.claude/projects/**
---

## 読む資料

`AO` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`、`P` = `AO/projects/p11-issue-list`、`T` = `P/teams/issues`、`DT` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`。

1. `T/charter.md` 全体 — チームの完了条件。中間の確かめ（下の「段取り」）もここにある。
2. `P/charter.md` の「目的」「範囲」 — 材料の 4 種類、書いてよい場所（`P` の中だけ）、p10 は材料に含めない、数はスクリプトで数える。
3. `DT/docs/todo/ai-org-plan.md` の決定ログ 2026-10-24「問題だけを控え、直し方は着手の直前に考える」の行 — なぜ直し方を書かないか。作業者・レビュアーと食い違ったときの拠り所。
4. `AO/projects/p9-org-watch/reports/audit/p9-org-watch.md` — 「起きたこと＋参照元」だけで書いた実物（形の手本。材料でもある）。

## 事業の文脈の要約

事業の案件ではない（組織の改善材料）。

- 受け取るのは川崎さん。`issues.md` を上から読んで「どれから直すか」を選ぶ。だから、題だけで中身が分かること・回数が数えた値であること・参照元を辿って原文に行けることが要る。直し方が混じると、着手の直前に考えるという決まり（資料 3）を崩す。
- 材料の原文（セッション報告の `unclear`、p3 の監査役の改訂案、「うまくいかなかったこと」）には、直し方・「〜すべき」が混じっている。作業者は起きたことだけを抜く。ここが一番崩れやすい。
- 「直った」は甘くなりやすい。雛形や orgctl が変わった記録があるだけでは「直った」にしない。証拠（直した記録＋その後のプロジェクトで同じことが起きていない）が揃わなければ「不明」。
- dev-tools の PR は #9〜#14 が main にマージ済み（2026-10-24 時点、`git -C DT log --oneline main`）。マージされていない変更は「直った」の根拠にならない。

## 段取り（受け持ちの線）

- 作業者 1 人が、抜き出し → まとめ → 直ったかの照合 → 数えて並べる、まで全部やる。書くのは作業者だけ（`issues.md`・中間ファイル・スクリプト）。レビュアーとあなたは読むだけ。
- **中間の確かめ（1 回目の `review_request`）**: 作業者は抜き出しが終わった時点で、まとめに入る前にレビュアーへ出す。見るのは網羅（材料の一覧と、ファイルごとの抜いた件数・抜かなかった理由）だけ。通ってから まとめに入る。この段の往復は、レビュアーの指摘の回数（通算 3 回まで）とは別に数える（`T/charter.md`）。
- 2 回目以降の `review_request` が `issues.md` 本体。
- PM へ出す前に、あなたも `issues.md` の上位 5 件を自分で参照元まで辿り、題と起きたことが原文と合うかを見る。

## これまでの経緯

- 2026-10-24 19:13 根っこが p11 を立てた。PM がコーディネーターに切り方を相談し、チーム `issues` 1 つ（リーダー・作業者 1・レビュアー 1）、抜き出しのあとに網羅を確かめる段を挟む形にした。
- 並行して p10（ビューアでの見せ方）が動いている。こちらは一覧の中身まで。p10 の記録は読まない。
