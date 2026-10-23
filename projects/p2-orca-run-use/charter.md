# 目的

dev-tools の共通スキル `orca-multi-agent` の、Run の結び直し（`run-use`）と戻りの受け方を、今の Orca に合わせて直す。実装 repo に依頼すると、依頼したセッションではなく別のセッションに戻りの通知が届く混線を止めるため。

job の別のセッションが調べた事実と直す案がある: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.claude/plans/tmp/2026-10-22-orca-multi-agent-run-use-handover.md`。出発点として読む。ただし採るかどうかはチームで判断する（案どおりでなくてよい。変えたら理由を残す）。

AI 組織の 2 回目の試走でもある。前回は題材が小さく、作業者とレビュアーの往復が起きなかった。今回は判断の要る題材で、往復が回るかも見る。

# 完了条件

1. `SKILL.md` の B（依頼する）・C（一覧）・D（戻りを受ける）の `run-use`・`check` の記述が、調査ファイルの「確認した事実」と矛盾しない。古い記述は消さず、「2026-10-22 時点では〜」と併記する。
2. `run-use` してよい場面（依頼する直前・引き取るとき）と、それ以外では `run-use` しないことが書かれている。
3. 戻りを受ける入口が「結ばずに `inbox` で見る → 未処理があれば `run-show` で通知先を見る → 通知先が自分／端末が無い／別のセッションが生きている」の分岐になっていて、分岐ごとに打つコマンドがある。
4. `ticket-template.md` の Orca の表に「依頼元の端末」の行がある。
5. 自分が依頼していない戻りが届いたときの扱いが書かれている。
6. job 固有の値（Run の ID・引き取るまでの時間の具体値・観察ログ）は dev-tools に入れない。時間は「親 repo が決める」と書く。
7. 変えたのは `orca-multi-agent/SKILL.md` と `ticket-template.md` の 2 ファイルだけ。

# 範囲

- 書いてよい場所: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/claude/plugins/dev-tools/skills/orca-multi-agent/SKILL.md`・同じディレクトリの `ticket-template.md`、このプロジェクトのディレクトリの中。
- job のファイルは読むだけ。
- git の操作と `setup.sh` はしない（dev-tools のコミットは川崎さん）。
- Orca を確かめるときは、読むだけのコマンド（`orca orchestration inbox`・`run-show`・`run-list`、`orca terminal show`・`list`）だけ打ってよい。`run-use`・`task-create`・`worker-start`・`send`・`check` は打たない（通知先を奪う・実際の Run に残る）。`orca` は単独の 1 コマンドで打つ。
- チームは 1 つ。作業者は dev-tools で作業する（`--workdir /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`）。作業者は sonnet・レビュアーは opus。
- うまくいかなかったこと（連絡・決まり・手順）は、隠さずセッション報告の `unclear` と最後の報告に書く。
