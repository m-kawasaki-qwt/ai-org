# 目的

チームコーディネーターの役割を「PM がコンポーネントを作ったあとに 1 回呼ぶ」から、「PM が作る**前に**相談し、コーディネーターがチームの切り方（数・チームか子プロジェクトか・つなぎ方・順番）まで責任を持って編成案とパックを返し、往復して合意してから PM が作る。1 相談に 1 人」へ改める。親プロジェクト `p7-coordinator-role` の完了条件 1〜5 をすべてこのチームで満たす（親の charter: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p7-coordinator-role/charter.md`）。

以下 `W` = `/Users/maka343noshi/orca/workspaces/dev-tools/coordinator-role`。

# 完了条件

1. `W/org/positions/coordinator/position.md` が、相談を受ける → 切り方まで決めた編成案とパックを返す → PM の視点を受けて直す → 合意で終わる、の流れになっている。返すものに「切り方・つなぎ方（誰から何を受け誰へ何を渡すか）・順番とその理由」「この編成で実現できる理由と、崩れる前提」「チームごとに charter に入れてほしいこと」がある。往復で使う event の種類（相談・返し・視点を足して返す・合意）と、終わり方（PM が作って assign し終えたあとの `wrap_up`）が書かれている。責任の範囲（切り方まで持つ／完了条件を決めるのは PM）が書かれている。
2. `W/org/positions/pm/position.md` と `W/org/positions/pm/skills/org-team-setup/SKILL.md` が「先に相談 → 往復して合意 → 作る → assign」の順になっている。コンポーネントごとにコーディネーターを立てる手順（`coordinator-<チーム名>`）が無い。
3. パックの置き場が新しい流れで決まっている（相談した親の `packs/<チーム名>/<立場>.md` に書き、作ったあと `assign --pack` でそのパスを渡す、を基本に、作業者が判断してよい）。リーダーの手順（`W/org/positions/leader/skills/org-assign/SKILL.md` の §2・`W/org/positions/leader/position.md` の「組むとき」）と org-team-setup の §4・§5（入れ替え）がその置き場を指している。`orgctl new` がチームにも `packs/` を作る件をどうするか決め、orgctl を直したか・直さなかった理由が報告にある。
4. `grep` で、`W/org/` と `W/docs/todo/ai-org-plan.md`（決定ログ・決まったこと 16 の元の文など、過去の記録として残す箇所は除く）に古い流れの残り（`coordinator-<`・`<T>/packs/`・「作ったあとに 1 回だけ」の趣旨）が無い。打った grep と結果が報告にある。
5. `W/docs/todo/ai-org-plan.md` の「決まったこと」16 に、元の文を消さずに改めた内容が併記され（改めた日付と決定ログへの参照付き）、16 の補足のうち改めた点も同じ形になっている。「立場と職種」にコーディネーターの行（または記述）があり、新しい流れに合っている。
6. `W/org/README.md` が新しい流れに合っている。
7. `W/org/scripts/orgctl.py` で `$TMPDIR` の下の仮の根っこに対して、`new project` → `assign coordinator` → 相談の往復を模した event（相談・返し・視点を足して返す・合意。少なくとも 2 往復）→ 親の `packs/<チーム名>/` にパックを置く → `new team` → `assign leader/worker/reviewer --pack <親>/packs/<チーム名>/...` まで打ち、assign されたメンバーの `CLAUDE.md`・`pack.md`・`.claude/settings.json`（deny）にパックが入ったことを確かめた結果が報告にある。`launch` は打たない。レビュアーも自分で打ち直して確かめる。
8. `W/claude/plugins/dev-tools/skills/org-project-new/` にコーディネーターの古い流れの記述があれば、合わせて直っている（無ければ無いと報告）。

# 範囲

- 書いてよい場所: `W` の中だけ（`org/`・`docs/todo/ai-org-plan.md`・`claude/plugins/dev-tools/skills/org-project-new/`）と、`$TMPDIR` の仮の根っこ。
- 触らないもの: dev-tools の本体（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`。動いている組織が使っている）。git の操作（コミット・ブランチ・worktree）。`launch`・Orca のタブ。
- 人にしかできない操作が要ったら: 手順を書いて escalate。
- うまくいかなかったこと（パックの過不足・連絡・決まり）は隠さず報告に書く。
