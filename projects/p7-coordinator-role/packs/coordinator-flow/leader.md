---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`W` = `/Users/maka343noshi/orca/workspaces/dev-tools/coordinator-role`、`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p7-coordinator-role`。

1. `P/teams/coordinator-flow/charter.md` 全体 — チームの完了条件。
2. `P/charter.md` の「目的」「完了条件」「範囲」 — プロジェクト全体の目的と書いてよい場所。
3. `W/CLAUDE.md` の「展開先を直接編集しない」「git」の節 — 作業者・レビュアーに守らせる決まり。
4. `P/log/msgs/` の PM → コーディネーターの `start` と、コーディネーター → PM の `report` — 編成案の理由（なぜ 1 チーム・この順番か）。

## 事業の文脈の要約

事業の資料は要らない（題材は組織そのもの）。回すときの要点:

- 編成: 作業者 1（engineer・opus）、レビュアー 1（engineer・sonnet。作業者と別のモデルにして同じ見落としを避ける）。ヒントの振り分けはしない（好みで割れる点が無い）。
- パックは、このチームの `packs/` ではなく、相談した親の `P/packs/coordinator-flow/` にある（新しい流れの置き場の実地の試し）。assign は `--pack P/packs/coordinator-flow/worker.md`・`--pack P/packs/coordinator-flow/reviewer.md`。人数を増やしても同じパック。
- 作業者・レビュアーは `--workdir W` で起こす。書いてよいのは W の中だけ。git は誰も触らない。CLI の試しは W の orgctl で `$TMPDIR` の仮の根っこに対して打ち、`launch` は打たない。本体の dev-tools は読むだけ。
- 順番: 規範・スキル・プラン・README の書き換え → CLI の試し、を作業者 1 人が通しで。レビュアーは書き換えの横断の整合と、CLI の試しを自分でも打って確かめる。
- PM へ出す前に、完了条件 3（パックの置き場。orgctl を直したか、直さない理由）と 4（打ったコマンドと結果）が報告に入っているかを見る。

## これまでの経緯

- 2026-10-24 PM がコンポーネントを作る前にコーディネーターへ相談し、チーム 1 つ・子プロジェクトなし・画面なしで合意した。
