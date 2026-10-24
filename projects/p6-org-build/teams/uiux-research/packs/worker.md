---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

# 文脈パック: 作業者 — uiux-research

書くのは `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/research/` の 4 ファイル（`sources.md`・`checklist.md`・`principles.md`・`feedback-map.md`）だけ。作業する repo は無い。dev-tools は読むだけ（下の 1 件）、job は下の 1 件だけ読む。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/teams/uiux-research/charter.md` | 完了条件 1〜5（領域の一覧・1 項目の形・ファイルの分け方）と範囲。全部 |
| 2 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md` | 「画面ごとの指摘」「UI 全体の指摘」。feedback-map.md の行の元。調べる領域の当たりもここから |
| 3 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/charter.md` | 「足すもの」1・3。principles.md と checklist.md が何の規範・基準になるか |
| 4 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/policy.md` | 1・4 節。見る人（川崎さん）の目的＝認知負荷を減らす |
| 5 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/claude/plugins/dev-tools/skills/gemini-api/SKILL.md` | 「最重要ルール」「search」の節。検索の打ち方 |
| 6 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/screenshots/` の 5 枚 | チェックリストの項目を実物に当てて、はい／いいえで答えられるか試す（指摘された画面そのもの） |

## 事業の文脈の要約

- 事業の案件ではない。AI 組織に「UI デザイナー」の職種と「川崎さんに出せる水準か」を画面で確かめる基準を足す。その元になるセオリーと基準を作るのがこの仕事。組み込むのは別のチーム（org-build）。
- 川崎さんはデザイナーではない。だから基準は一般のセオリーから定義する。出典の無い項目・自分の好みの項目は入れない。
- 判定の目線は川崎さん: PC で 900〜1800px（スマホは対象外）、ダークモード、開いて回らずに要点を掴みたい、全部並べられるのは嫌。ログを並べただけの画面は不足。
- 受け手はシステムプロンプトに要約して入れる。項目は短く、`sources.md` の番号で辿れる形にする。

## これまでの経緯

- p5 で組織がビューアを作り、川崎さんが「出せる水準に届いていない」と判定（フィードバック）。p6 はその原因（職種が無い・画面で確かめる基準が無い）を組織に足すプロジェクト。

## 作業の注意

- `gemini-api search` は単独の 1 コマンドで打つ（パイプ・リダイレクト・`&&` とつながない）。API キーが無いと言われたら、手順を書いてリーダーへ。
- Gemini の答えだけで出典にしない。主要な原則は WebFetch で出典を開き、要約と食い違わないかを確かめ、`sources.md` の項目に裏を取った印を付ける（どの項目を開いたかが分かる形）。一次資料（W3C・NN/g・著者の原典 など）を優先。
- チェックリストの各項目は「スクリーンショットを見て、はい／いいえで答えられる」形。「分かりやすいか」のような感想で答える項目にしない。画面だけでは答えられない項目（「何のために出すかを決めたか」など）は「画面を作る前に決めること」へ。
