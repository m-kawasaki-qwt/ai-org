# 目的

p9-org-watch（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p9-org-watch/charter.md`）の完了条件 1〜5 をすべて満たす。川崎さんがプロジェクトを組織に「投げっぱなし」にして、知らせが届いたときだけ見ればよい状態にするための、見張り（watch・patrol・wait）と、閉じるときの監査を作る。起きた問題 1〜4 と記録の場所は上の charter にある。

# 完了条件

1. 全員待ちの形（全員が `wait` の中、またはターンを終えて止まっていて、誰も相手に何も出していない。例: リーダーが配下の `done` を全部受けたのに PM へ `report` を出していない）を、patrol が止まりと判定し、`gchat-notify`（slug `ai-org`）と `log/user-inbox.yaml` に知らせる。本文から、誰が誰を待っていて、何が出ていないかが分かる。同じ詰まりで知らせを繰り返し出さない（出す間隔・まとめ方が決まっている）。仮のプロジェクト（scratchpad / `$TMPDIR`）で確かめた結果が報告にある。試しの送信は本文の頭に「［試し］」を付け、要る分だけ。
2. `watch` が、待っているだけのメンバーと、止まっている・ループしているメンバーを出し分ける。p8 の記録（`events.log` 16:25〜16:31 など）から scratchpad に作り直した 16:30 ごろの状態で、PM が「ループ?」と出ない。そのうえで、本当に止まった・ループしたメンバー（作った例）は今までどおり「止まっている?」「ループ?」と出る。確かめた結果が報告にある。
3. 開いている全プロジェクトを 1 回見て終わる形（例: `patrol --projects <dir> --once`）が CLI にある。Orca の automation の定義（コマンド・間隔・どの repo で動かすか）と登録までの手順が、org-project-new か README にある。org-project-new の 5（根っこのセッションが裏で patrol を回す手順）が、常駐に切り替わる前と後の扱いが分かる形になっている。automation の登録はしない。
4. 閉じる手順（org-project-new の 7）に、監査役が動く段がある（誰が・いつ assign し、何を渡し、出力を待ってから teardown する）。監査役の立場（`org/positions/auditor/`）の出力は「起きたこと（問題・課題）と参照元」で、直し方を含まない。出力の置き場が決まっていて、`orgctl export` の snapshot に載る。`export --check` が通り、p3 の前の形の監査も読めたまま。p9 を閉じるときに worktree の orgctl（`/Users/maka343noshi/orca/workspaces/dev-tools/org-watch/org/scripts/orgctl.py`）で新しい監査役を assign して動かせることを確かめた結果と、PM がそのとき打つコマンドが報告にある。
5. `org/README.md` と、プラン（`docs/todo/ai-org-plan.md`）の決まったこと 22（とその補足）が新しい形に合っている。決まったことを改める場合は、元の文を消さずに併記している。
6. dev-tools の本体と ai-org の `projects/` は書き換えていない。

# つなぎ

- 受けるもの: PM（p9-org-watch/pm）からこの charter。
- 渡すもの: PM へ `report`（完了条件ごとに、確かめた結果・変えたファイル・打ったコマンド）。リーダーは配下全員の `done` を読んだら、その場で PM へ `report` を出す（wait に戻らない。これが問題 1 の形そのもの）。
- うまくいかなかったこと（パックの過不足・連絡・決まり）は報告に隠さず書く。

# 範囲

- 書いてよい場所: dev-tools の worktree `/Users/maka343noshi/orca/workspaces/dev-tools/org-watch` の中だけ（`org/`・`docs/todo/ai-org-plan.md`・`claude/plugins/dev-tools/skills/org-project-new/`・`claude/plugins/dev-tools/bin/`）。試しは scratchpad / `$TMPDIR` の仮のプロジェクト。
- 触らないもの: dev-tools の本体（読むだけ）、ai-org の `projects/`（読むだけ）、Orca の automation の登録・Orca の設定、git の操作。
- 人にしかできない操作が要ったら: 手順を書いて escalate。
