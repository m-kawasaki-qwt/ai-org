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

1. `T/charter.md` 全体 — 照らす完了条件。指摘は番号で書く。
2. `P/charter.md` の「目的」の材料 4 種類と「範囲」 — 網羅を見るときの元の一覧。
3. 材料そのもの（作業者と同じ。読むだけ）: `AO/projects/p1-*〜p9-*/reports/sessions/*.yaml` の `self`（56 本）、`AO/projects/p1-*〜p9-*/log/msgs/*.md`（226 本）と各 `log/events.log`、`AO/projects/p9-org-watch/reports/audit/p9-org-watch.md`、`JOB/company/system/ai-org/README.md` の「組織の直し待ち」。
4. 「直った」の照合の元: `git -C DT log main`、`DT/docs/todo/ai-org-plan.md` の決まったことと決定ログ。
5. 作業者の成果物: `T/work/`（中間ファイル・件数表・対応表）、`P/scripts/`、`P/issues.md`。

## 事業の文脈の要約

事業の案件ではない（組織の改善材料）。

- 読むのは川崎さんで、`issues.md` から「どれから直すか」を選ぶ。直し方が混じる・回数が違う・参照元が辿れない・別の問題が 1 件にまとめられている、のどれも選び方を誤らせる。
- **直し方を書かない**の拠り所は `DT/docs/todo/ai-org-plan.md` の決定ログ 2026-10-24「問題だけを控え、直し方は着手の直前に考える」。原文（`unclear`・p3 の改訂案）に直し方が混じっているので、写しただけの件に残りやすい。全件を見る（完了条件の 5）。目で全件を読むのに加え、「すべき」「にする」「改める」「足す」などの言い回しをスクリプトで拾って当たりを付けてよい（拾えた語だけで通さない）。
- 参照元の抜き取り（完了条件の 6）は、選び方を作業者に寄せないため、乱数（種を `review_ok` に書く）で 10 件以上を選び、ファイルと行を開いて中身が合うかを見る。
- まとめ方: 「まとめたものが本当に同じか」「別に残したものが本当に別か」を、少なくとも回数の上位と、題の似た件どうしで見る。
- 「直った」は、直した記録（main にマージ済み）**かつ**その後のプロジェクトで起きていない、の両方が揃っているかを全件で見る。片方だけで「直った」にしていれば指摘。
- 数は、`P/scripts/` を自分で回して `issues.md` の数と合うかを見る。
- あなたは書かない（`P` の中も、作業者の成果物も）。確かめるためのスクリプトは scratchpad か `$TMPDIR` に置く。git・orgctl の書き出す種類のコマンドは打たない。

## 段取り

- 1 回目の `review_request` は抜き出しの網羅だけ: 材料の 4 種類が全部入っているか、件数表で 0 件のファイルの理由が妥当か、`unclear`・`not_done`・「うまくいかなかったこと」の見出しの揺れ・`review_ng`／`rework`／`blocked`／`escalate` の本文を取りこぼしていないか（数本を自分で開いて突き合わせる）。この段の往復は、通算の指摘の回数（3 回まで）とは別に数える（`T/charter.md`）。
- 2 回目以降が `issues.md` 本体（完了条件の全部）。

## これまでの経緯

- 2026-10-24 19:13 根っこが p11 を立てた。PM とコーディネーターで、チーム `issues` に作業者 1 人、抜き出しのあとにあなたが網羅を見る段を挟む形にした。
- p9 の監査では、受け持ちが review_ng で初めて決まった件があった。このチームで書くのは作業者だけ、あなたとリーダーは読むだけ。
