# 目的

初めて AI 組織（ai-org）を使う人（川崎さん本人の将来も含む）が、README だけを読んでプロジェクトを立ち上げ、状況を見て、閉じられるようにする。上のプロジェクト（p3-org-visibility）の成果物 B。ai-org の `policy.md` の「川崎さんの番は少なく」「記録が残り、調べられる」を、手引きの側から支える。

作るもの: ai-org の `README.md` を、運用の手引きとして書き直す（いまは 8 バイトの空に近いもの）。

# 完了条件

1. README に次の節がある:
   - プロジェクトの立ち上げ方（入口のスキル `org-project-new`。スキルの中身は dev-tools の `claude/plugins/dev-tools/skills/org-project-new/` を読んで、何をするスキルかと、その後に起きること）
   - いまの状況の見方（`orgctl watch`・`tools/org_status.py`・`tools/org_timeline.py` が作る `projects/<slug>/timeline.html`）
   - 記録の在り処（`log/events.log`・`log/msgs/`・`reports/sessions/`・チームの `thread.md`・`result.md`）
   - コミットの決まり（ai-org の `CLAUDE.md` の要約と、そこへのリンク）
   - 川崎さん（人）がやること（webhook を置く・dev-tools の `setup.sh` を打つ など。dev-tools の `org/` と `orgctl.py` の `patrol` を読んで、実際に要るものだけ）
2. 初めて読む人が、上から順にたどればプロジェクトを立ち上げられる順番になっている。
3. README の中のコマンドは 1 コマンド 1 行（`\` の行継続・heredoc なし）。orgctl のサブコマンド・引数は、`python3 <dev-tools>/org/scripts/orgctl.py <サブコマンド> --help` の出力と突き合わせて実在するものだけ。`tools/org_status.py` は実物の引数と合っている。
4. `tools/org_timeline.py` は別のチームが並行して作っている。README では「プロジェクトのディレクトリを渡すと `<そのディレクトリ>/timeline.html` を書く」（`python3 tools/org_timeline.py projects/<slug>`）として書いてよい。この形を前提とすることを報告に書く。
5. 報告（leader → PM の report）に、突き合わせた `--help` のサブコマンドの一覧と、README の節の一覧を書く。

# 範囲

- 書いてよい場所: ai-org の `README.md`・このチームのディレクトリの中。
- 触らないもの: dev-tools（読むだけ）、ai-org の `tools/`（別のチームが書く）・`CLAUDE.md`・`policy.md`、git の操作。
- 作業者・レビュアーのモデルはリーダーが決める（変えてよい）。
- 人にしかできない操作が要ったら: 手順を書いて escalate。
