# 監査: p9-org-watch

範囲: 17:27〜17:54 の 1 行報告（`log/events.log`）・本文（`log/msgs/`）・セッション報告 6 本・charter（根っこ・チーム watch）・パック・ヒント・`orgctl notify-stats`。深く読んだのは review_ng 2 件・作り直しの start 1 件・各報告の unclear。

1. **チームの完了条件 4 で、閉じる側を PM と書いていた（p9 は根っこなので閉じるのは user）**
   - 起きたこと: PM がチームの charter の完了条件 4 に「PM がそのとき打つコマンド」を足して渡した。作業者はその文のとおり「閉じる側＝PM」の並びを出し、リーダーが後から start で「閉じるのは根っこのセッション（user）」と直させた。PM 自身も、自分の立場の「閉じる手順で監査役が動く」と、誰が打つかの線が charter から読み取りにくかったと申告している。
   - 参照元: `teams/watch/charter.md:10`・`544cc1`（`log/events.log:16`）・`0c2fd0`（`log/events.log:24`）・`log/msgs/6bc6a5.md:10`・`a92788`（`log/events.log:80`、`log/msgs/a92788.md:2`）・`reports/sessions/p9-org-watch__pm-f743150d.yaml:70`

2. **プランの決まったこと 22 の書き手が、パックとレビューで食い違った**
   - 起きたこと: パックは、22 の補足を「worker-watch の承認のあと、リーダーの start を受けて worker-audit が書く」と分けていた。レビュアーは worker-watch の review_ng で「22 の補足に差分が無い」を指摘に入れ（監査の分をどちらが書くかは作業者とリーダーで決めて、と添えた）、worker-audit の review_ng でも申し送りとして同じ点を出した。結果として 22 には 2 人とも書いた。リーダー・レビュアー・worker-audit の 3 人が、受け持ちが明示されておらず review_ng で初めて決まったと申告している（パックには書いてあった）。
   - 参照元: `packs/watch/worker-audit.md:34`・`packs/watch/worker-watch.md:33`・`packs/watch/leader.md:32`・`cc2161`（`log/events.log:71`、`log/msgs/cc2161.md:10-11`）・`f08c2f`（`log/events.log:59`、`log/msgs/f08c2f.md:12`）・`reports/sessions/p9-org-watch__teams__watch__leader-36cfe0d2.yaml:66`・`reports/sessions/p9-org-watch__teams__watch__reviewer-512bbb7a.yaml:59`

3. **同じファイルを 2 人で同時に直し、パックの編集の決まりと受け持ちの線から外れた**
   - 起きたこと: orgctl.py を作業者 2 人が関数で分けて同時に直した。worker-watch は Edit が「読んだあとに変わった」で止まり続け、1 度 Python でファイルを読み書きして置き換えた（パックは「Edit で差分だけ、ファイル全体の書き直しをかけない」）。また、試しのために受け持ちの関数の外（`projects_dir`）に手を入れた（リーダーの start は「受け持ちの関数だけ」）。どちらも本人の unclear に書かれ、escalate は出ていない。
   - 参照元: `packs/watch/worker-watch.md:32`・`34de0a`（`log/msgs/34de0a.md:2`）・`reports/sessions/p9-org-watch__teams__watch__worker-watch-f06de01a.yaml:64`・`reports/sessions/p9-org-watch__teams__watch__worker-watch-f06de01a.yaml:70-71`

4. **PM が検収で、本物の ai-org/projects に書き込む patrol --dry を打った**
   - 起きたこと: `patrol --dry` は受け箱（`log/user-inbox.yaml`）と `.patrol.json` に書く作り。リーダーはそれを理由に本物の projects/ には打たなかったが、PM は検収で `patrol --projects <ai-org>/projects --once --dry` を打った。チームの範囲では ai-org の `projects/` は「読むだけ」。PM は、検収で本物のプロジェクトに打ってよいかの決まりが無いと申告している。
   - 参照元: `teams/watch/charter.md:23`・`e4536d`（`log/events.log:113`、`log/msgs/e4536d.md:2`）・`reports/sessions/p9-org-watch__teams__watch__leader-36cfe0d2.yaml:62`・`reports/sessions/p9-org-watch__pm-f743150d.yaml:71`
