
## 作業者 第1版

- run-use.md を SKILL.md の節（B「run-use の使いどころ」・C・D の入口と分岐 1〜3・D「自分が依頼していない戻りが届いたとき」・D の consumer_fenced）への参照＋job の値の表に置き換えた。見出し 1〜4 の番号・名前は据え置き、参照元は直していない。
- 退避: _archive/2026-10-24-run-use-before.md（Write。diff・cmp とも差分なし）。run-use.md の 1 行目がそれを指す。
- 外したもの: 冒頭の経緯段落、「dev-tools より優先する」、2 の手順の言い換え、consumer_fenced の段落、3 の言い換えと文例。
- 報告（完了条件 3・4・5）: teams/run-use-thin/worker-1-report.md

## レビュアー 第1回

承認（指摘なし）。確かめたこと:
- 条件2: HEAD の run-use.md を取り出して退避ファイルと diff・cmp → 差分なし。run-use.md 1 行目が退避を指す。
- 条件1: 残りは Run の ID・`依頼元の端末` の印・`--limit 100`・見る範囲・2 時間・automation の即引き取り・〔誤配〕の運用・ログのみ。共通手順は SKILL.md の B「`run-use` の使いどころ」・C・D の入口と分岐 1〜3・D「自分が依頼していない戻りが届いたとき」・`consumer_fenced` の節名で指し、いずれも実在。「dev-tools より優先」は外れている。
- 条件3: 見出し 1〜4 を据え置いたため、inbox.md 38・automation-followup/inbox.md 35・implement.md 58 の節番号参照は合う。inbox.md の「取り方」3〜5 も実在。
- 条件4: 旧版の食い違い（新しい端末は最初に結ぶ・read が 0 で未処理・null の通知先・誤配の 1 行の文例）は解消。印の書式は ticket-template.md の行と矛盾しない。
申し送り: tasks/ 等は読み取り拒否で grep が届かず、manager.yaml 15 行目の古いコメントは未確認・範囲外（PM へ）。
