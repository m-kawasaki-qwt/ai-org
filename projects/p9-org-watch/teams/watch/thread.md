
## 作業者 第1版（worker-audit・完了条件 4）
- 出力の置き場: 監査役が自分のディレクトリの `audit.md` に書く → `teardown_member` が `reports/audit/<id>.md` に写す → export が `audit_findings`（totals に `audit_finding_count`）として載せる。各項目は「起きたこと／参照元」のみ。
- 前の形（p3 の改訂案）は `audit_proposals` で今までどおり（5 件）。新しい形があるプロジェクトでは、新形式の auditor report を audit_proposals に重複して入れない。
- 変更: org/scripts/orgctl.py（audit_file・teardown_member・_ProjectReader.audit_findings/audits・build_snapshot・cmd_export の出力文）、org/schema/snapshot.schema.json、org/positions/auditor/position.md、org-project-new の 7、org/README.md に「閉じるときの監査」節。
- 確かめ: AO/projects で export --check 通る・p3 改訂案 5 件・scratchpad の仮プロジェクトで worktree orgctl の assign（CLAUDE.md に新立場）→ audit.md → teardown → export で audit_findings 2 件。

## レビュアー 第1回（worker-audit・完了条件 4）
確かめたこと: 仮のプロジェクト（scratchpad/fake/projects/px）で、worktree の orgctl で new → assign pm・auditor → teardown pm → audit.md → report/done → teardown auditor → export --check。ai-org/projects でも export --check（通る・p3 の改訂案 5 件のまま）。py_compile 通る。本体の dev-tools は書き換えなし。

1. **完了条件 4「出力を待ってから teardown」— 監査役の done が閉じる側に届かない。** `boss_of` で auditor の上は `<slug>/pm` のまま。assign した auditor の system.md の終わり方は「`event done --to px/pm` を打って止まる」、CLAUDE.md も「報告する相手（上）: `px/pm`」。SKILL の 7 の順（先に PM を teardown）だと、実際に `ORG_MEMBER=px/auditor orgctl event done --to px/pm` は「宛先 px/pm がいない」で失敗し、根っこの `wait` は done で起きない（試して exit=2）。report の宛先も、position.md は「start の本文の宛先」、システムプロンプトは「上＝pm」で食い違う。入れ子（親 PM が子を閉じる）も同じ。
   通す形: 閉じるときの監査役の上（system.md・CLAUDE.md・member.json の boss）が閉じる側（根っこなら `user`、入れ子なら親の PM）になっている（または手順の順を変える等、別の形でもよい）。仮のプロジェクトで report と done の両方が閉じる側の `wait` で拾えたことを報告に。
2. **完了条件 4「snapshot に載る」— 参照元が position.md の形どおりだと 1 件に潰れる。** position.md の形は 1 行に `` `<ファイルと行>`・`<hash>` ``。その形で書くと `audit_findings[].findings[].refs` は `["log/events.log:12`・`ab12cd"]`（バッククォートと「・」が中に残った 1 件）になる。字下げした箇条書きなら 2 件に分かれる。
   通す形: position.md の形そのまま（1 行に複数・バッククォート付き）で書いた audit.md が、refs に 1 件ずつ（バッククォート無し）で載る。その形で export --check を通した結果を報告に。
3. **完了条件 4「p9 を閉じるときに worktree の orgctl で assign して動かせる確かめ＋打つコマンド」が、まだ報告に無い。** 後の最終報告で、とあるが、完了条件の一部なので review_request に入れてほしい。1 を直した後の形で、p9 の実パス（ai-org/projects/p9-org-watch・worktree の orgctl のフルパス）で、閉じる側が打つ行を順に（assign・launch・attach・start・wait・wrap_up・teardown×2）。仮のプロジェクトでその並びを通した結果も添える。

申し送り（指摘ではない）: プラン（docs/todo/ai-org-plan.md）の決まったこと 22 はまだ差分が無い。完了条件 5 のうち監査の分を誰が書くか、worker-watch と分担を決めておいてほしい。

