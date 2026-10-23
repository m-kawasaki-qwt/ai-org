# worker-1 へのヒント

## 方向

- 読み手は「ai-org を初めて触る人」。上から順にやれば、立ち上げ → 状況を見る → 閉じる、までたどれる並びにする。おすすめの並び: 何の repo か（3 行）→ はじめに人がやること（準備）→ プロジェクトの立ち上げ方 → いまの状況の見方 → 記録の在り処 → 閉じ方とコミットの決まり。「川崎さん（人）がやること」は準備の節にまとめ、途中で人の番が来る箇所（閉じたあとのコミットなど）はその場で一言触れる。
- 書く前に実物を読む。推測で書かない。
  - 立ち上げ: dev-tools の `claude/plugins/dev-tools/skills/org-project-new/`（何をするスキルか、そのあと PM が起きて何が起きるか）。
  - 人がやること: dev-tools の `org/`（README・common・scripts）と `orgctl.py` の `patrol`（webhook・setup.sh など、実際に要るものだけ。要らないものを足さない）。
  - コマンド: `python3 <dev-tools>/org/scripts/orgctl.py --help` と、README に載せるサブコマンドごとの `--help`。`tools/org_status.py` は実物の引数（`--help` か中身）。
  - 記録: `projects/p1-org-status/`・`projects/p2-orca-run-use/` に実物がある。ファイルの置き場は実物のツリーと合わせる。
  - コミットの決まり: ai-org の `CLAUDE.md` を要約し、リンクを張る（中身を丸写ししない）。
- `tools/org_timeline.py` はまだ無いかもしれない。charter の完了条件 4 の形（`python3 tools/org_timeline.py projects/<slug>` で `projects/<slug>/timeline.html` を書く）で書く。

## 気をつけてほしい点

- コマンドは 1 コマンド 1 行。`\` の行継続・heredoc を使わない。dev-tools のパスは `<dev-tools>` のような置き換えを 1 回だけ説明して使うか、`$DEV_TOOLS_REPO_PATH` を使う（どちらかに揃える）。
- 実在しないサブコマンド・引数を書かない。突き合わせた `--help` のサブコマンド一覧を、review_request の本文に付ける（リーダーが PM への報告に使う）。
- 書いてよいのは ai-org の `README.md` だけ。`tools/`・`CLAUDE.md`・`policy.md`・dev-tools は読むだけ。git は触らない。
- 長くしすぎない。手引きとして、迷う所だけ詳しく。
