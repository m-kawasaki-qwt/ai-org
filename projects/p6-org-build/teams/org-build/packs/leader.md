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
---

# 文脈パック: リーダー — org-build

事業の案件ではなく、組織そのものの改修。job は川崎さんのフィードバック 1 本だけ読む（台帳の `job.deny` と、事業の資料は読まない）。以下の「worktree」は `/Users/maka343noshi/orca/workspaces/dev-tools/org-build`、「ai-org」は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | ai-org `projects/p6-org-build/teams/org-build/charter.md` | 完了条件 1〜8 と範囲。全部 |
| 2 | ai-org `projects/p6-org-build/charter.md` | 上の目的。「足すもの」と「進め方」 |
| 3 | job `company/system/ai-org/feedback/2026-10-24-viewer.md` | 防ぎたい失敗の実物。「画面ごとの指摘」「UI 全体の指摘」「組織の側の原因と足すもの」。完了条件 8 の対応表の行になる |
| 4 | ai-org `policy.md` | 判断の基準。1 節（何のための組織か）・3 節（視点を分ける）・4 節（川崎さんの番は少なく） |
| 5 | worktree `docs/todo/ai-org-plan.md` | 「立場と職種」節（117〜142 行。完了条件 6 で書き足す先）と、決定ログ 2026-10-24 の最後の行（3 つ足す決定） |
| 6 | worktree `org/README.md`・`org/context.yaml`・`org/positions/*/position.md` | 何がどこで決まっているかの地図。中身は作業者が読む |
| 7 | ai-org `projects/p5-org-viewer/teams/viewer/result.md` | p5 で起きたこと。「申し送り」「うまくいかなかったこと」（撮り方の実例と、承認の後にリーダーが rework を出した経緯） |
| 8 | ai-org `projects/p6-org-build/research/`（届いてから） | `principles.md`・`checklist.md`・`feedback-map.md`。後半の材料 |

## 事業の文脈の要約

- この組織の目的は川崎さんの認知負荷を減らすこと。p5 のビューアは「ログを HTML にしただけ」で、出せる水準に届かなかった。原因は組織の側にある: UI の職種が無い／使う人の目線で見る立場が無い／実際の画面で「出せる水準か」を問う基準が無い。今回はこの 3 つを雛形と orgctl に足す。
- 川崎さんはデザイナーではない。だから UI の規範と判定の基準は、自分たちの好みではなく、一般のセオリー（別チーム uiux-research の出力）から作る。規範へは要約と参照で入れ、全文を写さない（システムプロンプトが膨らむ）。
- 見るのは川崎さん 1 人・PC・画面幅 900〜1800px・ダークモード。

## これまでの経緯

- p1〜p5 で、状況ツール・タイムライン・監査役・コーディネーターと文脈パック・ビューアを作ってきた。p5 のフィードバックで今回の 3 つを足すことが決まった（決定ログ 2026-10-24）。
- 同時に uiux-research チームが `research/` を作っている。届いたら PM から知らせが来る。

## 段取り（コーディネーターの案）

1. **前半（research を待たずに進める）**: worker-orgctl が `--persona`（引数・存在しないときの止まり方・システムプロンプトへの入れ方・`context.yaml`）を作り、worker-norms が `org/personas/` の 3 ファイルと、立場（レビュアー・リーダー・PM）・コーディネーターの規範の「受け口」（Playwright で撮って判定する流れ・撮り方。判定の中身はチェックリストを参照する形にしておく）を書く。レビュアーは前半の orgctl を仮の repo で確かめる。
2. **後半（research が届いてから）**: worker-norms が `org/occupations/ui-designer/` を書き、受け口にチェックリストへの参照を入れ、org-project-new のスキル・README・プランを書く。対応表（完了条件 8）は research の `feedback-map.md` に「組み込んだ先」を足して作る。レビュアーが全体を見る。

- 担当の境目: `orgctl.py` と `context.yaml` は worker-orgctl、それ以外の文面（personas・positions・occupations・スキル・README・プラン）は worker-norms。README の `--persona` の説明は worker-orgctl が文案を渡し、worker-norms が README に入れる（同じファイルを 2 人で触らない）。
- 複数のペルソナを指定できるか（完了条件 3）は前半でリーダーが決めて両方に渡す。コーディネーターの推奨は「複数可（`--persona` を何度でも。`--pack` と同じ形）」。編成案でペルソナを複数付けると決めているので。
