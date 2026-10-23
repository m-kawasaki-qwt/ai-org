# ヒント: worker-1

## 方向

- 先に退避（`_archive/2026-10-24-run-use-before.md` を `cp` で作り、`diff` で一致を確かめる）。そのあとで run-use.md を書き換える。順番を逆にしない。
- run-use.md は「SKILL.md のこの節に従う」＋「job ではこの値・この運用」の表に近い形にすると薄くなる。共通の手順を言い換えて残さない（言い換えが食い違いの元）。SKILL.md の参照は節の見出し名で書く（番号だけにしない）。
- 冒頭の「🔴 dev-tools より、ここを優先する」は前提が古いので外す（消さず、退避ファイルに残っていればよい）。
- 見出しの番号・名前はなるべく変えない。参照元（manager/sources/orca/inbox.md・automation-followup/inbox.md が「2. 結ばずに見る」、manager/advance/implement.md が「1」）を直さずに済むならそれが最小の差分。変えるなら参照元も直し、外した文を退避する。
- 完了条件 3 の grep は全件を一覧にする。`tasks/`・`self-tasks/`・`**/_history/`・`.claude/skills/_archive/`・`history.md` は開かず「直さない（範囲外／履歴）」。`tasks/_master/manager.yaml` のコメントの矛盾は直さず報告に書く。
- 完了条件 4 の突き合わせ表は、事柄（いつ結ぶか・結ばずに見る・一覧の範囲・引き取り・依頼していない戻り・fenced・Run の ID・時間・印・ログ）ごとに 1 行。

## 気をつけること

- job は他のセッションも書いている。書く直前に読み直す。
- 成果物の報告（完了条件 3・4・5 の一覧と表）は、このチームのディレクトリに md で置き、review_request の本文にパスを書く。
- git は触らない。
