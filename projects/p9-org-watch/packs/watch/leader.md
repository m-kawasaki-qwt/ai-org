---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p9-org-watch`、`T` = `P/teams/watch`（チームのディレクトリ）、`W` = `/Users/maka343noshi/orca/workspaces/dev-tools/org-watch`（dev-tools の worktree。作業者が書く所）、`p8` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild`（読むだけ）。

1. `T/charter.md` 全体 — 照らす完了条件。
2. `P/charter.md` の「起きた問題」「範囲」 — 問題 1〜4 の元の記録と、書いてよい場所・Google Chat の試しの決まり。
3. `p8/log/events.log` の 16:25〜16:31 と `p8/log/msgs/b20186.md` の「うまくいかなかったこと」 — 問題 1 の実物。あなた自身が同じ形を起こさないためにも読む。
4. `W/org/scripts/orgctl.py` の `member_state`・`cmd_watch`・`patrol_once`・`cmd_patrol`・`cmd_wait` と、`_ProjectReader.audits`・`build_snapshot` — 作業者の受け持ちの境目（下の「回し方」）を確かめるため。読むだけ。
5. `W/claude/plugins/dev-tools/skills/org-project-new/SKILL.md` の 5 と 7 — 直される手順。

## 事業の文脈の要約

事業の案件ではない（組織の基盤。使う人は川崎さんと根っこのセッション）。

- 目的は「川崎さんが投げっぱなしにして、知らせが来たときだけ見ればよい」。見張り（watch・patrol）の判定と常駐、閉じるときの監査の 2 つを、1 つの worktree・1 つのファイル（`orgctl.py`）で直す。
- 編成（コーディネーターの案）:
  - `worker-watch`（職種 `engineer`・opus・`--workdir W`）: 完了条件の 1・2・3（見張りの判定・全員待ちの検出・`watch` の出し分け・全プロジェクトを 1 回見る形・automation の定義・org-project-new の 5）。
  - `worker-audit`（職種 `engineer`・sonnet・`--workdir W`）: 完了条件の 4（監査役の立場・閉じる手順の段・出力の置き場・export とスキーマ・org-project-new の 7）と、最後に 5（README・プランの通しの揃え）。
  - `reviewer`（職種 `engineer`・opus）: 両方を見る。
  - パックは `P/packs/watch/<名前>.md`（`worker-watch.md`・`worker-audit.md`・`reviewer.md`）。
- 回し方の順:
  1. 2 人の作業者を並べて始める。`orgctl.py` の受け持ちを分ける: `worker-watch` は定数（`WAITING_SEC`・`STALL_MIN`・`LOOP_MIN`）・`cmd_wait`・`member_state`・`cmd_watch`・`patrol_once`・`cmd_patrol`・`main()` の引数。`worker-audit` は `_ProjectReader`（`audits` など）・`build_snapshot`・`cmd_export`・`teardown_*`・`org/schema/snapshot.schema.json`。`main()` に引数が要るときは `worker-audit` からあなたへ言わせ、`worker-watch` に足させる（同じ所を 2 人が直さない）。
  2. 共有の文書は節で分ける: org-project-new の 5 と README の見張りの節は `worker-watch`、7 と監査の節は `worker-audit`。プランの決まったこと 22 の補足は、`worker-watch` の承認のあとに `worker-audit` が通して書く（併記。元の文を消さない）。
  3. 両方の承認が出たら、`worker-audit` に README とプランの通しの揃え（完了条件 5）を `start` で渡す。
  4. 全員の `done` を読んだら、**その場で PM へ `report` を出す**（p8 で、リーダーがここで `wait` に戻って全員が待つ形になった。このプロジェクトが直す問題そのもの）。
- 割れやすい所: 「待っている」の判定（何をもって全員待ちとするか、どこまでを止まりとするか）。作業者とレビュアーで割れたら、charter の完了条件 1・2 の確かめ（仮のプロジェクト・p8 の再現）で通るかで裁定する。
- 作業者の「`.waiting` が残っていないので p8 では確かめられない」は取り合わない。p8 の `events.log` から当時の状態を scratchpad に作り直せば確かめられる（member.json・`.waiting` は teardown で消えているので、作り直す前提）。
- dev-tools の本体（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`）を誰も書き換えていないことを、PM へ出す前に `git -C <本体> status --short` で確かめる。

## これまでの経緯

- 2026-10-24 17:27 根っこが p9 を立て、PM を起こした。PM がコーディネーターに切り方を相談し、チーム 1 つ（作業者 2・レビュアー 1）で合意した。PM は charter の完了条件 1 に「ターンを終えて止まっている場合も含む・同じ詰まりで知らせを繰り返さない」、4 に「p9 を閉じるとき PM が打つコマンドを報告に」を足した。
- 前のプロジェクト（p8）の閉じ際、全員が待つ形で止まり、見張りは止まりと判定しなかった（`p8/log/events.log` 16:25〜16:31）。p6 でも研究チームのリーダーが約 9 分、同じ形で止まった。
- 監査役が動いたのは p3 だけ（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p3-org-visibility/log/events.log` の 13:36 以降）。いまの監査役の出力は「改訂案」の形で、export はその節を読んでいる。今回は「起きたこと＋参照元」に変える。