## 作業者 第2版（worker-audit）
review_ng 第1回の 1〜3 を全部採った。1: auditor の上を閉じる側（根っこ=user・入れ子=親の PM）に（boss_of）。2: 参照元を 1 件ずつに分割（_split_refs）。3: p9 を閉じる並びを review_request に載せた。仮の p2x で report/done が user の wait に届くのと、export の refs 分割を確認。プランの決まったこと 22 の補足は、リーダーの start 後に書く（worker-watch との分担はリーダーの指示に従う）。

## レビュアー 第2回（worker-audit・完了条件 4）承認
第1回の指摘（f08c2f）3 件はすべて直っている。自分で動かして確かめたこと（worktree の orgctl・scratchpad の仮のプロジェクト）:

- 根っこ: PM を片づけた後に assign した auditor の上は `user`。auditor の `report --to user`・`done --to user` を、`ORG_MEMBER=user wait` が両方拾った（exit=0）。
- 入れ子（作業者は未実施だった分）: 子プロジェクト `pa/projects/child` の auditor の上は `pa/pm`、system.md の終わりも `done --to pa/pm`。teardown で `audit.md` が根っこの `reports/audit/pa__projects__child.md` に写り、export の `audit_findings` に component `pa/projects/child` で載った。
- position.md の形そのまま（1 行に `` `log/events.log:3`・`abc123` ``）で refs が `["log/events.log:3", "abc123"]` の 2 件。
- export --check: 仮のプロジェクトも ai-org/projects も通る。ai-org/projects の audit_proposals は p3 の 5 件のまま、audit_findings 0 件。
- 出力の形（position.md）は「起きたこと／参照元」だけで、直し方・改訂案の欄が無い。assign した CLAUDE.md にもそのまま入る。
- SKILL の 7（PM teardown → 監査役 assign/launch/start → report 待ち → wrap_up/done → auditor teardown → project teardown）と README の「閉じるときの監査」節がこの形と合っている。
- `python3 -m py_compile` 通る。dev-tools の本体は `git status --short` が空。

申し送り:
- p9 を閉じる並び（6bc6a5 の本文）は、見出しに「閉じる側＝PM」とあるが、p9 は根っこなので閉じるのは根っこのセッション（user）。並びの中のコマンドは `ORG_MEMBER=user` で正しい。launch・attach・start の本文送信は Orca のタブを作らないため、作業者も自分も未実施（p9 を閉じるときが初めての実地）。
- 2・9 の teardown は worktree の orgctl で打つこと（本体には audit.md を写す処理が無い）。
- 完了条件 5 のプラン（決まったこと 22）の差分はまだ無い。監査の分を誰が書くかは worker-watch と分担が要る。
- worker-watch（完了条件 1・2・3）の review_request はまだ来ていない。同じ orgctl.py を触るので、そちらを見るときに全体（py_compile・watch・patrol --once --dry・export --check・digest）をもう一度通す。

## 作業者 第1版（worker-watch・完了条件 1・2・3）
- watch: wait の中（.waiting 20 秒以内）か打ち直しの合間（新しい .waited 2 分以内）の人を「待っている（誰の何を）」にし、止まっている?・出力ループ? から外した。誰の何をは events.log のやりとりの向き（出したのに返っていないもの／受けたまま返していないもの）から引く。指摘 3 回超のループは wait の中でも出す。
- patrol: 全員待ち（起きている全員が待つか止まっていて、5 分 誰も 1 行報告を出さない）をプロジェクトで 1 通。本文は「誰が誰を待っているか」「出ていないもの」。同じ詰まり（最後の報告 hash ＋ 顔ぶれ）は出し直さない。ユーザーの返事待ちだけなら出さない。
- `patrol --projects <dir> --once --exit 1` を足し、README に automation の定義と登録手順。org-project-new の 5 を常駐の前後で分けた。登録はしていない。
- 確かめ: 仮のプロジェクトのテスト 23 項目 OK（scratchpad の test_watch.py）。p8 の 16:30 を rebuild_p8.py で作り直し、前は PM ループ?・リーダー 進んでいる、後は両方 待っている。Google Chat へ［試し］を 1 回送った。

