# 抜き出しの件数表（scripts/extract.py が書いた。手で直さない）

抜いた件数の合計: 431

## 材料ごとの小計

| 材料 | ファイル数 | 抜いた件数 | 0 件のファイル |
|---|---|---|---|
| sessions | 56 | 163 | 1 |
| msgs | 226 | 251 | 171 |
| user_inbox | 6 | 1 | 5 |
| notify_outbox | 1 | 0 | 1 |
| audit | 1 | 4 | 0 |
| job_readme | 1 | 5 | 0 |
| events_audit | 9 | 7 | 2 |

## 抜いた件の出どころ（source）ごと

| source | 件数 |
|---|---|
| audit | 4 |
| auditor | 15 |
| event:nudge | 1 |
| event:review_ng | 40 |
| event:rework | 6 |
| events:no_auditor | 7 |
| job_readme | 5 |
| msg:札B | 29 |
| msg:節A | 87 |
| msg:節B | 73 |
| session | 163 |
| user_inbox:stuck | 1 |

## 抜き方（source の意味）

- `session`: セッション報告の `self` の `unclear`・`not_done` の 1 項目＝1 件（`machine` は読まない）
- `msg:節A`: msgs の見出しが「うまくいかなかった・試走で・試走として・気づき・気づいた・食い違・unclear」の節。上の階層の箇条書き 1 つ（子は親に足す）か地の文の段落 1 つ＝1 件
- `user_inbox:<kind>`: `log/user-inbox.yaml` の項のうち kind が report でないもの（見張りの stuck など）。report の項は log/msgs と同じ本文を指すので抜かない。`log/notify-outbox.log`（p3 だけ）は根っこへの知らせの写しで、本文は log/msgs と同じなので抜かない
- `msg:節B`: 同じく見出しが「残る不明点・残ること・残った・申し送り・〔仮〕・上げること・未確認」の節（網羅のための候補。問題かどうかはまとめで決める）
- `msg:札B`: 見出しでなく地の文の行頭の札（「申し送り:」など）で始まる塊。札の行の本文と、続く箇条書き（空行まで）を 1 つ 1 件
- `event:<種類>`: events.log で種類が review_ng・rework・blocked・escalate・nudge の行が指す本文の全体を、箇条書き・段落ごとに 1 件（blocked・escalate は p1〜p9 に 0 行。nudge は根っこの見張りの促しで、pack の 4 種に足した）
- `auditor`: 送り手が監査役の本文（p3 の 95df09・p9 の 63bb4d）の `##` 節の項目ごと
- `audit`: p9 の `reports/audit/p9-org-watch.md` の番号つきの項 1 つ＝1 件
- `job_readme`: job の README の「組織の直し待ち」の箇条書き（p10 以降の行は除く）と、「〜の時点」の節の「残ったこと・残っている課題・申し送り」で始まる行。読んだ版: sha1 5060bd4ae884・更新 2026-10-24 19:41（job の git の管理外なので、読んだ時点の中身の指紋）
- `events:no_auditor`: 各プロジェクトの events.log に監査役（position=auditor）の assign が無いまま閉じたもの 1 つ＝1 件（参照元は根っこの component_closed の行。レビュー第1回の指摘で足した）

## 読まなかったもの（材料の外）

- セッション報告の `machine`（会話ログ由来）と `~/.claude/projects/` の会話ログ
- `teams/*/msgs/`（5 本。作業者の版の写し。往復の本文は log/msgs にある）・`teams/*/thread.md`・`teams/*/result.md`（材料の指定に無い。結果は PM・リーダーの report の本文として log/msgs で読んでいる）
- p10-viewer-ideas・p11-issue-list

## ファイルごと

