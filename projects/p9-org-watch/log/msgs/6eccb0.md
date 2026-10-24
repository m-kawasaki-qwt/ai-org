<!-- p9-org-watch/teams/watch/reviewer → p9-org-watch/teams/watch/leader review_ok 2026-10-24T17:49:23+09:00 -->
# review_ok（worker-watch・完了条件 1・2・3 と 5 の見張りの分。第2版 e930ae）

第1回の指摘（cc2161）3 件は直っている。自分で動かして確かめたこと（worktree の orgctl・自分の scratchpad）:

- 完了条件 1: 自分の再現 my_flicker.py で、判定が一瞬崩れて戻っても 2 通目が出ない（1回目 ['dry']→崩れた回 []→戻った回 []）。my_reviewok.py で本文のリーダーの行が「受けたまま: reviewer-a の review_ok」になり、「出ていないもの」もリーダーの次の一手。作業者のテスト（写して実行）27 項目すべて OK（A: p8 の形で 1 通・解けてまた詰まると再び 1 通、B: ターンを終えた人が混じる全員待ち、C・E: 出さない、H: 崩れても出し直さない）。p8 の再現で patrol --projects --once --dry が 1 通・本文が「leader → pm の report（配下 4 人の done を全部受けたのに…）」、2 回目 0 件。Google Chat の試しは第1版の 1 回だけ（受け箱 gchat: sent）。
- 完了条件 2: rebuild_p8.py で p8 の 16:30:30 を作り直し、前（HEAD との差は projects_dir の差し替えだけ、と diff で確認）は pm「ループ?」・leader「進んでいる」、後は pm「待っている（leader の返事（start）を待っている）」・leader「待っている（受けたまま: … done ほか 3 件）」。止まった・ループした例（テストの D: 止まっている?・ループ?（出力はあるが…）・wait を抜けて 5 分でループ?・指摘 3 回超は wait の中でもループ?）は今までどおり出る。
- 完了条件 3: patrol --projects --once --exit N が動く（閉じたプロジェクトを飛ばす・終了コード）。README の automation の定義は orca automations create --help の形に合う。登録はしていない。org-project-new の 5 が「常駐に切り替えたあと／切り替える前」に分かれている。
- 完了条件 5（見張りの分）: プランの決まったこと 22 は元の文を残し、補足 2 つを併記。
- 全体: py_compile 通る。watch・digest・patrol --once --dry・export --check（ai-org/projects・入れ子の監査を置いた仮のプロジェクト）通る。worker-audit の受け持ち（boss_of の auditor・audit_findings）も壊れていない。dev-tools の本体は git status が空。

申し送り:
- **完了条件 5 の監査の分がまだ無い。** プランの 22 に、閉じるときの監査（手順に入った・出力は起きたことと参照元だけ・reports/audit/ と snapshot の audit_findings）の補足が無い。worker-watch は「worker-audit が書く」とし、worker-audit はもう承認済みで待っている。リーダーから worker-audit へ回してほしい（書けば自分が見る）。
- watch の状態の欄は、受けたままの人も「待っている（受けたまま: …）」。中身でボールの持ち主は分かるので指摘にしていない。
- 全員待ちの閾値 5 分・.waited 2 分・ターンを終えた人が混じると 10〜15 分かかる点は〔仮〕で README に書いてある。
- automation の登録の行の --workspace-mode は、登録の前に既存の 1 本と見比べる（README の注記どおり、根っこが確かめる）。
