# 目的

AI 組織のビューア（ai-org の `viewer/`）を作り直し、川崎さんが「組織の中で何が起きているか（どのエージェントがどう動き、誰と誰がどうやりとりしたか・いま何が止まっているか・自分が何を判断すればよいか）」を、ログを開いて回らずに掴めるようにする。プロジェクト p8-viewer-rebuild の目的そのもの（プロジェクトの charter: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild/charter.md`。必ず全文を読む）。

出発点（必ず読む）:

- 川崎さんのフィードバック: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md`
- ペルソナ: dev-tools の `org/personas/kawasaki.md`
- UI のチェックリスト・原則: dev-tools の `org/common/ui/`、撮って確かめる手順: `org/common/screen-check.md`
- 前の静的 HTML の図: ai-org の `tools/org_timeline.py`（川崎さんが「こちらの方がはるかによかった」と言ったもの）

# 完了条件

1. **画面ごとに「何のために、何を判断するために出すか」が先に決まっている。** `worker-ui` が `teams/viewer/design.md`（checklist の B-01〜B-09 への答え）を書き、画面と画面の中の要素ごとに目的を書いている。一覧に載せる列は一つ一つ「なぜ詳細ではなく一覧に載せるのか」の理由がある。目的を言えない画面・要素は載せない（パフォーマンス・監査の画面も、何を判断する画面かを言えなければ作り直すか外す）。
2. **`design.md` は `reviewer-kawasaki` が B に照らして通してから、画面を組み立てる。** 通る前に組み立てを始めていない（thread.md・1 行報告で順番が追える）。
3. **フィードバックの指摘が一つ残らず潰れている。** 指摘ごとに「どの画面のどの要素で、どう直したか（または、なぜ外したか）」の対応表が、チームの結果（PM への `report`）にある。最低限: ダークモード、900〜1800px で崩れない、一覧の概要は 10 文字程度、表が改行で崩れない、Markdown は整形して出す、クリックできるものが見て分かる（ポインタ・見た目）。
4. **時系列は「構造」が見える図になっている。** メンバーごとの帯に時刻順で並べ、誰から誰へのやりとりが線で分かり、入れ子（プロジェクト → チーム → メンバー）が分かる。ログを縦に並べただけの表示は主役にしない。記録にある次の流れが、図から読める: p7 のコーディネーターとの相談の往復（相談 → 返し → 合意）、p6 の並行する 2 チーム（コーディネーター 2 人）、p2・p3・p5 のレビューの差し戻し（`review_ng` → `rework`）、p1 の PM の入れ替え（2 回目の assign）。
5. **川崎さんの目線で撮って確かめてある。** 900px と 1800px の両方で全画面を `org/common/ui/tools/screen-probe.mjs` で撮り、`reviewer-kawasaki` が「判定の問い」と checklist の C に照らして合格を出し、リーダーが自分で撮り直して判定している。撮った画像と json は `teams/viewer/screenshots/` に置き、報告に画像のパスと判定（いいえ の番号が残っていないこと）を書く。
6. **実データで動く。** ai-org の `projects/` の p1〜p8 を `orgctl export` で書き出した `snapshot.json` で表示が崩れない。`design.md` に「snapshot に要るもの」の節があり、その項目が全部 snapshot に入り、`--check` が通る。
7. **export は既存を壊さない。** `orgctl.py` の export とスキーマへの変更は追加だけで、既存の関数の振る舞いを変えない。標準ライブラリだけ。`reviewer-export` が通している。振る舞いを変える必要が出たら、変える前に PM へ `escalate`。

# つなぎ

- 受けるもの: PM からこの charter。
- 渡すもの: PM へ結果の `report`（対応表・撮った画像のパスと判定・変えたファイルの一覧・うまくいかなかったこと）。
- チームの中: `worker-ui` の `design.md`「snapshot に要るもの」→ リーダー → `worker-export`。`worker-export` が `A/viewer/data/snapshot.json` を書き出し、`worker-ui` が実データで組み立てる。作業者どうしは直接やりとりしない。

# 範囲

- 書いてよい場所:
  - ai-org の worktree `/Users/maka343noshi/orca/workspaces/ai-org/viewer-v2` の `viewer/`（と要れば `tools/`）
  - dev-tools の worktree `/Users/maka343noshi/orca/workspaces/dev-tools/viewer-v2` の `org/scripts/orgctl.py`（export）と `org/schema/snapshot.schema.json`
  - チームのディレクトリ（`design.md`・`screenshots/`・`thread.md`）
- 触らないもの: 本体（`~/ghq/.../ai-org`・`~/ghq/.../dev-tools`）は読むだけ。本体のビューア（4390 番）に触らない。4321・4322 番はほかのプロジェクトのもの。git の操作（コミット・ブランチ・worktree）はしない。
- ポート: worker-ui 4391・reviewer-kawasaki 4392・leader 4393・PM 4394。待ち受けと Playwright はサンドボックスの外。worktree の `viewer/` は最初に `npm ci --prefix viewer`。
- 技術の選び方（Astro のまま・図の描き方・ライブラリ）はチームで決めてよい。ただし `snapshot.json` だけを読む形は変えない。
- 監査のまとめ方（要点 → 元の記録へ辿れる 2 段の仕組み）の設計は範囲外。監査の画面は、いまあるデータで「何を判断する画面か」を決める所まで。
- 人にしかできない操作が要ったら: 手順を書いて escalate。
- うまくいかなかったこと（パックの過不足・連絡・決まり）は、隠さず報告とセッション報告の `unclear` に書く。
