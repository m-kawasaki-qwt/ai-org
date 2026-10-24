---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`W` = `/Users/maka343noshi/orca/workspaces/dev-tools/coordinator-role`（書いてよいのはこの中だけ）、`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p7-coordinator-role`。

1. `P/teams/coordinator-flow/charter.md` 全体 — 自分のチームの完了条件（照らす相手）。
2. `P/charter.md` の「目的」「完了条件」「範囲」 — 元の 1〜4 の流れと川崎さんの言葉。言い回しはここに寄せる。
3. `W/CLAUDE.md` 全体 — dev-tools で書くときの決まり（コマンドは 1 行・展開先を直さない）。
4. `W/org/positions/coordinator/position.md` 全体 — 書き換える本体。
5. `W/org/positions/pm/position.md` の「判断してよいこと」「はじめにやること」と、`W/org/positions/pm/skills/org-team-setup/SKILL.md` 全体 — 「先に相談 → 往復 → 作る」に並べ替える。§3 の `coordinator-<チーム名>` を消す。§4・§5 のパックのパスも直す。
6. `W/org/positions/leader/skills/org-assign/SKILL.md` の §2（`--pack <T>/packs/...` と「パックは `<T>/packs/` に置いている」）と `W/org/positions/leader/position.md` の「組むとき」 — パックの置き場が変わるので、ここも直さないとリーダーが空の場所を見る。
7. `W/docs/todo/ai-org-plan.md` の「立場と職種」（表にコーディネーターの行が無い）、「決まったこと」16・16 の補足・17、「決定ログ」の 2026-10-24 の最後の行 — 16 は元の文を残して改めた内容を併記する。
8. `W/org/README.md` 全体 — 雛形の地図。コーディネーターと packs の説明を合わせる。
9. `W/org/scripts/orgctl.py` の `cmd_new`（`packs/` を作る行）・`cmd_assign`（`--pack` の読み込み・front matter の deny・`pack.md` への写し）・`digest_text` — `--pack` は任意のパスの md を読み、assign の時点でメンバーのディレクトリへ写す。置き場がどこでも動くかを確かめる材料。
10. `P/log/msgs/` の PM → コーディネーターの `start`（相談）と、コーディネーター → PM の `report`（編成案） — この相談そのものが、新しい流れの最初の実例。規範に書く「返すもの」の形の材料に使ってよい。

## 事業の文脈の要約

事業の資料は要らない（題材は組織そのもの）。押さえること:

- いまのコーディネーターは「PM がコンポーネントを作ったあと、そのためだけに 1 回呼ばれる」。p6 ではチームの数だけ 2 人立ち、チーム同士のつなぎ（どこで分けるか・何を渡し合うか・どの順か）を誰も持たなかった。
- 改めた形: PM は作る前に目的とおおまかな考えを相談 → コーディネーターが切り方（数・チームか子プロジェクトか・つなぎ・順番）まで責任を持って、編成案と一人ずつのパックを返す → PM が視点を足して往復 → 合意してから PM が作って assign。1 つの相談にコーディネーターは 1 人。
- パックの置き場は、この相談で実地に試している形: 相談した親の `packs/<チーム名>/<立場>.md` に書き、作ったあと `assign --pack <親>/packs/<チーム名>/<立場>.md` で渡す（このパック自体がそこにある）。orgctl を直さずに済むかは、9 を読んで判断し、直さないなら理由を報告に書く。
- 規範に入れるかを判断してほしい点（コーディネーターが相談される側として動いて気づいたもの。採否は作業者の判断でよい）:
  - パックは charter より先に書かれる。charter の完了条件とパックがずれないよう、コーディネーターはチームごとに「charter に入れてほしいこと（完了条件の要点・つなぎ＝誰から何を受け、誰へ何を渡すか）」を編成案に添える。完了条件を決めるのは PM のまま。
  - 往復で使う event の種類が決まっていない（今回は相談＝`start`、返し＝`report`）。PM が視点を足して返すとき・合意したときの種類を書く。
  - コーディネーターの終わり: 往復のあいだは残り、合意（と PM の作成・assign）のあとの `wrap_up` で終わる。あとで別のチームが要るときは新しい相談として扱う。
  - `orgctl digest <親>` はコンポーネントの名前だけだと根っこが見つからず失敗した（`/…/ai-org/p7-coordinator-role から上に、根っこのプロジェクトが無い`）。絶対パスなら通る。規範ではパスで書く。
  - `orgctl new` はチームにも `packs/` を作る。新しい流れではチームの `packs/` は使わない（使うのはプロジェクトの `packs/<チーム名>/`）。残すか、プロジェクトだけにするかを決める。
- 完了条件 4 の CLI の試しは、`W/org/scripts/orgctl.py`（雛形が W の `org/` を指す）で、`$TMPDIR` の下の仮の根っこに対して打つ。`launch` は Orca のタブを開くので打たない（assign まで）。動いている組織の本体の orgctl・本体の `org/` は書き換えない。

## これまでの経緯

- 2026-10-24 15:06 根っこがプロジェクトを作り PM を起こした。15:07 PM がコーディネーターを 1 人だけ assign し、コンポーネントを作る前に相談（`start`）した。
- コーディネーターはチーム 1 つ（engineer のリーダー・作業者 1・レビュアー 1）、子プロジェクトなし・画面なし、で PM の案に同意して返した。順番は 規範・スキル・プラン・README の書き換え → CLI の試し、を同じ作業者が通しで。
