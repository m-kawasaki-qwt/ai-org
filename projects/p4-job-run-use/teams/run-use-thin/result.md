# run-use-thin の結果

編成: 作業者 1 人（engineer・Opus）、レビュアー 1 人（engineer・Sonnet）。往復 1 回でレビュアーが承認（指摘 0 回）、リーダーも目的に照らして通した。

## 完了条件ごとの結果

| # | 結果 | 確かめたこと |
|---|---|---|
| 1 | 満たす | `run-use.md`（61 行 → 54 行）は、共通の手順を SKILL.md の節の見出し名（「B. 依頼する（Orca に投げる）」の「`run-use` の使いどころ」・「C. 一覧を出す（「何が動いてる？」）」・「D. 戻りを受ける（`worker_done`）」の分岐 1〜3・「自分が依頼していない戻りが届いたとき」・`consumer_fenced`）で指し、残っているのは job の値と運用だけ（Run の ID 2 本・`依頼元の端末` の印・`--limit 100`・見る範囲・2 時間・automation の依頼はすぐ引き取る・〔誤配〕の扱いと川崎さんへの 1 行・ログ）。リーダーが参照先の見出しが SKILL.md にあることを確かめた |
| 2 | 満たす | `_archive/2026-10-24-run-use-before.md` は、作業者・レビュアー・リーダーがそれぞれ diff を取り、一字一致（リーダーは git の HEAD の版と比べた）。`run-use.md` の 1 行目が退避ファイルを指している |
| 3 | 満たす（直したファイルは無し） | 見出し「1.」〜「4.」の番号と名前を変えなかったので、節番号で指している参照元（manager の `sources/orca/inbox.md` 38 行目・`automation-followup/inbox.md` 35 行目・`advance/implement.md` 58 行目など）も合ったまま。grep で当たった全件と判定の一覧は作業者の報告にある |
| 4 | 満たす | 突き合わせの表は作業者の報告にある。前の版の食い違い 4 件（新しい端末は最初に結ぶ・`read` が 0 なら未処理と言い切る・通知先が null の場合が抜けている・誤配の 1 行の文例）は、言い換えをやめて SKILL.md を指す形にしたことで解消 |
| 5 | あり | 作業者の報告の「完了条件 5」の節と、下の「文脈パックの過不足」 |

## 成果物

- job `.claude/skills/manager/sources/orca/run-use.md`（変更）
- job `.claude/skills/manager/sources/orca/_archive/2026-10-24-run-use-before.md`（新規）
- 作業者の報告（完了条件 3 の一覧・4 の表・5）: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p4-job-run-use/teams/run-use-thin/worker-1-report.md`
- job は未コミット（`run-use.md` が変更、`_archive/` が未追跡）。コミットは job の持ち主の判断。

## 文脈パックの過不足

- パックに無くて作業者が自分で探した資料: dev-tools `orca-multi-agent/ticket-template.md` の `依頼元の端末` の行（印の書式が食い違わないかを見るため）、job `manager/sources/orca/inbox.md` の「取り方」0〜5 と「続行の 2 段」（パックは grep の当たりの前後だけだったが、30〜60 行を読む必要があった）、`automation-followup/followup.md` の「戻りを受ける」の節。
- パックにあって要らなかった資料: 無し（job `CLAUDE.md`「情報を消さない」は、作業者が job で起動したので最初から入っていた）。
- パックと実際が違った点: リーダーのヒントは退避を `cp` でと書いたが、`.claude/skills/` は Bash から書けないので作業者は Write にした（パックの方が正しかった）。
- リーダーのパックは、編成と段取りの見当（節番号の参照元・範囲外の扱い）がそのまま使えて、過不足は無かった。

## 申し送り

- job `tasks/_master/manager.yaml` 15 行目のコメント（「毎回のはじめに `orca orchestration run-use --id <これ>` で結び直す」）は、いまの手順と食い違う。`tasks/` は範囲外なので直していない。サンドボックスで読めず、中身もこのチームでは確かめていない（パックの記述による）。
- `manager/_failures/2026-10-22-orca-check-unbound-fenced.md` の「dev-tools の `orca-multi-agent` は未対応（job 側で上書き）」は古いが、記録として残した（直していない）。

## 目的に照らして残る不明点

- `tasks/`・`self-tasks/`・`**/_history/`・`.claude/skills/_archive/` は読み取りが拒否されていて、grep が届かない。この中に `run-use.md` の節番号や旧手順（「最初に結び直す」）を指す箇所があっても、洗い出せていない。分かっているのは上の `manager.yaml` の 1 件だけ。
