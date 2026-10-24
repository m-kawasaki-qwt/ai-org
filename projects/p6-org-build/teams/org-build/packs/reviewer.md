---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/businesses/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/partners/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/tasks/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/teams/org-build/hints/**
---

# 文脈パック: レビュアー — org-build

作業のヒント（`hints/`）は読まない。見るのは完了条件に照らした出来と、実際に orgctl を打った結果。「worktree」は `/Users/maka343noshi/orca/workspaces/dev-tools/org-build`、「ai-org」は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | ai-org `projects/p6-org-build/teams/org-build/charter.md` | 完了条件 1〜8 と範囲。全部。指摘は完了条件の番号で書く |
| 2 | job `company/system/ai-org/feedback/2026-10-24-viewer.md` | 対応表（完了条件 8）の突き合わせ。「画面ごとの指摘」「UI 全体の指摘」の行が全部あるか |
| 3 | worktree `CLAUDE.md` | この repo の決まり |
| 4 | worktree `org/scripts/orgctl.py` の `cmd_assign`（290 行〜）と `assign` の引数（1374 行〜） | 既存の挙動が変わっていないか・標準ライブラリだけか |
| 5 | worktree の変更されたファイル（`git -C <worktree> status`・`diff` で一覧） | 範囲の外に書いていないか |
| 6 | ai-org `projects/p6-org-build/research/`（届いてから） | ui-designer の規範・判定の基準が、`principles.md`・`checklist.md` から辿れるか（要約と参照で、全文の写しでないか） |

## 事業の文脈の要約

- p5 のビューアは、撮ってはいたが「出せる水準か」を問う基準が無く、レビュアーが承認した後でリーダーが目的に照らして作り直しを出した。今回足す規範は、それを防ぐためのもの。規範を読んで「この手順を踏めば p5 の指摘に引っかかるか」で見る。
- 規範はシステムプロンプトに入る。research を丸写しして膨らんでいたら指摘する。

## 確かめ方（完了条件 7）

- worktree の orgctl（`python3 /Users/maka343noshi/orca/workspaces/dev-tools/org-build/org/scripts/orgctl.py`）を使う。本体の orgctl ではない。
- 仮の repo は scratchpad に作る。ai-org の本体の `projects/` に作らない。
- 打つもの: `new` → `assign ... --occupation ui-designer --persona <名前>`（できた `system.md` にペルソナと職種が入っているか）→ 存在しないペルソナ（一覧つきで止まり、終了コードが 0 でないか）→ 複数指定（リーダーが複数可と決めた場合）→ `--persona` 無しの assign が今までどおりか。
- 打ったコマンドと出力の要点を review の本文に残す（報告にそのまま載る）。

## これまでの経緯

- 前半に orgctl と personas が先に来る。research が届く前の段では、ui-designer と判定の中身は未着で正しい（それだけで NG にしない）。
