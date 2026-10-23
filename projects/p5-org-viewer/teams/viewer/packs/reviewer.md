---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/hints/**
---

# 文脈パック: レビュアー — viewer

作業のヒント（`hints/`）は読まない。見るのは目的と完了条件に照らした出来だけ。job は読まない。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | ai-org `projects/p5-org-viewer/teams/viewer/charter.md` | 完了条件 1〜4 と範囲。全部。指摘は完了条件の番号で書く |
| 2 | ai-org `policy.md` | 1・4・5 節。「要点を先に・詳細は畳む」が守られているかの基準 |
| 3 | dev-tools worktree `/Users/maka343noshi/orca/workspaces/dev-tools/org-viewer/CLAUDE.md` と ai-org worktree `/Users/maka343noshi/orca/workspaces/ai-org/viewer/CLAUDE.md` | 2 つの repo の決まり |
| 4 | dev-tools worktree `org/scripts/orgctl.py` の `NOISE_KINDS`（44 行）と、足された `export` | 完了条件 1 の「二重に定義しない」「標準ライブラリだけ」を見る |
| 5 | ai-org 本体の `projects/p1-org-status`〜`p4-job-run-use` | 表示が実物と合っているかの突き合わせ（抜き取りでよい） |

## 事業の文脈の要約

- 見る人は川崎さん 1 人、PC。ビューアの目的は認知負荷を減らすこと。各画面は「開いて 10 秒でどこを見ればいいか分かるか」で見る。全部を並べていたら、それは不足。
- 記録を読む正は orgctl の 1 か所。ビューア（Astro）が `snapshot.json` 以外を読んでいたり、数え直していたりしたら完了条件 1・2 に反する。

## 見るときの当て（実物で確かめやすい所）

- 数えるための行（`ack`・`notify_*`・`patrol`）が時系列や往復の数に混ざっていないか。
- 開いているプロジェクト（p5 自身。セッション報告がまだ無い）で export・画面が落ちないか。
- 監査の改訂案は p3 にしかない（監査役の報告の本文）。p3 で出ているか。unclear はセッション報告の多くにある。
- `astro build` が通るか、README のコマンドがそのまま 1 行ずつ打てるか、スクリーンショットが 5 画面ぶん `screenshots/` にあるか。

## これまでの経緯

- p3 の `org_timeline.py`（1 プロジェクト 1 枚の HTML）の後継。スキーマを先に固め、export とビューアを 2 人で並べて作る編成。
