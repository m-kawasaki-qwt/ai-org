---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p9-org-watch`、`T` = `P/teams/watch`、`W` = `/Users/maka343noshi/orca/workspaces/dev-tools/org-watch`（作業者が書く所。あなたは読んで動かすだけ）、`p8` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild`、`AO` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`。

1. `T/charter.md` 全体 — 照らす完了条件。指摘は番号で書く。
2. `P/charter.md` の「起きた問題」と「範囲」 — 元の記録と、書いてよい場所（worktree の中だけ・本体と `AO/projects/` は読むだけ・Google Chat の試しは「［試し］」付きで要る分だけ・automation は登録しない・git は触らない）。
3. `p8/log/events.log` の 15:30〜16:35 と `p8/log/msgs/b20186.md` の「うまくいかなかったこと」 — 問題 1・2 の実物。作業者の確かめがこの形を本当に再現しているかを見る。
4. `W/org/scripts/orgctl.py` の差分（`git -C W diff`） — 見るのは `member_state`・`cmd_watch`・`patrol_once`・`cmd_patrol`・`cmd_wait`（`worker-watch`）と、`_ProjectReader`・`build_snapshot`・`cmd_export`・`teardown_*`（`worker-audit`）。
5. `W/org/schema/snapshot.schema.json` の差分 — `orgctl export --check` が通るか。
6. `W/org/positions/auditor/position.md`・`W/claude/plugins/dev-tools/skills/org-project-new/SKILL.md`・`W/org/README.md`・`W/docs/todo/ai-org-plan.md` の差分 — 手順と決まりが新しい形に合っているか。決まったことを改めるときに元の文が消されていないか。

## 事業の文脈の要約

事業の案件ではない（組織の基盤）。

- 目的は「川崎さんが投げっぱなしにして、知らせが来たときだけ見ればよい」。見るのは 2 つ:
  - 見張りが、全員待ち（誰も相手に何も出していない）を止まりと判定して知らせ、本文から「誰が誰を待ち、何が出ていないか」が分かるか。待っているだけの人を「ループ?」と出さないか。その一方で、本当に止まった・ループした人を見逃す形になっていないか（待ちの判定を緩めすぎて、元の「止まっている?」「ループ?」が出なくなっていないか）。`wait` を打たずにターンを終えて止まった人が混じる全員待ちも拾うか。同じ詰まりで知らせが繰り返されないか。
  - 閉じるときの監査が手順に入り、監査役の出力が「起きたこと＋参照元」だけ（直し方を含まない）で、snapshot に載るか。p3 の前の形も読めたままか。
- 作業者の確かめは自分で動かして見る（報告を読むだけで通さない）。仮のプロジェクトは scratchpad か `$TMPDIR` に作る。Google Chat への送信はあなたはしない（`--dry` で見る）。
- p8 の `member.json`・`.waiting` は片づけで消えている。完了条件 2 の確かめは `events.log` から作り直した状態で行われているはず。どう作り直したかが報告にあり、あなたが同じ手順で再現できるかを見る。
- dev-tools の本体（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`）が書き換えられていないこと（`git -C <本体> status --short`）。
- 作業者 2 人が同じ `orgctl.py` を同時に直している。片方の差分がもう片方の受け持ちの関数を壊していないか、全体で `python3 -m py_compile` と主なサブコマンド（`watch`・`patrol --once --dry`・`export --check`・`digest`）が動くかを見る。

## これまでの経緯

- 2026-10-24 17:27 根っこが p9 を立て、PM がコーディネーターに切り方を相談した。チーム `watch` 1 つに、`worker-watch`（見張り・opus）と `worker-audit`（閉じるときの監査・sonnet）が並び、あなたが両方を見る。
