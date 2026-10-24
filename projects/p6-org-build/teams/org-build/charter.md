# 目的

AI 組織の雛形（dev-tools の `org/`）と `orgctl` に、ビューアの試走（p5）で足りないと分かった 3 つを足す。組織が作るものを、川崎さんが見る前に組織の中で「川崎さんに出せる水準か」まで持っていけるようにする（上のプロジェクト p6-org-build の完了条件 1〜4）。

足すもの（詳細は上の charter `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/charter.md` の「足すもの」）:

1. 職種「UI デザイナー」（`org/occupations/ui-designer/`）
2. ペルソナで見るレビュアー（`org/personas/` と `orgctl assign` の `--persona`）。最初のペルソナは 3 つ: 川崎さん本人／実際に使うエンドユーザー／営業する側。
3. 「出せる水準か」を実際の画面で確かめる基準（Playwright で撮って、ペルソナの目線で判定する。レビュアー・リーダー・PM・根っこのセッション）

1 と 3 の中身の元は、別のチーム uiux-research が作る `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/research/`（`sources.md`・`checklist.md`・`principles.md`・`feedback-map.md`）。届くまでは 2（ペルソナと `--persona`）とコーディネーターの規範・立場の側の受け口から進める。届いたら PM から知らせる。research の中身を規範に写すときは、要約して参照を付ける（全文を写さない。システムプロンプトが膨らむ）。

出発点: 川崎さんのフィードバック `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md`、プランの決定ログ（dev-tools の `docs/todo/ai-org-plan.md` の 2026-10-24 の行）、p5 の撮り方の経緯（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/` の `result.md`・`thread.md`）。

# 完了条件

1. `org/occupations/ui-designer/` があり、規範が research の `principles.md`・`checklist.md` を元にしている（どの原則から来たかが辿れる）。画面を作る・直すときに、要素ごとに「何のために、誰に出すか」を先に決めてから組み立てる手順が入っている。
2. `org/personas/` に 3 つのペルソナがファイル 1 つずつある（川崎さん本人＝認知負荷を減らしたい・全部並べない・開いて回らずに掴みたい・明るい画面は嫌／実際に使うエンドユーザー／営業する側）。
3. `orgctl assign ... --persona <名前>` でペルソナがメンバーのシステムプロンプトに入る。複数指定できるか 1 つかはチームで決めて README に書く。存在しないペルソナを指定したら、使えるペルソナの一覧を添えた分かる言葉で止まる（終了コードが 0 でない）。`org/context.yaml` に personas の扱いが入っている。
4. 立場（`org/positions/` のレビュアー・リーダー・PM）とコーディネーターの規範に、次が入っている: 画面を作るチームでは、レビュアーとリーダーが Playwright で実際の画面を撮り、ペルソナの目線でチェックリストに照らして「このまま川崎さんに出せるか」を判定する／PM は撮った画面を見てから上へ上げる／コーディネーターは編成案で、UI デザイナーを入れるか・どのペルソナのレビュアーを付けるか（複数可）を決める。撮り方（ローカルのポートの待ち受けはサンドボックスの外で動かす 等、p5 で分かったこと）が手順にある。
5. `claude/plugins/dev-tools/skills/org-project-new/` のスキルに、根っこのセッションが上へ出す前に同じ基準で画面を見ることが書いてある。
6. `org/README.md` とプラン（`docs/todo/ai-org-plan.md` の「立場と職種」）に、足したものが書いてある。
7. 仮の repo（scratchpad 等。ai-org の本体の `projects/` は使わない）で、worktree の orgctl を使って `new`→`assign --persona`（UI デザイナーの職種つき、存在しないペルソナも）を打ち、ペルソナと職種がシステムプロンプトに入ること・存在しないペルソナで止まることを確かめた結果（打ったコマンドと出力の要点）が報告にある。
8. フィードバックの指摘の一つ一つについて、足したもののどこ（ファイルと節）でそれを防げるかの対応表が報告にある（research の `feedback-map.md` を元に、組み込んだ先を足す。防げないものは「防げない」と書く）。

# 範囲

- 書いてよい場所: dev-tools の worktree `/Users/maka343noshi/orca/workspaces/dev-tools/org-build` の中だけ（`org/`・`docs/todo/ai-org-plan.md`・`claude/plugins/dev-tools/skills/org-project-new/`）と、このチームのディレクトリの中。
- dev-tools の本体（`~/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`）は読むだけ。動いている組織は本体の orgctl を使っているので、本体を書き換えない。ai-org の本体の `projects/` に試しのコンポーネントを作らない。
- 作業者は worktree を `--workdir` にして起動する。
- orgctl は標準ライブラリだけで動くこと（今の決まり）を崩さない。
- git の操作はしない（コミットと PR は根っこの側）。
- 人にしかできない操作が要ったら: 手順を書いて escalate。
- うまくいかなかったこと（文脈パックの過不足・連絡・決まり）は、隠さずセッション報告の `unclear` と最後の報告に書く。
