# timeline-tool の結果

成果物 A（`tools/org_timeline.py`）ができた。完了条件 1〜6 をすべて満たす。作業者は worker-1（sonnet）、レビュアーは opus。レビュアーの承認 2 回、リーダーの rework 1 回、レビュアーの指摘は通算 1 回。

## 成果物

- `tools/org_timeline.py`（新規）
- `tools/tests/test_org_timeline.py`・`tools/tests/fixtures/tl/`（新規）
- `projects/p1-org-status/timeline.html`（生成）
- `projects/p2-orca-run-use/timeline.html`（生成）

呼び方は charter と PM の指定どおり: `python3 tools/org_timeline.py projects/<slug>` → `<そのディレクトリ>/timeline.html`。

## 完了条件ごとの結果（リーダーが ai-org の直下で打ち直して確かめた）

1. 上の 2 コマンドで、それぞれ `projects/p1-org-status/timeline.html`・`projects/p2-orca-run-use/timeline.html` ができた。
2. どちらの HTML も `http://` `https://` は 0 件。script タグは無い（JS 無し、本文は `<details>`）。ヘッドレス Chrome で file:// から開いて表示できた。
3. 目で見て確かめた（p2 のスクリーンショット）: user・PM・リーダー・作業者・レビュアーの帯／報告は時刻順に 1 件 1 列、種類ごとに色と記号、列の頭に時刻、宛先は受け手の帯の丸印と一覧の「→」／本文は一覧の折りたたみで読める（p1 14 件・p2 18 件）／帯の頭と表にセッションごとの時間（分）と tokens_total（セッション報告がある全員分。p1・p2 とも 4 人）。
4. import は標準ライブラリのみ（html・json・pathlib・re・sys・datetime）。YAML は自前で読む。
5. `python3 -m unittest discover -s tools/tests` → **Ran 16 tests, OK**（既存の test_org_status を含む）。
6. この報告。

## 作業者が決めたこと（リーダーが確認済み）

- events.log の行の扱い: 人の報告と未知の種類は列に出す／assign・launch・teardown は帯の頭に畳む／ack・notify_* は件数だけ／component_new・component_closed は落とす。ページ下に何を畳んだかを書いている。
- 5 分以上空いた所は間隔の列を挟む。

## 申し送り

- p1 の PM は 2 回起動しているが、セッション報告は 1 ファイルに上書きされて 2 回目の分（18.5 分）しか残っていない。HTML では「最後の起動分のみ（起動 2 回）」と出すようにした。全起動分を残すかは、orgctl teardown のファイル名（p2 以降はハッシュ付きで分かれている）の側の話。
- p3 のように動いている最中のプロジェクトにかけても落ちない（セッション報告が無い帯は「セッション報告なし」と出る）。
