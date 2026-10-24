---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p9-org-watch`、`T` = `P/teams/watch`、`W` = `/Users/maka343noshi/orca/workspaces/dev-tools/org-watch`（あなたの `--workdir`。書くのはここだけ）、`AO` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`（記録。読むだけ）。

1. `T/charter.md` 全体 — 照らす完了条件（あなたの受け持ちは 4 と、最後に 5）。
2. `P/charter.md` の「起きた問題」の 4 と「範囲」。
3. `W/org/positions/auditor/position.md` — 直す立場。いまは「雛形の改訂案」を出す形で、今回の決まり（直し方を書かない）と食い違っている。
4. `W/org/scripts/orgctl.py` の `_ProjectReader`（とくに `audits`・`inbox`）・`build_snapshot`・`cmd_export`・`teardown_member`・`teardown_component`・`cmd_assign` の auditor の扱い — 監査の出力を snapshot に載せる所と、閉じる流れ。
5. `W/org/schema/snapshot.schema.json` の `audit_proposals` まわり — 形を変えるならスキーマも。`orgctl export --check` が通ること。
6. `W/claude/plugins/dev-tools/skills/org-project-new/SKILL.md` の 7 — 監査役の段を入れる所。
7. `W/docs/todo/ai-org-plan.md` の決まったこと 22 と、決定ログの 2026-10-24 の「監査の目的を分ける」「起きたこと（問題・課題）と参照元だけを控え」の行。
8. `AO/policy.md` — 監査役が照らす方針の 1 枚。
9. `AO/projects/p3-org-visibility/log/events.log` の 13:36 以降と、そこから辿れる監査役の `report` の本文（`log/msgs/`） — これまでに 1 回だけ動いた監査の実物。export が今もこれを読めること。
10. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/README.md` の「組織の直し待ち」 — 監査が回るまでの控え。監査の出力がこれと同じ粒度（起きたこと＋参照元）になる目安。job は読むだけ。

## 事業の文脈の要約

事業の案件ではない（組織の基盤）。

- 決まったこと 22: 進め方の監査は常駐させず、プロジェクトを閉じるときに 1 回（入れ子なら子が閉じるたび）。いまは閉じる手順に入っておらず、監査が回ったのは p3 だけ。セッション報告の unclear は 111 件溜まって誰も読んでいない。
- 監査役の出力は「起きたこと（問題・課題）と参照元」だけ。直し方は書かない（直し方は着手の直前に、そのときのモデル・組織で考える）。
- 出力の置き場を決め、`orgctl export` の `snapshot.json` に載せる（ビューアの画面の改修は範囲外。snapshot に載ればよい）。前の形（p3 の「改訂案」）も読めたままにする。
- 閉じる手順で、監査役を誰が・いつ assign し、何を `start` で渡し、出力を待ってから teardown する、までを書く。このプロジェクト（p9）自身を閉じるときにこの手順で監査役が動く。そのとき監査役の立場は worktree の `position.md` から入る必要がある（本体はまだ古い）。手順に「マージ前に試すときは worktree の orgctl で assign する」ことが分かる形にするか、PM がそうできることを確かめて報告に書く。**報告には、p9 を閉じるときに PM が打つコマンドを、そのまま打てる形（1 コマンド 1 行）で並べる**（PM が charter に足した）。
- `orgctl.py` は `worker-watch` も同時に直している。あなたの受け持ちは上の 4・5 に挙げた所だけ。定数・`cmd_wait`・`member_state`・`cmd_watch`・`patrol_once`・`cmd_patrol`・`main()` は触らない（`main()` に引数が要るときはリーダーへ言う）。編集は Edit で差分だけ。Edit が「読んだあとに変わった」と止まったら、読み直してから直す。
- 共有の文書: org-project-new の 7 と、`W/org/README.md` の監査の節はあなた。5 と見張りの節は `worker-watch`。プランの決まったこと 22 の補足は、`worker-watch` の承認のあと、リーダーの `start` を受けてからあなたが通して書く（元の文を消さず併記）。最後に README とプランの通しの揃え（完了条件 5）もあなた。
- 確かめ: `orgctl export --projects <AO>/projects --out <scratchpad>/snapshot.json --check` が通る。仮の監査の出力を scratchpad の仮のプロジェクトに置いて、snapshot に載ることを見る。

## これまでの経緯

- 2026-10-24 17:27 根っこが p9 を立て、PM がコーディネーターに切り方を相談した。チーム `watch` 1 つに、あなた（閉じるときの監査）と `worker-watch`（見張り）が並び、レビュアー 1 人が両方を見る。
- 監査役が動いたのは p3 だけ。p4〜p8 は閉じても監査が無い。
