# 目的

ai-org の中で使う道具 `tools/org_status.py` を作る。根っこのプロジェクトのディレクトリを渡すと、コンポーネントの木（プロジェクト・チーム・メンバー）と、メンバーごとの最後の 1 行報告（種類・時刻・何分前）と状態（未起動・動いている・終わった・片づけ済み）を一覧で出す。人が「いま組織の中で誰が何をしているか」を 1 回のコマンドで掴めるようにする。

上のプロジェクト（`projects/p1-org-status`）は AI 組織の最初の試走で、「チーム（リーダー・作業者・レビュアー）→ 報告 → 片づけ」が一周回るかを確かめるのが本当の目的。このチームはその一周そのもの。

# 完了条件

1. ai-org の repo 直下で `python3 tools/org_status.py projects/p1-org-status` を打つと、木（プロジェクト → チーム → メンバー）と、各メンバーの最後の 1 行報告（種類・時刻・何分前）と状態（未起動・動いている・終わった・片づけ済み）が出る。その実行結果をそのまま報告に貼る。
2. `--json` を付けると、1 と同じ中身が JSON で出る（`python3 -m json.tool` で読める）。
3. 標準ライブラリだけで動く（`import` に標準ライブラリ以外が無い）。
4. `tools/tests/` に unittest があり、`python3 -m unittest discover -s tools/tests` が通る。テスト用の見本（events.log・component.json・member.json）は `tools/tests/` の中に持ち、状態 4 種（未起動・動いている・終わった・片づけ済み）がそれぞれ 1 件以上テストされている。
5. 1 行報告（events.log の 1 行）・component.json・member.json の形と、状態の決め方（どの値・どの 1 行報告で 4 種を分けるか）は、dev-tools の `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/org/scripts/orgctl.py` を読んで合わせる。合わせた根拠（orgctl のどこを見たか）を報告に 1〜3 行で書く。orgctl は直さない。
6. レビュアーが完了条件 1〜5 に照らして `review_ok` を出している。

# 範囲

- 書いてよい場所: ai-org の `tools/`（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/tools`）と、このチームのディレクトリの中。
- 触らないもの: dev-tools（読むだけ）、他のコンポーネント・メンバーのディレクトリ、git の操作（add・commit・push・branch・worktree）。
- 編成: リーダー 1・作業者 1（engineer、model sonnet）・レビュアー 1（engineer、model opus）。作業者とレビュアーのモデルは変える。
- 試走なので、うまくいかなかったこと（連絡が届かない・決まりが分かりにくい・手順が足りない）は隠さず、最後の report とセッション報告の `unclear` に書く。
- 人にしかできない操作が要ったら: 手順を書いて escalate。
