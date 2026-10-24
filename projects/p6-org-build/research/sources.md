# UI・UX のセオリーの一覧（出典つき）

## Summary

- 10 の領域で、一般に良いとされている UI・UX の原則を 45 件集めた（各領域 3〜8 件）。1 件ごとに番号・名前・要約（1〜3 行）・出典・裏取りの印がある。
- 番号は `checklist.md`・`principles.md`・`feedback-map.md` と共通。途中で振り直さない。接頭辞: H ヒューリスティクス／A アクセシビリティ／V 視覚の階層／P 段階的開示／D ダッシュボード／G データの見せ方／K ダークモード／F アフォーダンス／R レスポンシブ／W 文章。
- 一次資料（Nielsen Norman Group・W3C・著者の原典・Apple・Microsoft・MDN）を優先した。裏取りの印: **✅** ＝ 2026-10-24 に出典を開き、要約と食い違わないことを確かめた ／ **△** ＝ 一部だけ確かめた（何を確かめていないかを備考に書く）。Gemini の回答だけの項目は無い。
- 川崎さんの条件（PC で 900〜1800px・ダークモード・開いて回らずに要点・全部並べない）は出典ではなく、セオリーを当てはめるときの条件として `checklist.md` の判定の基準に入れた。

## 目次

- [H ユーザビリティのヒューリスティクス](#h-ユーザビリティのヒューリスティクス)
- [A アクセシビリティ（WCAG 2.2）](#a-アクセシビリティwcag-22)
- [V 情報の階層と視覚の階層](#v-情報の階層と視覚の階層)
- [P 段階的開示](#p-段階的開示)
- [D ダッシュボードの設計](#d-ダッシュボードの設計)
- [G データの見せ方](#g-データの見せ方)
- [K ダークモードの配色](#k-ダークモードの配色)
- [F アフォーダンス（クリックできるものが分かる）](#f-アフォーダンスクリックできるものが分かる)
- [R レスポンシブ](#r-レスポンシブ)
- [W 文章の書き方](#w-文章の書き方)
- [調べ方の記録](#調べ方の記録)

---

## H ユーザビリティのヒューリスティクス

出典の多くは Jakob Nielsen「10 Usability Heuristics for User Interface Design」（Nielsen Norman Group、1994 初出・2024-01-30 見直し）<https://www.nngroup.com/articles/ten-usability-heuristics/>。10 原則のうち、画面の判定に使うものだけを載せた。

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| H-01 | システムの状態が見える（Visibility of system status） | 何が起きているかを、適切なフィードバックで、いつも使う人に知らせる。 | 10 Heuristics（上） #1 | ✅ |
| H-02 | 実世界との一致（Match between system and the real world） | 使う人の言葉で話す。内部の用語・コードではなく、なじみのある言葉と自然な順序を使う。 | 10 Heuristics #2（エラーは「plain language (no error codes)」#9 も同じ趣旨） | ✅ |
| H-03 | 一貫性と標準（Consistency and standards） | 違う言葉・見た目が同じ意味かを使う人に迷わせない。プラットフォームの慣習に従う。 | 10 Heuristics #4 | ✅ |
| H-04 | 記憶より認識（Recognition rather than recall） | 要素・操作・選択肢を見える所に置き、画面の別の場所の情報を覚えておかせない。 | 10 Heuristics #6 | ✅ |
| H-05 | 美的で最小限のデザイン（Aesthetic and minimalist design） | 無関係な情報・めったに要らない情報を載せない。余分な情報は、必要な情報と注意を奪い合う。 | 10 Heuristics #8 | ✅ |
| H-06 | 認知負荷を減らす | 認知負荷＝システムを使うのに要る心的な資源。①意味の無い視覚の雑音を削る ②なじみのある型を使う ③読む・覚える・決める仕事を画面の側で肩代わりする。 | Kathryn Whitenton「Minimize Cognitive Load to Maximize Usability」NN/g <https://www.nngroup.com/articles/minimize-cognitive-load/> | ✅ |

[↑ 目次へ](#目次)

## A アクセシビリティ（WCAG 2.2）

出典はすべて W3C「Understanding WCAG 2.2」の各達成基準のページ。

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| A-01 | コントラスト（最低限）1.4.3・AA | 文字と背景のコントラスト比は 4.5:1 以上。大きい文字（18pt 以上、太字は 14pt 以上）は 3:1 以上。 | <https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html> | ✅ |
| A-02 | 文字以外のコントラスト 1.4.11・AA | UI の部品（の境界・状態）と、内容の理解に要る図形（グラフの棒・線など）は、隣の色と 3:1 以上。 | <https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html> | ✅ |
| A-03 | 色だけに頼らない 1.4.1・A | 情報・操作の指示・要素の区別を、色だけで伝えない（文字・形・位置を併せる）。 | <https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html> | ✅ |
| A-04 | フォーカスが見える 2.4.7・AA | キーボードで操作できる UI では、フォーカスの位置を示す表示が見える。 | <https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html> | ✅ |
| A-05 | フォーカスが隠れない（最低限）2.4.11・AA | フォーカスを受けた部品が、作り手の置いた要素（固定のヘッダー等）で完全に隠れない。 | <https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html> | ✅ |
| A-06 | 操作対象の大きさ（最低限）2.5.8・AA | ポインタで押す対象は 24×24 CSS px 以上（周りに 24px の間隔がある・文中のリンク などは例外）。 | <https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html> | ✅ |
| A-07 | 情報と関係 1.3.1・A | 見た目で伝えている構造・関係（見出し・表・リスト）が、プログラムでも読み取れる（見出しは見出しの要素、表は表の要素で書く）。 | <https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html> | ✅ |
| A-08 | 視覚的な表示 1.4.8・AAA | 文章のかたまりは、1 行 80 字以内（CJK は 40 字以内）・両端揃えにしない・行間は 1.5 倍以上、を使う人が選べる。 | <https://www.w3.org/WAI/WCAG22/Understanding/visual-presentation.html> | ✅ |

[↑ 目次へ](#目次)

## V 情報の階層と視覚の階層

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| V-01 | 視覚の階層 | 重要な順に目が届くように並べる。手段は色とコントラスト・大きさ・まとまり。大きさは 3 段（見出し・小見出し・本文）、強調の段は 3 つまで（「全部を強調すると何も目立たない」）。目を細める（ぼかす）と意図しない焦点が分かる。作る前に内容の階層と要点を決める。 | Aurora Harley「Visual Hierarchy in UX: Definition」NN/g <https://www.nngroup.com/articles/visual-hierarchy-ux-definition/> | ✅ |
| V-02 | 近接（ゲシュタルト） | 近い物は同じまとまり、離れた物は別のまとまりに見える。見出しはその中身の近くに置く。画面幅が変わるとまとまりが崩れるので、幅ごとに確かめる。 | 「The Principle of Proximity」NN/g <https://www.nngroup.com/articles/gestalt-proximity/> | ✅ |
| V-03 | F 字の走査と、見出しの頭に情報を置く | 整っていない文章では、人は上の数行と各行の頭だけを読む。要点を最初の 2 段落に置き、見出しは情報を運ぶ語から始める（頭の 2 語で中身が分かる）。 | Kara Pernice「F-Shaped Pattern of Reading on the Web」NN/g <https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/> | ✅ |
| V-04 | 逆ピラミッド（結論が先） | いちばん大事なことを最初に書き、補足を重要な順に続ける。どこで読むのをやめても要点が残る。 | 「Inverted Pyramid: Writing for Comprehension」NN/g <https://www.nngroup.com/articles/inverted-pyramid/> | ✅ |

[↑ 目次へ](#目次)

## P 段階的開示

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| P-01 | 段階的開示 | 最初は少数の最も大事なものだけを見せ、専門的なものは求められたら出す。頻繁に要るものは最初の画面に置く。段は 2 段まで（3 段以上は使いにくい）。開く操作は見える所に置き、開くと何が出るかが分かる名前を付ける。 | Jakob Nielsen「Progressive Disclosure」NN/g <https://www.nngroup.com/articles/progressive-disclosure/> | ✅ |
| P-02 | デスクトップのアコーディオン | 向くのは「使う人が少しの情報しか要らない」「項目が独立している」とき。向かないのは「ほとんど全部を読む」「入れ子が深い」「要約しにくい」とき。開けると分かる印（▶・＋）を付け、見出しと印の両方を押せるようにする。 | 「Accordions on Desktop: When and How to Use」NN/g <https://www.nngroup.com/articles/accordions-on-desktop/> | ✅ |
| P-03 | 情報探索のマントラ（Overview first, zoom and filter, then details-on-demand） | まず全体を見せ、絞り込み、詳細は求められたら出す。7 つの作業の 1 つに「Relate: 項目どうしの関係を見る」がある（入れ子の木・ネットワークのデータ型も挙げている）。 | Ben Shneiderman「The Eyes Have It: A Task by Data Type Taxonomy for Information Visualizations」IEEE Visual Languages 1996 <https://www.cs.umd.edu/~ben/papers/Shneiderman1996eyes.pdf> | ✅ |
| P-04 | 大事な情報はツールチップに隠さない | 作業に要る情報は画面に出しておく。ツールチップはマウスを載せないと出ず、見つけにくく、キーボードでは出ないことがある。 | 「Tooltip Guidelines」NN/g <https://www.nngroup.com/articles/tooltip-guidelines/> | ✅ |

[↑ 目次へ](#目次)

## D ダッシュボードの設計

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| D-01 | ダッシュボードの定義（Few） | 「1 つ以上の目的を果たすのに要る、最も重要な情報を、1 画面にまとめて並べ、一目で見張れるようにした視覚的な表示」。網羅でなくてよいが、行動が要るかが分かる概観と、詳細への入口を持つ。 | Stephen Few「Common Pitfalls in Dashboard Design」Perceptual Edge 2006, p.2 <https://www.perceptualedge.com/articles/Whitepapers/Common_Pitfalls.pdf> | ✅ |
| D-02 | 見張りの 3 段（Few） | ①全体像を見る ②注意が要る項目に焦点を当てる ③行動に要る詳細へすぐ降りる。③はリンクで足りるが、①②は一目で走査できる見た目が要る。 | 同 p.3 | ✅ |
| D-03 | ダッシュボードの 13 の落とし穴（Few） | 判定に使うもの: #1 1 画面を超える ／ #2 数字に比べる文脈（目標・前回・基準）が無い ／ #3 細かすぎる・精度が高すぎる ／ #10 大事なものが強調されていない ／ #11 役に立たない装飾で画面が散らかる ／ #12 色の誤用・使いすぎ。 | 同 p.3（13 項目の一覧） | ✅（一覧の題を確かめた。各項目の本文は読んでいない） |
| D-04 | 一目で読める・量は長さと位置で（NN/g） | ダッシュボードは「最小限の操作と認知処理で」一目で読めるもの。量は長さと 2 次元の位置（棒・折れ線・散布図）で表し、面積・角度（円グラフ等）・3D・色の濃さで量を表さない。 | Page Laubheimer「Dashboards: Making Charts and Graphs Easier to Understand」NN/g <https://www.nngroup.com/articles/dashboards-preattentive/> | ✅ |

[↑ 目次へ](#目次)

## G データの見せ方

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| G-01 | データインク比（Tufte） | 図のインクのうち、データを表すインクの割合を、無理の無い範囲で最大にする。データでないインク（飾り・重複した罫線）を削る。 | Edward Tufte『The Visual Display of Quantitative Information』Graphics Press 1983（著者のページ <https://www.edwardtufte.com/book/the-visual-display-of-quantitative-information/>） | △（書籍。著者のページで「The data-ink ratio」が本の主題の 1 つであることを確かめた。定義の文言は本文を開いていない） |
| G-02 | 目的でグラフの種類を選ぶ | 時間の変化は折れ線、項目の比較は棒、2 変数の関係は散布図。円・積み上げ棒・サンキー等は、基本のグラフで伝わらないときだけ。 | 「Choosing Chart Types: Consider Context」NN/g <https://www.nngroup.com/articles/choosing-chart-types/> | ✅ |
| G-03 | データの表 | 列は重要な順に、関係する列は隣に置く。先頭の列は人が読める識別子にする。画面より大きい表は見出しの行・列を固定する。どのセルがどの行・列か常に分かるようにする。 | Page Laubheimer「Data Tables: Four Major User Tasks」NN/g <https://www.nngroup.com/articles/data-tables/> | ✅ |
| G-04 | 数値の列は右揃え | 数値の列は右揃えにして、桁の大きさを縦に比べられるようにする。 | Government of Alberta Design System「Display numbers in a table so they can be scanned easily」<https://design.alberta.ca/examples/display-numbers-in-a-table-so-they-can-be-scanned-easily/> | ✅（行政のデザインシステム。NN/g・Few の一次資料では未確認） |

[↑ 目次へ](#目次)

## K ダークモードの配色

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| K-01 | どちらの見た目でも十分なコントラスト（Apple） | 色のコントラスト比は最低 4.5:1、独自の色の組み合わせ（とくに小さい文字）は 7:1 を目指す。色は見た目に合わせて変わるものを使い、固定の値にしない。明るい・暗いの両方で読めるかを試す。 | Apple「Human Interface Guidelines: Dark Mode」<https://developer.apple.com/design/human-interface-guidelines/dark-mode> | ✅ |
| K-02 | 背景は真っ黒ではなく濃いグレー（Material） | Material の暗いテーマの背景・面は黒ではなく濃いグレー（影が見え、明るい文字の目の負担を減らす）。ガイドラインの推奨値は #121212。 | Material Components for Android「Dark theme」<https://github.com/material-components/material-components-android/blob/master/docs/theming/Dark.md> ／ Material Design 2「Dark theme」<https://m2.material.io/design/color/dark-theme.html> | △（前者で「dark grey instead of black」と理由を確かめた。#121212 は後者のページが JavaScript 描画で開けず、Gemini の回答だけ） |
| K-03 | 真っ白・鮮やかすぎる色を和らげる | 暗い背景で真っ白の文字・白い背景の画像はにじんで光る。少し暗い白にし、画像は少し暗く・鮮やかさを抑える。色の変数は色名ではなく役割で名付ける。 | Thomas Steiner「prefers-color-scheme: Hello darkness, my old friend」web.dev <https://web.dev/articles/prefers-color-scheme> ／ Apple HIG Dark Mode「Soften the color of white backgrounds」 | ✅ |
| K-04 | ダークモードは使う人が選ぶもの・全画面で一貫させる | 一般の利用者には明るい表示が既定として読みやすいが、ダークモードを選べるようにし、選んだら全画面で一貫させる。 | Raluca Budiu「Dark Mode vs. Light Mode: Which Is Better?」NN/g <https://www.nngroup.com/articles/dark-mode/> | ✅（この出典は「既定は明るい表示」を勧めている。今回は使う人＝川崎さんがダークを選んでいる、という適用の条件で使う） |

[↑ 目次へ](#目次)

## F アフォーダンス（クリックできるものが分かる）

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| F-01 | シグニファイア（Norman） | 人に要るのは「何ができるか・どこを操作するか」を示す知覚できる手がかり（シグニファイア）。設計者はそれを用意する。「Forget affordances… Provide signifiers.」 | Donald A. Norman「Signifiers, Not Affordances」ACM interactions 15(6), 2008 <https://www.alice.id.tue.nl/references/norman-2008.pdf>（DOI 10.1145/1409040.1409044） | ✅ |
| F-02 | クリックできる要素を見た目で分かるようにする | リンクは本文と色で区別し、クリックできない文字にリンクの色・下線を使わない。ボタンは角丸の矩形など押せる形を保つ。見出しをボタンのように見せない。 | Kate Moran「Beyond Blue Links: Making Clickable Elements Recognizable」NN/g <https://www.nngroup.com/articles/clickable-elements/> | ✅ |
| F-03 | 弱いシグニファイアは迷いを生む | 平たいデザインで押せる印が弱いと、目当てを探すのに約 22% 長くかかり、視線が散る。情報の多い画面では強い印を使う。 | Kate Moran「Flat UI Elements Attract Less Attention and Cause Uncertainty」NN/g <https://www.nngroup.com/articles/flat-ui-less-attention-cause-uncertainty/> | ✅ |
| F-04 | 押せるものにポインタのカーソル | CSS の `cursor: pointer` は「リンクを示すポインタ（指の形）」。既定（矢印）のままだと押せることが伝わらない。 | MDN「cursor」<https://developer.mozilla.org/en-US/docs/Web/CSS/cursor> | ✅ |
| F-05 | 開閉（ディスクロージャー）の型 | 開閉の部品はボタンで、閉じているときは右向き、開いているときは下向きの三角を付けるのが慣習。開閉の状態を `aria-expanded` で示し、Enter・Space で開閉する。 | W3C WAI-ARIA Authoring Practices「Disclosure (Show/Hide) Pattern」<https://www.w3.org/WAI/ARIA/apg/patterns/disclosure/> | ✅ |

[↑ 目次へ](#目次)

## R レスポンシブ

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| R-01 | 柔らかい配置・固定幅にしない | Flexbox・Grid で幅に合わせて伸び縮みさせる。固定幅は狭い画面で横スクロール、広い画面で余白過多になる。切り替え点は機器ではなく「中身が崩れ始める幅」で決める。 | MDN「Responsive web design」<https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design> | ✅ |
| R-02 | リフロー 1.4.10・AA | 幅 320 CSS px 相当でも 2 方向にスクロールさせずに読める（縦スクロールだけで読める）。2 方向のスクロールは読む位置を見失わせる。 | W3C「Understanding SC 1.4.10 Reflow」<https://www.w3.org/WAI/WCAG22/Understanding/reflow.html> | ✅ |
| R-03 | 1 行の長さ | 本文の 1 行は 50〜75 字（欧文）が読みやすい。WCAG 1.4.8 は 80 字以内（CJK は 40 字以内、A-08）。広い画面で文章を端まで伸ばさない。 | Baymard Institute「Readability: the Optimal Line Length」<https://baymard.com/blog/line-length-readability> | ✅ |

[↑ 目次へ](#目次)

## W 文章の書き方

| 番号 | 原則 | 要約 | 出典 | 裏取り |
|---|---|---|---|---|
| W-01 | 人は読まずに走査する | 79% の人は新しいページを走査し、1 語ずつ読むのは 16%。強調した語・中身を言う小見出し・箇条書き・1 段落 1 つの考え・結論を先に・語数を半分に。 | Jakob Nielsen「How Users Read on the Web」NN/g <https://www.nngroup.com/articles/how-users-read-on-the-web/> | ✅ |
| W-02 | 見出し・ラベル（マイクロコンテンツ） | 平易な言葉で短く、大事な語を頭に置き、前後の文脈なしで意味が通るようにする。 | 「Microcontent: A Few Small Words Have a Mega Impact on Business」NN/g <https://www.nngroup.com/articles/microcontent-how-to-write-headlines-page-titles-and-subject-lines/> | ✅ |
| W-03 | 短く・要点を先に（Microsoft） | 「Use bigger ideas, fewer words」「Get to the point fast」「Be brief」。決めるのに足りるだけの情報を出し、余分な語を削る。専門用語を避け、話すように書く。 | Microsoft Writing Style Guide「Top 10 tips for Microsoft style and voice」<https://learn.microsoft.com/en-us/style-guide/top-10-tips-style-voice> | ✅ |

[↑ 目次へ](#目次)

## 調べ方の記録

- 出典は WebFetch で開いて要約と照らした（2026-10-24）。PDF（Few・Shneiderman・Norman）はページの画像を開いて本文を読んだ。
- Gemini（`gemini-api search`）は 2 回: Material Design のダークテーマの推奨値（K-02 の #121212。Material のページが JavaScript 描画で WebFetch では開けなかった）と、表の数値の揃え方の一次資料探し（G-04。Gemini の挙げた Material・Few の出典は開けず、Alberta のデザインシステムを WebSearch で見つけて開いた）。
- 開けなかった・使わなかった: Material Design のページ（m2・m3。描画が JavaScript）、NN/g の signifier の記事（URL が 404。代わりに Norman の原典 F-01）。

[↑ 目次へ](#目次)