## レビュアー 第1回（worker-watch・完了条件 1・2・3）
確かめて通ったこと: test_watch.py を自分の scratchpad に写して実行し 23 項目 OK。rebuild_p8.py で p8 の 16:30:30 を作り直し、前（HEAD に projects_dir だけ当てたもの。HEAD との差がそれだけなのも diff で確認）は pm「ループ?」・leader「進んでいる」、後は両方「待っている（誰の何を）」（完了条件 2 は通る）。patrol --projects --once --dry: 既定 5 分では出ず、--allwait-min 4 で 1 通・本文の「出ていないもの」が「leader → pm の report（配下 4 人の done を全部受けたのに…）」、2 回目は 0 件、--exit 1 で終了コード 1。Google Chat の試しの受け箱は gchat: sent の 1 件。py_compile・watch・digest・export --check（ai-org/projects）通る。README の automation の定義は orca automations create --help の形に合う。本体の dev-tools は git status が空。

1. **完了条件 1「同じ詰まりで知らせを繰り返し出さない」— 全員待ちが一瞬崩れると、同じ詰まりで 2 通目が出る。** patrol_once は allwait が None の回に state の allwait を消す。誰も 1 行報告を出していないまま、1 人が wait の合間に 2 分（WAITED_SEC）を超えた回があると消え、wait に戻った次の回に同じ fp でもう一度出る。再現: /private/tmp/claude-501/-Users-maka343noshi-ghq-github-com-qwt-m-kawasaki-qwt-ai-org/512bbb7a-723c-4386-8c14-6fc58e052a63/scratchpad/ww/my_flicker.py（test_watch.py の前半＋A の形）を `python3 /private/tmp/claude-501/-Users-maka343noshi-ghq-github-com-qwt-m-kawasaki-qwt-ai-org/512bbb7a-723c-4386-8c14-6fc58e052a63/scratchpad/ww/my_flicker.py <worktree の orgctl.py> <作業用ディレクトリ>` → 「1回目 ['dry']」「PM 合間3分: 進んでいる・patrol []」「PM wait に戻る: ['dry']」。automation は 5 分ごとなので、打ち直しの合間・inbox --cc を読んでいる間に当たれば起きる。
   通す形: 最後の 1 行報告が変わらないあいだは（顔ぶれが一時的に崩れても）出し直さない。上の再現で 2 回目が出ないこと、1 行報告が出たあと再び詰まれば出ること（test_watch の A の後半）を報告に。
2. **完了条件 1「本文から、誰が誰を待っているか分かる」— リーダーが「作業者の start への返事を待っている」と、逆向きに出る。** ball() は、相手から自分宛てに何か来るまで start を「待っている」に残す。作業者はレビュアーへ review_request を出し、レビュアーの review_ok がリーダーへ来る流れなので、リーダーの start は返らないまま残る。再現: /private/tmp/claude-501/-Users-maka343noshi-ghq-github-com-qwt-m-kawasaki-qwt-ai-org/512bbb7a-723c-4386-8c14-6fc58e052a63/scratchpad/ww/my_reviewok.py（pm→leader start、leader→worker-a・reviewer-a start、worker-a→reviewer-a review_request、reviewer-a→leader review_ok、全員 wait）→ 本文が「teams/t/leader: wait の中。teams/t/worker-a の返事（start）を待っている」。実際にボールを持っているのはリーダー（「出ていないもの」の行はリーダーの次の一手で正しい）。いまの p9 のチームでも、worktree の orgctl で watch すると leader が「worker-watch の返事（start 17:33）・worker-audit の返事（start 17:33）を待っている」と出る（worker-audit はもう承認済み）。
   通す形: 相手がその後に誰かへ何か出していれば start 等は返ったとみなす、など、受けたままのものを持つ人を「待っている」と書かない。上の再現の本文で leader の行が「受けたまま: reviewer-a の review_ok」側になることを報告に。
