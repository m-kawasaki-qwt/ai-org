---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/teams/uiux-research/hints/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

# 文脈パック: レビュアー — uiux-research

作業のヒント（`hints/`）は読まない。見るのは完了条件 1〜5 に照らした出来だけ。指摘は完了条件の番号で書く。job は下の 1 件だけ読む。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/teams/uiux-research/charter.md` | 完了条件 1〜5 と範囲。全部 |
| 2 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md` | 「画面ごとの指摘」「UI 全体の指摘」。feedback-map.md に漏れ・まとめすぎが無いかの突き合わせ |
| 3 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/policy.md` | 1・4 節。判定の目線（認知負荷を減らす） |
| 4 | `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/screenshots/` の 5 枚 | チェックリストを実際に当て、はい／いいえで答えが出るかを自分で試す |
| 5 | 作業者の `research/` の 4 ファイル | 見る対象 |

## 事業の文脈の要約

- 事業の案件ではない。この research は、AI 組織の「UI デザイナー」の規範と「川崎さんに出せる水準か」を画面で確かめる基準の元になる。
- 川崎さんはデザイナーではないので、基準は一般のセオリーから定義する。出典の無い項目・組織の好みの項目は不足として扱う。
- 判定の目線は川崎さん: PC で 900〜1800px、ダークモード、開いて回らずに要点を掴みたい、全部並べられるのは嫌。

## 見るときの当て

- 出典: URL が実在するか、要約が出典と食い違っていないか。主要な原則（Nielsen の 10 原則・WCAG 2.2 のコントラスト／フォーカス／操作対象の大きさ・データインク比 など）は全部開く。残りは抜き取り。Gemini の要約をそのまま出典にしていないか。
- 領域: 完了条件 1 の 10 領域がそろっているか。
- チェックリスト: p5 のスクリーンショットに当てて、各項目にはい／いいえで答えられるか。感想で答える項目（「見やすいか」）が混ざっていないか。「作る前に決めること」と「撮って確かめること」が分かれているか。sources.md への参照が全項目にあるか。
- 対応表: フィードバックの指摘が 1 件ずつ行になっているか（まとめて 1 行にしていないか）。「引っかからない」と書くべきものを無理に当てていないか。

## これまでの経緯

- p5 で組織が作ったビューアを、川崎さんが「出せる水準に届いていない」と判定した。上の 5 枚はそのときの画面。p6 はその原因を組織に足すプロジェクト。
