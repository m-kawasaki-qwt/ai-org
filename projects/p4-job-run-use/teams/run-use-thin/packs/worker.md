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

# 文脈パック: 作業者 — run-use-thin

台帳の `job.deny` の `**/_archive/` は、ここでは `.claude/skills/_archive/` だけに絞っている（`.claude/skills/manager/sources/orca/_archive/` に退避ファイルを作るため）。

## 読む資料

job は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job`、dev-tools は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`。

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p4-job-run-use/teams/run-use-thin/charter.md` | 完了条件と範囲。全部 |
| 2 | job `.claude/skills/manager/sources/orca/run-use.md` | 薄くする対象。全部（61 行）。書く直前にもう一度読む |
| 3 | dev-tools `claude/plugins/dev-tools/skills/orca-multi-agent/SKILL.md` | 参照先。「B. 依頼する（Orca に投げる）」の「`run-use` の使いどころ」、「C. 一覧を出す」、「D. 戻りを受ける（`worker_done`）」（分岐 1〜3、「自分が依頼していない戻りが届いたとき」、`consumer_fenced` の箇条書き）。参照は節の見出し名で書く |
| 4 | job `.claude/plans/tmp/2026-10-22-orca-multi-agent-run-use-handover.md` | 何を残すかの根拠。「dev-tools に上げずに job に残すもの」の節だけ |
| 5 | job `CLAUDE.md` | 「## 情報を消さない」の節（41〜47 行）だけ |
| 6 | job `.claude/skills/manager/sources/orca/run-use-log.md` | 残す観察ログ。run-use.md の「4. ログ」との対応を崩さないため。全部（8 行） |
| 7 | job の `run-use` を参照しているファイル（`manager/sources/orca/inbox.md`・`automation-followup/inbox.md`・`automation-followup/followup.md`・`manager/advance/implement.md`・`manager/SKILL.md`・`manager/automation.md`・`manager/_failures/2026-10-22-orca-check-unbound-fenced.md`・`routine-work/README.md`・`routine-work/*/*/INDEX.md`） | 完了条件 3。grep で当たった行の前後だけ |

## 事業の文脈の要約

- job は川崎さんの業務のナレッジベースで、多数のセッションが同時に書く。決まり「情報を消さない」: 既存の文を消さない。今回は外した文を `_archive/` に全文退避することで満たす。書く直前に読み直し、差分は最小にする。
- job のマネージャー・定型業務（routine-work）・automation-followup が、Orca で別 repo の実装エージェントに依頼して戻りを受ける。常設の Run は manager `run_31ab18962379`、routine-work `run_5c5c7f0b494d`。
- run-use.md は 2026-10-22 に job 側だけで作った手順。その後 dev-tools の SKILL.md が同じ考え方に直ったので、共通部分（いつ結ぶか・結ばずに見る分岐・依頼していない戻りの扱い）は SKILL.md の節を指すだけにする。
- 残すもの: Run の ID、引き取るまでの時間（2 時間）、automation の印（`依頼元の端末` の行の書式 `<端末> （<手動｜automation: manager hourly｜automation: <group>/<task>>）`）、観察ログとその書き方（種別・書式・見直し方）、誤配の job での運用（ログに〔誤配〕・川崎さんへ 1 行）。manager は Run の全部・routine-work は自分の起票の Task だけを見る、という範囲の分け方も job 固有。
- 冒頭の「🔴 job では dev-tools の『新しい端末は最初に `run-use` で結び直す』より、ここを優先する」は前提が古い（dev-tools 側が直った）。

## これまでの経緯

- p4 は文脈パックの効きを見る試走。パックに無くて自分で探した資料・要らなかった資料を、リーダーへの報告に書く（完了条件 5）。

## 作業の注意

- 節番号で run-use.md を指している所がある: `manager/sources/orca/inbox.md` 38 行目と `automation-followup/inbox.md` 35 行目が「2. 結ばずに見る」、`manager/advance/implement.md` 58 行目が「1」。見出しを変えるなら、そちらも直す（外した文は退避）。
- grep の当たりのうち `self-tasks/`・`tasks/`・`_history/`・`.claude/skills/_archive/`・`history.md` は開かず「直さない（範囲外／履歴）」と一覧に載せる。`tasks/_master/manager.yaml` 15 行目は古いコメント（「毎回のはじめに run-use で結び直す」）だが、触らない範囲なので一覧に「直さない（範囲外。PM へ上げる）」と書く。
- 退避は `cp` ではなく、元の全文を Write で `_archive/2026-10-24-run-use-before.md` に書く（`.claude/skills/` 配下は Bash から書けない）。書いたら `diff` で一字も欠けていないことを確かめる。
- `orca` コマンドは打たない（文書の作業。手順の動作確認は範囲外）。
