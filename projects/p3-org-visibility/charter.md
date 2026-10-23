# 目的

川崎さんが、AI 組織の中で何が起きたか・起きているかを、ファイルを開いて回らずに一目で掴めるようにする。方針（ai-org の `policy.md`）の「記録が残り、調べられる」「川崎さんの番は少なく」を、見る側から支える。

成果物は 2 つ。

- A. `tools/org_timeline.py`: 根っこのプロジェクトのディレクトリを渡すと、1 枚の静的な HTML（`projects/<slug>/timeline.html`）を作る。メンバーごとの横の帯に 1 行報告を時刻順に並べ、誰から誰へ何が渡ったか（start・review_request・review_ng・review_ok・rework・report・done など）と、セッション報告の時間・トークンが見える。
- B. ai-org の `README.md` を、運用の手引きとして書き直す: プロジェクトの立ち上げ方（入口のスキル `org-project-new`）、いまの状況の見方（`orgctl watch`・`tools/org_status.py`・A の timeline）、記録の在り処（`log/`・`reports/`）、コミットの決まり（`CLAUDE.md`）、川崎さんがやること（webhook を置く・`setup.sh`）。

AI 組織の 3 回目の試走でもある。今回はチームを 2 つ並べ、最後に監査役を動かす。

# 完了条件

1. `python3 tools/org_timeline.py projects/p1-org-status` と `projects/p2-orca-run-use` で、それぞれ `timeline.html` ができ、ブラウザで開ける静的な HTML（外部の CDN・JS ライブラリを読まない）。メンバーごとの帯・報告の種類・時刻・宛先・セッションごとの時間とトークンが見える。生成した 2 つの HTML のパスを報告に書く。
2. 標準ライブラリだけ。`tools/tests/` に A のテストがあり、`python3 -m unittest discover -s tools/tests` が既存のテストと一緒に通る。
3. B の `README.md` は、初めて読む人が手順どおりにプロジェクトを立ち上げられる。中のコマンドは 1 行ずつで、実在するもの（dev-tools の `org/scripts/orgctl.py` の `--help` と突き合わせる）。
4. A と B はそれぞれ別のチームが作る。
5. 2 つのチームを閉じたあと、監査役をアサインして起こし、このプロジェクト（と、記録が残っている p1・p2）の動き方を `policy.md` に照らさせる。監査役の改訂案（dev-tools の `org/` のどのファイルをどう変えるか。5 件まで）を、最後の報告に入れる。改訂案は雛形に反映しない（決めるのは川崎さん）。

# 範囲

- 書いてよい場所: ai-org の `tools/`・`README.md`・このプロジェクトのディレクトリの中・`projects/p1-org-status/timeline.html`・`projects/p2-orca-run-use/timeline.html`。
- 触らないもの: dev-tools（読むだけ）、ai-org の `CLAUDE.md`・`policy.md`、git の操作。
- 作業者・レビュアーのモデルは、各チームのリーダーが決める（作業者とレビュアーで変えてよい）。
- うまくいかなかったこと（連絡・決まり・手順）は、隠さずセッション報告の `unclear` と最後の報告に書く。