| 材料 | ファイル | 抜いた件数 | 0 件の理由 |
|---|---|---|---|
| sessions | `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml` | 7 |  |
| sessions | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml` | 5 |  |
| sessions | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__reviewer.yaml` | 3 |  |
| sessions | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__worker-1.yaml` | 3 |  |
| sessions | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__pm-0775601b.yaml` | 4 |  |
| sessions | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__leader-70bafeda.yaml` | 3 |  |
| sessions | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__reviewer-f7de4d8b.yaml` | 3 |  |
| sessions | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__worker-1-56151c49.yaml` | 3 |  |
| sessions | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__auditor-074c4759.yaml` | 1 |  |
| sessions | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__pm-8512c441.yaml` | 4 |  |
| sessions | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__leader-4d653d8e.yaml` | 2 |  |
| sessions | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__reviewer-10b48465.yaml` | 2 |  |
| sessions | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__worker-1-7f90e6d2.yaml` | 2 |  |
| sessions | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__leader-e54a1b8a.yaml` | 1 |  |
| sessions | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__reviewer-8d87b16a.yaml` | 2 |  |
| sessions | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__worker-1-969f0ba1.yaml` | 2 |  |
| sessions | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__coordinator-run-use-thin-ad0d46dd.yaml` | 4 |  |
| sessions | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__pm-7fcade93.yaml` | 3 |  |
| sessions | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__leader-8e4fdd93.yaml` | 1 |  |
| sessions | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__reviewer-05ac7e08.yaml` | 1 |  |
| sessions | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__worker-1-b93bc6f4.yaml` | 2 |  |
| sessions | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__coordinator-viewer-2d6b3d7c.yaml` | 2 |  |
| sessions | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__pm-92edb217.yaml` | 2 |  |
| sessions | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__leader-6f1c1b6b.yaml` | 3 |  |
| sessions | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__reviewer-11df580d.yaml` | 4 |  |
| sessions | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml` | 6 |  |
| sessions | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml` | 5 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-org-build-b422e51c.yaml` | 4 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-uiux-research-057eafed.yaml` | 3 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__pm-16bc79bc.yaml` | 3 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__leader-15cbc271.yaml` | 2 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__reviewer-b8082b46.yaml` | 2 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-norms-7bbd0aab.yaml` | 4 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-orgctl-34b67ded.yaml` | 1 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__leader-00fa4e8f.yaml` | 3 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__reviewer-77f133a5.yaml` | 3 |  |
| sessions | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__worker-1-833d6b72.yaml` | 4 |  |
| sessions | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml` | 7 |  |
| sessions | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__pm-1c125b2e.yaml` | 3 |  |
| sessions | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__teams__coordinator-flow__leader-e917435e.yaml` | 1 |  |
| sessions | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__teams__coordinator-flow__reviewer-3a86e1a1.yaml` | 0 | not_done: []・unclear: [] |
| sessions | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__teams__coordinator-flow__worker-1-32df2698.yaml` | 2 |  |
| sessions | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__coordinator-087f6e79.yaml` | 2 |  |
| sessions | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__pm-129ad682.yaml` | 2 |  |
| sessions | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml` | 4 |  |
| sessions | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-export-baf05c27.yaml` | 1 |  |
| sessions | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-kawasaki-d30b4812.yaml` | 4 |  |
| sessions | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-export-fff11e32.yaml` | 3 |  |
| sessions | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml` | 5 |  |
| sessions | `projects/p9-org-watch/reports/sessions/p9-org-watch__auditor-272c70db.yaml` | 1 |  |
| sessions | `projects/p9-org-watch/reports/sessions/p9-org-watch__coordinator-37d1062a.yaml` | 3 |  |
| sessions | `projects/p9-org-watch/reports/sessions/p9-org-watch__pm-f743150d.yaml` | 4 |  |
| sessions | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__leader-36cfe0d2.yaml` | 2 |  |
| sessions | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__reviewer-512bbb7a.yaml` | 3 |  |
| sessions | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-audit-6bc5c166.yaml` | 3 |  |
| sessions | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-watch-f06de01a.yaml` | 4 |  |
| msgs | `projects/p1-org-status/log/msgs/1059a3.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/2f7495.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/3a1eb3.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/447504.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/4b45c1.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/4d68b5.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/7e08e5.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/803ffb.md` | 6 |  |
| msgs | `projects/p1-org-status/log/msgs/9997e5.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/aa6584.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/c47efc.md` | 3 |  |
| msgs | `projects/p1-org-status/log/msgs/d54a1d.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p1-org-status/log/msgs/d9ba25.md` | 7 |  |
| msgs | `projects/p1-org-status/log/msgs/f839b3.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/04802d.md` | 11 |  |
| msgs | `projects/p2-orca-run-use/log/msgs/161ad1.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/1d9e38.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/1f7fb5.md` | 6 |  |
| msgs | `projects/p2-orca-run-use/log/msgs/21e285.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/39bcd6.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/3c4f5f.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/46c029.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/63b813.md` | 1 |  |
| msgs | `projects/p2-orca-run-use/log/msgs/65dcd4.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/7ad811.md` | 8 |  |
| msgs | `projects/p2-orca-run-use/log/msgs/91f052.md` | 1 |  |
| msgs | `projects/p2-orca-run-use/log/msgs/974bc8.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/a9a0a2.md` | 1 |  |
| msgs | `projects/p2-orca-run-use/log/msgs/aa246f.md` | 0 | 種類 done・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/be9424.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/c5520c.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p2-orca-run-use/log/msgs/f863c1.md` | 3 |  |
| msgs | `projects/p3-org-visibility/log/msgs/081277.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/1cd772.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/258cd4.md` | 3 |  |
| msgs | `projects/p3-org-visibility/log/msgs/28755e.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/347d6c.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/61724e.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/693250.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/6acb52.md` | 2 |  |
| msgs | `projects/p3-org-visibility/log/msgs/711336.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/717cf9.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/75f23f.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/78205d.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/7cfa0f.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/83f3b8.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/8723ce.md` | 1 |  |
| msgs | `projects/p3-org-visibility/log/msgs/8cffd1.md` | 2 |  |
| msgs | `projects/p3-org-visibility/log/msgs/9010bf.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/95df09.md` | 14 |  |
| msgs | `projects/p3-org-visibility/log/msgs/a1e898.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/b44250.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/b589bb.md` | 2 |  |
| msgs | `projects/p3-org-visibility/log/msgs/b93761.md` | 3 |  |
| msgs | `projects/p3-org-visibility/log/msgs/c76d01.md` | 2 |  |
| msgs | `projects/p3-org-visibility/log/msgs/c9f2f9.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/ca9ca1.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/d951b5.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p3-org-visibility/log/msgs/dc84e7.md` | 2 |  |
| msgs | `projects/p3-org-visibility/log/msgs/f315e9.md` | 3 |  |
| msgs | `projects/p3-org-visibility/log/msgs/fa083d.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/0b845a.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/15e3a3.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/3b3654.md` | 4 |  |
| msgs | `projects/p4-job-run-use/log/msgs/41c2df.md` | 0 | 種類 review_ok・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/45b4ed.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/4a0a6c.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/74b9f7.md` | 3 |  |
| msgs | `projects/p4-job-run-use/log/msgs/82e0d6.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/986d0b.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/c7a08e.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/cb5bfc.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/d44a9d.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/ded3b3.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/e6cc13.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p4-job-run-use/log/msgs/f55556.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/0196f5.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/02a83f.md` | 4 |  |
| msgs | `projects/p5-org-viewer/log/msgs/146e61.md` | 11 |  |
| msgs | `projects/p5-org-viewer/log/msgs/17b6a4.md` | 2 |  |
| msgs | `projects/p5-org-viewer/log/msgs/2140aa.md` | 10 |  |
| msgs | `projects/p5-org-viewer/log/msgs/22d537.md` | 1 |  |
| msgs | `projects/p5-org-viewer/log/msgs/2330fc.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/28e68a.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/372e05.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/3c558c.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/403aad.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/5eb822.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/7ce09d.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/87b487.md` | 3 |  |
| msgs | `projects/p5-org-viewer/log/msgs/8c5725.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/94fa32.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/aa3336.md` | 4 |  |
| msgs | `projects/p5-org-viewer/log/msgs/ab626d.md` | 1 |  |
| msgs | `projects/p5-org-viewer/log/msgs/abd9db.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/af498c.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/b6e59b.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/b8283e.md` | 4 |  |
| msgs | `projects/p5-org-viewer/log/msgs/ba4c08.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/c2dd54.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/cf9712.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/f0102d.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/f407da.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p5-org-viewer/log/msgs/fc2678.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/11bdf9.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/1b9273.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/1dadf6.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/21efce.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/24cd7c.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/25786e.md` | 9 |  |
| msgs | `projects/p6-org-build/log/msgs/2f70ca.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/450931.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/46481e.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/49792b.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/4d8609.md` | 7 |  |
| msgs | `projects/p6-org-build/log/msgs/5959b9.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/5b4d3b.md` | 0 | 種類 review_ok・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/6e7f5c.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/6efb2b.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/737b25.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/740ed0.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/784785.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/7a426d.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/7e496b.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/82e016.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/8561b1.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/857958.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/867029.md` | 0 | 種類 review_ok・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/875f9d.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/915ebb.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/9232e0.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/933230.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/969ae8.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/ba8378.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/bd37ff.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/c0cf5d.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/c4cc0d.md` | 2 |  |
| msgs | `projects/p6-org-build/log/msgs/c5c370.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/cc3a09.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/d0cb32.md` | 0 | 種類 review_ok・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/d9cfb4.md` | 0 | 種類 review_ok・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/dd1184.md` | 8 |  |
| msgs | `projects/p6-org-build/log/msgs/e279bd.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/e2c4e2.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p6-org-build/log/msgs/f4b2dc.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/101739.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/103af4.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/1e8163.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/1f758b.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/2e8018.md` | 5 |  |
| msgs | `projects/p7-coordinator-role/log/msgs/4d25e4.md` | 7 |  |
| msgs | `projects/p7-coordinator-role/log/msgs/52a9c9.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/573f97.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/7195aa.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/765d10.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/83ac5d.md` | 0 | 種類 review_ok・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/891118.md` | 1 |  |
| msgs | `projects/p7-coordinator-role/log/msgs/9610d4.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/be01fb.md` | 4 |  |
| msgs | `projects/p7-coordinator-role/log/msgs/dd695e.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p7-coordinator-role/log/msgs/fa1620.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/014808.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/071fa5.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/176526.md` | 1 |  |
| msgs | `projects/p8-viewer-rebuild/log/msgs/1ec60a.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/3df696.md` | 12 |  |
| msgs | `projects/p8-viewer-rebuild/log/msgs/56ab10.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/5f8f8f.md` | 7 |  |
| msgs | `projects/p8-viewer-rebuild/log/msgs/67a7f5.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/76d8da.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/7f2930.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/83f7ad.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/8867ac.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/8881df.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/8bed08.md` | 0 | 種類 review_ok・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/931330.md` | 6 |  |
| msgs | `projects/p8-viewer-rebuild/log/msgs/94b8de.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/9e9875.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/a5676d.md` | 2 |  |
| msgs | `projects/p8-viewer-rebuild/log/msgs/b02ec2.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/b20186.md` | 11 |  |
| msgs | `projects/p8-viewer-rebuild/log/msgs/b43bfd.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/b87e1b.md` | 3 |  |
| msgs | `projects/p8-viewer-rebuild/log/msgs/b966d0.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/c03dcf.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/c60113.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/ca626b.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/cf0670.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/d447f3.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/deddba.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/e4168a.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/f1ff6d.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/f2caba.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p8-viewer-rebuild/log/msgs/fabde3.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/0c2fd0.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/199334.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/26be36.md` | 9 |  |
| msgs | `projects/p9-org-watch/log/msgs/279a7d.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/299393.md` | 4 |  |
| msgs | `projects/p9-org-watch/log/msgs/2e8bd2.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/34de0a.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/3cadd4.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/42793b.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/544cc1.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/5904f6.md` | 1 |  |
| msgs | `projects/p9-org-watch/log/msgs/635d9b.md` | 7 |  |
| msgs | `projects/p9-org-watch/log/msgs/63bb4d.md` | 1 |  |
| msgs | `projects/p9-org-watch/log/msgs/64a1bc.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/6aaf3b.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/6b837d.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/6bc6a5.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/6eccb0.md` | 4 |  |
| msgs | `projects/p9-org-watch/log/msgs/75ccd2.md` | 0 | 種類 done・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/7e3499.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/9012bd.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/9be5f1.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/a92788.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/b688e8.md` | 0 | 種類 start・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/b98a15.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/ca9ce0.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/cc2161.md` | 6 |  |
| msgs | `projects/p9-org-watch/log/msgs/e2b582.md` | 0 | 種類 report・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/e4536d.md` | 0 | 種類 wrap_up・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/e7eb08.md` | 0 | 種類 review_request・該当の節なし |
| msgs | `projects/p9-org-watch/log/msgs/e930ae.md` | 2 |  |
| msgs | `projects/p9-org-watch/log/msgs/f08c2f.md` | 4 |  |
| user_inbox | `projects/p4-job-run-use/log/user-inbox.yaml` | 0 | report 1 項だけ（log/msgs と同じ本文を指すので抜かない） |
| user_inbox | `projects/p5-org-viewer/log/user-inbox.yaml` | 0 | report 1 項だけ（log/msgs と同じ本文を指すので抜かない） |
| user_inbox | `projects/p6-org-build/log/user-inbox.yaml` | 0 | report 1 項だけ（log/msgs と同じ本文を指すので抜かない） |
| user_inbox | `projects/p7-coordinator-role/log/user-inbox.yaml` | 0 | report 1 項だけ（log/msgs と同じ本文を指すので抜かない） |
| user_inbox | `projects/p8-viewer-rebuild/log/user-inbox.yaml` | 1 | ほかに report 1 項は抜かない（log/msgs と同じ本文） |
| user_inbox | `projects/p9-org-watch/log/user-inbox.yaml` | 0 | report 2 項だけ（log/msgs と同じ本文を指すので抜かない） |
| notify_outbox | `projects/p3-org-visibility/log/notify-outbox.log` | 0 | 根っこへの知らせの写し。本文は log/msgs/b93761.md と同じなので抜かない |
| audit | `projects/p9-org-watch/reports/audit/p9-org-watch.md` | 4 |  |
| job_readme | `job:company/system/ai-org/README.md` | 5 | p10 以降の行は材料の外なので抜かない: 37 行目（p10） |
| events_audit | `projects/p1-org-status/log/events.log` | 1 |  |
| events_audit | `projects/p2-orca-run-use/log/events.log` | 1 |  |
| events_audit | `projects/p3-org-visibility/log/events.log` | 0 | 監査役の assign がある |
| events_audit | `projects/p4-job-run-use/log/events.log` | 1 |  |
| events_audit | `projects/p5-org-viewer/log/events.log` | 1 |  |
| events_audit | `projects/p6-org-build/log/events.log` | 1 |  |
| events_audit | `projects/p7-coordinator-role/log/events.log` | 1 |  |
| events_audit | `projects/p8-viewer-rebuild/log/events.log` | 1 |  |
| events_audit | `projects/p9-org-watch/log/events.log` | 0 | 監査役の assign がある |
