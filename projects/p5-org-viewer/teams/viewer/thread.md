
## 作業者 第1版
手書き snapshot.json で 5 画面と README を作った。build 通過・スクリーンショット 5 枚。実物（p1〜p4）での表示は export 待ち。詳細は msgs/worker-viewer-v1.md。

## 作業者（export） 第1版

- orgctl.py に `export`（`--projects` `--out` `--check`）を追加。既存の関数は変えず、`NOISE_KINDS`・`read_events`・`member_state` などをそのまま呼ぶ。標準ライブラリだけ（追加した import は textwrap）。
- JSON Schema `org/schema/snapshot.schema.json`（schema.md v1 から）。`--check` で確かめる。壊した写しでは 4 件とも検出した。
- 本番の projects/ で出力: 5 プロジェクト・受け箱 8・未読 1・監査の改訂案 5・unclear 56・セッション報告 22。未読・トークン・unclear の件数は記録を直接数えた値と一致。
- 読むだけ: export の前後で、閉じた p1〜p4 の中に新しくなったファイルが無いことを確かめた。
- 解釈して決めたこと 5 点は review_request の本文に書いた（トークンは入れ替え前の分も合計・done も受け箱に入れる・user-inbox の summary の # を落とす・立場ごとの remakes の数え方・--check の範囲）。

## レビュアー 第1回（worker-viewer）
review_ng（3 件）。実物の snapshot.json で build・5 画面は通る。直す点: (1) 監査・unclear 画面の 56 件が全部開いている→件数を先に・プロジェクトごとに畳む（完了条件 2）、(2) 受け箱に本文のない done が混ざる→畳むか表示を変える、(3) 一覧の「いま／最後」に絶対パスが折り返す→1 行に切る。詳細は msgs。

## レビュアー 第2回（worker-export）
review_ok（export・完了条件 1）。実物に向けて export・`--check` 通過、既存コードは変更なし（+409/-0）、NOISE_KINDS は流用、記録に書き込みなし、p5 でも落ちないことを確かめた。ビューアは第 1 回で review_ng 中。

## 作業者 第2版
review_ng 3 点（unclear を畳む・done 通知を畳む・一覧の一言を 1 行に）を採用して直した。詳細は msgs/worker-viewer-v2.md。

## レビュアー 第3回（worker-viewer 第2版）
review_ok。第 1 回の 3 点（unclear の畳み・受け箱の done の畳み・一覧の 1 行化）を実物の snapshot.json の build とスクリーンショットで確かめた。申し送り: 畳んだ中に未読が隠れる点、`npm install` のキャッシュ権限。

## 作業者 第3版
リーダーの rework 3 点（未読を見える所へ・「いま／最後」を結果の一言に・時系列をチームごとに畳む）を採用。export 打ち直し・撮り直し済み。msgs/worker-viewer-v3.md。

## レビュアー 第4回（worker-viewer 第3版）
review_ok。リーダーの rework（未読の見える化・「いま／最後」を最後の message／report に・時系列をチームごとに畳む）の 3 点を、スクリーンショットと build で確かめた。指摘は通算 1 回のまま。
