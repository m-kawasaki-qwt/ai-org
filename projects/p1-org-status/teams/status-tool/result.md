# status-tool チームの結果

完了条件 1〜6 をすべて満たした。作業者 worker-1（sonnet）・レビュアー（opus）とも片づけ済み（指摘 0 回・入れ替え 0 回）。

## 成果物

- `tools/org_status.py`
- `tools/tests/test_org_status.py`
- `tools/tests/fixtures/fx/`（見本の events.log・component.json・member.json）

## 完了条件ごとの結果

1. 本物に打った結果（ai-org 直下で `python3 tools/org_status.py projects/p1-org-status`。作業者・レビュアーの teardown 直後、12:02）:

```
p1-org-status（project・open）
  - pm（pm・opus）[動いている]  最後の報告: report 2026-10-23T11:58:46+09:00（3.6 分前）
  p1-org-status/teams/status-tool（team・open）
    - leader（leader・opus）[動いている]  最後の報告: teardown 2026-10-23T12:02:05+09:00（0.2 分前）
    - worker-1（ディレクトリなし）[片づけ済み]  最後の報告: done 2026-10-23T12:01:02+09:00（1.3 分前）
    - reviewer（ディレクトリなし）[片づけ済み]  最後の報告: done 2026-10-23T12:01:04+09:00（1.3 分前）
```

   teardown の直前（12:02）には worker-1・reviewer が `[終わった]  最後の報告: done ...` と出ていた。作業者の初回実行（11:49）では reviewer が `[未起動]` だった。本物でも 4 種がすべて出るのを見た。
2. `--json` の出力は `python3 -m json.tool` で読める（リーダーが自分で実行）。
3. import は argparse・datetime・json・pathlib・sys・`__future__` だけ。
4. `python3 -m unittest discover -s tools/tests` → 7 テスト OK（リーダーが自分で実行）。未起動・動いている（ack を数えない確認つき）・終わった・片づけ済み（status closed と、member ディレクトリ削除の 2 通り）を各テスト。
5. 合わせた根拠: 状態は orgctl の `member_state`（closed → session_id なし → 本人の最後の非ノイズ報告が done → それ以外）と、`cmd_watch` の「片づけ済み（ディレクトリなし）」の扱い。1 行報告の形は `append_event`/`read_events` の 6 欄で、`NOISE_KINDS`（ack・notify_sent・notify_recv）は数えない。木は component.json の `members`・`children` をたどる。orgctl の「止まっている?／ループ?」は 4 種に無いため「動いている」にまとめた。
6. レビュアーの review_ok（c47efc）が出ている。

## 申し送り（ツール）

- 根っこ以外（例: `teams/status-tool`）を渡すとトレースバックで落ちる（charter は根っこを渡す前提なので範囲外）。
- 「最後の報告」は本人が送った行だけで、受けた start は出ない（member_state と同じ）。leader の最後の報告に teardown のような orgctl の操作の行が出る。

## 試走で分かったこと（連絡・決まり）

- `wait --cc` が、作業者 → レビュアーの review_request（4d68b5、11:49）を拾わず、9 分の時間切れで戻った。このせいでレビュアーの起動が約 10 分遅れ、PM の確認で気づいた。
- 作業者がレビュアーへ review_request を出した時点でレビュアーにタブが無く、知らせを出せなかった（作業者の申告）。「レビュアーは最初の review_request の後に起こす」の決まりと合わせると、リーダーが cc を拾えないと止まる。
- `orca terminal send` は毎回「Enter が飲まれたかもしれない」と警告を出したが、相手はすべて受け取っていた（events.log の notify_recv で確認）。
- 2 件の知らせ（done 2 件）がほぼ同時に来ると、最初の `inbox --via notify --ref` で両方読まれ、2 件目の `--ref` は「新しいものは無い」になる。2 件目の notify での受信記録が残らない可能性がある（未確認）。
- 見本の id は根っこの親ディレクトリ基準（`rel_id`）で、見本のディレクトリ名と揃える必要がある。決まりに書かれていない（作業者の申告）。
