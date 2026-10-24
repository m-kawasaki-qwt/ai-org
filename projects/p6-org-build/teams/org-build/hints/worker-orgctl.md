# ヒント: worker-orgctl

## リーダーが決めたこと（両方の作業者に同じものを渡している）

- `--persona` は**複数可**。`--pack` と同じく `action="append"` で何度でも。
- ペルソナのファイルは `org/personas/<名前>.md`（ディレクトリではなく 1 ファイル）。名前は `kawasaki`・`end-user`・`sales` の 3 つ。中身は worker-norms が書く。
- 立場・職種を問わず付けられる（主な使い手はレビュアーだが、リーダーや作業者に付けたくなる場面を塞がない）。

## こう作ればいけると思う

- 職種の存在確認（`die(...)`）と同じ作り。存在しないペルソナが 1 つでもあれば、ファイルを何も作らずに止まる。メッセージに「使えるペルソナ: kawasaki, end-user, sales」のように `org/personas/*.md` から拾った一覧を添える（一覧はハードコードしない）。
- システムプロンプトには、職種の後ろに「# ペルソナ: <名前>（この目線で見る）」のような見出しで、指定した順に入れる。複数のときに、どれが誰の目線か読み分けられること。
- `component.json` / events の `assign` の行にもペルソナが残ると、後で誰がどの目線だったか辿れる（既存の行の形は壊さない。足すだけ）。
- `--persona` 無しの assign は、出力（system.md・行）が今までと 1 バイトも変わらないのが理想。確かめるなら、変更前後で同じ assign を打って diff。
- `context.yaml` は `positions`・`occupations` の書き方に合わせて `personas` を足す（どこから読み・いつ入り・誰が選ぶか＝コーディネーターが編成案で）。
- README の `--persona` の説明は文案を worker-norms に渡す（README は触らない）。文案は `<T>/msgs/` ではなく event の本文で直接 worker-norms へ送ってよい。

## 気をつけてほしい点

- 標準ライブラリだけ。本体の orgctl は読むだけ。
- 確かめは scratchpad の仮の repo で。personas がまだ無ければ仮のファイルで確かめてよいが、worktree の `org/personas/` には置かない（worker-norms の担当）。
- 確かめたコマンドと出力の要点を review_request の本文に書く（完了条件 7 の材料になる）。
