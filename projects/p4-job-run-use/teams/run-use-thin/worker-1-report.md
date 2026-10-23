# run-use.md を薄くした報告（worker-1 第1版）

## Summary

- job の `run-use.md` を、SKILL.md（`/dev-tools:orca-multi-agent`）の節の見出し名への参照＋job の値・運用の表に置き換えた。見出し「1.」〜「4.」の番号と名前は変えていないので、参照元は直していない。
- 置き換え前の全文を `_archive/2026-10-24-run-use-before.md` に Write で退避し、`diff`・`cmp` とも差分なしを確かめた。新しい `run-use.md` の 1 行目がそのファイルを指す。
- 外したもの: 冒頭の経緯の段落（通知先は端末 1 つ・69 回／280 回の付け替え・川崎さんの言葉）、「🔴 job では dev-tools より、ここを優先する」、2 の手順 1〜3 の言い換えと通知先の表のうち SKILL.md と重なる行、`consumer_fenced` の 🔴 段落、3 の「処理はする」の言い換え。どれも退避ファイルに全文が残る。

## 目次

- [触ったファイル](#触ったファイル)
- [完了条件 1・2: 置き換えと退避](#完了条件-12-置き換えと退避)
- [完了条件 3: run-use を参照している箇所](#完了条件-3-run-use-を参照している箇所)
- [完了条件 4: SKILL.md との突き合わせ](#完了条件-4-skillmd-との突き合わせ)
- [完了条件 5: 文脈パックの過不足](#完了条件-5-文脈パックの過不足)
- [上げること](#上げること)

## 触ったファイル

```
job/.claude/skills/manager/sources/orca/
├── run-use.md                              変更  61 行 → 54 行。共通部分を SKILL.md の節への参照に
└── _archive/
    └── 2026-10-24-run-use-before.md        新規  置き換え前の全文（一字一致）
ai-org/.../teams/run-use-thin/
├── worker-1-report.md                      新規  この報告
└── thread.md                               追記
```

[↑ 目次へ](#目次)

## 完了条件 1・2: 置き換えと退避

| 節 | 参照先（SKILL.md の節の見出し名） | 残した job の値・運用 |
|---|---|---|
| 冒頭 | `/dev-tools:orca-multi-agent` 全体 | 1 行目に退避ファイルへのリンク、Run の ID 2 本、`orca` は単独の 1 行（inbox.md へのリンク） |
| 1. `run-use` してよいのは 2 つの場面だけ | 「B. 依頼する（Orca に投げる）」の「`run-use` の使いどころ」 | A／B の呼び名（4 のログが使う）、`依頼元の端末` の行の書式（automation の印）、`echo $ORCA_TERMINAL_HANDLE` で文字列のまま書く |
| 2. 結ばずに見る（各回の最初・「戻りを確認して」） | 「D. 戻りを受ける（`worker_done`）」の入口と分岐 1〜3、「C. 一覧を出す（「何が動いてる？」）」、D の `consumer_fenced` の箇条書き | `--limit 100`、見る範囲（manager は Run 全部／routine-work は自分の起票の Task）、2 時間、automation の依頼は時間を待たず引き取る、引き取った後は inbox.md「取り方」3〜5、〔引き取り〕 |
| 3. 自分が依頼していないものが届いたとき | D の「自分が依頼していない戻りが届いたとき」 | `依頼元の端末` の行が無い起票も含める、1 行の相手は川崎さん、〔誤配〕 |
| 4. ログ（試行の観察） | （SKILL.md に無い） | そのまま。〔引き取り〕の「2 の 3 で」だけ「2 で」に（2 の中の手順番号を外したため） |

確かめ方と結果:

- `diff run-use.md _archive/2026-10-24-run-use-before.md` と `cmp` を、run-use.md を書き換える前に実行 → どちらも差分なし（退避は Bash から書けないので Write で全文を書いた）。
- 書き換えの直前に `cmp` でもう一度、元が他のセッションに変えられていないことを確かめた。
- 新しい run-use.md の 1 行目: `退避: 2026-10-24 に薄くする前の全文は [_archive/2026-10-24-run-use-before.md](...)`。

[↑ 目次へ](#目次)

## 完了条件 3: run-use を参照している箇所

`grep -rn --exclude='.env*' "run-use" /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job` の当たり。サンドボックスの読み取り拒否（`tasks/`・`self-tasks/`・`people/`・`businesses/`・`partners/`・`company/`・`**/_history/`・`.claude/skills/_archive/`）の中は grep が走らず、当たりに出ない。

| ファイル:行 | 何を指しているか | 判定 |
|---|---|---|
| `manager/sources/orca/inbox.md:38` | 「2. 結ばずに見る」 | 直さない。見出しを残したので矛盾なし |
| `manager/sources/orca/inbox.md:39` | 引き取るときだけ `run-use` | 直さない。新しい 2 の「引き取ったあと」と一致 |
| `manager/sources/orca/inbox.md:55` | 続行の前に結び、`依頼元の端末` を併記（「1」） | 直さない。書式は 1 に残した |
| `manager/sources/orca/inbox.md:90` | 2026-10-22 の経緯 | 直さない（履歴） |
| `automation-followup/inbox.md:34-35` | 「2. 結ばずに見る」で決めてから `run-use` → `check --peek` | 直さない。見出しを残した。結んだ後の `--peek` は SKILL.md D でも可 |
| `automation-followup/followup.md:11` | 依頼の直前に結ぶ、書式は「1」 | 直さない。書式は 1 に残した |
| `manager/advance/implement.md:46・58` | 依頼の直前に結ぶ、書式は「1」 | 直さない。同上 |
| `manager/SKILL.md:31` | 段 0 で `run-use` しない、run-use.md・inbox.md へ | 直さない。矛盾なし |
| `manager/automation.md:33` | 2026-10-22〜 毎回のはじめには結ばない（旧文に併記） | 直さない。矛盾なし |
| `manager/_failures/2026-10-22-orca-check-unbound-fenced.md` | 症状・手当（run-use.md へのリンク） | 直さない（記録）。新しい run-use.md の冒頭から経緯としてここを指した |
| `manager/_failures/2026-09-22-orca-fukugou-command.md:8・22` | 複合コマンドの失敗例 | 直さない（記録。run-use.md を指していない） |
| `manager/_failures/README.md:32` | 失敗一覧の行 | 直さない（記録） |
| `manager/sources/orca/run-use-log.md:3` | 「4. ログ」の書き先 | 直さない。4 の見出しを残した |
| `routine-work/README.md:67` | 各回の最初には結ばない、手順は run-use.md | 直さない。矛盾なし |
| `routine-work/baitai/clinic-error-triage/INDEX.md:49` | 依頼の直前に結ぶ、書式は「1」、印 | 直さない。書式は 1 に残した |
| `routine-work/idolone/ando-request-check/INDEX.md:49` | 同上 | 直さない |
| `routine-work/*/*/history.md`（clinic-error-triage 62 件・ando-request-check 59 件・sentry-api-triage 2 件） | 各回の実行記録 | 直さない（履歴。開いていない） |
| `.claude/plans/tmp/2026-10-22-orca-multi-agent-run-use-handover.md` | 引き継ぎの記録 | 直さない（記録） |
| `.claude/.doc-review/47870833-....flag` | doc-review の対象の印 | 直さない（ツールの状態ファイル） |
| `tasks/`・`self-tasks/`・`**/_history/`・`.claude/skills/_archive/` | grep が届かない（読み取り拒否） | 直さない（範囲外／履歴） |
| `tasks/_master/manager.yaml:15`（文脈パックより。読み取り拒否で未確認） | 「毎回のはじめに run-use で結び直す」という古いコメント | 直さない（範囲外。PM へ上げる） |

直したファイルは無い（見出しを変えなかったため）。

[↑ 目次へ](#目次)

## 完了条件 4: SKILL.md との突き合わせ

| 事柄 | 結果 |
|---|---|
| いつ結ぶか（依頼の直前と引き取るときだけ） | 一致。新しい run-use.md は SKILL.md B「`run-use` の使いどころ」を指すだけ |
| 新しい端末は最初に結び直すか | 食い違い→直した。旧 run-use.md の「dev-tools の『新しい端末は最初に run-use』より、ここを優先する」は前提が古く（SKILL.md B は今は「結び直さない」）、外した |
| 結ばずに見る（入口は `inbox`） | 一致。D の入口を指す |
| 未処理の判断（`read` が `0`） | 食い違い→直した。旧は「`read` が `0` が未処理」と言い切り、SKILL.md D は「`read` だけで決めつけず、通知先が自分なら `check` で確かめる」。言い換えを外し D に従う形にした |
| 通知先の分岐 | 食い違い→直した。旧は `coordinator_handle` が `null` の場合が無かった。SKILL.md D の分岐 1〜3 を指す形にして解消 |
| 一覧の範囲（manager は全部／routine-work は自分の Task） | job 固有で SKILL.md に無い |
| `inbox` の件数 | job 固有（`--limit 100`）。SKILL.md C・D の「最後に処理した時刻より前まで届く件数に、足りなければ増やす」と矛盾しない |
| 引き取りまでの時間 | job 固有（2 時間）。SKILL.md D 分岐 3「何時間で引き取るかは親 repo が決める」の値 |
| automation の依頼の引き取り | job 固有で SKILL.md に無い。分岐 3 の時間を automation の依頼では待たない、という job の決め |
| 依頼していない戻り | 一致（届いた側が ack まで処理し 1 行伝える）。job 固有: `依頼元の端末` の行が無い起票も含める・相手は川崎さん・〔誤配〕。旧の 1 行の文例（起票ファイルのパスが無い）は SKILL.md の「パスと見出しを書く」と食い違うので、文例を外し「中身は SKILL.md のとおり」にした |
| `consumer_fenced` | 一致。D の箇条書きを指す（旧の 🔴 段落は同じ内容の言い換えだったので外した） |
| Run の ID | job 固有 |
| 印（`依頼元の端末` の書式） | job 固有。SKILL.md の ticket-template.md「自分の `ORCA_TERMINAL_HANDLE` と、手動か automation か」の具体の書式で、矛盾しない |
| ログ（種別・書式・見直し方） | job 固有で SKILL.md に無い |

[↑ 目次へ](#目次)

## 完了条件 5: 文脈パックの過不足

- パックに無くて自分で探した資料:
  - dev-tools `orca-multi-agent/ticket-template.md` の `依頼元の端末` の行（印の書式が SKILL.md 側と食い違わないかを見るため）。
  - job `manager/sources/orca/inbox.md` の「取り方」0〜5 と「続行の 2 段」（新しい 2 の「引き取ったあと」が指す先と、`「1」` 参照の文脈）。パックの 7 は「grep の当たりの前後だけ」だったが、30〜60 行を読んだ。
  - `automation-followup/followup.md` の「戻りを受ける」の節。
- パックにあって要らなかった資料: 無し。job `CLAUDE.md`「情報を消さない」は会話の冒頭に入っているので、読み直しは要らなかった。
- パックの注意と実際が違った点:
  - ヒントは「退避は `cp`」、パックは「Write」。`.claude/skills/` は Bash から書けないので Write にした（パックが正しい）。
  - `tasks/_master/manager.yaml` はサンドボックスの読み取り拒否で開けず、15 行目のコメントは確かめられていない。grep も `tasks/` などの中には届かない。

[↑ 目次へ](#目次)

## 上げること

- `tasks/_master/manager.yaml` 15 行目の古いコメント（「毎回のはじめに run-use で結び直す」。パックの記述。未確認）は、範囲外なので直していない。PM へ。

[↑ 目次へ](#目次)
