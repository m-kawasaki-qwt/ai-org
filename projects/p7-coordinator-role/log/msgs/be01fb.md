<!-- p7-coordinator-role/pm → user report 2026-10-24T15:21:31+09:00 -->
# p7 チームコーディネーターの役割の改め ― 結果

親の完了条件 1〜5 をすべて満たした。変更は dev-tools の worktree `/Users/maka343noshi/orca/workspaces/dev-tools/coordinator-role` に置いたまま（git は誰も触っていない。本体へ入れるにはこの worktree からのコミット・PR が要る）。

## 変えたファイル（W = 上の worktree）

```
W/
├── org/positions/coordinator/position.md           変更（書き直し。新しい流れの正）
├── org/positions/pm/position.md                    変更（作る前に相談 → 往復 → 合意 → 作る）
├── org/positions/pm/skills/org-team-setup/SKILL.md 変更（§1 相談 → §2 往復して合意 → §3 作る → §4 assign。coordinator-<チーム名> を消した）
├── org/positions/leader/position.md                変更（パックの置き場）
├── org/positions/leader/skills/org-assign/SKILL.md 変更（パックは <親>/packs/<チーム名>/）
├── org/README.md                                   変更（「チームコーディネーターと文脈パック」の節）
├── org/scripts/orgctl.py                           変更（new が packs/ を作るのをプロジェクトだけに。2 行）
└── docs/todo/ai-org-plan.md                        変更（16・16 の補足に「2026-10-24 改めた」を併記、立場と職種の表にコーディネーター）
```

## 新しい流れ（決めたこと）

- PM が子を作る前に、プロジェクトに 1 人だけコーディネーターを立てて相談（`start`）。返し（`report`）に、切り方・つなぎ方・順番と理由／編成／実現できる理由と崩れる前提／チームごとに charter に入れてほしいこと／パックのパス。
- 視点を足して返す＝PM の `start`（本文の先頭「視点を足す」）、合意＝PM の `report`（先頭「合意」）。`rework` を使わないのは、ビューアで作り直しとして数えられるため。新しい種類は足していない。
- コーディネーターは合意のあとも残り、PM が作って assign し終えたあとの `wrap_up` で終わる。
- パックの置き場は、相談した親の `packs/<チーム名>/<立場>.md`。作ったあと `assign --pack` でそのパスを渡す。`--pack` は任意のパスを読み assign の時点で写すので、orgctl のその部分は直さなかった。
- `orgctl digest` が id では引けない件は直さず、規範に「絶対パスで」と書いた（watch・teardown・assign もパスで受けるのに揃えた）。

## このプロジェクト自身も新しい流れで回した

1. PM がチームを作る前に、`p7-coordinator-role/coordinator` を 1 人だけ立てて相談（私の案: チーム 1 つ・画面なし・パックは親の `packs/<チーム名>/`）。
2. コーディネーターは同意しつつ、範囲の足し（リーダーの手順もパックのパスを指している・プランの表に行が無い）と、規範に書くべき点 6 つを返した。パックは `projects/p7-coordinator-role/packs/coordinator-flow/` に書かれた。
3. 合意を返し、その中身を charter の完了条件に入れてチーム `coordinator-flow` を作り、親の packs からリーダーを assign。リーダーが作業者（opus）・レビュアー（sonnet）を同じ置き場のパックで assign。作業者・レビュアーの pack.md に入ったのを確かめてから、コーディネーターを wrap_up・teardown。
4. 作業者が通しで書き換え、レビュアーは 1 回目で承認（自分でも CLI の試しを打ち直した）。

## PM が自分で確かめたこと

- `git diff --stat`（8 本）。coordinator/position.md の全文、pm/position.md の diff、org-team-setup の §1〜3、plan の 16 と併記を読み、親の完了条件 1・2・5 に照らした。
- 古い流れの残りの grep: `grep -rn --exclude='.env*' -e 'coordinator-<' -e '<T>/packs' -e '1 回だけ' -e 'ためだけに' -e '作ったあとに' W/org W/docs/todo/ai-org-plan.md W/claude/plugins/dev-tools/skills/org-project-new` → 5 件。orgctl.py の patrol のコメント（無関係）と、plan の元の文・決定ログ（過去の記録として残すもの）だけ。
- `orgctl.py` の構文チェックが通った。
- 作業者の試しのスクリプト（`/tmp/claude-501/coord-trial.sh`）を `T=$TMPDIR/pm-rerun` で打ち直し、exit 0。new project → assign coordinator → 往復 2 回 → 合意 → 親の `packs/alpha/` にパック（2 回目で v2 に書き直し）→ new team → leader・worker・reviewer を `--pack` で assign。3 人とも `pack.md`・`CLAUDE.md` に v2 が入り、`.claude/settings.json` にパックの deny が入った。`teams/alpha/packs` は無く、`projects/tr/packs` はある。
- org-project-new にはコーディネーター・packs の記述が無い（直していない）。

## うまくいかなかったこと・残ること

- コーディネーターの規範（本体の古い position.md）が古い流れのままなので、相談の本文で「改めた後の形で動いて」と上書きして動かした。本体へ取り込まれるまで、ほかのプロジェクトのコーディネーターは古い規範で動く。
- 合意を PM からの `report` にしたので、種類だけでは「返し」と「合意」を見分けられない（本文の先頭で見分ける）。ビューアで往復の段を数えたいなら、`agree` などの種類を足すかを決める余地がある。
- パックの deny に `$TMPDIR` のパスを書くと `/tmp/…` のまま入り、ヒントの deny は `/private/tmp/…` になる（macOS のリンク）。試しの場所だけで、実運用（`~/ghq/…`）では起きない。直していない。
- Orca の知らせで「Enter が飲まれたかもしれない」の警告が出たが、再送せずに届いた。

## 記録

- チームの報告: `log/msgs/2e8018.md`。コーディネーターの返し: `log/msgs/4d25e4.md`。相談: `log/msgs/101739.md`。
- セッション報告: `reports/sessions/` の coordinator・leader・worker-1・reviewer。
