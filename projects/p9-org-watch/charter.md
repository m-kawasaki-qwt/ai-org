# 目的

川崎さんがプロジェクトを組織に「投げっぱなし」にして、知らせが届いたときだけ見ればよい状態にする。いまは根っこのセッションが張り付いて見ていないと、止まったことに誰も気づかない。

起きた問題（直し方はこのプロジェクトで考える。下は起きたことだけ）:

1. **全員が待っていて誰も動かない詰まりを、見張りが止まりと判定しない。** p8 で、リーダーがメンバー 4 人の done を読んだあと PM へ report を出さずに wait に戻り、PM もリーダーを待っていて、全員が待つ形になった。`orgctl watch` はリーダーを「進んでいる」、PM を「ループ?」と出し、`orgctl patrol` は知らせを出さなかった。根っこのセッションが 15 分おきに見て見つけ、手で促して動かした。p6 でも研究チームのリーダーが約 9 分、同じ形で止まった。
   - 記録: ai-org `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml` の unclear、`projects/p8-viewer-rebuild/log/msgs/b20186.md` の「うまくいかなかったこと」、`projects/p8-viewer-rebuild/log/events.log` の 16:25〜16:31
2. **見張りの判定が、待っているだけのメンバーを「ループ?」と出す。** p8 の PM は子の報告を待っているだけだったが、`watch` は 30 分以上「ループ?（出力はあるが状態が変わらない）」と出し続けた。本当の止まりと見分けがつかない。
3. **見張りが常駐していない。** `orgctl patrol` は、根っこのセッションがプロジェクトを立てるたびに裏で手で回していて、根っこのセッションが閉じると止まる。決まったこと 22 では、見張りを Orca の automation に載せて常駐させると決めたが、まだ載っていない。
4. **閉じるときの監査が回っていない。** 決まったこと 22 で「進め方の監査はプロジェクトを閉じるときに 1 回」と決めたが、閉じ方の手順（dev-tools のスキル `org-project-new` の 7）に入っておらず、監査役が動いたのは p3 だけ。セッション報告の unclear は溜まっている（ビューアの「決まりの直し候補」で 111 件）が、誰も読んでいない。
   - 監査の中身は「起きたこと（問題・課題）と参照元」までにする。直し方は書かない（決定ログ 2026-10-24「問題だけを控え、直し方は着手の直前に考える」）。

出発点: dev-tools の `docs/todo/ai-org-plan.md`（決まったこと 13・22、決定ログ）、`org/scripts/orgctl.py`（watch・patrol・wait）、`org/positions/`（leader・pm・auditor）、`claude/plugins/dev-tools/skills/org-project-new/SKILL.md`。job の `company/system/ai-org/README.md` の「組織の直し待ち」（上の 1・4 の控え）。

# 完了条件

1. 上の問題 1 の形（全員が待っていて、誰も相手に何も出していない）を、見張りが止まりと判定し、川崎さんへ知らせる（Google Chat の `gchat-notify` の slug `ai-org` と受け箱 `log/user-inbox.yaml`）。仮のプロジェクトでこの形を作って、知らせが出ることを確かめた結果が報告にある。知らせの本文から、誰が誰を待っていて、何が出ていないかが分かる。
2. 問題 2 について、待っているだけのメンバーと、本当に止まっている・ループしているメンバーを、`watch` の出力で見分けられる。p8 の記録（`events.log` と `.waiting` などの足場）で、PM が「ループ?」と出なくなることを確かめた結果が報告にある。
3. 問題 3 について、見張りを常駐させる形ができている。開いている全プロジェクトを 1 回見て終わる形（`patrol --once` など）が CLI にあり、Orca の automation に登録する定義（コマンド・間隔・どの repo で動かすか）が書けている。**automation の登録そのものはしない**（根っこのセッションが川崎さんの承認を取って登録する）。登録までの手順は org-project-new か README に書く。根っこのセッションが裏で patrol を回す手順（org-project-new の 5）は、常駐に切り替わったあとの扱いが分かる形に直っている。
4. 問題 4 について、プロジェクトを閉じる手順に、監査役が動く段が入っている。監査役の出力は「起きたこと（問題・課題）と参照元」で、直し方を含まない。出力の置き場が決まっていて、ビューア（`orgctl export` の `snapshot.json`）に載る。このプロジェクト自身を閉じるときに、その手順で監査役が動く。
5. 雛形の README（`org/README.md`）とプランの該当箇所（決まったこと 22 の補足など）が、新しい形に合っている。決まったことを改める場合は、元の文を消さずに併記する。

# 範囲

- 書いてよい場所: dev-tools の worktree `/Users/maka343noshi/orca/workspaces/dev-tools/org-watch` の中だけ（`org/`・`docs/todo/ai-org-plan.md`・`claude/plugins/dev-tools/skills/org-project-new/`・`claude/plugins/dev-tools/bin/`）。dev-tools の本体は読むだけ（動いている組織は本体の orgctl を使っている）。
- ai-org の記録（`projects/`）は読むだけ。試しは scratchpad や `$TMPDIR` の仮のプロジェクトで行う。
- 作業者は worktree を `--workdir` にして起動する。
- Google Chat への知らせの試しは、`gchat-notify` の slug `ai-org` に送ってよい（川崎さんが知らせを受け取る通知専用のスペース）。送る回数は確かめに要る分だけにし、本文の頭に「［試し］」と付ける。
- Orca の automation の登録・Orca の設定の書き換えはしない。
- git の操作はしない（コミットと PR は根っこの側）。
- うまくいかなかったこと（文脈パックの過不足・連絡・決まり）は、隠さずセッション報告の `unclear` と最後の報告に書く。
