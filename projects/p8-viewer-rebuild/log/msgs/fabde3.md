<!-- p8-viewer-rebuild/pm → p8-viewer-rebuild/coordinator start 2026-10-24T15:32:55+09:00 -->
# 相談: p8-viewer-rebuild の切り方（画面を作る）

## 目的・完了条件

charter: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild/charter.md`（必ず全文を読んでください）

要点:
- AI 組織のビューア（ai-org の `viewer/`、Astro、`snapshot.json` だけを読む）を作り直す。川崎さんが「何が起きているか・誰と誰がやりとりしたか・何が止まっているか・何を判断すればよいか」をログを開かずに掴めるようにする。
- 出発点: 川崎さんのフィードバック `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md`、ペルソナ `org/personas/kawasaki.md`、`org/common/ui/`（checklist・原則）、`org/common/screen-check.md`、前の静的 HTML `ai-org/tools/org_timeline.py`（「こちらの方がはるかによかった」）。
- 完了条件 5 つ: ①UI デザイナーの `design.md`（B への答え、画面・要素・一覧の列ごとの目的）②フィードバックの指摘の対応表 ③時系列は構造の図（メンバーの帯・やりとりの線・入れ子。p6・p7 の往復・差し戻し・入れ替えが読める）④900/1800px で全画面を撮り、kawasaki ペルソナのレビュアーが C と判定の問いで合格 ⑤p1〜p8 の `orgctl export` の snapshot.json で崩れない（足りなければ export とスキーマを直す）。

## 画面を作る

はい。UI デザイナーを入れるか・どのペルソナのレビュアーを付けるかを編成案で決めてください（私の見当は下）。

## 作業する repo（2 つにまたがる）

- ai-org の worktree `/Users/maka343noshi/orca/workspaces/ai-org/viewer-v2` の `viewer/`（本体）と要れば `tools/`
- dev-tools の worktree `/Users/maka343noshi/orca/workspaces/dev-tools/viewer-v2` の `org/scripts/orgctl.py`（export）と `org/schema/snapshot.schema.json`
- どちらを `--workdir` にするか、export の直しを同じ作業者に持たせるかを編成で決めてほしい。
- 開発サーバーは 4391〜4399 番。Playwright と待ち受けはサンドボックスの外。最初に `npm ci --prefix viewer`。

## おおまかな考え（どう思う？）

- 画面は 1 つのアプリで密につながっているので、**チーム 1 つ**（子プロジェクトにはしない）でよいと考えている。
- 編成の見当: 作業者 2 人（UI デザイナー: `design.md` を先に書き、画面の見た目・図の形を決める／エンジニア: Astro の実装と export・スキーマの直し）、レビュアー 1 人（`kawasaki` ペルソナ）。
- 順番: design.md（B への答え）→ レビュアーが B に照らして先に通す → 実装 → 撮って C で判定。design.md を通す前に実装を走らせない（p5 の失敗の筋）。ただし export に足りない項目の洗い出しは並行してよい。
- 時系列の図（完了条件 3）がいちばん難しい。`org_timeline.py` の帯の形を発展させる。描き方（SVG を自前で描く・ライブラリ）は組織で決めてよい。
- 崩れそうな前提: 2 つの repo を 1 人の作業者が触るときの権限・パス、p1〜p8 の実データの量（イベント数）で図が読めなくなること。
- 事業の案件ではない（組織の内部の道具）。経営戦略は不要と考えている。

## パックの置き場

`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild/packs/<チーム名>/<立場>.md`

返しには、切り方・順番とその理由、編成（職種・モデル・ペルソナ・workdir）、実現できる理由と崩れる前提、charter に入れてほしいこと、パックのパスを書いてください。
