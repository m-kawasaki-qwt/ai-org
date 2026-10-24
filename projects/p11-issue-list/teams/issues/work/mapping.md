# 対応表（scripts/build.py が書いた。手で直さない）

抜き出し 431 行の行き先。件に入れた 281 行・入れなかった 150 行。件の番号は `issues.md` の番号。

## 入れなかった理由ごとの行数

| 理由 | 行数 |
|---|---|
| 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） | 77 |
| 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） | 28 |
| 監査役の照合（p1・p2 の件が p3 で繰り返していない）。直ったかの照合の根拠に使った | 1 |
| 直し方の選択肢（監査役の「好みで決まる点」。直し方は書かない） | 4 |
| これからの段取り・マージ待ちの申し送り（起きたことではない） | 12 |
| 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） | 17 |
| 本人が影響なしと書いた環境の挙動（問題として上げていない） | 4 |
| 作業者の打ち間違いを directory-guard が止めたもの（本人が実害なしと申告） | 3 |
| 作業中で待っただけ（p6 の PM が止まりではないと書いている。job の控えの p6 の記述は「全員が wait に入って止まり…」の起きたことに書いた） | 1 |
| 同じ本文の中で前の回の指摘・警告を言い直したもの | 1 |
| 閉じたときは監査役がいなかったが、記録は p3 の監査役が照らした（p3-org-visibility/charter.md:18・log/msgs/95df09.md:30） | 2 |

## 行ごと

