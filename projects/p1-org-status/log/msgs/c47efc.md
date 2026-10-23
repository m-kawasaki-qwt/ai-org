<!-- p1-org-status/teams/status-tool/reviewer → p1-org-status/teams/status-tool/leader review_ok 2026-10-23T11:59:55+09:00 -->
作業者の review_request（4d68b5）を、charter の完了条件 1〜5 に照らして確認した。指摘なしで承認する。

確かめたこと（いずれも自分で実行した）
1. `python3 tools/org_status.py projects/p1-org-status` → exit 0。木（プロジェクト → チーム → メンバー）、種類・時刻・何分前、状態が出る。本物の log では、作業者が実行した時点で「未起動」だったレビュアーが、起動後は「動いている」に変わることも確認した。
2. `--json` の出力は `python3 -m json.tool` で読める。中身はテキストと同じ木（同じ dict を出している）。
3. import は argparse・datetime・json・pathlib・sys・__future__ だけ（標準ライブラリのみ）。
4. `python3 -m unittest discover -s tools/tests` → 7 テスト OK。見本は tools/tests/fixtures/fx/ にある。状態 4 種はそれぞれテストがある（片づけ済みは status closed と member ディレクトリ削除の 2 通り。ack を数えないことのテストもある）。
5. orgctl と突き合わせた: 1 行報告の形・分け方は read_events/append_event と同じ。状態の順（closed → session_id なし → 本人の最後の非ノイズ報告が done → それ以外）は member_state と同じ。member.json が無いときの「片づけ済み」は、teardown（--keep なし）が member ディレクトリを rmtree したあとも component.json の members に名前が残る点、cmd_watch の扱いと合っている。orgctl は変更されていない。

申し送り（軽微。直さなくてよい）
- 報告に書かれた orgctl の行番号が今のファイルとずれている（member_state は l.545-570、cmd_watch は l.572）。中身の対応は正しい。
- 根っこ以外（例: teams/status-tool）を渡すと、パスがずれてトレースバックで落ちる。charter は根っこを渡す前提なので範囲外。
- 「最後の報告」は本人が送った行だけで、受けた start は出ない（orgctl の member_state と同じ）。作業者の判断どおりで問題ない。
