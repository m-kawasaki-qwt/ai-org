---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**
---

# 文脈パック: 作業者（export）— viewer

workdir は dev-tools の worktree `/Users/maka343noshi/orca/workspaces/dev-tools/org-viewer`。書くのはここだけ。入力の記録は ai-org の本体 `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/`（読むだけ）。`snapshot.json` の出力先は ai-org の worktree `/Users/maka343noshi/orca/workspaces/ai-org/viewer` の中（置き場所はリーダーの指定に従う）。job は読まない。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | ai-org `projects/p5-org-viewer/teams/viewer/charter.md` | 完了条件（とくに 1）と範囲。全部 |
| 2 | リーダーから渡るスキーマ | これが正。形を変えたくなったら自分で変えず、リーダーへ |
| 3 | worktree `CLAUDE.md`・`org/README.md` | repo の決まりと、orgctl が作る記録の置き場の図 |
| 4 | worktree `org/scripts/orgctl.py` | 足す先。`NOISE_KINDS`（44 行）、`read_events`（204〜217）、`offset_file`（220〜223）、`member_state`（584〜608）、`cmd_notify_stats`（632〜653）、`digest_text`（656〜679）、`yaml_dump`（95〜127）、`user_inbox`（704〜720）、`session_metrics`・`teardown_member`（780〜892）、`main` のサブコマンドの並び（949〜） |
| 5 | ai-org `tools/org_timeline.py`・`tools/org_status.py` | 何を畳み、何を落としているかの前例。`LIFECYCLE`・`is_noise`・状態の決め方。中の定義は写さない（二重定義になる） |
| 6 | ai-org 本体の `projects/p1-org-status`〜`p4-job-run-use`（`log/`・`reports/sessions/`・`component.json`・`teams/*/component.json`） | 試す入力。下の「実物の癖」を確かめる |

## 事業の文脈の要約

- 記録を読む正を orgctl の 1 か所にする。ビューアは `snapshot.json` を描くだけで、数えたり解釈したりしない。だから時間・トークン・往復・作り直しの集計、ノイズの除外、状態の判定は全部 export の側で済ませる。
- orgctl は Python の標準ライブラリだけで動く（崩さない）。動いている組織は dev-tools 本体の orgctl を使っているので、本体は触らない。

## 実物の癖（書く前に知っておくと迷わないもの）

- **YAML を読む道具が無い。** orgctl は `yaml_dump` で書くだけ。セッション報告は `machine:`（orgctl が書いた形）と `self: |`（本人が手で書いた YAML を文字列で抱えたもの）。`self` は書き手ごとに形が揺れる（`{ what:, why: }` の流れ形式あり、`（自己申告なし）` あり）。全部を厳密に読むより、要る項目（`unclear`・`escalated` など）を拾い、読めなかったら原文の文字列を残す方が安全。
- p1 のセッション報告だけファイル名に session の頭 8 文字が無い。
- トークン・時間はセッション報告（teardown のとき）にしか無い。開いているプロジェクト（p5 自身）は報告ゼロで落ちないこと。
- `user-inbox.yaml` は p4 にしか無い。`read` は false のまま追記されるだけ。ユーザーの既読位置は `log/.inbox_user`（events.log の行番号）。未読の数え方はリーダーのスキーマに従う。
- 監査の改訂案は専用のファイルが無く、p3 の監査役の `report` 本文（`log/msgs/95df09.md`）にある。
- events.log の detail は `key=value` の並び（`read_events` の `kv`）。本文は `msg=log/msgs/<hash>.md`、本文の 1 行目は `<!-- from → to kind ts -->` の注記。

## これまでの経緯

- p3 で `org_timeline.py` を作った（timeline.html。今の見える化）。p5 はその後継。PM の指定でスキーマが先、そのあと export とビューアを並べる。

## 作業の注意

- export は読むだけ。本体の記録に書き込まない（`inbox` のように offset や ack を書く関数を呼ばない）。
- 試すときは worktree の orgctl を本体の `projects/` に向けて走らせる（ai-org 本体で `ORG_MEMBER` などの環境変数に頼らず、入力の場所を引数で渡せる形がよい）。
- 書いた `snapshot.json` がスキーマに合うかを、標準ライブラリだけで確かめる手段を用意する（スキーマが JSON Schema なら、最低限の型と必須の確認でよい）。
