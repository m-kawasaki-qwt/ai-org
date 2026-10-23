# 目的

AI 組織の最初の試走。本当の目的は「プロジェクト → チーム（リーダー・作業者・レビュアー）→ 報告 → 片づけ」が一周回るかを確かめること。題材は、ai-org の中で使う小さな道具を作ること。

題材: `tools/org_status.py`。根っこのプロジェクトのディレクトリを渡すと、コンポーネントの木（プロジェクト・チーム・メンバー）と、メンバーごとの最後の 1 行報告（種類・時刻・何分前）と状態（未起動・動いている・終わった・片づけ済み）を一覧で出す。人が「いま組織の中で誰が何をしているか」を 1 回のコマンドで掴めるようにするためのもの。

# 完了条件

1. `python3 tools/org_status.py projects/<slug>` で、木と各メンバーの状態が出る。この試走のプロジェクト（`projects/p1-org-status`）に対して実行した出力を、報告に貼る。
2. `--json` で同じ中身を JSON で出せる。
3. 標準ライブラリだけで動く。
4. `tools/tests/` に unittest があり、`python3 -m unittest discover -s tools/tests` が通る。テスト用の小さな見本（events.log・component.json・member.json）は tests の中に持つ。
5. 1 行報告・component.json・member.json の形は、dev-tools の `org/scripts/orgctl.py`（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/org/scripts/orgctl.py`）を読んで合わせる。orgctl は直さない。

# 範囲

- 書いてよい場所: ai-org の `tools/` と、このプロジェクトのディレクトリの中。
- 触らないもの: dev-tools（読むだけ）、git の操作。
- チームは 1 つ（リーダー・作業者 1・レビュアー 1）。作業者とレビュアーのモデルは変える（作業者 sonnet・レビュアー opus）。
- 試走なので、うまくいかなかったこと（連絡が届かない・決まりが分かりにくい・手順が足りない）は、隠さずセッション報告の `unclear` と最後の報告に書く。それがこの試走の一番の成果になる。
