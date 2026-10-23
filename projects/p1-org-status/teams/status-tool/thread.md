
## 作業者 第1版
- tools/org_status.py と tools/tests/ を作成。7 テスト OK、本物への実行結果は review_request 本文に記載。
- 最後の報告は「送り手が本人」の行のみ（orgctl の member_state と同じ）。

## レビュアー 第1回
- 判定: review_ok（指摘なし）。完了条件 1〜5 を実行して確認した。
- 申し送り（軽微・直さなくてよい）: 根拠の行番号が今の orgctl とずれている（member_state は l.545-570、cmd_watch は l.572）。根っこ以外のディレクトリを渡すとトレースバックで落ちる（charter の範囲外）。
