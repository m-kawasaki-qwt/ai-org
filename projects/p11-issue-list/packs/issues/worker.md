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

`AO` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`、`P` = `AO/projects/p11-issue-list`、`T` = `P/teams/issues`、`DT` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`、`JOB` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job`。

1. `T/charter.md` 全体 — 完了条件。
2. 材料（読むだけ）:
   - `AO/projects/p1-*〜p9-*/reports/sessions/*.yaml`（56 本）の `self` の `unclear`・`not_done`。`machine` は読まなくてよい（`machine.log` の会話ログは開かない）。
   - `AO/projects/p1-*〜p9-*/log/msgs/*.md`（226 本）。「うまくいかなかったこと」の節（見出しの言い方が揺れる。「・残ること」「（決まり・道具）」「試走で〜」など）と、`events.log` で種類が `review_ng`・`rework`・`blocked`・`escalate` の行の本文。どの本文が何の種類かは同じプロジェクトの `log/events.log`（`msg=log/msgs/<hash>.md`）で引く。
   - `AO/projects/p3-org-visibility/log/msgs/` のうち監査役の改訂案（`events.log` で送り手が監査役の行）。
   - `AO/projects/p9-org-watch/reports/audit/p9-org-watch.md` の 4 件。
   - `JOB/company/system/ai-org/README.md` の「組織の直し待ち」の節と、「の時点」の節の「残ったこと」「申し送り」。
3. 「直った」の照合（読むだけ）: `git -C DT log main -- org/ claude/plugins/dev-tools/skills/org-project-new/`、`DT/docs/todo/ai-org-plan.md` の「決まったこと」と決定ログ、`git -C AO log main`。
4. 形の手本: `AO/projects/p9-org-watch/reports/audit/p9-org-watch.md`（起きたことと参照元だけで書いた実物）。

## 事業の文脈の要約

事業の案件ではない（組織の改善材料）。

- 読むのは川崎さんで、`issues.md` を上から見て「どれから直すか」を選ぶ。題だけで中身が分かる・回数は数えた値・参照元から原文に行ける、が要る。
- **直し方は書かない**（`DT/docs/todo/ai-org-plan.md` の決定ログ 2026-10-24「問題だけを控え、直し方は着手の直前に考える」）。原文に「〜すべき」「〜にする」「改訂案」が混じっていても、起きたこと（誰が・何をして・どうなった）だけを抜く。
- 書いてよいのは `P` の中だけ。置き場の目安: 一覧は `P/issues.md`、スクリプトは `P/scripts/`（作り直すときに同じ手順で回せるように）、中間ファイルは `T/work/`。git は触らない。orgctl は `digest` 以外打たない（`export` などは書き出す先を持つ）。
- 数（件数・回数）はスクリプトで数える。手で数えた数を `issues.md` に載せない。
- 「直った」は、直した記録（main にマージ済みの PR・コミット、またはプロジェクト）があり、**かつ**そのあとに閉じたプロジェクトで同じことが起きていないときだけ。片方しか無ければ「不明」。直した記録が無く、あとでも起きているものは印なし（起きている）。
- 同じプロジェクトの中で、複数の人が同じことを書いているもの（例: p9 の受け持ちの線をリーダー・レビュアー・作業者が書いた）は、回数の数え方を末尾の「作り方」に書く（「プロジェクト数」と「記録の数」を分けて出すなど。どちらで並べたかを書く）。
- job の README の「組織の直し待ち」は、p8 の記録と同じ件を指している。根っこの控えは別の出どころとして参照元に足すが、回数を二重に数えない。

## 段取り

1. 抜き出し（スクリプト）→ `T/work/` に中間ファイル（1 行 1 件、参照元のファイルと行つき）と、材料ごとの件数表（ファイル・抜いた件数・0 件ならその理由）。**ここで 1 回目の `review_request` をレビュアーへ**（見てもらうのは網羅だけ）。通ってから 2 へ。
2. まとめ（同じ中身を 1 件に。判断）。中間ファイルの各行が `issues.md` のどの件に入ったか、または入れなかった理由（問題ではない・p10 など）を対応表に残す。
3. 直ったかの照合。「直った」には根拠（PR 番号・コミット・プロジェクト）を、「不明」には何が足りなかったかを 1 行。
4. 数えて並べて `P/issues.md`。末尾に作り方。2 回目の `review_request`。

## これまでの経緯

- 2026-10-24 19:13 根っこが p11 を立てた。PM とコーディネーターで、チーム `issues` に作業者 1 人、抜き出しのあとにレビュアーが網羅を見る段を挟む形にした。
- p9 から閉じるときの監査が手順に入った（監査役が出したのは p3 と p9 だけ）。p4〜p8 は監査が無いので、セッション報告と「うまくいかなかったこと」が主な材料。
