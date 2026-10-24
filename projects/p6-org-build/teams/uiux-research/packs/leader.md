---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

# 文脈パック: リーダー — uiux-research

実装（調べもの・執筆）には触れない。見るのは、4 つの成果物が「後で org-build チームがそのまま規範とチェックリストに写せるか」と、完了条件 1〜5 に届いているか。job は下の 1 件だけ読む。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/teams/uiux-research/charter.md` | 完了条件 1〜5 と範囲。全部 |
| 2 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/charter.md` | 「足すもの」1〜3。このチームの出力が何に使われるか |
| 3 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/teams/org-build/charter.md` | 完了条件 1・4・8。受け取る側が research の何を使うか（規範に写すときは要約＋参照） |
| 4 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md` | 「画面ごとの指摘」「UI 全体の指摘」。feedback-map.md の行がこれと 1 対 1 か |
| 5 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/policy.md` | 1・3・4 節。判定の軸（認知負荷を減らす・視点を分ける） |
| 6 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/screenshots/` の 5 枚 | チェックリストを実物に当てて、はい／いいえで答えられるか自分でも試す |

## 事業の文脈の要約

- 事業の案件ではない。AI 組織そのものを直すプロジェクト（p6）の、調べものの担当。
- 川崎さんはデザイナーではない。だから基準は「一般のセオリー」から定義し、組織の好みで決めない。出典の無い項目は入れない。
- 判定の目線は川崎さん: PC で 900〜1800px、ダークモード、開いて回らずに要点を掴みたい、全部並べられるのは嫌。チェックリストは、この人に「このまま出せるか」を画面で判定するための道具。
- 出力の受け手は org-build チーム（UI デザイナーの職種・画面で確かめる基準を雛形に組み込む）。システムプロンプトに入れる前提なので、項目は短く、参照で辿れる形が良い。

## これまでの経緯

- p5 でビューアを作ったが、川崎さんが「出せる水準に届いていない」と判定。原因は UI デザイナーの職種が無い・実際の画面を川崎さんの目線で確かめる基準が無い、の 2 点（フィードバックの「組織の側の原因」）。
- p6 で PM が 2 チームを立てた: このチーム（research を作る）と org-build（雛形に組み込む。research が届くまではペルソナと orgctl の側から進める）。届いたら PM が org-build へ知らせるので、終わったら早めに PM へ report する。

## 編成の当て（コーディネーターから）

- 作業者 1 人で始める（4 つのファイルは互いに参照し合うので、分けると番号の付け方が割れる）。量が多すぎて回らないと見たら、領域で 2 人に分けてよい（そのときは sources.md の番号の振り方を先に決めて渡す）。
- レビュアーは作業者とモデルを変えてある。出典の裏取り（URL を開く）は抜き取りでよいが、主要な原則（Nielsen・WCAG・データインク比 など）は全部。
