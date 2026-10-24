<!-- p10-viewer-ideas/coordinator → p10-viewer-ideas/pm report 2026-10-24T19:18:42+09:00 -->
# 編成案: p10-viewer-ideas（第 1 版）

## 1. 切り方・つなぎ方・順番

**チーム 1 つ `viewer-ideas`（子プロジェクトは要らない）。PM の案に同意。** 調べてレポート 1 本を書く作業で、成果物が 1 つに集まるため、チームを割るとつなぎが増えるだけ。チームの外とのつなぎは無し（p11 とは待ち合わせない。下の 3）。

PM の案から 2 点変える:

- **report.md を書くのはリーダーではなく作業者 A。** リーダーの規範は「実装には触れない」。2 人の出力をリーダーがまとめると、リーダーが成果物を作ることになり、レビュアーの指摘を受けて直す人もいなくなる。A がレポートの書き手で、B のリサーチを取り込む。
- **B の出力はレビューを通さず、リーダー経由で A へ渡す。** レビュアーは最後の report.md だけを見る（出典の裏取りは report.md からの抜き取りで足りる）。

チーム内のつなぎ:

| 誰 | 受ける | 渡す |
|---|---|---|
| worker-records（A） | リーダーの start、のちに research.md のパス | `P/report.md`・`T/screenshots/`・（長ければ）`T/evidence.md`・`T/scripts/` → レビュアーへ review_request |
| worker-research（B） | リーダーの start | `T/research.md` → リーダーへ report |
| リーダー | B の report | 出典を 3 件ほど開いて確かめ、research.md のパスを A へ start で渡す |
| reviewer-kawasaki | A の review_request | review_ok をリーダーへ |

順番: A と B は並行で始める。A は research.md を待たずに記録と画面から進め、届いたら取り込む → レビュー → リーダーが kawasaki の目線で読み直す → PM へ report。

（`P` = `projects/p10-viewer-ideas`、`T` = `P/teams/viewer-ideas`）

## 2. 編成

画面なし（成果物は Markdown のレポートと、いまの画面を撮った画像。画面を組み立てない）。ただし charter の完了条件 6 に従い、レビュアーに `kawasaki` のペルソナを付ける。

| 立場 | 名前 | 職種 | モデル | 人数 | 理由 |
|---|---|---|---|---|---|
| リーダー | leader | - | opus | 1 | 最後に kawasaki の目線で report.md を読んで rework を出せるかが要。 |
| 作業者 | worker-records | **ui-designer** | opus | 1 | 見せ方の案の質が UI の原則（U-03 概観と詳細・U-05 図の選び方・U-06 比べる相手）に照らせるかで決まる。p5 は記録の形から画面を作って失敗した。読む量（p1〜p9 の記録、約 1,100 行の 1 行報告）も多いので opus。 |
| 作業者 | worker-research | - | sonnet | 1 | 出典付きで集めて形に揃える作業。並行させると A の時間が空かない。 |
| レビュアー | reviewer-kawasaki | - | opus | 1 | `--persona kawasaki`。根拠の抜き取り（10 件以上）と、レポートが 1 分で掴めるかの判定。 |

- UI デザイナーについて: **入れる（作業者 A の職種）。** 画面は作らないので `design.md` は書かせない（パックに明記した）。原則とチェックリストの B は、見せ方の案を書く基準として使わせる。
- ペルソナ: `kawasaki` だけ。`end-user`・`sales` は付けない（ビューアの使い手は川崎さん 1 人で、売るものでもない）。
- 作業者を 2 人に分ける理由: 記録を読む作業とリサーチは材料が重ならず、並行させると早く終わる。リサーチの量が読めない点は、B に「8〜15 件・網羅しない」と上限を付けて抑えた。1 人にすると A が記録とリサーチを両方抱え、出典の裏取りが薄くなる見込み（推測）。

## 3. この編成で実現できる理由と、崩れる前提

実現できる理由:
- 材料が全部ローカルにあり、読める場所に収まっている（ai-org の記録・viewer のコード・dev-tools の雛形・job の `company/system/`）。台帳の範囲で足りる。
- 時間・トークンはセッション報告の `machine`（`span_min`・`tokens_total`）に、待ちの形は p9 の charter に経緯がある。叩き台 3・8 の根拠はすでにある。

崩れる前提（外れたら切り直す）:
- 4390 番のビューアが動いていて撮れる（止まっていたら、4391〜4399 で `viewer/` を立てて撮る。dist を作るために `viewer/` へ書くなら範囲の外なので、PM へ上げる）。
- `gemini-api` で Web 検索ができる（できなければ WebSearch に替える。出典の質は落ちうる）。
- p11 の一覧を待たずに叩き台 7 を判定できる（「どう見せるか」までに留めるため、中身の一覧は要らない）。
- report.md を `P` の直下に作業者が直接書いてよい（charter の書いてよい場所の中なので大丈夫と見ている）。

## 4. charter に入れてほしいこと（チーム `viewer-ideas`）

完了条件の要点（親の完了条件 1〜6 をそのまま下ろす形でよい。足してほしいもの）:
- 成果物の置き場: `P/report.md`（画像は `T/screenshots/`、report.md から相対パスで表示される）。根拠の一覧が長ければ `T/evidence.md`、数えたスクリプトは `T/scripts/`、リサーチは `T/research.md`。
- 案の数字（回数・時間・トークン）はスクリプトで出し、スクリプトを残している。
- レビュアーが根拠を 10 件以上・出典を 3 件以上、抜き取りで開いて確かめている。
- 実装していない（`viewer/`・dev-tools・job に差分が無い）。監査の指摘・unclear の一覧そのものは作っていない（p11 の範囲）。

つなぎ:
- worker-research は `T/research.md` を書いてリーダーへ report。リーダーが worker-records へパスを渡す。作業者どうしは直接やりとりしない。
- チームの外とのつなぎは無し（p11 を待たない。p11 の `issues.md` が先にできていれば参考にしてよい）。

## 5. パック

- `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p10-viewer-ideas/packs/viewer-ideas/leader.md`
- `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p10-viewer-ideas/packs/viewer-ideas/worker-records.md`
- `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p10-viewer-ideas/packs/viewer-ideas/worker-research.md`
- `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p10-viewer-ideas/packs/viewer-ideas/reviewer-kawasaki.md`

パックの中では charter を `P/teams/viewer-ideas/charter.md` で指している。名前を変えるなら言ってほしい（こちらで直す）。
