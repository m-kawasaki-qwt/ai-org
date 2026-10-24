# ヒント（worker-audit）

## こう作ればいけると思う

- 監査役の出力は 1 枚の md（例: 閉じるプロジェクトの `log/audit.md` か `reports/audit.md`）に決め打ちし、各項目を「起きたこと／参照元（ファイルと行・hash）」の 2 つだけにする。直し方・改訂案の欄を持たない。position.md にもそう書く（「直し方は書かない。着手の直前に考える」）。
- export は、新しい置き場を読む読み手を `_ProjectReader` に足し、前の形（p3 の「改訂案」の節を msgs から読むもの）は消さずに残す。snapshot には新しいキー（例: `audit_findings`）を足し、スキーマも足す。`export --check` が通ること、p3 の前の形が今までどおり出ることを確かめる。
- org-project-new の 7 には、閉じる直前に PM（入れ子なら閉じる側）が監査役を assign → launch → `start`（本文に閉じるプロジェクトの根っこと、読むもの: events.log・reports/sessions の unclear・thread.md・policy.md）→ 監査役の `report` を待つ → 監査役を teardown → その後でプロジェクトを teardown、の順で書く。

## 気をつけてほしい点

- p9 自身を閉じるとき、本体の orgctl はまだ古い position.md を入れる。worktree の orgctl で assign すれば新しい立場が入るかを実際に確かめ（仮のプロジェクトで assign まで打って、メンバーのディレクトリの CLAUDE.md に新しい立場が入るのを見る）、PM がそのとき打つコマンドを 1 コマンド 1 行で報告に並べる。
- 受け持ち（`_ProjectReader`・`build_snapshot`・`cmd_export`・`teardown_*`・スキーマ）以外の関数を触らない。`main()` に引数が要るなら、自分で足さずリーダーへ `escalate` で言う。
- README・プランの通しの揃え（完了条件 5）は、リーダーから `start` が来てから。プランの決まったこと 22 は元の文を消さずに併記。
