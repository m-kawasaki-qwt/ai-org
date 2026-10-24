# 監査: p11-issue-list

`log/events.log`（122 行）・`log/msgs/` の本文 23 本・`reports/sessions/` 5 本・`teams/issues/thread.md`・charter 2 本・パック 3 本・`orgctl notify-stats` を、`policy.md` に照らして読んだ（印: 本体の review_ng 2 回・宛先不在の中継・材料の途中変更）。

1. **レビュアーが起動される前に作業者が review_request を出し、宛先不在になって、リーダーを経由した中継と出し直しが起きた**
   - 起きたこと: 作業者の 1 回目の review_request は、orgctl が「宛先がいない」で受け付けず、リーダー宛ての report（f4a6be）として出された。リーダーはそれを受けてからレビュアーを assign・起動し（3f02d6）、本文を start で渡した（5f1755）。そのうえで作業者に出し直しを頼み（a43d4f）、作業者が同じ本文を review_request として出し直した（c4eb01）。同じ本文が 3 回流れている。この形は、このプロジェクトが作った一覧の 11 番（p1・p6 で起きたもの）と同じで、p11 でも起きた。リーダーは「中継する手順が決まりに無い」と申告している。
   - 参照元: `log/events.log:43`（f4a6be）・`log/events.log:46`（3f02d6）・`log/events.log:48`（5f1755）・`log/events.log:52`（a43d4f）・`log/events.log:55`（c4eb01）・`log/msgs/ffae2c.md:2`（「review_request を出せば私が起こします」）・`reports/sessions/p11-issue-list__teams__issues__leader-a986a4bb.yaml:124`・`reports/sessions/p11-issue-list__teams__issues__worker-1-937be0ce.yaml:57`・`issues.md:39`

2. **レビューの途中で材料（job の README）が書き足され、本体の review_ng の 1 点目になった**
   - 起きたこと: 材料の 1 つの job の `company/system/ai-org/README.md` に、19:41 に p10 の行が書き足された。作業者が第3版を出したのと同じ時刻（1db04c）。レビュアーが抜き出しから回し直すと行数が合わず build.py が止まり、参照元 3 つが 1 行ずれた。これが本体の 1 回目の review_ng（3cdad7）の指摘 1 になり、作業者が抜き方と作り方を直した。p10 は charter で範囲の外とされている。レビュアーは「材料が動くときに、どの時点の版で数が合うかを見るかは決まりに無い」と申告している。
   - 参照元: `log/events.log:68`（1db04c）・`log/events.log:71`（3cdad7）・`log/msgs/3cdad7.md:6-7`・`charter.md` の「範囲」（p10 を含めない）・`reports/sessions/p11-issue-list__teams__issues__reviewer-65ee1bb5.yaml:50`・`reports/sessions/p11-issue-list__teams__issues__worker-1-937be0ce.yaml:58`

3. **網羅の段の review_ok の宛先が、リーダーの指示とレビュアーの手順とで食い違った**
   - 起きたこと: リーダーはレビュアーへの start で「結果は作業者へ」と指示した（5f1755）。レビュアーの手順では review_ok はリーダー宛て。レビュアーはリーダーの指示に従い、網羅の段の review_ok（f25a86）を作業者へ、本体の review_ok（ddd45d）をリーダーへ出した。そのため、網羅の段の承認はリーダー宛ての 1 行報告に残っていない。
   - 参照元: `log/msgs/5f1755.md:2`・`log/events.log:65`（f25a86）・`log/events.log:83`（ddd45d）・`reports/sessions/p11-issue-list__teams__issues__reviewer-65ee1bb5.yaml:49`

4. **知らせに書かれた `inbox --via notify --ref` が「新しいものは無い」を返した（p11 で 3 つのセッション）**
   - 起きたこと: レビュアー・作業者は、起動直後の `inbox` で start を先に読んだ。あとから届いた知らせの `inbox --via notify --ref` を打つと「新しいものは無い」が返った。監査役（このセッション）でも同じことが起きた。start（bdbf0f）を poll で読んだあと（47e6b0）に届いた知らせの `--ref bdbf0f` が、同じ出力で終了コード 1 になった。notify_recv の行はレビュアー・作業者の分とも残っている。一覧の 5 番は、これを p1〜p3 の件とし、状態を「不明」にしている。
   - 参照元: `reports/sessions/p11-issue-list__teams__issues__reviewer-65ee1bb5.yaml:51`・`reports/sessions/p11-issue-list__teams__issues__worker-1-937be0ce.yaml:60`・`log/events.log:51`（6a6169）・`log/events.log:38`（5fa916）・`log/events.log:120`（bdbf0f）・`log/events.log:122`（47e6b0）・`issues.md:33`

5. **レビュアーの assign で `--occupation reviewer` が雛形の無いことで失敗した**
   - 起きたこと: リーダーがレビュアーを `--occupation reviewer` で assign しようとして、雛形が無く失敗した。職種なしで assign し直して通っている（3f02d6 は `occupation=-`）。
   - 参照元: `reports/sessions/p11-issue-list__teams__issues__leader-a986a4bb.yaml:125`・`log/events.log:46`（3f02d6）
