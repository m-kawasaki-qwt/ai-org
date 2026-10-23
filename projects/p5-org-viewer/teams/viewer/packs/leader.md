---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**
---

# 文脈パック: リーダー — viewer

事業の案件ではなく組織内の道具なので、job は丸ごと読ませない（台帳の `job.deny` を含む）。dev-tools は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`、ai-org は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | ai-org `projects/p5-org-viewer/teams/viewer/charter.md` | 完了条件と範囲。全部 |
| 2 | ai-org `policy.md` | 目的に照らす基準。1・4・5 節（認知負荷・選ぶだけ・記録が調べられる） |
| 3 | dev-tools `docs/todo/ai-org-plan.md` | 「決まったこと」の 14・22・24 と、決定ログの 2026-10-24 の 3 行（監査の分け方・ビューア） |
| 4 | dev-tools `org/scripts/orgctl.py` | スキーマを決める根拠。`NOISE_KINDS`（44 行）、`read_events`（204〜217）、`member_state`（584〜608）、`digest_text`（656〜679）、`session_metrics` と `teardown_member`（780〜892）、`user_inbox`（704〜720）。中身は作業者が読むので、リーダーは何がどこで決まっているかだけ |
| 5 | ai-org `tools/org_timeline.py`・`tools/org_status.py` | 後継・重複の元。冒頭の docstring だけ（何を出し、何を畳み、何を落とすか） |
| 6 | 下の「記録の実物の当て」の表 | スキーマの判断で迷う所 |

## 事業の文脈の要約

- この組織の目的は、川崎さんがボトルネックにならずに仕事が回り、間違いが分かり直ること。ビューアはその「分かる」の入口。見る人は川崎さん 1 人、PC。判断の基準は「川崎さんが開いて 10 秒で、どこを見ればいいか分かるか」。
- 監査の分け方（決定ログ 2026-10-24）: パフォーマンス（時間・トークン・往復・作り直し）は記録からスクリプトで数えてビューアに出す。だから集計は export の側（orgctl）でやり、ビューアは数えない。

## 記録の実物の当て（スキーマで迷いそうな所）

- **events.log**: 1 行 `<ts> <hash> <from> <kind> <to> <detail>`。detail は `key=value` の並び（`msg=log/msgs/<hash>.md` で本文）。数えるための行は `NOISE_KINDS`。ただし ai-org の `org_status.py` は独自に `{"ack","notify_sent","notify_recv"}`、`org_timeline.py` は `is_noise()` を持っている — これが「二重定義」の実例で、export は orgctl のものを使う。
- **component.json**: `kind`（project/team）・`id`・`parent`・`status`・`members`（名前→id）・`children`・`created_at`・`closed_at`。
- **reports/sessions/*.yaml**: 上半分 `machine:`（時間 `span_min`・`tokens`・`tokens_total`・`events_sent`・`review_ng_count`・`files_changed_in_window`）は機械、下半分 `self: |` は本人の自己申告の YAML を文字列で抱えたもの（`asked/did/outputs/decided/escalated/not_done/unclear`）。p1 だけファイル名に session の頭 8 文字が付いていない。**トークンは片づけ（teardown）のときにしか取れない** — 動いているプロジェクト（いまの p5 自身）にはまだ無い。
- **user-inbox.yaml**: p4 にだけある（patrol が入ってから）。`read: false` で追記のみで、既読にする仕組みは無い。ユーザーの既読の位置は別に `log/.inbox_user`（events.log の行番号）がある。「川崎さん宛ての未読の数」をどちらで数えるかは決める必要がある。
- **監査の改訂案**: 専用のファイルは無い。p3 の監査役（`p3-org-visibility/auditor`）の `report` 本文 `log/msgs/95df09.md` の中にある（改訂案 5 件）。export で拾うなら「立場が auditor の report の本文」になる。
- **unclear**: 21 件のセッション報告のうち多くにある。例: p3 の監査役「監査役の見るものに machine 欄の正しさが入るかがはっきりしない」。
- 作り直し: 種類 `rework`・`reassign`・`review_ng`。p3 の timeline-tool に rework と review_ng の実例がある。

## これまでの経緯

- p1〜p4 は試走（p1 状況ツール、p2 orca-multi-agent の直し、p3 timeline と README＋監査役、p4 コーディネーターと文脈パック）。p3 の timeline.html（`org_timeline.py`）が今の見える化で、それの後継を作る。
- PM の指定: スキーマを先に固めてから worker-export と worker-viewer を並べる。スキーマを後から変えるときは両方を揃える。

## 作業の注意

- スキーマ（形と、上の「決める必要がある」点）は、作業者 2 人を並べる前にリーダーが確定させて両方へ同じものを渡す。決めた点は charter の範囲内ならリーダーが決めてよい。
- p5 自身も `projects/` にあり、開いている。export は開いているプロジェクト（報告がまだ無い）でも落ちないこと。
