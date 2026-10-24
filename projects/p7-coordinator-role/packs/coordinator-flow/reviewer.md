---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`W` = `/Users/maka343noshi/orca/workspaces/dev-tools/coordinator-role`（作業者が書く場所。レビュアーは読むだけ）、`B` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools`（本体。直す前の比較用。読むだけ）、`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p7-coordinator-role`。

1. `P/teams/coordinator-flow/charter.md` 全体 — 照らす完了条件。指摘は必ずこの番号で書く。
2. `P/charter.md` の「目的」「完了条件」 — 元の 1〜4 の流れと川崎さんの言葉（ここから外れていないか）。
3. `W/CLAUDE.md` の「展開先を直接編集しない」「git」の節 — 書いた場所が W の中だけか。
4. 直した文書: `W/org/positions/coordinator/position.md`・`W/org/positions/pm/position.md`・`W/org/positions/pm/skills/org-team-setup/SKILL.md`・`W/org/positions/leader/skills/org-assign/SKILL.md`・`W/org/positions/leader/position.md`・`W/org/README.md`・`W/docs/todo/ai-org-plan.md`（「立場と職種」「決まったこと」16・補足・17）。差分は `git -C W diff` で見る（読むだけ）。
5. `W/org/scripts/orgctl.py` の `cmd_new`・`cmd_assign`（`--pack`） — パックの置き場の主張が実装と合っているか。

## 事業の文脈の要約

事業の資料は要らない（題材は組織そのもの）。見るときの要点:

- 新しい流れ: PM が作る前に相談 → コーディネーターが切り方・つなぎ・順番まで責任を持って編成案とパックを返す → 往復して合意 → PM が作って assign。1 つの相談にコーディネーターは 1 人。
- 古い流れの残りが無いか、文書を横断して grep で確かめる: `coordinator-<`・「作ったあとに」「1 回だけ呼ばれ」「返したら終わる」・`<T>/packs/`・`teams/<チーム名>/packs/`。プランの 16 は、元の文が残り改めた内容が併記されていること（消していたら NG）。
- パックの置き場は「相談した親の `packs/<チーム名>/<立場>.md` に書き、作ったあと `assign --pack` で渡す」形で試している（このパック自体がそこにある）。リーダーの org-assign が同じ置き場を指しているか。
- CLI の試し（完了条件 4）は、作業者の報告を読むだけで通さない。`W/org/scripts/orgctl.py` を使い、`$TMPDIR` の下の自分の仮の根っこで、`new` → コーディネーターの assign → 相談の往復の event → チームの `new` → `assign --pack <親>/packs/<チーム名>/...` を自分でも打ち、メンバーの `pack.md`・`CLAUDE.md` にパックの本文が入り、`.claude/settings.json` に deny が入ることを見る。`launch` は打たない。本体の orgctl・本体の `org/` は使わない。
- 書き方の好みは後。先に、流れが 1〜4 のとおりか・文書同士が食い違っていないか・CLI が通るか。

## これまでの経緯

- 2026-10-24 PM がコンポーネントを作る前にコーディネーターへ相談し、チーム 1 つ（engineer のリーダー・作業者 1・レビュアー 1）で合意した。この相談が新しい流れの最初の実例（`P/log/msgs/` に PM の `start` とコーディネーターの `report`）。