| id | 参照元 | 行き先 |
|---|---|---|
| E001 | `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:70` | 36. リーダーの `wait --cc` が、作業者 → 未起動のレビュアーの review_request を拾わず、約 10 分止まった |
| E002 | `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:71` | 11. レビュアーは最初の review_request の後に起こす順番なので、作業者が review_request を知らせる相手（タブ）が無い |
| E003 | `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:72` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E004 | `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:73` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E005 | `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:74` | 68. PM がリーダーへ催促・確認するための種類が無く、report で代用した |
| E006 | `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:75` | 54. PM の入れ替えで、前の PM の状況が新しい PM に引き継がれなかった |
| E007 | `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:76` | 17. 根っこ（user）にはタブが無く、user 宛ての report・wrap_up に Orca の知らせが出ない |
| E008 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:66` | 36. リーダーの `wait --cc` が、作業者 → 未起動のレビュアーの review_request を拾わず、約 10 分止まった |
| E009 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:67` | 11. レビュアーは最初の review_request の後に起こす順番なので、作業者が review_request を知らせる相手（タブ）が無い |
| E010 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:68` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E011 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:69` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E012 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:70` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E013 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__reviewer.yaml:50` | 11. レビュアーは最初の review_request の後に起こす順番なので、作業者が review_request を知らせる相手（タブ）が無い |
| E014 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__reviewer.yaml:51` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E015 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__reviewer.yaml:52` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E016 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__worker-1.yaml:56` | 40. 見本の id が根っこの親ディレクトリ基準（rel_id）で、見本のディレクトリ名を揃える必要が決まりに書かれていない |
| E017 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__worker-1.yaml:57` | 入れない: 本人が影響なしと書いた環境の挙動（問題として上げていない） |
| E018 | `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__worker-1.yaml:58` | 11. レビュアーは最初の review_request の後に起こす順番なので、作業者が review_request を知らせる相手（タブ）が無い |
| E019 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__pm-0775601b.yaml:67` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E020 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__pm-0775601b.yaml:68` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E021 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__pm-0775601b.yaml:69` | 29. レビュアーの承認のあとにリーダーが rework を出したとき、レビュアーがもう一度見るかが決まりに無かった |
| E022 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__pm-0775601b.yaml:70` | 17. 根っこ（user）にはタブが無く、user 宛ての report・wrap_up に Orca の知らせが出ない |
| E023 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__leader-70bafeda.yaml:65` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E024 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__leader-70bafeda.yaml:66` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E025 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__leader-70bafeda.yaml:67` | 29. レビュアーの承認のあとにリーダーが rework を出したとき、レビュアーがもう一度見るかが決まりに無かった |
| E026 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__reviewer-f7de4d8b.yaml:58` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E027 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__reviewer-f7de4d8b.yaml:59` | 29. レビュアーの承認のあとにリーダーが rework を出したとき、レビュアーがもう一度見るかが決まりに無かった |
| E028 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__reviewer-f7de4d8b.yaml:60` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E029 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__worker-1-56151c49.yaml:56` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E030 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__worker-1-56151c49.yaml:58` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E031 | `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__worker-1-56151c49.yaml:59` | 入れない: 作業者の打ち間違いを directory-guard が止めたもの（本人が実害なしと申告） |
| E032 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__auditor-074c4759.yaml:50` | 64. 監査役の見るものに、セッション報告の machine 欄（files_changed_in_window など）の正しさが入るかがはっきりしない |
| E033 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__pm-8512c441.yaml:83` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E034 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__pm-8512c441.yaml:84` | 4. orgctl のコマンドを変数（O="python3 …"）に入れて打つと、zsh で 1 語扱いになり失敗する |
| E035 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__pm-8512c441.yaml:85` | 62. PM の wrap_up に、PM が自分で確かめたことが書かれていなかった |
| E036 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__pm-8512c441.yaml:86` | 61. 起こした直後の相手にも「wait で待っているので知らせは出さない」と出た |
| E037 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__leader-4d653d8e.yaml:76` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E038 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__leader-4d653d8e.yaml:77` | 63. リーダーの残る不明点がセッション報告の unclear にだけあり、PM への report に無かった |
| E039 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__reviewer-10b48465.yaml:62` | 51. 承認のときにも thread.md に追記するかが決まりに無かった |
| E040 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__reviewer-10b48465.yaml:63` | 66. tools/org_timeline.py に --help が無く、打つとディレクトリとして扱われて例外で止まる |
| E041 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__worker-1-7f90e6d2.yaml:64` | 52. 並行する別チームの成果物を、できる前に前提にして書いた |
| E042 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__worker-1-7f90e6d2.yaml:66` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E043 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__leader-e54a1b8a.yaml:74` | 入れない: 本人が影響なしと書いた環境の挙動（問題として上げていない） |
| E044 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__reviewer-8d87b16a.yaml:63` | 51. 承認のときにも thread.md に追記するかが決まりに無かった |
| E045 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__reviewer-8d87b16a.yaml:64` | 6. 画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった |
| E046 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__worker-1-969f0ba1.yaml:70` | 67. Claude in Chrome の拡張が繋がらず、実ブラウザで確かめられなかった |
| E047 | `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__worker-1-969f0ba1.yaml:72` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E048 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__coordinator-run-use-thin-ad0d46dd.yaml:58` | 7. 規範どおり `orgctl digest <親のコンポーネント>` を id で打つと「根っこのプロジェクトが無い」で失敗した |
| E049 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__coordinator-run-use-thin-ad0d46dd.yaml:59` | 59. 台帳の deny（**/_archive/）が、案件の成果物の置き場と重なった |
| E050 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__coordinator-run-use-thin-ad0d46dd.yaml:60` | 20. パックの deny は Read の拒否だけで、grep（Bash）では見え、glob でしか書けない |
| E051 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__coordinator-run-use-thin-ad0d46dd.yaml:61` | 9. 起動した直後の `inbox` に、上からの start がまだ無い |
| E052 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__pm-7fcade93.yaml:71` | 13. charter・ヒント・パックに書かれた前提が実物と違った（無いファイル・食い違う指示・件数） |
| E053 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__pm-7fcade93.yaml:72` | 60. サンドボックスの中で Bash のパイプ（git show | diff）が Operation not permitted になる |
| E054 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__pm-7fcade93.yaml:73` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E055 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__leader-8e4fdd93.yaml:63` | 13. charter・ヒント・パックに書かれた前提が実物と違った（無いファイル・食い違う指示・件数） |
| E056 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__reviewer-05ac7e08.yaml:49` | 14. 読み取り拒否の場所に grep・stat が届かず、洗い出し・確かめが言い切れない |
| E057 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__worker-1-b93bc6f4.yaml:60` | 13. charter・ヒント・パックに書かれた前提が実物と違った（無いファイル・食い違う指示・件数） |
| E058 | `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__worker-1-b93bc6f4.yaml:61` | 14. 読み取り拒否の場所に grep・stat が届かず、洗い出し・確かめが言い切れない |
| E059 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__coordinator-viewer-2d6b3d7c.yaml:60` | 39. 文脈の台帳（context.yaml）に、題材が組織そのもの（ai-org・dev-tools の org）のときに読む先が無い |
| E060 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__coordinator-viewer-2d6b3d7c.yaml:61` | 9. 起動した直後の `inbox` に、上からの start がまだ無い |
| E061 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__pm-92edb217.yaml:81` | 4. orgctl のコマンドを変数（O="python3 …"）に入れて打つと、zsh で 1 語扱いになり失敗する |
| E062 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__pm-92edb217.yaml:82` | 19. PM の `wait` が配下のやりとり（cc）でも戻り、自分宛てが来るまで打ち直した |
| E063 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__leader-6f1c1b6b.yaml:77` | 13. charter・ヒント・パックに書かれた前提が実物と違った（無いファイル・食い違う指示・件数） |
| E064 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__leader-6f1c1b6b.yaml:78` | 28. 作業者が手書きデータの版で先に review_request を出し、実物の版と 2 通になって往復が 1 回増えた |
| E065 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__leader-6f1c1b6b.yaml:79` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E066 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__reviewer-11df580d.yaml:61` | 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった |
| E067 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__reviewer-11df580d.yaml:63` | 28. 作業者が手書きデータの版で先に review_request を出し、実物の版と 2 通になって往復が 1 回増えた |
| E068 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__reviewer-11df580d.yaml:64` | 8. レビュアーの承認のあとで、リーダーが目的に届いていない点を見つけて rework を出した |
| E069 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__reviewer-11df580d.yaml:65` | 23. ~/.npm のキャッシュの権限が壊れていて npm install が失敗する |
| E070 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:70` | 3. 作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る |
| E071 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:72` | 13. charter・ヒント・パックに書かれた前提が実物と違った（無いファイル・食い違う指示・件数） |
| E072 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:73` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E073 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:74` | 58. zsh で `echo =====` と打つと「==== not found」で失敗する |
| E074 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:75` | 12. directory-guard が、引数の `/` を含む文字列や /dev/stdin を許可外の読み書きとして止める |
| E075 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:76` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E076 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml:89` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E077 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml:91` | 23. ~/.npm のキャッシュの権限が壊れていて npm install が失敗する |
| E078 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml:92` | 6. 画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった |
| E079 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml:93` | 12. directory-guard が、引数の `/` を含む文字列や /dev/stdin を許可外の読み書きとして止める |
| E080 | `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml:94` | 28. 作業者が手書きデータの版で先に review_request を出し、実物の版と 2 通になって往復が 1 回増えた |
| E081 | `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-org-build-b422e51c.yaml:66` | 9. 起動した直後の `inbox` に、上からの start がまだ無い |
| E082 | `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-org-build-b422e51c.yaml:67` | 7. 規範どおり `orgctl digest <親のコンポーネント>` を id で打つと「根っこのプロジェクトが無い」で失敗した |
| E083 | `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-org-build-b422e51c.yaml:68` | 20. パックの deny は Read の拒否だけで、grep（Bash）では見え、glob でしか書けない |
| E084 | `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-org-build-b422e51c.yaml:69` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E085 | `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-uiux-research-057eafed.yaml:64` | 7. 規範どおり `orgctl digest <親のコンポーネント>` を id で打つと「根っこのプロジェクトが無い」で失敗した |
| E086 | `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-uiux-research-057eafed.yaml:65` | 9. 起動した直後の `inbox` に、上からの start がまだ無い |
| E087 | `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-uiux-research-057eafed.yaml:66` | 47. 調べもの・出典の裏取りが本業の職種が台帳に無く、リーダーの職種なしが許されるかも書かれていない |
| E088 | `projects/p6-org-build/reports/sessions/p6-org-build__pm-16bc79bc.yaml:86` | 19. PM の `wait` が配下のやりとり（cc）でも戻り、自分宛てが来るまで打ち直した |
| E089 | `projects/p6-org-build/reports/sessions/p6-org-build__pm-16bc79bc.yaml:87` | 7. 規範どおり `orgctl digest <親のコンポーネント>` を id で打つと「根っこのプロジェクトが無い」で失敗した |
| E090 | `projects/p6-org-build/reports/sessions/p6-org-build__pm-16bc79bc.yaml:88` | 47. 調べもの・出典の裏取りが本業の職種が台帳に無く、リーダーの職種なしが許されるかも書かれていない |
| E091 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__leader-15cbc271.yaml:72` | 12. directory-guard が、引数の `/` を含む文字列や /dev/stdin を許可外の読み書きとして止める |
| E092 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__leader-15cbc271.yaml:73` | 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった |
| E093 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__reviewer-b8082b46.yaml:73` | 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった |
| E094 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__reviewer-b8082b46.yaml:75` | 48. assign でペルソナを重ねて指定すると、黙って 1 つにまとめる（README に書かれていない） |
| E095 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-norms-7bbd0aab.yaml:91` | 57. 別の作業者へ送った文案が、相手の成果物に入ったか確かめられなかった |
| E096 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-norms-7bbd0aab.yaml:93` | 49. 規範から org/ の資料を辿る書き方が「orgctl のパスから scripts/orgctl.py を外した所」になった |
| E097 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-norms-7bbd0aab.yaml:94` | 6. 画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった |
| E098 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-norms-7bbd0aab.yaml:95` | 3. 作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る |
| E099 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-orgctl-34b67ded.yaml:80` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E100 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__leader-00fa4e8f.yaml:65` | 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった |
| E101 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__leader-00fa4e8f.yaml:66` | 入れない: 本人が影響なしと書いた環境の挙動（問題として上げていない） |
| E102 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__leader-00fa4e8f.yaml:67` | 4. orgctl のコマンドを変数（O="python3 …"）に入れて打つと、zsh で 1 語扱いになり失敗する |
| E103 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__reviewer-77f133a5.yaml:55` | 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった |
| E104 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__reviewer-77f133a5.yaml:56` | 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった |
| E105 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__reviewer-77f133a5.yaml:58` | 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった |
| E106 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__worker-1-833d6b72.yaml:70` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E107 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__worker-1-833d6b72.yaml:71` | 50. JavaScript で描くページを WebFetch で読めず、出典の裏取りがほかの道頼みになった |
| E108 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__worker-1-833d6b72.yaml:73` | 11. レビュアーは最初の review_request の後に起こす順番なので、作業者が review_request を知らせる相手（タブ）が無い |
| E109 | `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__worker-1-833d6b72.yaml:74` | 50. JavaScript で描くページを WebFetch で読めず、出典の裏取りがほかの道頼みになった |
| E110 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:65` | 15. 組織を直すプロジェクトの最中は、動いている本体の規範・orgctl が直す前のままで、上書きや使い分けが要った |
| E111 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:66` | 43. 文脈パックが charter より先に書かれ、まだ無い charter を指した |
| E112 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:67` | 44. コーディネーターと PM の往復で使う event の種類が決まっていなかった |
| E113 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:68` | 34. コーディネーターの終わり方と、返しに書くもの（実現できる理由・崩れる前提）が規範に無かった |
| E114 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:69` | 7. 規範どおり `orgctl digest <親のコンポーネント>` を id で打つと「根っこのプロジェクトが無い」で失敗した |
| E115 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:70` | 45. orgctl new がチームにも packs/ を作り、新しい流れでは空のまま残った |
| E116 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:71` | 34. コーディネーターの終わり方と、返しに書くもの（実現できる理由・崩れる前提）が規範に無かった |
| E117 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__pm-1c125b2e.yaml:72` | 15. 組織を直すプロジェクトの最中は、動いている本体の規範・orgctl が直す前のままで、上書きや使い分けが要った |
| E118 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__pm-1c125b2e.yaml:73` | 33. 往復の「合意」と「返し」が同じ report の種類で、種類だけでは見分けられない |
| E119 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__pm-1c125b2e.yaml:74` | 18. 同じ立場が複数いるときの名前（コーディネーター・パックのファイル名）の付け方が決まりに無い |
| E120 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__teams__coordinator-flow__leader-e917435e.yaml:67` | 33. 往復の「合意」と「返し」が同じ report の種類で、種類だけでは見分けられない |
| E121 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__teams__coordinator-flow__worker-1-32df2698.yaml:73` | 3. 作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る |
| E122 | `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__teams__coordinator-flow__worker-1-32df2698.yaml:74` | 35. パックの deny に $TMPDIR のパスを書くと /tmp のまま入り、ヒントの deny は /private/tmp になる |
| E123 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__coordinator-087f6e79.yaml:68` | 18. 同じ立場が複数いるときの名前（コーディネーター・パックのファイル名）の付け方が決まりに無い |
| E124 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__coordinator-087f6e79.yaml:69` | 32. 指摘の回数（3 回まで）を、design.md の段と画面の段で通算するかが決まりに無い |
| E125 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__pm-129ad682.yaml:415` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E126 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__pm-129ad682.yaml:416` | 56. プロジェクトの charter の完了条件が記録と食い違うとき、PM が子の charter で補ってよいかがはっきりしない |
| E127 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml:406` | 24. 全員が wait に入って止まり、見張りは全員待ちとしては出さなかった（待っている PM を「ループ?」として出した） |
| E128 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml:407` | 25. 画面を撮るとき、作業者の待ち受けを使うのか自分で立てるのかが screen-check.md に無い（ビルドし直すと 404） |
| E129 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml:408` | 26. screen-probe が本文の Markdown の表も折り返しの候補に数え、印を押して出る引き出しを撮れない |
| E130 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml:409` | 27. チェックリストの設計の段（B）に「押せる大きさと間隔」が無く、設計で通した配置が画面で押せない印になった |
| E131 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-export-baf05c27.yaml:388` | 38. `orgctl export --check` を `--out` と一緒に打つと、書き出し直してから検査する |
| E132 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-kawasaki-d30b4812.yaml:396` | 22. 実データに判断待ち・止まっているものが無く、その見た目を写しでしか確かめられない |
| E133 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-kawasaki-d30b4812.yaml:398` | 32. 指摘の回数（3 回まで）を、design.md の段と画面の段で通算するかが決まりに無い |
| E134 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-kawasaki-d30b4812.yaml:399` | 27. チェックリストの設計の段（B）に「押せる大きさと間隔」が無く、設計で通した配置が画面で押せない印になった |
| E135 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-kawasaki-d30b4812.yaml:400` | 25. 画面を撮るとき、作業者の待ち受けを使うのか自分で立てるのかが screen-check.md に無い（ビルドし直すと 404） |
| E136 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-export-fff11e32.yaml:395` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E137 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-export-fff11e32.yaml:397` | 3. 作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る |
| E138 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-export-fff11e32.yaml:398` | 14. 読み取り拒否の場所に grep・stat が届かず、洗い出し・確かめが言い切れない |
| E139 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:432` | 3. 作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る |
| E140 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:434` | 25. 画面を撮るとき、作業者の待ち受けを使うのか自分で立てるのかが screen-check.md に無い（ビルドし直すと 404） |
| E141 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:435` | 26. screen-probe が本文の Markdown の表も折り返しの候補に数え、印を押して出る引き出しを撮れない |
| E142 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:436` | 26. screen-probe が本文の Markdown の表も折り返しの候補に数え、印を押して出る引き出しを撮れない |
| E143 | `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:437` | 22. 実データに判断待ち・止まっているものが無く、その見た目を写しでしか確かめられない |
| E144 | `projects/p9-org-watch/reports/sessions/p9-org-watch__auditor-272c70db.yaml:48` | 42. 監査役の参照元の形（1 行に複数・バッククォート付き）が、export の refs で 1 件に潰れる |
| E145 | `projects/p9-org-watch/reports/sessions/p9-org-watch__coordinator-37d1062a.yaml:63` | 15. 組織を直すプロジェクトの最中は、動いている本体の規範・orgctl が直す前のままで、上書きや使い分けが要った |
| E146 | `projects/p9-org-watch/reports/sessions/p9-org-watch__coordinator-37d1062a.yaml:64` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E147 | `projects/p9-org-watch/reports/sessions/p9-org-watch__coordinator-37d1062a.yaml:65` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E148 | `projects/p9-org-watch/reports/sessions/p9-org-watch__pm-f743150d.yaml:68` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E149 | `projects/p9-org-watch/reports/sessions/p9-org-watch__pm-f743150d.yaml:70` | 41. p9 のチームの完了条件で、閉じる側を PM と書いていた（根っこなので閉じるのは user） |
| E150 | `projects/p9-org-watch/reports/sessions/p9-org-watch__pm-f743150d.yaml:71` | 55. PM が検収で、本物の ai-org/projects に書き込みのある patrol --dry を打った |
| E151 | `projects/p9-org-watch/reports/sessions/p9-org-watch__pm-f743150d.yaml:72` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E152 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__leader-36cfe0d2.yaml:66` | 21. 受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった |
| E153 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__leader-36cfe0d2.yaml:67` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E154 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__reviewer-512bbb7a.yaml:57` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E155 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__reviewer-512bbb7a.yaml:59` | 21. 受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった |
| E156 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__reviewer-512bbb7a.yaml:60` | 4. orgctl のコマンドを変数（O="python3 …"）に入れて打つと、zsh で 1 語扱いになり失敗する |
| E157 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-audit-6bc5c166.yaml:58` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E158 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-audit-6bc5c166.yaml:59` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E159 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-audit-6bc5c166.yaml:61` | 30. 「閉じる並び」を review_request に入れるのか最終報告に入れるのかを、作業者がパックから読み取れなかった |
| E160 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-watch-f06de01a.yaml:67` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E161 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-watch-f06de01a.yaml:69` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E162 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-watch-f06de01a.yaml:70` | 31. 同じファイル（orgctl.py）を 2 人で同時に直し、Edit の衝突と受け持ちの外への手入れが起きた |
| E163 | `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-watch-f06de01a.yaml:71` | 31. 同じファイル（orgctl.py）を 2 人で同時に直し、Edit の衝突と受け持ちの外への手入れが起きた |
| E164 | `projects/p1-org-status/log/msgs/803ffb.md:45` | 36. リーダーの `wait --cc` が、作業者 → 未起動のレビュアーの review_request を拾わず、約 10 分止まった |
| E165 | `projects/p1-org-status/log/msgs/803ffb.md:46` | 11. レビュアーは最初の review_request の後に起こす順番なので、作業者が review_request を知らせる相手（タブ）が無い |
| E166 | `projects/p1-org-status/log/msgs/803ffb.md:47` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E167 | `projects/p1-org-status/log/msgs/803ffb.md:48` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E168 | `projects/p1-org-status/log/msgs/803ffb.md:49` | 54. PM の入れ替えで、前の PM の状況が新しい PM に引き継がれなかった |
| E169 | `projects/p1-org-status/log/msgs/803ffb.md:50` | 40. 見本の id が根っこの親ディレクトリ基準（rel_id）で、見本のディレクトリ名を揃える必要が決まりに書かれていない |
| E170 | `projects/p1-org-status/log/msgs/c47efc.md:12` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E171 | `projects/p1-org-status/log/msgs/c47efc.md:13` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E172 | `projects/p1-org-status/log/msgs/c47efc.md:14` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E173 | `projects/p1-org-status/log/msgs/d9ba25.md:34` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E174 | `projects/p1-org-status/log/msgs/d9ba25.md:35` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E175 | `projects/p1-org-status/log/msgs/d9ba25.md:39` | 36. リーダーの `wait --cc` が、作業者 → 未起動のレビュアーの review_request を拾わず、約 10 分止まった |
| E176 | `projects/p1-org-status/log/msgs/d9ba25.md:40` | 11. レビュアーは最初の review_request の後に起こす順番なので、作業者が review_request を知らせる相手（タブ）が無い |
| E177 | `projects/p1-org-status/log/msgs/d9ba25.md:41` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E178 | `projects/p1-org-status/log/msgs/d9ba25.md:42` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E179 | `projects/p1-org-status/log/msgs/d9ba25.md:43` | 40. 見本の id が根っこの親ディレクトリ基準（rel_id）で、見本のディレクトリ名を揃える必要が決まりに書かれていない |
| E180 | `projects/p2-orca-run-use/log/msgs/04802d.md:4` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E181 | `projects/p2-orca-run-use/log/msgs/04802d.md:6` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E182 | `projects/p2-orca-run-use/log/msgs/04802d.md:8` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E183 | `projects/p2-orca-run-use/log/msgs/04802d.md:11` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E184 | `projects/p2-orca-run-use/log/msgs/04802d.md:14` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E185 | `projects/p2-orca-run-use/log/msgs/04802d.md:17` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E186 | `projects/p2-orca-run-use/log/msgs/04802d.md:21` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E187 | `projects/p2-orca-run-use/log/msgs/04802d.md:22` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E188 | `projects/p2-orca-run-use/log/msgs/04802d.md:23` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E189 | `projects/p2-orca-run-use/log/msgs/04802d.md:24` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E190 | `projects/p2-orca-run-use/log/msgs/04802d.md:25` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E191 | `projects/p2-orca-run-use/log/msgs/1f7fb5.md:66` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E192 | `projects/p2-orca-run-use/log/msgs/1f7fb5.md:67` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E193 | `projects/p2-orca-run-use/log/msgs/1f7fb5.md:71` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E194 | `projects/p2-orca-run-use/log/msgs/1f7fb5.md:72` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E195 | `projects/p2-orca-run-use/log/msgs/1f7fb5.md:73` | 29. レビュアーの承認のあとにリーダーが rework を出したとき、レビュアーがもう一度見るかが決まりに無かった |
| E196 | `projects/p2-orca-run-use/log/msgs/1f7fb5.md:74` | 入れない: 作業者の打ち間違いを directory-guard が止めたもの（本人が実害なしと申告） |
| E197 | `projects/p2-orca-run-use/log/msgs/63b813.md:2` | 8. レビュアーの承認のあとで、リーダーが目的に届いていない点を見つけて rework を出した |
| E198 | `projects/p2-orca-run-use/log/msgs/7ad811.md:46` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E199 | `projects/p2-orca-run-use/log/msgs/7ad811.md:50` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E200 | `projects/p2-orca-run-use/log/msgs/7ad811.md:51` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E201 | `projects/p2-orca-run-use/log/msgs/7ad811.md:55` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E202 | `projects/p2-orca-run-use/log/msgs/7ad811.md:56` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E203 | `projects/p2-orca-run-use/log/msgs/7ad811.md:57` | 29. レビュアーの承認のあとにリーダーが rework を出したとき、レビュアーがもう一度見るかが決まりに無かった |
| E204 | `projects/p2-orca-run-use/log/msgs/7ad811.md:58` | 入れない: 作業者の打ち間違いを directory-guard が止めたもの（本人が実害なしと申告） |
| E205 | `projects/p2-orca-run-use/log/msgs/7ad811.md:59` | 17. 根っこ（user）にはタブが無く、user 宛ての report・wrap_up に Orca の知らせが出ない |
| E206 | `projects/p2-orca-run-use/log/msgs/91f052.md:11` | 入れない: 同じ本文の中で前の回の指摘・警告を言い直したもの |
| E207 | `projects/p2-orca-run-use/log/msgs/a9a0a2.md:30` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E208 | `projects/p2-orca-run-use/log/msgs/f863c1.md:17` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E209 | `projects/p2-orca-run-use/log/msgs/f863c1.md:18` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E210 | `projects/p2-orca-run-use/log/msgs/f863c1.md:19` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E211 | `projects/p3-org-visibility/log/msgs/258cd4.md:21` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E212 | `projects/p3-org-visibility/log/msgs/258cd4.md:22` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E213 | `projects/p3-org-visibility/log/msgs/258cd4.md:23` | 52. 並行する別チームの成果物を、できる前に前提にして書いた |
| E214 | `projects/p3-org-visibility/log/msgs/6acb52.md:2` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E215 | `projects/p3-org-visibility/log/msgs/6acb52.md:4` | 16. 1 行報告を読む道具が、数えるための行（NOISE_KINDS）を自前で持ち、orgctl とずれる |
| E216 | `projects/p3-org-visibility/log/msgs/8723ce.md:2` | 8. レビュアーの承認のあとで、リーダーが目的に届いていない点を見つけて rework を出した |
| E217 | `projects/p3-org-visibility/log/msgs/8cffd1.md:21` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E218 | `projects/p3-org-visibility/log/msgs/8cffd1.md:22` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E219 | `projects/p3-org-visibility/log/msgs/95df09.md:8` | 62. PM の wrap_up に、PM が自分で確かめたことが書かれていなかった |
| E220 | `projects/p3-org-visibility/log/msgs/95df09.md:12` | 63. リーダーの残る不明点がセッション報告の unclear にだけあり、PM への report に無かった |
| E221 | `projects/p3-org-visibility/log/msgs/95df09.md:16` | 51. 承認のときにも thread.md に追記するかが決まりに無かった |
| E222 | `projects/p3-org-visibility/log/msgs/95df09.md:20` | 16. 1 行報告を読む道具が、数えるための行（NOISE_KINDS）を自前で持ち、orgctl とずれる |
| E223 | `projects/p3-org-visibility/log/msgs/95df09.md:24` | 65. teardown の files_changed_in_window に、並行チームの変更が混じる |
| E224 | `projects/p3-org-visibility/log/msgs/95df09.md:30` | 入れない: 監査役の照合（p1・p2 の件が p3 で繰り返していない）。直ったかの照合の根拠に使った |
| E225 | `projects/p3-org-visibility/log/msgs/95df09.md:31` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E226 | `projects/p3-org-visibility/log/msgs/95df09.md:32` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E227 | `projects/p3-org-visibility/log/msgs/95df09.md:33` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E228 | `projects/p3-org-visibility/log/msgs/95df09.md:34` | 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる |
| E229 | `projects/p3-org-visibility/log/msgs/95df09.md:38` | 入れない: 直し方の選択肢（監査役の「好みで決まる点」。直し方は書かない） |
| E230 | `projects/p3-org-visibility/log/msgs/95df09.md:39` | 入れない: 直し方の選択肢（監査役の「好みで決まる点」。直し方は書かない） |
| E231 | `projects/p3-org-visibility/log/msgs/95df09.md:40` | 入れない: 直し方の選択肢（監査役の「好みで決まる点」。直し方は書かない） |
| E232 | `projects/p3-org-visibility/log/msgs/95df09.md:41` | 入れない: 直し方の選択肢（監査役の「好みで決まる点」。直し方は書かない） |
| E233 | `projects/p3-org-visibility/log/msgs/b589bb.md:48` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E234 | `projects/p3-org-visibility/log/msgs/b589bb.md:49` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E235 | `projects/p3-org-visibility/log/msgs/b93761.md:34` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E236 | `projects/p3-org-visibility/log/msgs/b93761.md:35` | 4. orgctl のコマンドを変数（O="python3 …"）に入れて打つと、zsh で 1 語扱いになり失敗する |
| E237 | `projects/p3-org-visibility/log/msgs/b93761.md:36` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E238 | `projects/p3-org-visibility/log/msgs/c76d01.md:31` | 53. 同じ人が 2 回起動すると、セッション報告が 1 ファイルに上書きされた |
| E239 | `projects/p3-org-visibility/log/msgs/c76d01.md:32` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E240 | `projects/p3-org-visibility/log/msgs/dc84e7.md:11` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E241 | `projects/p3-org-visibility/log/msgs/dc84e7.md:12` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E242 | `projects/p3-org-visibility/log/msgs/f315e9.md:13` | 53. 同じ人が 2 回起動すると、セッション報告が 1 ファイルに上書きされた |
| E243 | `projects/p3-org-visibility/log/msgs/f315e9.md:14` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E244 | `projects/p3-org-visibility/log/msgs/f315e9.md:15` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E245 | `projects/p4-job-run-use/log/msgs/3b3654.md:34` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E246 | `projects/p4-job-run-use/log/msgs/3b3654.md:35` | 14. 読み取り拒否の場所に grep・stat が届かず、洗い出し・確かめが言い切れない |
| E247 | `projects/p4-job-run-use/log/msgs/3b3654.md:36` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E248 | `projects/p4-job-run-use/log/msgs/3b3654.md:40` | 13. charter・ヒント・パックに書かれた前提が実物と違った（無いファイル・食い違う指示・件数） |
| E249 | `projects/p4-job-run-use/log/msgs/74b9f7.md:32` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E250 | `projects/p4-job-run-use/log/msgs/74b9f7.md:33` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E251 | `projects/p4-job-run-use/log/msgs/74b9f7.md:37` | 14. 読み取り拒否の場所に grep・stat が届かず、洗い出し・確かめが言い切れない |
| E252 | `projects/p5-org-viewer/log/msgs/02a83f.md:4` | 8. レビュアーの承認のあとで、リーダーが目的に届いていない点を見つけて rework を出した |
| E253 | `projects/p5-org-viewer/log/msgs/02a83f.md:6` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E254 | `projects/p5-org-viewer/log/msgs/02a83f.md:8` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E255 | `projects/p5-org-viewer/log/msgs/02a83f.md:12` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E256 | `projects/p5-org-viewer/log/msgs/146e61.md:28` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E257 | `projects/p5-org-viewer/log/msgs/146e61.md:29` | 23. ~/.npm のキャッシュの権限が壊れていて npm install が失敗する |
| E258 | `projects/p5-org-viewer/log/msgs/146e61.md:30` | 6. 画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった |
| E259 | `projects/p5-org-viewer/log/msgs/146e61.md:31` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E260 | `projects/p5-org-viewer/log/msgs/146e61.md:32` | 16. 1 行報告を読む道具が、数えるための行（NOISE_KINDS）を自前で持ち、orgctl とずれる |
| E261 | `projects/p5-org-viewer/log/msgs/146e61.md:36` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E262 | `projects/p5-org-viewer/log/msgs/146e61.md:37` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E263 | `projects/p5-org-viewer/log/msgs/146e61.md:41` | 28. 作業者が手書きデータの版で先に review_request を出し、実物の版と 2 通になって往復が 1 回増えた |
| E264 | `projects/p5-org-viewer/log/msgs/146e61.md:42` | 8. レビュアーの承認のあとで、リーダーが目的に届いていない点を見つけて rework を出した |
| E265 | `projects/p5-org-viewer/log/msgs/146e61.md:43` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E266 | `projects/p5-org-viewer/log/msgs/146e61.md:44` | 12. directory-guard が、引数の `/` を含む文字列や /dev/stdin を許可外の読み書きとして止める |
| E267 | `projects/p5-org-viewer/log/msgs/17b6a4.md:32` | 16. 1 行報告を読む道具が、数えるための行（NOISE_KINDS）を自前で持ち、orgctl とずれる |
| E268 | `projects/p5-org-viewer/log/msgs/17b6a4.md:33` | 39. 文脈の台帳（context.yaml）に、題材が組織そのもの（ai-org・dev-tools の org）のときに読む先が無い |
| E269 | `projects/p5-org-viewer/log/msgs/2140aa.md:29` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E270 | `projects/p5-org-viewer/log/msgs/2140aa.md:30` | 23. ~/.npm のキャッシュの権限が壊れていて npm install が失敗する |
| E271 | `projects/p5-org-viewer/log/msgs/2140aa.md:31` | 6. 画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった |
| E272 | `projects/p5-org-viewer/log/msgs/2140aa.md:32` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E273 | `projects/p5-org-viewer/log/msgs/2140aa.md:33` | 16. 1 行報告を読む道具が、数えるための行（NOISE_KINDS）を自前で持ち、orgctl とずれる |
| E274 | `projects/p5-org-viewer/log/msgs/2140aa.md:37` | 28. 作業者が手書きデータの版で先に review_request を出し、実物の版と 2 通になって往復が 1 回増えた |
| E275 | `projects/p5-org-viewer/log/msgs/2140aa.md:38` | 8. レビュアーの承認のあとで、リーダーが目的に届いていない点を見つけて rework を出した |
| E276 | `projects/p5-org-viewer/log/msgs/2140aa.md:39` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E277 | `projects/p5-org-viewer/log/msgs/2140aa.md:40` | 12. directory-guard が、引数の `/` を含む文字列や /dev/stdin を許可外の読み書きとして止める |
| E278 | `projects/p5-org-viewer/log/msgs/2140aa.md:41` | 39. 文脈の台帳（context.yaml）に、題材が組織そのもの（ai-org・dev-tools の org）のときに読む先が無い |
| E279 | `projects/p5-org-viewer/log/msgs/22d537.md:11` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E280 | `projects/p5-org-viewer/log/msgs/87b487.md:20` | 23. ~/.npm のキャッシュの権限が壊れていて npm install が失敗する |
| E281 | `projects/p5-org-viewer/log/msgs/87b487.md:21` | 6. 画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった |
| E282 | `projects/p5-org-viewer/log/msgs/87b487.md:22` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E283 | `projects/p5-org-viewer/log/msgs/aa3336.md:4` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E284 | `projects/p5-org-viewer/log/msgs/aa3336.md:6` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E285 | `projects/p5-org-viewer/log/msgs/aa3336.md:7` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E286 | `projects/p5-org-viewer/log/msgs/aa3336.md:8` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E287 | `projects/p5-org-viewer/log/msgs/ab626d.md:10` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E288 | `projects/p5-org-viewer/log/msgs/b8283e.md:10` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E289 | `projects/p5-org-viewer/log/msgs/b8283e.md:11` | 23. ~/.npm のキャッシュの権限が壊れていて npm install が失敗する |
| E290 | `projects/p5-org-viewer/log/msgs/b8283e.md:12` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E291 | `projects/p5-org-viewer/log/msgs/b8283e.md:13` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E292 | `projects/p6-org-build/log/msgs/25786e.md:64` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E293 | `projects/p6-org-build/log/msgs/25786e.md:65` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E294 | `projects/p6-org-build/log/msgs/25786e.md:66` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E295 | `projects/p6-org-build/log/msgs/25786e.md:67` | 48. assign でペルソナを重ねて指定すると、黙って 1 つにまとめる（README に書かれていない） |
| E296 | `projects/p6-org-build/log/msgs/25786e.md:73` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E297 | `projects/p6-org-build/log/msgs/25786e.md:74` | 49. 規範から org/ の資料を辿る書き方が「orgctl のパスから scripts/orgctl.py を外した所」になった |
| E298 | `projects/p6-org-build/log/msgs/25786e.md:80` | 6. 画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった |
| E299 | `projects/p6-org-build/log/msgs/25786e.md:81` | 3. 作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る |
| E300 | `projects/p6-org-build/log/msgs/25786e.md:82` | 12. directory-guard が、引数の `/` を含む文字列や /dev/stdin を許可外の読み書きとして止める |
| E301 | `projects/p6-org-build/log/msgs/4d8609.md:79` | 6. 画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった |
| E302 | `projects/p6-org-build/log/msgs/4d8609.md:80` | 7. 規範どおり `orgctl digest <親のコンポーネント>` を id で打つと「根っこのプロジェクトが無い」で失敗した |
| E303 | `projects/p6-org-build/log/msgs/4d8609.md:81` | 3. 作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る |
| E304 | `projects/p6-org-build/log/msgs/4d8609.md:82` | 12. directory-guard が、引数の `/` を含む文字列や /dev/stdin を許可外の読み書きとして止める |
| E305 | `projects/p6-org-build/log/msgs/4d8609.md:83` | 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった |
| E306 | `projects/p6-org-build/log/msgs/4d8609.md:84` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E307 | `projects/p6-org-build/log/msgs/4d8609.md:85` | 入れない: 作業中で待っただけ（p6 の PM が止まりではないと書いている。job の控えの p6 の記述は「全員が wait に入って止まり…」の起きたことに書いた） |
| E308 | `projects/p6-org-build/log/msgs/c4cc0d.md:18` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E309 | `projects/p6-org-build/log/msgs/c4cc0d.md:19` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E310 | `projects/p6-org-build/log/msgs/dd1184.md:28` | 46. p5 の画面の確かめが、明るい表示・幅 1400px の 1 枚だけだった |
| E311 | `projects/p6-org-build/log/msgs/dd1184.md:29` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E312 | `projects/p6-org-build/log/msgs/dd1184.md:30` | 46. p5 の画面の確かめが、明るい表示・幅 1400px の 1 枚だけだった |
| E313 | `projects/p6-org-build/log/msgs/dd1184.md:31` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E314 | `projects/p6-org-build/log/msgs/dd1184.md:35` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E315 | `projects/p6-org-build/log/msgs/dd1184.md:36` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E316 | `projects/p6-org-build/log/msgs/dd1184.md:40` | 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった |
| E317 | `projects/p6-org-build/log/msgs/dd1184.md:41` | 入れない: 本人が影響なしと書いた環境の挙動（問題として上げていない） |
| E318 | `projects/p7-coordinator-role/log/msgs/2e8018.md:44` | 35. パックの deny に $TMPDIR のパスを書くと /tmp のまま入り、ヒントの deny は /private/tmp になる |
| E319 | `projects/p7-coordinator-role/log/msgs/2e8018.md:45` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E320 | `projects/p7-coordinator-role/log/msgs/2e8018.md:49` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E321 | `projects/p7-coordinator-role/log/msgs/2e8018.md:50` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E322 | `projects/p7-coordinator-role/log/msgs/2e8018.md:54` | 33. 往復の「合意」と「返し」が同じ report の種類で、種類だけでは見分けられない |
| E323 | `projects/p7-coordinator-role/log/msgs/4d25e4.md:36` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E324 | `projects/p7-coordinator-role/log/msgs/4d25e4.md:38` | 43. 文脈パックが charter より先に書かれ、まだ無い charter を指した |
| E325 | `projects/p7-coordinator-role/log/msgs/4d25e4.md:39` | 44. コーディネーターと PM の往復で使う event の種類が決まっていなかった |
| E326 | `projects/p7-coordinator-role/log/msgs/4d25e4.md:40` | 34. コーディネーターの終わり方と、返しに書くもの（実現できる理由・崩れる前提）が規範に無かった |
| E327 | `projects/p7-coordinator-role/log/msgs/4d25e4.md:41` | 7. 規範どおり `orgctl digest <親のコンポーネント>` を id で打つと「根っこのプロジェクトが無い」で失敗した |
| E328 | `projects/p7-coordinator-role/log/msgs/4d25e4.md:42` | 45. orgctl new がチームにも packs/ を作り、新しい流れでは空のまま残った |
| E329 | `projects/p7-coordinator-role/log/msgs/4d25e4.md:43` | 34. コーディネーターの終わり方と、返しに書くもの（実現できる理由・崩れる前提）が規範に無かった |
| E330 | `projects/p7-coordinator-role/log/msgs/891118.md:66` | 35. パックの deny に $TMPDIR のパスを書くと /tmp のまま入り、ヒントの deny は /private/tmp になる |
| E331 | `projects/p7-coordinator-role/log/msgs/be01fb.md:45` | 15. 組織を直すプロジェクトの最中は、動いている本体の規範・orgctl が直す前のままで、上書きや使い分けが要った |
| E332 | `projects/p7-coordinator-role/log/msgs/be01fb.md:46` | 33. 往復の「合意」と「返し」が同じ report の種類で、種類だけでは見分けられない |
| E333 | `projects/p7-coordinator-role/log/msgs/be01fb.md:47` | 35. パックの deny に $TMPDIR のパスを書くと /tmp のまま入り、ヒントの deny は /private/tmp になる |
| E334 | `projects/p7-coordinator-role/log/msgs/be01fb.md:48` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E335 | `projects/p8-viewer-rebuild/log/msgs/176526.md:2` | 24. 全員が wait に入って止まり、見張りは全員待ちとしては出さなかった（待っている PM を「ループ?」として出した） |
| E336 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:86` | 22. 実データに判断待ち・止まっているものが無く、その見た目を写しでしか確かめられない |
| E337 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:87` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E338 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:88` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E339 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:89` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E340 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:90` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E341 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:94` | 24. 全員が wait に入って止まり、見張りは全員待ちとしては出さなかった（待っている PM を「ループ?」として出した） |
| E342 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:95` | 25. 画面を撮るとき、作業者の待ち受けを使うのか自分で立てるのかが screen-check.md に無い（ビルドし直すと 404） |
| E343 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:96` | 26. screen-probe が本文の Markdown の表も折り返しの候補に数え、印を押して出る引き出しを撮れない |
| E344 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:97` | 27. チェックリストの設計の段（B）に「押せる大きさと間隔」が無く、設計で通した配置が画面で押せない印になった |
| E345 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:98` | 32. 指摘の回数（3 回まで）を、design.md の段と画面の段で通算するかが決まりに無い |
| E346 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:99` | 38. `orgctl export --check` を `--out` と一緒に打つと、書き出し直してから検査する |
| E347 | `projects/p8-viewer-rebuild/log/msgs/3df696.md:103` | 22. 実データに判断待ち・止まっているものが無く、その見た目を写しでしか確かめられない |
| E348 | `projects/p8-viewer-rebuild/log/msgs/5f8f8f.md:4` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E349 | `projects/p8-viewer-rebuild/log/msgs/5f8f8f.md:6` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E350 | `projects/p8-viewer-rebuild/log/msgs/5f8f8f.md:8` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E351 | `projects/p8-viewer-rebuild/log/msgs/5f8f8f.md:13` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E352 | `projects/p8-viewer-rebuild/log/msgs/5f8f8f.md:18` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E353 | `projects/p8-viewer-rebuild/log/msgs/5f8f8f.md:23` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E354 | `projects/p8-viewer-rebuild/log/msgs/5f8f8f.md:28` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E355 | `projects/p8-viewer-rebuild/log/msgs/931330.md:4` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E356 | `projects/p8-viewer-rebuild/log/msgs/931330.md:6` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E357 | `projects/p8-viewer-rebuild/log/msgs/931330.md:8` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E358 | `projects/p8-viewer-rebuild/log/msgs/931330.md:10` | 27. チェックリストの設計の段（B）に「押せる大きさと間隔」が無く、設計で通した配置が画面で押せない印になった |
| E359 | `projects/p8-viewer-rebuild/log/msgs/931330.md:16` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E360 | `projects/p8-viewer-rebuild/log/msgs/931330.md:21` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E361 | `projects/p8-viewer-rebuild/log/msgs/a5676d.md:51` | 22. 実データに判断待ち・止まっているものが無く、その見た目を写しでしか確かめられない |
| E362 | `projects/p8-viewer-rebuild/log/msgs/a5676d.md:52` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E363 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:64` | 22. 実データに判断待ち・止まっているものが無く、その見た目を写しでしか確かめられない |
| E364 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:65` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E365 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:66` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E366 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:67` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E367 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:71` | 24. 全員が wait に入って止まり、見張りは全員待ちとしては出さなかった（待っている PM を「ループ?」として出した） |
| E368 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:72` | 25. 画面を撮るとき、作業者の待ち受けを使うのか自分で立てるのかが screen-check.md に無い（ビルドし直すと 404） |
| E369 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:73` | 26. screen-probe が本文の Markdown の表も折り返しの候補に数え、印を押して出る引き出しを撮れない |
| E370 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:74` | 27. チェックリストの設計の段（B）に「押せる大きさと間隔」が無く、設計で通した配置が画面で押せない印になった |
| E371 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:75` | 32. 指摘の回数（3 回まで）を、design.md の段と画面の段で通算するかが決まりに無い |
| E372 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:76` | 38. `orgctl export --check` を `--out` と一緒に打つと、書き出し直してから検査する |
| E373 | `projects/p8-viewer-rebuild/log/msgs/b20186.md:77` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E374 | `projects/p8-viewer-rebuild/log/msgs/b87e1b.md:22` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E375 | `projects/p8-viewer-rebuild/log/msgs/b87e1b.md:23` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E376 | `projects/p8-viewer-rebuild/log/msgs/b87e1b.md:24` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E377 | `projects/p9-org-watch/log/msgs/26be36.md:30` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E378 | `projects/p9-org-watch/log/msgs/26be36.md:31` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E379 | `projects/p9-org-watch/log/msgs/26be36.md:32` | 37. プランの「立場」の表と P3 の完了の目安が、監査役の新しい形（起きたことだけを書く）と食い違ったまま |
| E380 | `projects/p9-org-watch/log/msgs/26be36.md:36` | 21. 受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった |
| E381 | `projects/p9-org-watch/log/msgs/26be36.md:37` | 31. 同じファイル（orgctl.py）を 2 人で同時に直し、Edit の衝突と受け持ちの外への手入れが起きた |
| E382 | `projects/p9-org-watch/log/msgs/26be36.md:38` | 30. 「閉じる並び」を review_request に入れるのか最終報告に入れるのかを、作業者がパックから読み取れなかった |
| E383 | `projects/p9-org-watch/log/msgs/26be36.md:39` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E384 | `projects/p9-org-watch/log/msgs/26be36.md:43` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E385 | `projects/p9-org-watch/log/msgs/26be36.md:44` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E386 | `projects/p9-org-watch/log/msgs/299393.md:15` | 41. p9 のチームの完了条件で、閉じる側を PM と書いていた（根っこなので閉じるのは user） |
| E387 | `projects/p9-org-watch/log/msgs/299393.md:16` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E388 | `projects/p9-org-watch/log/msgs/299393.md:17` | 21. 受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった |
| E389 | `projects/p9-org-watch/log/msgs/299393.md:18` | 入れない: これからの段取り・マージ待ちの申し送り（起きたことではない） |
| E390 | `projects/p9-org-watch/log/msgs/5904f6.md:11` | 37. プランの「立場」の表と P3 の完了の目安が、監査役の新しい形（起きたことだけを書く）と食い違ったまま |
| E391 | `projects/p9-org-watch/log/msgs/635d9b.md:45` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E392 | `projects/p9-org-watch/log/msgs/635d9b.md:46` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E393 | `projects/p9-org-watch/log/msgs/635d9b.md:47` | 37. プランの「立場」の表と P3 の完了の目安が、監査役の新しい形（起きたことだけを書く）と食い違ったまま |
| E394 | `projects/p9-org-watch/log/msgs/635d9b.md:51` | 21. 受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった |
| E395 | `projects/p9-org-watch/log/msgs/635d9b.md:52` | 31. 同じファイル（orgctl.py）を 2 人で同時に直し、Edit の衝突と受け持ちの外への手入れが起きた |
| E396 | `projects/p9-org-watch/log/msgs/635d9b.md:53` | 30. 「閉じる並び」を review_request に入れるのか最終報告に入れるのかを、作業者がパックから読み取れなかった |
| E397 | `projects/p9-org-watch/log/msgs/635d9b.md:54` | 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている） |
| E398 | `projects/p9-org-watch/log/msgs/63bb4d.md:2` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E399 | `projects/p9-org-watch/log/msgs/6eccb0.md:13` | 21. 受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった |
| E400 | `projects/p9-org-watch/log/msgs/6eccb0.md:14` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E401 | `projects/p9-org-watch/log/msgs/6eccb0.md:15` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E402 | `projects/p9-org-watch/log/msgs/6eccb0.md:16` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E403 | `projects/p9-org-watch/log/msgs/cc2161.md:4` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E404 | `projects/p9-org-watch/log/msgs/cc2161.md:6` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E405 | `projects/p9-org-watch/log/msgs/cc2161.md:8` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E406 | `projects/p9-org-watch/log/msgs/cc2161.md:10` | 21. 受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった |
| E407 | `projects/p9-org-watch/log/msgs/cc2161.md:14` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E408 | `projects/p9-org-watch/log/msgs/cc2161.md:15` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E409 | `projects/p9-org-watch/log/msgs/e930ae.md:19` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E410 | `projects/p9-org-watch/log/msgs/e930ae.md:20` | 入れない: 未実施・〔仮〕の申告（範囲の外、またはこれから実地で確かめるもの） |
| E411 | `projects/p9-org-watch/log/msgs/f08c2f.md:4` | 入れない: 何も起きなかった・確かめて通ったことの行（review_ng の「確かめたこと」・判定の要約・「特になし」など） |
| E412 | `projects/p9-org-watch/log/msgs/f08c2f.md:6` | 入れない: 成果物の中身への指摘・申し送り・未確認点（組織の動き方の問題ではない） |
| E413 | `projects/p9-org-watch/log/msgs/f08c2f.md:8` | 42. 監査役の参照元の形（1 行に複数・バッククォート付き）が、export の refs で 1 件に潰れる |
| E414 | `projects/p9-org-watch/log/msgs/f08c2f.md:10` | 30. 「閉じる並び」を review_request に入れるのか最終報告に入れるのかを、作業者がパックから読み取れなかった |
| E415 | `projects/p8-viewer-rebuild/log/user-inbox.yaml:1` | 24. 全員が wait に入って止まり、見張りは全員待ちとしては出さなかった（待っている PM を「ループ?」として出した） |
| E416 | `projects/p9-org-watch/reports/audit/p9-org-watch.md:5` | 41. p9 のチームの完了条件で、閉じる側を PM と書いていた（根っこなので閉じるのは user） |
| E417 | `projects/p9-org-watch/reports/audit/p9-org-watch.md:9` | 21. 受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった |
| E418 | `projects/p9-org-watch/reports/audit/p9-org-watch.md:13` | 31. 同じファイル（orgctl.py）を 2 人で同時に直し、Edit の衝突と受け持ちの外への手入れが起きた |
| E419 | `projects/p9-org-watch/reports/audit/p9-org-watch.md:17` | 55. PM が検収で、本物の ai-org/projects に書き込みのある patrol --dry を打った |
| E420 | `job:company/system/ai-org/README.md:28` | 24. 全員が wait に入って止まり、見張りは全員待ちとしては出さなかった（待っている PM を「ループ?」として出した） |
| E421 | `job:company/system/ai-org/README.md:36` | 24. 全員が wait に入って止まり、見張りは全員待ちとしては出さなかった（待っている PM を「ループ?」として出した） |
| E422 | `job:company/system/ai-org/README.md:38` | 2. p4〜p8 は監査役なしで閉じ、セッション報告の unclear が読まれないまま溜まった |
| E423 | `job:company/system/ai-org/README.md:53` | 33. 往復の「合意」と「返し」が同じ report の種類で、種類だけでは見分けられない |
| E424 | `job:company/system/ai-org/README.md:59` | 22. 実データに判断待ち・止まっているものが無く、その見た目を写しでしか確かめられない |
| E425 | `projects/p1-org-status/log/events.log:84` | 入れない: 閉じたときは監査役がいなかったが、記録は p3 の監査役が照らした（p3-org-visibility/charter.md:18・log/msgs/95df09.md:30） |
| E426 | `projects/p2-orca-run-use/log/events.log:91` | 入れない: 閉じたときは監査役がいなかったが、記録は p3 の監査役が照らした（p3-org-visibility/charter.md:18・log/msgs/95df09.md:30） |
| E427 | `projects/p4-job-run-use/log/events.log:82` | 2. p4〜p8 は監査役なしで閉じ、セッション報告の unclear が読まれないまま溜まった |
| E428 | `projects/p5-org-viewer/log/events.log:130` | 2. p4〜p8 は監査役なしで閉じ、セッション報告の unclear が読まれないまま溜まった |
| E429 | `projects/p6-org-build/log/events.log:207` | 2. p4〜p8 は監査役なしで閉じ、セッション報告の unclear が読まれないまま溜まった |
| E430 | `projects/p7-coordinator-role/log/events.log:84` | 2. p4〜p8 は監査役なしで閉じ、セッション報告の unclear が読まれないまま溜まった |
| E431 | `projects/p8-viewer-rebuild/log/events.log:153` | 2. p4〜p8 は監査役なしで閉じ、セッション報告の unclear が読まれないまま溜まった |
