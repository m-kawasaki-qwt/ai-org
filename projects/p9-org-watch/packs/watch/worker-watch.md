---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p9-org-watch`、`T` = `P/teams/watch`、`W` = `/Users/maka343noshi/orca/workspaces/dev-tools/org-watch`（あなたの `--workdir`。書くのはここだけ）、`p8` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild`（読むだけ）。

1. `T/charter.md` 全体 — 照らす完了条件（あなたの受け持ちは 1・2・3）。
2. `P/charter.md` の「起きた問題」の 1〜3 と「範囲」 — 元の記録の場所、Google Chat の試しの決まり。
3. `W/org/scripts/orgctl.py` の定数（41〜49 行あたり）・`cmd_event`（相手が wait 中かの判定）・`cmd_wait`・`member_state`・`cmd_watch`・`notify_user`・`patrol_once`・`cmd_patrol`・`main()` の `patrol` / `watch` — 直す所。
4. `p8/log/events.log` の 15:30〜16:35 と `p8/log/msgs/b20186.md` の「うまくいかなかったこと」、`p8/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml` の unclear — 問題 1・2 の実物。完了条件 2 の確かめの元。
5. `W/claude/plugins/dev-tools/skills/org-project-new/SKILL.md` の 5 — 常駐に切り替わったあとの扱いに直す。
6. `W/docs/todo/ai-org-plan.md` の決まったこと 22 と決定ログの 2026-10-24 の行 — 常駐の決まり（Orca の automation にスクリプトだけで回る 1 本）。
7. `orca automations create --help`・`orca automations list`（読むだけ。`create`・`edit`・`run` は打たない） — automation の定義の書き方。
8. `W/claude/plugins/dev-tools/skills/gchat-notify/SKILL.md` — 送り方と `--dry`。

## 事業の文脈の要約

事業の案件ではない（組織の基盤）。

- 目的は「川崎さんが投げっぱなしにして、知らせが来たときだけ見ればよい」。見張りが本当の止まりを拾い、待っているだけの人を止まりと出さないこと。
- p8 で起きた形: リーダーがメンバー 4 人の `done` を読んだあと PM へ `report` を出さずに `wait` に戻り、PM もリーダーを待っていた。誰も相手に何も出しておらず、全員が `wait` の中。`watch` はリーダーを「進んでいる」、PM を 30 分以上「ループ?」と出し、`patrol` は知らせなかった。
- 知らせの本文から「誰が誰を待っていて、何が出ていないか」が分かること（例: リーダーは配下の `done` を全部受けたが、PM へ `report` を出していない）。
- 全員待ちには、`wait` の中にいる人だけでなく、`wait` を打たずにターンを終えて止まっている人が混じる形も含む（PM が charter に足した）。同じ詰まりで知らせを繰り返さない（詰まりが解けて、また詰まったら知らせてよい）。
- 常駐は、開いている**全プロジェクト**を 1 回見て終わる形を CLI に持ち、それを Orca の automation に載せる定義を書く。**登録はしない**（根っこが川崎さんの承認を取って登録する）。
- `orgctl.py` は `worker-audit` も同時に直している。あなたの受け持ちは上の 3 に挙げた関数と定数と `main()`。`_ProjectReader`・`build_snapshot`・`cmd_export`・`teardown_*`・スキーマは触らない。編集は Edit で差分だけ（ファイル全体の書き直し・整形をかけない）。Edit が「読んだあとに変わった」と止まったら、読み直してから直す。
- 共有の文書: org-project-new の 5 と、`W/org/README.md` の見張りの節はあなた。7・監査の節・プランの通しの揃えは `worker-audit`。
- 確かめ:
  - 完了条件 1: scratchpad か `$TMPDIR` に仮のプロジェクトを作り、全員待ちの形を作って patrol が知らせることを見る。Google Chat（`gchat-notify` の slug `ai-org`）へ送るのは確かめに要る分だけ、本文の頭に「［試し］」。それ以外の試しは `--dry`。
  - 完了条件 2: p8 の `member.json`・`.waiting` は片づけで消えている。`events.log` から 16:30 ごろの状態を scratchpad に作り直して確かめる（「残っていないので確かめられない」で止めない）。
- 動いている組織は dev-tools の本体の orgctl を使っている。本体は読むだけ。worktree の orgctl は、本体が書いた記録（`events.log`・`member.json`）をそのまま読めること。

## これまでの経緯

- 2026-10-24 17:27 根っこが p9 を立て、PM がコーディネーターに切り方を相談した。チーム `watch` 1 つに、あなた（見張り）と `worker-audit`（閉じるときの監査）が並び、レビュアー 1 人が両方を見る。
- 見張りはこれまで、根っこのセッションが裏で手で回してきた（org-project-new の 5）。根っこが閉じると止まる。決まったこと 22 で常駐を決めたが、まだ載っていない。