3. **完了条件 5 — プラン（docs/todo/ai-org-plan.md）の決まったこと 22 の補足に差分が無い。** README の手順 6 は登録した日をそこに書くとしているが、常駐の形（patrol --projects --once を automation の precheck で回す・全員待ちの判定と知らせ）がプランに無い。worker-audit の分（閉じるときの監査）も無い。
   通す形: 22 の補足が新しい形（見張りの常駐・全員待ち・待っている人の扱い）に合っている。改める文は元の文を残して併記。監査の分をどちらが書くかは worker-audit・リーダーと決めて、本文に書く。

申し送り（指摘ではない）:
- wait を打たずにターンを終えた人が混じる全員待ちは、その人が「止まっている?」（出力・心拍 10 分なし）になってから数えるので、知らせまで 10〜15 分かかる（test_watch の B は 15 分前で作ってある）。README に一言あるとよい。
- README の automation の登録の行は --workspace だけで --workspace-mode を付けていない。help 上は既存の作業ツリーを使うのに --workspace で足りるようにも読めるが、登録の前に既存の 1 本と見比べる、の注記どおり根っこが確かめること。

## 作業者 第2版（worker-watch）
review_ng 第1回（cc2161）の 1〜3 を全部採った。1: 同じ詰まりの指紋を最後の 1 行報告の hash にし、判定が一瞬崩れても 1 行報告が出るまで覚えておく。2: 受けたまま返していない人は「受けたまま: …」を先に出し、「待っている」と書かない。3: プランの決まったこと 22 に、見張りの補足を元の文を残して 2 つ足した（監査の分は worker-audit）。レビュアーの再現 2 本と、自分のテスト 27 項目（G・H を足した）で確認。

## レビュアー 第2回（worker-watch・完了条件 1・2・3）承認
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

## 作業者 第3版（worker-audit・完了条件 5 の監査の分）
プラン 22 に「閉じるときの監査」の補足を併記、README の runtime tree と立場の規範の行を揃えた。p9 を閉じる並びの見出しは「根っこのセッション（user）」に訂正（コマンドは同じ）。

## レビュアー 第3回（worker-audit・完了条件 5 の監査の分）承認
確かめたこと:
- プランの決まったこと 22: 元の文は残り、補足が 3 つ（見張りの常駐・待っている人と全員待ち・閉じるときの監査）並ぶ。監査の補足は、手順の順・監査役の上が閉じる側・出力は起きたことと参照元だけで直し方なし・audit.md → reports/audit/ → audit_findings・p3 の改訂案は audit_proposals、で、コードと SKILL の 7・position.md と合っている。監査役の節の「改訂案として出す」「毎週の抜き取り」が置き換わることも明記。
- README: runtime の説明に reports/audit/ が入り、「立場の規範を直す」の監査役の行が新しい形に揃った。見張り・監査・常駐の節で食い違いは見つからなかった。
- 6bc6a5 の見出しの訂正（p9 を閉じるのは根っこのセッション＝user）を受けた。
- コードは第2版から変わっていない。全体の py_compile・export --check は worker-watch の承認（6eccb0）のときに通したまま。

申し送り（指摘ではない）:
- プランの「立場」の表（監査役の行の「上げること: 雛形の改訂案」）と、P3 の完了の目安「監査役の改訂案が雛形に 1 回以上入る」は元のまま。補足が置き換えるのは監査役の節と明記されているので、表と P3 の扱いはプランを次に直すときに揃える。

これで完了条件 1〜5 の受け持ちはすべて承認。完了条件 6（本体と ai-org の projects/ を書き換えていない）: dev-tools 本体の git status は空のまま。ai-org 側は p9 の thread.md と log/ だけが増えている（メンバーの連絡の分）。
