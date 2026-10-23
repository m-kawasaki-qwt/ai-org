# 目的

dev-tools の共通スキル `orca-multi-agent` の、Run の結び直し（`run-use`）と戻りの受け方を、今の Orca に合わせて直す。実装 repo に依頼すると、依頼したセッションではなく別のセッションに戻りの通知が届く混線を止めるため。上のプロジェクト（`projects/p2-orca-run-use`）の目的そのもので、このチームが全部を受け持つ。

出発点: job の別のセッションが調べた事実と直す案 `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.claude/plans/tmp/2026-10-22-orca-multi-agent-run-use-handover.md`。採るかどうかはチームで判断する（案どおりでなくてよい。変えたら、どこをなぜ変えたかを報告に書く）。

AI 組織の 2 回目の試走でもある。今回は判断の要る題材で、作業者とレビュアーの往復（`review_ng` → 直し → `review_ok`）が回るかを見る。指摘が無いのに往復を作る必要はないが、レビュアーは完了条件の各番号に照らして、根拠（調査ファイル・SKILL.md の該当箇所）付きで判定する。

# 完了条件

対象のファイル: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/claude/plugins/dev-tools/skills/orca-multi-agent/SKILL.md`（以下 SKILL.md）と、同じディレクトリの `ticket-template.md`。

1. SKILL.md の B（依頼する）・C（一覧）・D（戻りを受ける）にある `run-use`・`check` の記述が、調査ファイルの「確認した事実」と矛盾しない。古い記述は消さず、「2026-10-22 時点では〜」と併記する。報告に、B・C・D で直した箇所と、それぞれが調査ファイルのどの事実に対応するかを一覧で書く。
2. `run-use` してよい場面（依頼する直前・引き取るとき）と、それ以外では `run-use` しないことが SKILL.md に書かれている。
3. 戻りを受ける入口が「結ばずに `inbox` で見る → 未処理があれば `run-show` で通知先を見る → 通知先が自分／端末が無い／別のセッションが生きている」の分岐になっていて、3 つの分岐ごとに打つコマンドが書かれている。
4. `ticket-template.md` の Orca の表に「依頼元の端末」の行がある。
5. 自分が依頼していない戻りが届いたときの扱いが SKILL.md に書かれている。
6. job 固有の値（Run の ID・引き取るまでの時間の具体値・観察ログ）が dev-tools に入っていない。時間は「親 repo が決める」と書かれている。
7. 変えたのは SKILL.md と `ticket-template.md` の 2 ファイルだけ（dev-tools の `git status` / `git diff --stat` を報告に貼る）。SKILL.md の中のコマンドは 1 行で書かれ、`orca` は単独の 1 コマンドの形になっている。
8. レビュアーが 1〜7 に照らして `review_ok` を出している。

# 範囲

- 書いてよい場所: 上の 2 ファイルと、このチームのディレクトリの中。
- 触らないもの: job（読むだけ）、`worker-instructions.md` を含む dev-tools の他のファイル、他のコンポーネント・メンバーのディレクトリ。git の操作（add・commit・push・branch・worktree）と `setup.sh` はしない（dev-tools のコミットは川崎さん）。
- Orca を確かめるときは、読むだけのコマンド（`orca orchestration inbox`・`run-show`・`run-list`、`orca terminal show`・`list`）だけ打ってよい。`run-use`・`task-create`・`worker-start`・`send`・`check` は打たない（通知先を奪う・実際の Run に残る）。`orca` は単独の 1 コマンドで打つ。
- 編成: リーダー 1（engineer、opus）・作業者 1（engineer、sonnet、`--workdir /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`）・レビュアー 1（engineer、opus）。
- レビュアーは作業者と同時に起こす（前回、最初の `review_request` の後に起こす形にしたら、作業者が知らせる相手のタブが無く、レビューが約 10 分止まった）。
- 調査ファイルの案で、目的に照らして判断が分かれる点（範囲が変わる・川崎さんの好みで決まる）が出たら、推奨付きの 2〜5 択で PM へ `escalate`。
- 試走なので、うまくいかなかったこと（連絡が届かない・決まりが分かりにくい・手順が足りない）は隠さず、最後の report とセッション報告の `unclear` に書く。
- 人にしかできない操作が要ったら: 手順を書いて escalate。
