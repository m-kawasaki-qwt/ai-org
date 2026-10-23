# 目的

川崎さんが、AI 組織のプロジェクトで何が起きたかを、ファイルを開いて回らずに 1 枚で掴めるようにする。上のプロジェクト（p3-org-visibility）の成果物 A。ai-org の `policy.md` の「記録が残り、調べられる」を、見る側から支える。

作るもの: `tools/org_timeline.py`。根っこのプロジェクトのディレクトリを渡すと、1 枚の静的な HTML（`<そのディレクトリ>/timeline.html`）を書く。入力は、そのプロジェクトの `log/events.log`（1 行報告）・`log/msgs/*.md`（本文）・`reports/sessions/*.yaml`（セッション報告）・`component.json`（子のチームも含む）。

# 完了条件

1. `python3 tools/org_timeline.py projects/p1-org-status` と `python3 tools/org_timeline.py projects/p2-orca-run-use`（ai-org の直下で打つ）で、それぞれ `projects/p1-org-status/timeline.html`・`projects/p2-orca-run-use/timeline.html` ができる。
2. HTML は静的で、ブラウザでそのまま開ける。外部の CDN・JS ライブラリ・フォント・画像を読まない（`http://` `https://` への参照が無い）。
3. HTML に、次が見える:
   - メンバーごとの横の帯（user・PM・リーダー・作業者・レビュアーなど、events.log に出てくる送り手・宛先の全員）
   - 1 行報告を時刻順に、送り手の帯に置き、報告の種類（start・review_request・review_ng・review_ok・rework・report・wrap_up・done など）と時刻と宛先が分かる。種類ごとに見分けがつく（色・記号など）
   - 本文（`msg=log/msgs/<hash>.md`）がある報告は、その中身を HTML の中で読める（折りたたみ・ホバーなど方式は任せる）
   - セッションごとの時間（span_min など）とトークン（tokens_total など）。セッション報告がある全メンバー分
4. 標準ライブラリだけで動く（PyYAML も使わない。セッション報告の YAML は、必要な項目を自前で読む）。
5. `tools/tests/` に org_timeline のテストがあり、ai-org の直下で `python3 -m unittest discover -s tools/tests` が既存のテスト（test_org_status.py）と一緒に全部通る。テストの入力は `tools/tests/fixtures/` に置く小さな作り物でよい。
6. 報告（leader → PM の report）に、生成した 2 つの HTML のパスと、テストの実行結果（通った件数）を書く。

# 範囲

- 書いてよい場所: ai-org の `tools/org_timeline.py`・`tools/tests/`（既存のテストは壊さない）・`projects/p1-org-status/timeline.html`・`projects/p2-orca-run-use/timeline.html`・このチームのディレクトリの中。
- 触らないもの: dev-tools（読むだけ）、ai-org の `README.md`（別のチームが書く）・`CLAUDE.md`・`policy.md`・`tools/org_status.py`、p1・p2 の log と reports（読むだけ）、git の操作。
- 作業者・レビュアーのモデルはリーダーが決める（変えてよい）。
- 人にしかできない操作が要ったら: 手順を書いて escalate。
