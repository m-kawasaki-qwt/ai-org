# 目的

一般に良いとされている UI・UX のセオリーを出典つきで集め、そこから「川崎さんに出せる水準か」を判定する基準（チェックリスト）と、UI デザイナーの職種の規範の元になる原則の一覧を作る。上のプロジェクト p6-org-build の完了条件 0 そのもので、後の「職種 UI デザイナー」「画面で確かめる基準」はこのチームの出力を元に作られる（別のチーム org-build が組み込む）。

川崎さんはデザイナーではない。だから「一般のセオリー」から定義する（自分たちの好みで決めない）。目的は川崎さんの認知負荷を減らすこと（ai-org の `policy.md`）。

出発点:
- 川崎さんのフィードバック `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md`（画面ごとの指摘・UI 全体の指摘）
- 上のプロジェクトの charter `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/charter.md`

# 完了条件

1. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/research/sources.md` に、調べたセオリーの一覧がある。少なくとも次の領域を含む: ユーザビリティのヒューリスティクス（Nielsen の 10 原則など）／アクセシビリティの指針（WCAG 2.2 のコントラスト・フォーカス・操作対象の大きさ など）／情報の階層と視覚の階層／段階的開示（要点を先に・詳細は畳む）／ダッシュボードの設計／データの見せ方（表・グラフ・時系列。データインク比 など）／ダークモードの配色／アフォーダンス（クリックできるものが分かる）／レスポンシブ（決めた画面幅の範囲で崩れない）／文章の書き方（UI ライティング・簡潔さ）。1 項目ごとに: 原則の名前・1〜3 行の要約・出典（タイトルと URL。一次資料を優先）。
2. 出典の URL は実在し、要約が出典の内容と食い違っていない（Gemini の回答だけで済ませず、主要なものは出典を開いて裏を取った印を付ける）。
3. `.../p6-org-build/research/checklist.md` に、判定の基準（チェックリスト）がある。各項目は「実際の画面（スクリーンショット）を見て、はい／いいえで答えられる」形で、元になったセオリー（sources.md の項目）への参照が付いている。「画面を作る前に決めること（要素ごとに何のために誰に出すか、など）」と「画面を撮って確かめること」に分けてある。
4. `.../p6-org-build/research/principles.md` に、UI デザイナーの規範の元になる原則（作るときの考え方・手順）が、sources.md への参照つきでまとまっている。
5. フィードバックの指摘（画面ごと・UI 全体）の一つ一つが、checklist.md のどの項目で引っかかるかの対応表が `.../p6-org-build/research/feedback-map.md` にある。引っかからないものは「引っかからない」と書く。

# 範囲

- 書いてよい場所: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/research/` と、このチームのディレクトリの中。
- 調べるのは Gemini（dev-tools のスキル `gemini-api`。`gemini-api search` を単独の 1 コマンドで打つ）を使ってよい。WebFetch で出典を精読してよい。
- 触らないもの: dev-tools（本体・worktree とも）・job（読むだけ）。git の操作はしない。
- 人にしかできない操作が要ったら（Gemini の API キーが無い 等）: 手順を書いて escalate。
- うまくいかなかったこと（文脈パックの過不足・連絡・決まり）は、隠さずセッション報告の `unclear` と最後の報告に書く。
