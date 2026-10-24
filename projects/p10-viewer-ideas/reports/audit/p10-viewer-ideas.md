# 監査: p10-viewer-ideas

`log/events.log`（全行）・`log/msgs/` の本文 18 件・`reports/sessions/` の 6 件（自己申告の unclear・not_done）・`orgctl notify-stats`・プロジェクトとチームの `charter.md`・`thread.md`・パックを、`policy.md` に照らして見た。

1. **根っこが charter に書いた叩き台 2 の前提が、記録のどこにも無かった**
   - 起きたこと: 叩き台 2 には「古い写しで『動いている』と出て川崎さんが混乱した」という前提が付いていたが、参照元は書かれていなかった。作業者が p1〜p9・プラン・job のフィードバックを探しても見つからず、いま同じことが起きる画面を撮って根拠の代わりにした。このことは作業者・レビュアー・リーダー・PM の 4 段の報告すべてに申し送りとして残り、根っこへ上がった後もそのまま閉じに進んだ。
   - 参照元: `projects/p10-viewer-ideas/charter.md:14`・`reports/sessions/p10-viewer-ideas__teams__viewer-ideas__worker-records-fcb4ed2e.yaml:90`・`e3de66`（先に言っておくこと）・`a9c4b3`（申し送り）・`1bbe73`（申し送り）・`58e395`（申し送り・うまくいかなかったこと）

2. **「画面を作るか」の二択に、画像付きのレポートが当てはまらず、撮って判定する決まりが誰にも掛からなかった**
   - 起きたこと: コーディネーターが「画面なし」と決め、ui-designer の職種だけを付けた。立場の規範（レビュアー・リーダー・PM の「自分で撮って判定する」）は「画面を作るチームでは」に限られ、パックでもレビュアーの screen-probe は対象外とされた。その結果、レビュアーとリーダーは作業者の画像だけで判定し、職種の規範にある 900px・1800px のうち 1800px だけを撮る判断が、作業者・リーダー・PM のそれぞれで上へ上げずに通った。同じ迷いを、コーディネーター・リーダー・レビュアーの 3 人が別々に unclear に書いている。
   - 参照元: `reports/sessions/p10-viewer-ideas__coordinator-b305fe87.yaml:65`・`reports/sessions/p10-viewer-ideas__teams__viewer-ideas__leader-096d31af.yaml:98`・`reports/sessions/p10-viewer-ideas__teams__viewer-ideas__reviewer-kawasaki-cbcd8d26.yaml:68`・`packs/viewer-ideas/reviewer-kawasaki.md:22`・dev-tools `org/positions/reviewer/position.md:16-20`・`org/positions/leader/position.md:10-12`・`org/occupations/ui-designer/occupation.md:30`・`org/common/screen-check.md:15-16`・`e3de66`・`1bbe73`・`58e395`

3. **リーダーが「確かめた」とした出典と、レポートに載った出典が食い違い、確かめていない側でレビューの差し戻しが出た**
   - 起きたこと: リーダーは作業者へ「incident.io timeline を含む 4 件を開いて確認済み」と渡したが、レポートの ③ に使われたのは別ページ（incident.io の roles）だった。そのページで、書いた内容を出典が半分しか裏付けていないとレビュアーが差し戻した。リサーチの作業者は start から約 2 分で report を出し、裏取りはキーワードの有無までで通読していないと自己申告しており、PM もその速さを unclear に挙げたが開き直していない。
   - 参照元: `d13000`・`b91484`・`6bd641`（指摘 3）・`teams/viewer-ideas/thread.md:14`・`teams/viewer-ideas/research.md:57,64`・`report.md:88`・`reports/sessions/p10-viewer-ideas__teams__viewer-ideas__worker-research-94b3e8e6.yaml:66`・`reports/sessions/p10-viewer-ideas__pm-52fa013b.yaml:89`

4. **作業者 2 人の受け渡しが、作業者の規範「他の作業者の成果物を見ない」と食い違った**
   - 起きたこと: 編成で、リサーチの作業者の `research.md` を記録の作業者が取り込む形にした。作業者の規範は並べられた作業者どうしが互いの成果物を見ないとしており、コーディネーターがリーダー経由でパスを渡す形にして unclear に残した。
   - 参照元: `7dab3e`（1 のつなぎ・4 のつなぎ）・`d13000`・`reports/sessions/p10-viewer-ideas__coordinator-b305fe87.yaml:66`・dev-tools `org/positions/worker/` の position の 8 行目

5. **作業者からの done の知らせ 2 件が、宛先の受信として記録されないまま、送り手が片づけられた**
   - 起きたこと: `notify-stats` で、知らせ 9 件のうち 2 件が「届かなかった（出したのに宛先が受けていない）」。レビュアーと記録の作業者の done（Orca で送った）で、リーダーは poll で拾い、受信の行が残らないまま 3〜7 秒後に送り手を teardown した。
   - 参照元: `5cf0ba`・`82ca59`・`bd54c9`・`c423a1`・`815f34`・`6b63a8`・`dc084b`・`f79f63`・`orgctl notify-stats`（2026-10-24 19:4x 時点）
