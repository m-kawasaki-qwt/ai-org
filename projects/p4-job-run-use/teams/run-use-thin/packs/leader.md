---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.claude/skills/_archive/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/businesses/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/partners/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/tasks/**
---

# 文脈パック: リーダー（engineer）— run-use-thin

台帳の `job.deny` の `**/_archive/` は、ここでは `.claude/skills/_archive/` だけに絞っている。作業者が `.claude/skills/manager/sources/orca/_archive/` に退避ファイルを作り、レビュアーがそれを読んで diff するため。事業・会社・台帳（`businesses/` `partners/` `company/` `tasks/`）はこの案件に要らないので読ませない。

## 読む資料

| # | パス（job は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job`、dev-tools は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`） | 何のため・どこまで |
|---|---|---|
| 1 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p4-job-run-use/teams/run-use-thin/charter.md` | 完了条件 1〜5 と範囲。全部 |
| 2 | job `.claude/skills/manager/sources/orca/run-use.md` | 薄くする対象。全部（61 行） |
| 3 | dev-tools `claude/plugins/dev-tools/skills/orca-multi-agent/SKILL.md` | 参照先。「B. 依頼する（Orca に投げる）」の「`run-use` の使いどころ」、「C. 一覧を出す」、「D. 戻りを受ける（`worker_done`）」の分岐 1〜3 と「自分が依頼していない戻りが届いたとき」だけ |
| 4 | job `.claude/plans/tmp/2026-10-22-orca-multi-agent-run-use-handover.md` | 出発点。「dev-tools に上げずに job に残すもの」「job 側で直したもの（参考）」の節だけ |
| 5 | job `CLAUDE.md` | 「## 情報を消さない」の節（41〜47 行）だけ |
| 6 | job `.claude/skills/manager/sources/orca/run-use-log.md` | 観察ログ。run-use.md の「4. ログ」が指す先で、残すもの。全部（8 行） |

## 事業の文脈の要約

- job は川崎さんの業務のナレッジベース。多数のセッションが同時に書くので「情報を消さない」が最優先の決まり。外した文は消さず退避し、併記する。書く直前に読み直す。
- job のマネージャー（毎時の automation と手動）・定型業務（routine-work）・automation-followup が、Orca で別 repo の実装エージェントに依頼して戻りを受ける。常設の Run は 2 本: manager `run_31ab18962379`、routine-work `run_5c5c7f0b494d`。
- 2026-10-22 に「各回の最初に `run-use` していたので、戻りが依頼したセッションでなく最後に結んだセッションへ届いていた」と分かり、job 側で run-use.md を作って手順を絞った。2026-10-23 に dev-tools の SKILL.md も同じ考え方（`run-use` は依頼の直前と引き取りだけ・戻りは結ばずに `inbox`）に直った。今回は job 側を、その差分だけに薄くする。
- 残す job 固有のもの（出発点の記録より）: Run の ID、引き取るまでの時間（2 時間）、automation の印（`依頼元の端末` の行の `手動｜automation: manager hourly｜automation: <group>/<task>`）、観察ログ（run-use-log.md）とその書き方、誤配の job での運用（ログに〔誤配〕・川崎さんへ 1 行）。manager は Run の全部、routine-work は自分の起票の Task だけを見る、という見る範囲の分け方も job 固有に当たる。
- run-use.md の冒頭の「🔴 job では、dev-tools の『新しい端末は最初に `run-use` で結び直す』より、ここを優先する」は、dev-tools が直ったので前提が古い。

## これまでの経緯（親 p4-job-run-use の digest から）

- 川崎さんが p4 を立ち上げ、PM がこのチームを作り、コーディネーターに編成と文脈パックを頼んだ。試走の主眼は文脈パックの効き。過不足は完了条件 5 として報告に入る。
- 親の charter の「台帳は job の org/context.yaml」は誤りで、dev-tools の `org/context.yaml` が台帳（PM の指示）。

## 段取りの見当（判断はリーダー）

- 完了条件 3 の要注意: run-use.md を節番号で指している所がある。`manager/sources/orca/inbox.md` 38 行目と `automation-followup/inbox.md` 35 行目が「2. 結ばずに見る」、`manager/advance/implement.md` 58 行目が「1」。見出しの番号と名前を変えるなら、そこも直す（外した文は退避）。
- `grep` の結果のうち、`self-tasks/`・`tasks/`・`**/_history/`・`.claude/skills/_archive/`・各 `history.md`（実行の記録）は、触らない範囲か履歴。開かず「直さない（範囲外／履歴）」として一覧に載せればよい。
- `tasks/_master/manager.yaml` 15 行目のコメントは「毎回のはじめに `orca orchestration run-use --id <これ>` で結び直す」のままで、今の手順と矛盾する。`tasks/` は触らない範囲なので直さず、報告で PM に上げる（パックを組む段で見つけた事実）。
- `manager/_failures/2026-10-22-orca-check-unbound-fenced.md` の手当の節に「dev-tools の `orca-multi-agent` は未対応（job 側で上書き）」とあり、今は古い。直すなら併記で。
