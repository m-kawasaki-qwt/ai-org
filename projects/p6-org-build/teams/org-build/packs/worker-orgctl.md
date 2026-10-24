---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**
---

# 文脈パック: 作業者（engineer）— org-build の orgctl

担当は `org/scripts/orgctl.py` と `org/context.yaml`。job は読まない。「worktree」は `/Users/maka343noshi/orca/workspaces/dev-tools/org-build`（作業する場所。ここ以外に書かない）。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | ai-org `projects/p6-org-build/teams/org-build/charter.md` | 完了条件 3・7 と範囲（標準ライブラリだけ・本体を書き換えない） |
| 2 | worktree `CLAUDE.md` | この repo の決まり |
| 3 | worktree `org/scripts/orgctl.py` | `cmd_assign`（290〜405 行。職種の確かめ方 300〜302、システムプロンプトの組み立て 350〜390）と、`assign` の引数（1374〜1385 行。`--pack` の `action="append"` が複数指定の手本） |
| 4 | worktree `org/context.yaml` | personas の扱いを足す先。`positions`・`occupations` の書き方に合わせる |
| 5 | worktree `org/README.md` | 冒頭〜「足すとき」節（38 行〜）。`--persona` の説明の文案を書くため（README へ入れるのは worker-norms） |
| 6 | worktree `org/personas/`（worker-norms が作る） | 読み込む先。ファイル名＝ペルソナ名（例 `kawasaki.md`）の形をリーダーと揃える |

ai-org は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`。

## 事業の文脈の要約

- レビュアーに「誰の目線で見るか」を持たせる。`orgctl assign ... --persona <名前>` で `org/personas/<名前>.md` をメンバーのシステムプロンプトに入れる。存在しない名前なら、使えるペルソナの一覧を添えて止まる（終了コード 0 以外）。職種の存在確認（`die(...)`）と同じ作り。
- 複数指定にするかはリーダーが決める（コーディネーターの推奨は `--pack` と同じく何度でも）。
- 動いている組織は本体の orgctl を使っている。本体は読むだけ。

## これまでの経緯

- p5 で orgctl に `export` が足された（既存の関数は変えずに足した）。今回も既存の挙動を変えずに足す。
- `org/personas/` は同じチームの worker-norms が前半で書く。まだ無ければ、名前の形だけリーダーと決めて仮のファイルで確かめてよい（worktree に残さない）。
- 確かめは仮の repo（scratchpad 等）で `new`→`assign`。ai-org の本体の `projects/` に作らない。
