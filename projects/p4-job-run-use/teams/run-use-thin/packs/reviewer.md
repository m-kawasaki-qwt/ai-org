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
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.claude/plans/**
---

# 文脈パック: レビュアー — run-use-thin

出発点の記録（job の `.claude/plans/`）は読ませない。何を残すべきかは charter と下の要約で足り、作業者と同じ下書きに引っ張られずに照らすため。`.claude/skills/manager/sources/orca/_archive/` は読める（退避の diff に要る）。

## 読む資料

job は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job`、dev-tools は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`。

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p4-job-run-use/teams/run-use-thin/charter.md` | 完了条件 1〜5 が照らす基準。全部 |
| 2 | job `.claude/skills/manager/sources/orca/_archive/2026-10-24-run-use-before.md` と `run-use.md` | 退避が一字も欠けていないか（元の版はコミット済み。`git -C <job> show HEAD:.claude/skills/manager/sources/orca/run-use.md` を scratchpad に出して `diff`。読むだけの git は可）、薄くした版が job 固有だけを持つか |
| 3 | dev-tools `claude/plugins/dev-tools/skills/orca-multi-agent/SKILL.md` | 食い違いの照合先。「B. 依頼する（Orca に投げる）」の「`run-use` の使いどころ」、「C. 一覧を出す」、「D. 戻りを受ける（`worker_done`）」。run-use.md が指す見出し名が実在するかも見る |
| 4 | job `CLAUDE.md` | 「## 情報を消さない」の節（41〜47 行）だけ |
| 5 | job `.claude/skills/manager/sources/orca/run-use-log.md` | run-use.md の「ログ」の節と書き先・種別が噛み合うか |
| 6 | 完了条件 3 で作業者が直したファイルと、その退避先 | 参照元の矛盾が無いか。節番号で指している 3 か所（下）を必ず見る |

## 事業の文脈の要約

- job は多数のセッションが同時に書くナレッジベースで、「情報を消さない」が最優先。外した文は退避されていなければならない。
- job の常設 Run は manager `run_31ab18962379`、routine-work `run_5c5c7f0b494d`。
- run-use.md に残ってよい job 固有のもの: Run の ID、引き取るまでの時間（2 時間）、automation の印（`依頼元の端末` の行の `手動｜automation: manager hourly｜automation: <group>/<task>`）、観察ログとその書き方、誤配の job での運用（ログに〔誤配〕・川崎さんへ 1 行）、manager は Run の全部・routine-work は自分の起票の Task だけを見る範囲の分け方。これ以外で SKILL.md と同じ事柄を書き直している文は、完了条件 1 の不足。
- dev-tools は 2026-10-23 に直り、「新しい端末は最初に `run-use`」はもう書いていない。run-use.md に「dev-tools より優先する」旨が残っていれば、前提が古い。

## 照らすときの目印

- 節番号での参照: `manager/sources/orca/inbox.md` 38 行目・`automation-followup/inbox.md` 35 行目が「2. 結ばずに見る」、`manager/advance/implement.md` 58 行目が「1」を指していた。薄くした後の見出しと合っているか。
- 食い違いの見どころ: `inbox` の `--limit` の決め方（SKILL.md は「最後に処理した時刻より前まで届く件数」）、`read` の扱い（SKILL.md は `read` だけで未処理と決めつけない）、引き取りの分岐（通知先が無い・`connected: false`・放置）、依頼していない戻りの扱い（SKILL.md は処理して `--ack`、ユーザーへ 1 行）。
- `tasks/_master/manager.yaml` 15 行目の古いコメントは範囲外で直さないのが正しい。報告で上がっていればよい。
