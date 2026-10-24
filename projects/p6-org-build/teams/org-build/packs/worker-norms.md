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

# 文脈パック: 作業者（engineer）— org-build の雛形・規範の文面

担当は `org/personas/`・`org/occupations/ui-designer/`・`org/positions/`（レビュアー・リーダー・PM・コーディネーター）・`claude/plugins/dev-tools/skills/org-project-new/`・`org/README.md`・`docs/todo/ai-org-plan.md`。`orgctl.py` と `context.yaml` は worker-orgctl の担当なので触らない。「worktree」は `/Users/maka343noshi/orca/workspaces/dev-tools/org-build`、「ai-org」は `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | ai-org `projects/p6-org-build/teams/org-build/charter.md` | 完了条件 1・2・4・5・6・8 と範囲 |
| 2 | job `company/system/ai-org/feedback/2026-10-24-viewer.md` | 防ぎたい失敗の実物。全部。川崎さんのペルソナの元にもなる |
| 3 | ai-org `policy.md` | 1 節・3 節・4 節。川崎さんのペルソナと「出せる水準」の言い方の元 |
| 4 | worktree `org/positions/{reviewer,leader,pm,coordinator}/position.md` | 書き足す先。今の節立て（見るもの・見方・判断してよいこと・上げること・はじめにやること）に合わせて足す |
| 5 | worktree `org/occupations/engineer/occupation.md`・`strategy/occupation.md` | 職種の書き方の手本（短い） |
| 6 | worktree `claude/plugins/dev-tools/skills/playwright/SKILL.md` | 撮り方の手順の元。撮る手順を規範に写さず、このスキルを参照させる |
| 7 | worktree `claude/plugins/dev-tools/skills/org-project-new/SKILL.md` | 完了条件 5 の書き足す先 |
| 8 | worktree `org/README.md`・`docs/todo/ai-org-plan.md` の「立場と職種」（117〜142 行） | 完了条件 6 の書き足す先 |
| 9 | ai-org `projects/p6-org-build/research/`（届いてから） | `principles.md`→ui-designer の規範、`checklist.md`→判定の基準、`feedback-map.md`→対応表。要約して参照を付ける（全文を写さない） |

## 事業の文脈の要約

- p5 のビューアは「ログを HTML にしただけ」で、川崎さんに出せる水準に届かなかった。足すのは 3 つ: UI デザイナーの職種（要素ごとに「何のために、誰に出すか」を先に決めてから組み立てる）／ペルソナで見るレビュアー／実際の画面を撮って「このまま川崎さんに出せるか」を判定する基準。
- ペルソナは 3 つ。川崎さん本人（認知負荷を減らしたい・全部並べない・開いて回らずに掴みたい・明るい画面は嫌・PC で 900〜1800px）はフィードバックと policy から具体に書ける。エンドユーザーと営業する側は、案件ごとに相手が変わるので、「何を見て何を判断する人か」の観点を書き、具体（どんな人か）はコーディネーターが文脈パックで足す形にすると、雛形が特定の事業に寄らない（コーディネーターの推奨。決めるのはリーダー）。
- 川崎さんはデザイナーではないので、UI の規範と判定は一般のセオリー（research）を元にする。自分の好みで項目を作らない。

## p5 で分かった撮り方（手順に入れる）

- 画面の待ち受け（`astro preview` 等）と Playwright は、localhost の待ち受け・接続のためサンドボックスの外で動かした。
- 撮影用の Playwright は scratchpad に入れ、作業する repo の依存に入れなかった。
- `~/.npm` のキャッシュの権限が壊れていて、`npm install` は `--cache` を TMPDIR に向けて回避した。
- 撮影スクリプトの引数に `/=名前` の形を使うと directory-guard が絶対パスと誤判定した（`名前,/パス` に変えて回避）。
- 撮ってはいたが「出せる水準か」を問う基準が無く、レビュアーの承認後にリーダーが目的に照らして rework を出した。レビュアー自身も「画面の数字が指す先が初期表示で見えるかを承認の基準に入れるべきだった」と残している。

## これまでの経緯

- 前半（research を待たずに）: personas の 3 ファイルと、立場・コーディネーターの規範の受け口（誰が・いつ撮って・何に照らして判定するか。判定の中身はチェックリストの参照にしておく）。
- 後半（research が届いてから。PM→リーダー経由で知らせが来る）: ui-designer、受け口へのチェックリストの参照、スキル、README、プラン、対応表。
- README の `--persona` の説明は worker-orgctl から文案が来る。
