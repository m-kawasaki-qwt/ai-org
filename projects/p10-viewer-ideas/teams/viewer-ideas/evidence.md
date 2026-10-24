# 根拠の一覧（report.md の案ごと）

report.md の各案の「問題」の根拠を、開いて確かめられる場所で並べる。パスは ai-org の `projects/` からの相対（`p8/` は `p8-viewer-rebuild/` の略ではなく、下の表の正式名で書く）。数はすべて `scripts/` のスクリプトの出力（`scripts/output.txt`）から写した。

## Summary

- 根拠は 27 件。記録の中（events.log・本文・セッション報告・design.md・監査）が 21 件、いまの画面のコードと撮った画像が 6 件。
- 叩き台 2 の元になった「古い写しで川崎さんが混乱した」という根っこの申告そのものは、記録（p1〜p9・プラン・job のフィードバック）の中に見つからなかった。代わりに、同じことがいま起きるのを画面で撮って示した（E-08・E-09）。

## 目次

- [① 結果と監査を分ける](#-結果と監査を分ける)
- [② 写しの古さを出す（叩き台 2）](#-写しの古さを出す叩き台-2)
- [③ 全員待ちを出す（叩き台 3）](#-全員待ちを出す叩き台-3)
- [④ 直し待ちを束ねる（叩き台 7）](#-直し待ちを束ねる叩き台-7)
- [⑤ 人の手に印（叩き台 6）](#-人の手に印叩き台-6)
- [⑥〜⑨ と叩き台 8](#-と叩き台-8)
- [スクリプト](#スクリプト)

## ① 結果と監査を分ける

| # | 何が分かるか | 場所 |
|---|---|---|
| E-01 | p9 の結論の 1 文が「終わった — audit.md に 4 件書いた」（監査役の報告）になっている | `teams/viewer-ideas/screenshots/p9-1800.png` |
| E-02 | 川崎さん宛ての最後の報告が監査役のもの（17:55:46）で、PM の結果（17:53:27）より後 | `p9-org-watch/log/events.log`（`635d9b` と `63bb4d` の行） |
| E-03 | 結論の 1 文は「川崎さん宛ての最後の報告」の本文から取る決め | `p8-viewer-rebuild/teams/viewer/design.md:111-112`、コード `viewer/src/pages/p/[id].astro`（`lastReportToUser`） |
| E-04 | 閉じるときに監査役が動く手順が入った（以後のプロジェクトは毎回、最後の報告が監査役になる） | dev-tools `docs/todo/ai-org-plan.md:307`、`p9-org-watch/charter.md` の問題 4 |
| E-05 | PM の結果の表題に「4 の最後の 1 つは閉じるときに確かめる」（一部保留）があるが、画面に出ない | `p9-org-watch/log/msgs/635d9b.md:2` |
| E-06 | snapshot に `audit_findings`（指摘 4 件）が載っているのに、画面のコードが読んでいない | `scripts/checks.py` の出力 3、`p9-org-watch/reports/audit/p9-org-watch.md` |

[↑ 目次へ](#目次)

## ② 写しの古さを出す（叩き台 2）

| # | 何が分かるか | 場所 |
|---|---|---|
| E-07 | 画面の「いま」は書き出した時刻で固定（`NOW = generated_at`）。開いた時刻ではない | `viewer/src/lib/snap.ts:5` |
| E-08 | p10 の画面が「止まっているものは無い（最後の動き 0 分前）」。写しは 19:14、撮ったのは 19:36（右上は「22 分前」） | `teams/viewer-ideas/screenshots/p10-1800.png` |
| E-09 | 19:28 の時点で、p10 は写しの後に 21 行進み、メンバーは記録 6 人・写し 2 人。p11 も 21 行・5 人／2 人 | `scripts/checks.py` の出力 1 |
| E-10 | 写しの時刻と、開いた時刻から数えた古さ（「22 分前に書き出し」）は右上に 12px の補足の色で出ている。本体の文の分は書き出した時刻で数えていて（E-07）、警告の表示は無い | `viewer/src/layouts/Layout.astro:40,106,113-116`、`screenshots/home-1800.png` |
| E-11 | 書き出しは手で、プロジェクトを立てるたびにビューアを起こし直している（定期の書き出しはまだ無い） | dev-tools `docs/todo/ai-org-plan.md:349,352` |

[↑ 目次へ](#目次)

## ③ 全員待ちを出す（叩き台 3）

| # | 何が分かるか | 場所 |
|---|---|---|
| E-12 | p8: リーダーが 16:25:58 にメンバー 4 人の done を受け、16:30:56 に根っこが促す（nudge）まで誰も何も出していない | `p8-viewer-rebuild/log/events.log`（16:25〜16:31）、`p8-viewer-rebuild/log/msgs/176526.md` |
| E-13 | p8 のリーダー本人の申告（done を読んだあと wait に入った） | `p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml:406` |
| E-14 | p6: 研究チームのリーダーが 13:35:15 に done を受けてから 13:44:22 まで 9.1 分、何も出していない | `scripts/gaps.py` の出力、`p6-org-build/log/events.log:121,126` |
| E-15 | 画面の「止まっているかもしれない」の規則（ア〜エ）は、閉じた 7 プロジェクトで p1 の 2 件にしか出ない（p6 の 9 分は出ない） | `p8-viewer-rebuild/teams/viewer/design.md:73-88` |
| E-16 | p9 で patrol が全員待ちを判定するようになったが、その判定は snapshot に載らない（ビューアは別の規則で判定している） | dev-tools `org/scripts/orgctl.py:51,836`（全員待ち）、`org/schema/snapshot.schema.json`（該当の項目なし）、`viewer/src/lib/model.ts` |

[↑ 目次へ](#目次)

## ④ 直し待ちを束ねる（叩き台 7）

| # | 何が分かるか | 場所 |
|---|---|---|
| E-17 | 「決まりの直し候補」の見出しは p3 の改訂案 5 件だけ。p9 の監査の指摘 4 件が無い | `screenshots/rules-1800.png`、E-06 |
| E-18 | 迷った点 142 件がプロジェクトごとに畳んであるだけ。同じ迷いが別のセッションに重なっている例: 「レビュアーの指摘の回数を 2 段で通算するか」が p8 のコーディネーターと PM の両方にある | `p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__coordinator-087f6e79.yaml` の unclear 2 つ目、`p8-viewer-rebuild/log/msgs/b20186.md:75` |
| E-19 | 川崎さんの求め: 「要点をまとめて課題として渡し、深掘りしたら元の記録まで辿れる」 | job `company/system/ai-org/feedback/2026-10-24-viewer.md` の「監査のまとめ方」 |
| E-20 | p9 の charter: unclear は溜まっているが誰も読んでいない | `p9-org-watch/charter.md` の問題 4 |

[↑ 目次へ](#目次)

## ⑤ 人の手に印（叩き台 6）

| # | 何が分かるか | 場所 |
|---|---|---|
| E-21 | 9 プロジェクトで、手続き（依頼・終わりの指示・閉じるときの片づけ）以外の根っこの手は 2 回だけ記録にある: p1 の PM の入れ替え（11:46、3 行）と p8 の促し（16:30、1 行） | `scripts/count_records.py` の出力 |
| E-22 | 促し（`nudge`）は画面の種類の表に無く、灰色の「·」・名前は英語のまま。凡例にも無い | `viewer/src/lib/model.ts:43-56`、`screenshots/p8-1800.png` |
| E-23 | 根っこは 15 分おきに見て手で促していた（記録に残るのは 1 回） | `p9-org-watch/charter.md` の問題 1 |
| E-24 | ビューアの直しを根っこが直接入れた（記録の 1 行報告には残らない） | dev-tools `docs/todo/ai-org-plan.md:345` |

[↑ 目次へ](#目次)

## ⑥〜⑨ と叩き台 8

| # | 何が分かるか | 場所 |
|---|---|---|
| E-25 | 直しの回数は 9 プロジェクトで 0 か 2 だけ。判断の依頼・止まっているは 9 件とも 0。時間とトークンは p8 が中央値の 2.2 倍・3.1 倍 | `scripts/count_records.py` の出力 |
| E-26 | 結果の報告の「完了条件ごと」の書き方がそろっていない（表は p8 だけ。ほかは箇条書きか文） | `scripts/checks.py` の出力 2 |
| E-27 | 成果物は worktree に置いたまま、PR は根っこ、と報告に書かれる（p5〜p9 の 5 件）。PR の番号は git のコミットのメッセージにしか無い | `scripts/checks.py` の出力 2、ai-org の `git log`（8b76c47「ai-org の PR #2・dev-tools の PR #12 に載せた」） |

叩き台 1（前回から何が変わったか）は、記録の中に「何が変わったか分からなかった」場面が見つからなかった（根拠なし）。

[↑ 目次へ](#目次)

## スクリプト

| ファイル | 何を出すか |
|---|---|
| `scripts/count_records.py` | プロジェクトごとの時間・トークン・やりとり・直し・判断の依頼・人の手・迷った点、中央値との比 |
| `scripts/gaps.py` | プロジェクト全体で 5 分以上だれも何も出さなかった間 |
| `scripts/checks.py` | 写しの古さ・結果の報告の書き方・snapshot にあって画面が読んでいない項目 |
| `scripts/annot.mjs` | いまの画面（4390）を撮り、変える所に枠を描く（Playwright。scratchpad で動かした） |
| `scripts/output.txt` | 上の 3 つを 19:28 に動かした出力 |

再現: `python3 <T>/scripts/count_records.py <ai-org>/projects`・`python3 <T>/scripts/gaps.py <ai-org>/projects`・`python3 <T>/scripts/checks.py <ai-org>`（`<T>` はこのディレクトリ）。

[↑ 目次へ](#目次)
