# worker-1 へのヒント

## 方向

- まず orgctl（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/org/scripts/orgctl.py`）を読む。events.log の 1 行の書き出し方、component.json・member.json を書く所、member.json の `status` が変わる所（assign・launch・teardown など）、`done` の 1 行報告の扱いを押さえる。状態 4 種は「member.json の status」と「最後の 1 行報告の種類」の組み合わせで決まるはず。決め方は自分で推さず、orgctl の値に合わせる。
- 木は component.json の `children`・`members` を根っこからたどるのが素直。ディレクトリを総なめするより、orgctl が書いた構造に従う方が orgctl とずれない。
- 「最後の 1 行報告」は、そのメンバーが出した（送り手が本人の）行で取るのが基本。宛先が本人の行・orgctl が書いた行（user の assign/launch など）をどう扱うかは、出力を見て人が掴みやすい方に決め、理由を報告に書く。
- 中身を作る部分（木と状態を dict で組み立てる）と、出す部分（テキスト・`--json`）を分けると、テストも `--json` も楽になる。
- 「何分前」は今の時刻に依存するので、テストでは今の時刻を渡せるようにしておく。

## 気をつけてほしい点

- 書いてよいのは ai-org の `tools/` だけ。dev-tools・他のメンバーのディレクトリは読むだけ。git は触らない。
- テストの見本は `tools/tests/` の中に持つ。本物の `projects/p1-org-status` をテストの入力にしない（動いている間に中身が変わる）。
- 完了条件 1 の実行結果は、本物の `projects/p1-org-status` に打った結果をそのまま貼る。
- 完了条件 5 の根拠（orgctl のどこを見たか。関数名や行）を 1〜3 行で、review_request の本文に入れておく。
