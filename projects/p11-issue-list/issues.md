# AI 組織の問題・課題の一覧（閉じた p1〜p9 の記録から）

書いてあるのは起きたこと（問題・課題）と参照元だけ。直し方は書かない（直し方は着手の直前に考える。dev-tools の `docs/todo/ai-org-plan.md` の決定ログ 2026-10-24）。数はすべて `scripts/build.py` が数えた値。

## Summary

- **68 件**（印なし＝まだ起きている 14・不明 39・直った 15）。材料から抜いた 431 行のうち 281 行をこの 68 件に寄せ、150 行は入れなかった（理由は対応表）。
- 分類ごとの件数（記録の数の合計）: 規範の書き方 13 件（33）・道具 12 件（37）・連絡 11 件（72）・レビュー 11 件（46）・文脈パック 10 件（36）・環境 8 件（31）・見張り 2 件（10）・人の操作 1 件（1）
- 何度も起きているもの（プロジェクト数の多い順の上位 5）:
  - [Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている）](#i01) — 9 プロジェクト・記録 30・印なし
  - [p4〜p8 は監査役なしで閉じ、セッション報告の unclear が読まれないまま溜まった](#i02) — 5 プロジェクト・記録 5・不明
  - [作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る](#i03) — 4 プロジェクト・記録 7・印なし
  - [orgctl のコマンドを変数（O="python3 …"）に入れて打つと、zsh で 1 語扱いになり失敗する](#i04) — 4 プロジェクト・記録 5・印なし
  - [知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる](#i05) — 3 プロジェクト・記録 12・不明

## 目次

- [Summary](#summary)
- [一覧](#一覧)
- [件ごと](#件ごと)
- [作り方](#作り方)

## 一覧

並びはプロジェクト数の多い順（同じなら記録の数の多い順、それも同じなら新しい順）。状態の「印なし」はまだ起きているもの。

| # | 題 | 分類 | プロジェクト数 | 記録の数 | 状態 |
|---|---|---|---|---|---|
| 1 | [Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている）](#i01) | 連絡 | 9（p1・p2・p3・p4・p5・p6・p7・p8・p9） | 30 |  |
| 2 | [p4〜p8 は監査役なしで閉じ、セッション報告の unclear が読まれないまま溜まった](#i02) | 見張り | 5（p4・p5・p6・p7・p8） | 5 | 不明 |
| 3 | [作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る](#i03) | 連絡 | 4（p5・p6・p7・p8） | 7 |  |
| 4 | [orgctl のコマンドを変数（O="python3 …"）に入れて打つと、zsh で 1 語扱いになり失敗する](#i04) | 環境 | 4（p3・p5・p6・p9） | 5 |  |
| 5 | [知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる](#i05) | 連絡 | 3（p1・p2・p3） | 12 | 不明 |
| 6 | [画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった](#i06) | 環境 | 3（p3・p5・p6） | 8 | 直った |
| 7 | [規範どおり `orgctl digest <親のコンポーネント>` を id で打つと「根っこのプロジェクトが無い」で失敗した](#i07) | 道具 | 3（p4・p6・p7） | 7 | 直った |
| 8 | [レビュアーの承認のあとで、リーダーが目的に届いていない点を見つけて rework を出した](#i08) | レビュー | 3（p2・p3・p5） | 6 | 不明 |
| 9 | [起動した直後の `inbox` に、上からの start がまだ無い](#i09) | 連絡 | 3（p4・p5・p6） | 4 | 不明 |
| 10 | [レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった](#i10) | レビュー | 2（p5・p6） | 9 | 不明 |
| 11 | [レビュアーは最初の review_request の後に起こす順番なので、作業者が review_request を知らせる相手（タブ）が無い](#i11) | 連絡 | 2（p1・p6） | 7 |  |
| 12 | [directory-guard が、引数の `/` を含む文字列や /dev/stdin を許可外の読み書きとして止める](#i12) | 環境 | 2（p5・p6） | 7 | 不明 |
| 13 | [charter・ヒント・パックに書かれた前提が実物と違った（無いファイル・食い違う指示・件数）](#i13) | 文脈パック | 2（p4・p5） | 6 | 不明 |
| 14 | [読み取り拒否の場所に grep・stat が届かず、洗い出し・確かめが言い切れない](#i14) | 文脈パック | 2（p4・p8） | 5 | 不明 |
| 15 | [組織を直すプロジェクトの最中は、動いている本体の規範・orgctl が直す前のままで、上書きや使い分けが要った](#i15) | 規範の書き方 | 2（p7・p9） | 4 |  |
| 16 | [1 行報告を読む道具が、数えるための行（NOISE_KINDS）を自前で持ち、orgctl とずれる](#i16) | 道具 | 2（p3・p5） | 4 |  |
| 17 | [根っこ（user）にはタブが無く、user 宛ての report・wrap_up に Orca の知らせが出ない](#i17) | 連絡 | 2（p1・p2） | 3 | 直った |
| 18 | [同じ立場が複数いるときの名前（コーディネーター・パックのファイル名）の付け方が決まりに無い](#i18) | 規範の書き方 | 2（p7・p8） | 2 |  |
| 19 | [PM の `wait` が配下のやりとり（cc）でも戻り、自分宛てが来るまで打ち直した](#i19) | 連絡 | 2（p5・p6） | 2 | 不明 |
| 20 | [パックの deny は Read の拒否だけで、grep（Bash）では見え、glob でしか書けない](#i20) | 文脈パック | 2（p4・p6） | 2 | 不明 |
| 21 | [受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった](#i21) | 文脈パック | 1（p9） | 7 |  |
| 22 | [実データに判断待ち・止まっているものが無く、その見た目を写しでしか確かめられない](#i22) | レビュー | 1（p8） | 6 | 不明 |
| 23 | [~/.npm のキャッシュの権限が壊れていて npm install が失敗する](#i23) | 環境 | 1（p5） | 6 | 不明 |
| 24 | [全員が wait に入って止まり、見張りは全員待ちとしては出さなかった（待っている PM を「ループ?」として出した）](#i24) | 見張り | 1（p8） | 5 | 不明 |
| 25 | [画面を撮るとき、作業者の待ち受けを使うのか自分で立てるのかが screen-check.md に無い（ビルドし直すと 404）](#i25) | 道具 | 1（p8） | 5 | 不明 |
| 26 | [screen-probe が本文の Markdown の表も折り返しの候補に数え、印を押して出る引き出しを撮れない](#i26) | 道具 | 1（p8） | 5 | 不明 |
| 27 | [チェックリストの設計の段（B）に「押せる大きさと間隔」が無く、設計で通した配置が画面で押せない印になった](#i27) | レビュー | 1（p8） | 5 | 不明 |
| 28 | [作業者が手書きデータの版で先に review_request を出し、実物の版と 2 通になって往復が 1 回増えた](#i28) | レビュー | 1（p5） | 5 | 不明 |
| 29 | [レビュアーの承認のあとにリーダーが rework を出したとき、レビュアーがもう一度見るかが決まりに無かった](#i29) | レビュー | 1（p2） | 5 | 直った |
| 30 | [「閉じる並び」を review_request に入れるのか最終報告に入れるのかを、作業者がパックから読み取れなかった](#i30) | 文脈パック | 1（p9） | 4 |  |
| 31 | [同じファイル（orgctl.py）を 2 人で同時に直し、Edit の衝突と受け持ちの外への手入れが起きた](#i31) | 規範の書き方 | 1（p9） | 4 |  |
| 32 | [指摘の回数（3 回まで）を、design.md の段と画面の段で通算するかが決まりに無い](#i32) | レビュー | 1（p8） | 4 | 不明 |
| 33 | [往復の「合意」と「返し」が同じ report の種類で、種類だけでは見分けられない](#i33) | 規範の書き方 | 1（p7） | 4 |  |
| 34 | [コーディネーターの終わり方と、返しに書くもの（実現できる理由・崩れる前提）が規範に無かった](#i34) | 規範の書き方 | 1（p7） | 4 | 直った |
| 35 | [パックの deny に $TMPDIR のパスを書くと /tmp のまま入り、ヒントの deny は /private/tmp になる](#i35) | 文脈パック | 1（p7） | 4 | 不明 |
| 36 | [リーダーの `wait --cc` が、作業者 → 未起動のレビュアーの review_request を拾わず、約 10 分止まった](#i36) | 連絡 | 1（p1） | 4 | 直った |
| 37 | [プランの「立場」の表と P3 の完了の目安が、監査役の新しい形（起きたことだけを書く）と食い違ったまま](#i37) | 規範の書き方 | 1（p9） | 3 |  |
| 38 | [`orgctl export --check` を `--out` と一緒に打つと、書き出し直してから検査する](#i38) | 道具 | 1（p8） | 3 | 不明 |
| 39 | [文脈の台帳（context.yaml）に、題材が組織そのもの（ai-org・dev-tools の org）のときに読む先が無い](#i39) | 文脈パック | 1（p5） | 3 | 不明 |
| 40 | [見本の id が根っこの親ディレクトリ基準（rel_id）で、見本のディレクトリ名を揃える必要が決まりに書かれていない](#i40) | 道具 | 1（p1） | 3 | 不明 |
| 41 | [p9 のチームの完了条件で、閉じる側を PM と書いていた（根っこなので閉じるのは user）](#i41) | 規範の書き方 | 1（p9） | 2 |  |
| 42 | [監査役の参照元の形（1 行に複数・バッククォート付き）が、export の refs で 1 件に潰れる](#i42) | 道具 | 1（p9） | 2 | 不明 |
| 43 | [文脈パックが charter より先に書かれ、まだ無い charter を指した](#i43) | 文脈パック | 1（p7） | 2 | 直った |
| 44 | [コーディネーターと PM の往復で使う event の種類が決まっていなかった](#i44) | 規範の書き方 | 1（p7） | 2 | 直った |
| 45 | [orgctl new がチームにも packs/ を作り、新しい流れでは空のまま残った](#i45) | 道具 | 1（p7） | 2 | 直った |
| 46 | [p5 の画面の確かめが、明るい表示・幅 1400px の 1 枚だけだった](#i46) | レビュー | 1（p6） | 2 | 直った |
| 47 | [調べもの・出典の裏取りが本業の職種が台帳に無く、リーダーの職種なしが許されるかも書かれていない](#i47) | 文脈パック | 1（p6） | 2 | 不明 |
| 48 | [assign でペルソナを重ねて指定すると、黙って 1 つにまとめる（README に書かれていない）](#i48) | 道具 | 1（p6） | 2 | 不明 |
| 49 | [規範から org/ の資料を辿る書き方が「orgctl のパスから scripts/orgctl.py を外した所」になった](#i49) | 規範の書き方 | 1（p6） | 2 | 不明 |
| 50 | [JavaScript で描くページを WebFetch で読めず、出典の裏取りがほかの道頼みになった](#i50) | 環境 | 1（p6） | 2 | 不明 |
| 51 | [承認のときにも thread.md に追記するかが決まりに無かった](#i51) | レビュー | 1（p3） | 2 | 直った |
| 52 | [並行する別チームの成果物を、できる前に前提にして書いた](#i52) | 規範の書き方 | 1（p3） | 2 | 不明 |
| 53 | [同じ人が 2 回起動すると、セッション報告が 1 ファイルに上書きされた](#i53) | 道具 | 1（p3） | 2 | 直った |
| 54 | [PM の入れ替えで、前の PM の状況が新しい PM に引き継がれなかった](#i54) | 規範の書き方 | 1（p1） | 2 | 直った |
| 55 | [PM が検収で、本物の ai-org/projects に書き込みのある patrol --dry を打った](#i55) | 人の操作 | 1（p9） | 1 |  |
| 56 | [プロジェクトの charter の完了条件が記録と食い違うとき、PM が子の charter で補ってよいかがはっきりしない](#i56) | 規範の書き方 | 1（p8） | 1 | 不明 |
| 57 | [別の作業者へ送った文案が、相手の成果物に入ったか確かめられなかった](#i57) | 連絡 | 1（p6） | 1 | 不明 |
| 58 | [zsh で `echo =====` と打つと「==== not found」で失敗する](#i58) | 環境 | 1（p5） | 1 | 不明 |
| 59 | [台帳の deny（**/_archive/）が、案件の成果物の置き場と重なった](#i59) | 文脈パック | 1（p4） | 1 | 不明 |
| 60 | [サンドボックスの中で Bash のパイプ（git show \| diff）が Operation not permitted になる](#i60) | 環境 | 1（p4） | 1 | 不明 |
| 61 | [起こした直後の相手にも「wait で待っているので知らせは出さない」と出た](#i61) | 連絡 | 1（p3） | 1 | 不明 |
| 62 | [PM の wrap_up に、PM が自分で確かめたことが書かれていなかった](#i62) | レビュー | 1（p3） | 1 | 直った |
| 63 | [リーダーの残る不明点がセッション報告の unclear にだけあり、PM への report に無かった](#i63) | レビュー | 1（p3） | 1 | 直った |
| 64 | [監査役の見るものに、セッション報告の machine 欄（files_changed_in_window など）の正しさが入るかがはっきりしない](#i64) | 規範の書き方 | 1（p3） | 1 | 不明 |
| 65 | [teardown の files_changed_in_window に、並行チームの変更が混じる](#i65) | 道具 | 1（p3） | 1 | 不明 |
| 66 | [tools/org_timeline.py に --help が無く、打つとディレクトリとして扱われて例外で止まる](#i66) | 道具 | 1（p3） | 1 | 不明 |
| 67 | [Claude in Chrome の拡張が繋がらず、実ブラウザで確かめられなかった](#i67) | 環境 | 1（p3） | 1 | 不明 |
| 68 | [PM がリーダーへ催促・確認するための種類が無く、report で代用した](#i68) | 連絡 | 1（p1） | 1 | 不明 |

[↑ 目次へ](#目次)

## 件ごと

<a id="i01"></a>

### 1. Orca の知らせが毎回「Enter が飲まれたかもしれない」と警告する（実際は届いている）

- 分類: 連絡
- 回数: 9 プロジェクト（p1・p2・p3・p4・p5・p6・p7・p8・p9）・記録 30
- 状態: 印なし — 再送しない決まりは PR #1（f48f81d）で入ったが、警告そのものは p9 まで毎回出ている
- 起きたこと: `orca terminal send` で知らせを出すたびに「Enter が飲まれたかもしれない」の警告が出た。p1 では PM が `--retry-request` で再送を試し、同じ警告が出た。p2 以降は決まりどおり再送せず、相手には届いていたが、届いたかは相手の次の動きを見るまで分からなかったと書かれている。
- 参照元:
  - `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:72`
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:68`
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__reviewer.yaml:52`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__pm-0775601b.yaml:68`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__leader-70bafeda.yaml:65`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__reviewer-f7de4d8b.yaml:58`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__worker-1-56151c49.yaml:58`
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__pm-8512c441.yaml:83`
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__leader-4d653d8e.yaml:76`
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__pm-7fcade93.yaml:73`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:73`
  - `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-org-build-b422e51c.yaml:69`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__pm-129ad682.yaml:415`
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__coordinator-37d1062a.yaml:65`
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__pm-f743150d.yaml:72`
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__leader-36cfe0d2.yaml:67`
  - `projects/p1-org-status/log/msgs/803ffb.md:47`（803ffb・`log/events.log:75`）
  - `projects/p1-org-status/log/msgs/d9ba25.md:41`（d9ba25・`log/events.log:61`）
  - `projects/p2-orca-run-use/log/msgs/1f7fb5.md:71`（1f7fb5・`log/events.log:68`）
  - `projects/p2-orca-run-use/log/msgs/7ad811.md:55`（7ad811・`log/events.log:82`）
  - `projects/p2-orca-run-use/log/msgs/f863c1.md:19`（f863c1・`log/events.log:37`）
  - `projects/p3-org-visibility/log/msgs/95df09.md:31`（95df09・`log/events.log:126`）（別の出どころ。数えない）
  - `projects/p3-org-visibility/log/msgs/b93761.md:34`（b93761・`log/events.log:136`）
  - `projects/p5-org-viewer/log/msgs/146e61.md:43`（146e61・`log/events.log:110`）
  - `projects/p5-org-viewer/log/msgs/2140aa.md:39`（2140aa・`log/events.log:120`）
  - `projects/p6-org-build/log/msgs/4d8609.md:84`（4d8609・`log/events.log:198`）
  - `projects/p7-coordinator-role/log/msgs/2e8018.md:49`（2e8018・`log/events.log:65`）
  - `projects/p7-coordinator-role/log/msgs/be01fb.md:48`（be01fb・`log/events.log:76`）
  - `projects/p8-viewer-rebuild/log/msgs/b20186.md:77`（b20186・`log/events.log:145`）
  - `projects/p9-org-watch/log/msgs/26be36.md:39`（26be36・`log/events.log:110`）
  - `projects/p9-org-watch/log/msgs/635d9b.md:54`（635d9b・`log/events.log:121`）

[↑ 目次へ](#目次)

<a id="i02"></a>

### 2. p4〜p8 は監査役なしで閉じ、セッション報告の unclear が読まれないまま溜まった

- 分類: 見張り
- 回数: 5 プロジェクト（p4・p5・p6・p7・p8）・記録 5
- 状態: 不明 — 閉じるときの監査は PR #14（9bb11a5、10-24 18:56）で手順に入り p9 で動いたが、マージのあとに閉じたプロジェクトが無い
- 起きたこと: events.log に監査役の assign があるのは p3・p9 だけで、p4〜p8 は監査役なしで閉じた（スクリプトで判定）。p1・p2 も閉じたときは監査役がいなかったが、記録は次の p3 の監査役が照らしている（p3 の charter の完了条件 5・log/msgs/95df09.md:30）。job の控えは、p4〜p8 は閉じても監査が無く、セッション報告の unclear がビューアの「決まりの直し候補」で 111 件溜まっているが誰も読んでいない、と書いている。
- 参照元:
  - `job:company/system/ai-org/README.md:38`（別の出どころ。数えない）
  - `projects/p4-job-run-use/log/events.log:82`
  - `projects/p5-org-viewer/log/events.log:130`
  - `projects/p6-org-build/log/events.log:207`
  - `projects/p7-coordinator-role/log/events.log:84`
  - `projects/p8-viewer-rebuild/log/events.log:153`

[↑ 目次へ](#目次)

<a id="i03"></a>

### 3. 作業者がレビュアーの返事（review_ok）を受け取らないまま wrap_up が来る

- 分類: 連絡
- 回数: 4 プロジェクト（p5・p6・p7・p8）・記録 7
- 状態: 印なし — 直した記録が見つからず、p8 まで起きている
- 起きたこと: review_ok はリーダー宛てに出るので、作業者は自分の版が承認されたかを thread.md か wrap_up の本文でしか知れなかった。review_request を出した直後にリーダーから wrap_up が来て、レビュアーの判定を経たかを作業者が確かめられなかった例が p5〜p8 にある。
- 参照元:
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:70`
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-norms-7bbd0aab.yaml:95`
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__teams__coordinator-flow__worker-1-32df2698.yaml:73`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-export-fff11e32.yaml:397`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:432`
  - `projects/p6-org-build/log/msgs/25786e.md:81`（25786e・`log/events.log:186`）
  - `projects/p6-org-build/log/msgs/4d8609.md:81`（4d8609・`log/events.log:198`）

[↑ 目次へ](#目次)

<a id="i04"></a>

### 4. orgctl のコマンドを変数（O="python3 …"）に入れて打つと、zsh で 1 語扱いになり失敗する

- 分類: 環境
- 回数: 4 プロジェクト（p3・p5・p6・p9）・記録 5
- 状態: 印なし — 直した記録が見つからず、p9 まで起きている
- 起きたこと: p3・p5・p6・p9 の PM・リーダー・レビュアーが、長い orgctl のパスを変数に入れて `$O …` で打ち、zsh で語分割されず失敗した。打ち直すか、scratchpad にラッパーの sh を作って回した。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__pm-8512c441.yaml:84`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__pm-92edb217.yaml:81`
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__leader-00fa4e8f.yaml:67`
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__reviewer-512bbb7a.yaml:60`
  - `projects/p3-org-visibility/log/msgs/b93761.md:35`（b93761・`log/events.log:136`）

[↑ 目次へ](#目次)

<a id="i05"></a>

### 5. 知らせの `inbox --via notify --ref` が、先に wait で読んだ件だと「新しいものは無い」になる

- 分類: 連絡
- 回数: 3 プロジェクト（p1・p2・p3）・記録 12
- 状態: 不明 — 直した記録が見つからない（org-report の手順は同じ）。p4 以降の記録には同じ申告が無い
- 起きたこと: `[org]` の知らせが、`wait`・最初の `inbox` で読んだあとに届き、書かれた `inbox --via notify --ref` を打つと「新しいものは無い」と出た。done 2 件がほぼ同時に来たときは 1 件目の `--ref` で両方が読まれた。p1〜p3 の受け手が、通知の届き方の数え方がずれるかを心配して書いた。p3 の監査役は、届いた記録（notify_recv）は残っていて表示だけの話と書いている。
- 参照元:
  - `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:73`
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:69`
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:70`
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__reviewer.yaml:51`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__pm-0775601b.yaml:67`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__leader-70bafeda.yaml:66`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__reviewer-f7de4d8b.yaml:60`
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__worker-1-969f0ba1.yaml:72`
  - `projects/p1-org-status/log/msgs/803ffb.md:48`（803ffb・`log/events.log:75`）
  - `projects/p1-org-status/log/msgs/d9ba25.md:42`（d9ba25・`log/events.log:61`）
  - `projects/p2-orca-run-use/log/msgs/1f7fb5.md:72`（1f7fb5・`log/events.log:68`）
  - `projects/p2-orca-run-use/log/msgs/7ad811.md:56`（7ad811・`log/events.log:82`）
  - `projects/p3-org-visibility/log/msgs/95df09.md:34`（95df09・`log/events.log:126`）（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i06"></a>

### 6. 画面の待ち受け・Playwright・Chromium がサンドボックスの中で動かず、パックの注意は理由が足りなかった

- 分類: 環境
- 回数: 3 プロジェクト（p3・p5・p6）・記録 8
- 状態: 直った — screen-check.md に「待ち受けと Playwright はサンドボックスの外で動かす（localhost と Chromium の起動）」が PR #10（54385d3、10-24 15:05）で入り、p7〜p9 に同じ申告が無い
- 起きたこと: p3 でヘッドレス Chrome がサンドボックスの中では $TMPDIR のファイルを読めず、repo のファイルを直接開いた。p5 で astro preview と Playwright をサンドボックスの外で動かした。p6 で Chromium がサンドボックスの中で起動しない（mach port）と分かり、p5 由来のパックの注意は「localhost だから」の理由だけだった。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__reviewer-8d87b16a.yaml:64`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml:92`
  - `projects/p5-org-viewer/log/msgs/146e61.md:30`（146e61・`log/events.log:110`）
  - `projects/p5-org-viewer/log/msgs/2140aa.md:31`（2140aa・`log/events.log:120`）
  - `projects/p5-org-viewer/log/msgs/87b487.md:21`（87b487・`log/events.log:50`）
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-norms-7bbd0aab.yaml:94`
  - `projects/p6-org-build/log/msgs/25786e.md:80`（25786e・`log/events.log:186`）
  - `projects/p6-org-build/log/msgs/4d8609.md:79`（4d8609・`log/events.log:198`）

[↑ 目次へ](#目次)

<a id="i07"></a>

### 7. 規範どおり `orgctl digest <親のコンポーネント>` を id で打つと「根っこのプロジェクトが無い」で失敗した

- 分類: 道具
- 回数: 3 プロジェクト（p4・p6・p7）・記録 7
- 状態: 直った — コーディネーターの規範が「digest の引数は id ではなくパス」に PR #11（5c1bcd2、10-24 15:30）で変わり、p8・p9 に同じ申告が無い（orgctl の解決のしかたは変わっていない）
- 起きたこと: p4・p6・p7 のコーディネーターと PM が、規範どおり `orgctl digest <親のコンポーネント>` を id で打つと、打った場所（ai-org の直下）から根っこが見つからず失敗した。絶対パスや projects/ からのパスで渡すと通った。
- 参照元:
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__coordinator-run-use-thin-ad0d46dd.yaml:58`
  - `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-org-build-b422e51c.yaml:67`
  - `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-uiux-research-057eafed.yaml:64`
  - `projects/p6-org-build/reports/sessions/p6-org-build__pm-16bc79bc.yaml:87`
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:69`
  - `projects/p6-org-build/log/msgs/4d8609.md:80`（4d8609・`log/events.log:198`）
  - `projects/p7-coordinator-role/log/msgs/4d25e4.md:41`（4d25e4・`log/events.log:13`）

[↑ 目次へ](#目次)

<a id="i08"></a>

### 8. レビュアーの承認のあとで、リーダーが目的に届いていない点を見つけて rework を出した

- 分類: レビュー
- 回数: 3 プロジェクト（p2・p3・p5）・記録 6
- 状態: 不明 — 直した記録が特定できない。p6 以降は承認のあとの rework が出ていない
- 起きたこと: p2・p3・p5 で、レビュアーが review_ok を出したあと、リーダーが目的に照らして成果物を見直し rework を出した（p2: 依頼していない戻りが依頼元から見えない／p3: 帯の頭の数字が合計に見える／p5: 未読の行が畳みに隠れる・閉じたプロジェクトの一言が component_closed）。p5 のレビュアーは、承認が目的に届いていなかったと書いている。
- 参照元:
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__reviewer-11df580d.yaml:64`
  - `projects/p2-orca-run-use/log/msgs/63b813.md:2`（63b813・`log/events.log:42`）
  - `projects/p3-org-visibility/log/msgs/8723ce.md:2`（8723ce・`log/events.log:81`）
  - `projects/p5-org-viewer/log/msgs/02a83f.md:4`（02a83f・`log/events.log:79`）
  - `projects/p5-org-viewer/log/msgs/146e61.md:42`（146e61・`log/events.log:110`）
  - `projects/p5-org-viewer/log/msgs/2140aa.md:38`（2140aa・`log/events.log:120`）

[↑ 目次へ](#目次)

<a id="i09"></a>

### 9. 起動した直後の `inbox` に、上からの start がまだ無い

- 分類: 連絡
- 回数: 3 プロジェクト（p4・p5・p6）・記録 4
- 状態: 不明 — 直した記録が見つからない。p7 以降の記録には同じ申告が無い
- 起きたこと: 起動してすぐ打った `inbox` が「新しいものは無い」を返し、start は少しあと（約 20 秒）に届いた。events.log に start が見えたので `--ref` で読んだ人と、`wait` で拾った人がいた。
- 参照元:
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__coordinator-run-use-thin-ad0d46dd.yaml:61`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__coordinator-viewer-2d6b3d7c.yaml:61`
  - `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-org-build-b422e51c.yaml:66`
  - `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-uiux-research-057eafed.yaml:65`

[↑ 目次へ](#目次)

<a id="i10"></a>

### 10. レビュアーが短時間で承認し、確かめが一部だけ・作業者の表や本文頼みだった

- 分類: レビュー
- 回数: 2 プロジェクト（p5・p6）・記録 9
- 状態: 不明 — 画面は PR #10（54385d3、10-24 15:05）の screen-check.md で「判定する人が自分で撮る」となり p8 のレビュアーは自分で撮った。出典・本文頼みの確かめの分は直した記録が無い
- 起きたこと: p6 の研究チームのレビュアーは約 2 分で承認し、スクリーンショット 5 枚のうち自分で当てたのは 2 枚、出典 45 件は主要なものと URL の到達まで。リーダーが当て直した。org-build のリーダーも、レビュアーが 1 分前後で承認し、どこまで自分で打ったかは本文頼みと書いた。p5 のレビュアーは dev 起動での表示を確かめていない。パックの「5 枚に当てる」「主要な原則は全部開く」の範囲が曖昧だったと書かれている。
- 参照元:
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__reviewer-11df580d.yaml:61`
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__leader-15cbc271.yaml:73`
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__reviewer-b8082b46.yaml:73`
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__leader-00fa4e8f.yaml:65`
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__reviewer-77f133a5.yaml:55`
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__reviewer-77f133a5.yaml:56`
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__reviewer-77f133a5.yaml:58`
  - `projects/p6-org-build/log/msgs/4d8609.md:83`（4d8609・`log/events.log:198`）
  - `projects/p6-org-build/log/msgs/dd1184.md:40`（dd1184・`log/events.log:128`）

[↑ 目次へ](#目次)

<a id="i11"></a>

### 11. レビュアーは最初の review_request の後に起こす順番なので、作業者が review_request を知らせる相手（タブ）が無い

- 分類: 連絡
- 回数: 2 プロジェクト（p1・p6）・記録 7
- 状態: 印なし — org-assign の「レビュアーは作業者の最初の review_request が出てから起こす」は今もそのままで、p6 でも起きている
- 起きたこと: 作業者が review_request を出した時点でレビュアーにタブが無く、知らせを出せなかった。p1 ではレビュアーの起動前に依頼が出せてしまい、起動時の poll で 550 秒の遅れとして記録された。p6 の研究チームの作業者も、レビュアーの宛先のタブが分からず知らせが出なかったと書いている。
- 参照元:
  - `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:71`
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:67`
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__reviewer.yaml:50`
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__worker-1.yaml:58`
  - `projects/p1-org-status/log/msgs/803ffb.md:46`（803ffb・`log/events.log:75`）
  - `projects/p1-org-status/log/msgs/d9ba25.md:40`（d9ba25・`log/events.log:61`）
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__worker-1-833d6b72.yaml:73`

[↑ 目次へ](#目次)

<a id="i12"></a>

### 12. directory-guard が、引数の `/` を含む文字列や /dev/stdin を許可外の読み書きとして止める

- 分類: 環境
- 回数: 2 プロジェクト（p5・p6）・記録 7
- 状態: 不明 — 直した記録が見つからない。p7 以降の記録には同じ申告が無い
- 起きたこと: p5 で、$TMPDIR を含むパスを python -c に書く・撮影スクリプトに '/=名前' の形の引数を渡すと、絶対パスと誤判定されて止まった（2 人。言い換えて回避）。p6 で、リーダーの `event --body-file /dev/stdin` が止められ、本文をファイルに書いて渡した。
- 参照元:
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:75`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml:93`
  - `projects/p5-org-viewer/log/msgs/146e61.md:44`（146e61・`log/events.log:110`）
  - `projects/p5-org-viewer/log/msgs/2140aa.md:40`（2140aa・`log/events.log:120`）
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__leader-15cbc271.yaml:72`
  - `projects/p6-org-build/log/msgs/25786e.md:82`（25786e・`log/events.log:186`）
  - `projects/p6-org-build/log/msgs/4d8609.md:82`（4d8609・`log/events.log:198`）

[↑ 目次へ](#目次)

<a id="i13"></a>

### 13. charter・ヒント・パックに書かれた前提が実物と違った（無いファイル・食い違う指示・件数）

- 分類: 文脈パック
- 回数: 2 プロジェクト（p4・p5）・記録 6
- 状態: 不明 — 直した記録が見つからない。p6 以降の記録には同じ形の申告が無い（p9 の閉じる側の誤りは「p9 のチームの完了条件で、閉じる側を PM と書いていた」に分けた）
- 起きたこと: p4 の charter が「job の org/context.yaml」を指したが job には無く、PM が dev-tools のものと読み替えた。p4 のヒントは退避を cp で、パックは Write でと食い違い、.claude/skills/ は Bash から書けなかった。p5 のパックは「p5 は報告ゼロ」としたが、片づいたコーディネーターの報告が 1 件あった。
- 参照元:
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__pm-7fcade93.yaml:71`
  - `projects/p4-job-run-use/log/msgs/3b3654.md:40`（3b3654・`log/events.log:73`）
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__leader-8e4fdd93.yaml:63`
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__worker-1-b93bc6f4.yaml:60`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__leader-6f1c1b6b.yaml:77`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:72`

[↑ 目次へ](#目次)

<a id="i14"></a>

### 14. 読み取り拒否の場所に grep・stat が届かず、洗い出し・確かめが言い切れない

- 分類: 文脈パック
- 回数: 2 プロジェクト（p4・p8）・記録 5
- 状態: 不明 — 直した記録が見つからない。p9 の記録には同じ申告が無い
- 起きたこと: p4 で tasks/・self-tasks/・**/_history/ などが読み取り拒否で grep が届かず、参照を全件洗い出せたとは言えなかった（manager.yaml 15 行目のコメントは未確認）。p8 では、サンドボックスが hints/ と worker-*/CLAUDE.md の stat を拒否し、不変の確かめから外した。
- 参照元:
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__reviewer-05ac7e08.yaml:49`
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__teams__run-use-thin__worker-1-b93bc6f4.yaml:61`
  - `projects/p4-job-run-use/log/msgs/3b3654.md:35`（3b3654・`log/events.log:73`）
  - `projects/p4-job-run-use/log/msgs/74b9f7.md:37`（74b9f7・`log/events.log:62`）
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-export-fff11e32.yaml:398`

[↑ 目次へ](#目次)

<a id="i15"></a>

### 15. 組織を直すプロジェクトの最中は、動いている本体の規範・orgctl が直す前のままで、上書きや使い分けが要った

- 分類: 規範の書き方
- 回数: 2 プロジェクト（p7・p9）・記録 4
- 状態: 印なし — 直した記録が見つからず、p9 まで起きている
- 起きたこと: p7 では、コーディネーターの規範（本体）が古い流れのままで、PM が相談の本文で「改めた後の形で動いて」と上書きした。p9 では、本体の orgctl で監査役を assign すると古い立場が入るので、worktree の orgctl で assign する前提をパックに書いたが、両方を混ぜて同じ記録に書いてよいかは決まりに無かった。
- 参照元:
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:65`
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__pm-1c125b2e.yaml:72`
  - `projects/p7-coordinator-role/log/msgs/be01fb.md:45`（be01fb・`log/events.log:76`）
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__coordinator-37d1062a.yaml:63`

[↑ 目次へ](#目次)

<a id="i16"></a>

### 16. 1 行報告を読む道具が、数えるための行（NOISE_KINDS）を自前で持ち、orgctl とずれる

- 分類: 道具
- 回数: 2 プロジェクト（p3・p5）・記録 4
- 状態: 印なし — NOISE_KINDS を正とする説明は PR #2（f394306）で README に入ったが、p5 で道具のずれが再び書かれた
- 起きたこと: p3 の時系列の道具は数えるための行を p1・p2 のログから自前で決めたため、あとで増えた notify_skipped が漏れ、人の報告の列 31 件中 11 件を占めた（review_ng 6acb52）。p5 でも ai-org の tools/org_status.py・org_timeline.py が NOISE_KINDS を自前で持ち、orgctl とずれていると書かれた。
- 参照元:
  - `projects/p3-org-visibility/log/msgs/6acb52.md:4`（6acb52・`log/events.log:87`）
  - `projects/p3-org-visibility/log/msgs/95df09.md:20`（95df09・`log/events.log:126`）（別の出どころ。数えない）
  - `projects/p5-org-viewer/log/msgs/146e61.md:32`（146e61・`log/events.log:110`）
  - `projects/p5-org-viewer/log/msgs/17b6a4.md:32`（17b6a4・`log/events.log:15`）
  - `projects/p5-org-viewer/log/msgs/2140aa.md:33`（2140aa・`log/events.log:120`）

[↑ 目次へ](#目次)

<a id="i17"></a>

### 17. 根っこ（user）にはタブが無く、user 宛ての report・wrap_up に Orca の知らせが出ない

- 分類: 連絡
- 回数: 2 プロジェクト（p1・p2）・記録 3
- 状態: 直った — user 宛ては受け箱 log/user-inbox.yaml と Google Chat に出す形が PR #2（f394306、10-23 14:07）で入り、p4〜p9 に同じ申告が無い
- 起きたこと: p1・p2 で PM が user へ report を出しても、user にはタブが無いので知らせが出なかった。user が気づく経路が決まりに書かれていなかった。
- 参照元:
  - `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:76`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__pm-0775601b.yaml:70`
  - `projects/p2-orca-run-use/log/msgs/7ad811.md:59`（7ad811・`log/events.log:82`）

[↑ 目次へ](#目次)

<a id="i18"></a>

### 18. 同じ立場が複数いるときの名前（コーディネーター・パックのファイル名）の付け方が決まりに無い

- 分類: 規範の書き方
- 回数: 2 プロジェクト（p7・p8）・記録 2
- 状態: 印なし — p7 の分は PR #11 で coordinator-<チーム名> が廃止されたが、p8 で同じ立場が 2 人のときのパックの名前が決まっていなかった
- 起きたこと: p7 では、本体の古い手順が coordinator-<チーム名> を前提にしていたが名前 coordinator で assign した。p8 では、作業者 2・レビュアー 2 のチームでパック packs/<チーム名>/<立場>.md の名前が決まらず、worker-ui.md のように名前で置いた。
- 参照元:
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__pm-1c125b2e.yaml:74`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__coordinator-087f6e79.yaml:68`

[↑ 目次へ](#目次)

<a id="i19"></a>

### 19. PM の `wait` が配下のやりとり（cc）でも戻り、自分宛てが来るまで打ち直した

- 分類: 連絡
- 回数: 2 プロジェクト（p5・p6）・記録 2
- 状態: 不明 — 直した記録が見つからない。p7 以降の記録には同じ申告が無い
- 起きたこと: p5・p6 の PM が、`wait` が自分宛てでない配下のやりとりでも戻るため、何度も打ち直した。cc で戻ることが決まりに書かれているか分からなかった。
- 参照元:
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__pm-92edb217.yaml:82`
  - `projects/p6-org-build/reports/sessions/p6-org-build__pm-16bc79bc.yaml:86`

[↑ 目次へ](#目次)

<a id="i20"></a>

### 20. パックの deny は Read の拒否だけで、grep（Bash）では見え、glob でしか書けない

- 分類: 文脈パック
- 回数: 2 プロジェクト（p4・p6）・記録 2
- 状態: 不明 — 直した記録が見つからない。p7 以降の記録には同じ申告が無い
- 起きたこと: p4 では、パックの deny が Read の拒否なので、grep では self-tasks/ などの行が見えた。p6 では「job は 1 ファイルだけ読める」を直接書けず、job のディレクトリを列挙して deny した（新しいディレクトリが増えると漏れる）。
- 参照元:
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__coordinator-run-use-thin-ad0d46dd.yaml:60`
  - `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-org-build-b422e51c.yaml:68`

[↑ 目次へ](#目次)

<a id="i21"></a>

### 21. 受け持ち（プランの決まったこと 22 を誰が書くか）が作業者に明示されず、review_ng で初めて決まった

- 分類: 文脈パック
- 回数: 1 プロジェクト（p9）・記録 7
- 状態: 印なし — 直した記録が見つからない。p9 が最後に閉じたプロジェクト
- 起きたこと: p9 のパックは 22 の補足を「worker-watch の承認のあと、リーダーの start を受けて worker-audit が書く」と分けていたが、作業者 2 人には始めから明示されていなかった。レビュアーが両方の review_ng で同じ点を出し、結果として 22 には 2 人とも書いた。リーダー・レビュアー・worker-audit の 3 人が同じことを書いている。
- 参照元:
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__leader-36cfe0d2.yaml:66`
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__reviewer-512bbb7a.yaml:59`
  - `projects/p9-org-watch/log/msgs/26be36.md:36`（26be36・`log/events.log:110`）
  - `projects/p9-org-watch/log/msgs/299393.md:17`（299393・`log/events.log:65`）
  - `projects/p9-org-watch/log/msgs/635d9b.md:51`（635d9b・`log/events.log:121`）
  - `projects/p9-org-watch/log/msgs/6eccb0.md:13`（6eccb0・`log/events.log:77`）
  - `projects/p9-org-watch/log/msgs/cc2161.md:10`（cc2161・`log/events.log:71`）
  - `projects/p9-org-watch/reports/audit/p9-org-watch.md:9`（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i22"></a>

### 22. 実データに判断待ち・止まっているものが無く、その見た目を写しでしか確かめられない

- 分類: レビュー
- 回数: 1 プロジェクト（p8）・記録 6
- 状態: 不明 — 直した記録が見つからない。p9 は画面を撮るチームでなかった
- 起きたこと: p8 で、判断待ち・止まっているものがある状態は実データに無く、作業者が scratchpad の写しにデータを足して撮った画像でしか見ていない。規則は閉じたプロジェクトでだけ当てて確かめた。job の控えにも申し送りとして書かれている。
- 参照元:
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-kawasaki-d30b4812.yaml:396`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:437`
  - `projects/p8-viewer-rebuild/log/msgs/3df696.md:86`（3df696・`log/events.log:134`）
  - `projects/p8-viewer-rebuild/log/msgs/3df696.md:103`（3df696・`log/events.log:134`）
  - `projects/p8-viewer-rebuild/log/msgs/a5676d.md:51`（a5676d・`log/events.log:97`）
  - `projects/p8-viewer-rebuild/log/msgs/b20186.md:64`（b20186・`log/events.log:145`）
  - `job:company/system/ai-org/README.md:59`（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i23"></a>

### 23. ~/.npm のキャッシュの権限が壊れていて npm install が失敗する

- 分類: 環境
- 回数: 1 プロジェクト（p5）・記録 6
- 状態: 不明 — 直した記録が見つからない。p6 以降の記録には同じ申告が無い
- 起きたこと: p5 の作業者が `--cache` を TMPDIR に向けて回避した。レビュアー・リーダーも同じことを書いた。
- 参照元:
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__reviewer-11df580d.yaml:65`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml:91`
  - `projects/p5-org-viewer/log/msgs/146e61.md:29`（146e61・`log/events.log:110`）
  - `projects/p5-org-viewer/log/msgs/2140aa.md:30`（2140aa・`log/events.log:120`）
  - `projects/p5-org-viewer/log/msgs/87b487.md:20`（87b487・`log/events.log:50`）
  - `projects/p5-org-viewer/log/msgs/b8283e.md:11`（b8283e・`log/events.log:76`）

[↑ 目次へ](#目次)

<a id="i24"></a>

### 24. 全員が wait に入って止まり、見張りは全員待ちとしては出さなかった（待っている PM を「ループ?」として出した）

- 分類: 見張り
- 回数: 1 プロジェクト（p8）・記録 5
- 状態: 不明 — 全員待ちを止まりと判定する直しと、待っている人を「待っている」と出す直しは PR #14（9bb11a5、10-24 18:56）で入ったが、そのあとに閉じたプロジェクトが無い
- 起きたこと: p8 のリーダーがメンバー 4 人の done を 16:26 に読んだあと、PM へ report を出さずに wait に戻った。PM もリーダーを待っていて、全員が待つ形で止まった。patrol は 16:29:37 に PM を「ループ?（出力はあるが状態が変わらない）のまま 20 分」として stuck を受け箱に置き Google Chat へも送ったが、全員が待っている形としては出さなかった。根っこの 15 分おきの見張りが見つけ、16:30:56 にリーダーへ nudge を出して動かした。job の控えは p6 の研究チームのリーダーも約 9 分止まったと書いている（p6 の PM の報告は「作業中だっただけ」）。
- 参照元:
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml:406`
  - `projects/p8-viewer-rebuild/log/msgs/176526.md:2`（176526・`log/events.log:127`）
  - `projects/p8-viewer-rebuild/log/msgs/3df696.md:94`（3df696・`log/events.log:134`）
  - `projects/p8-viewer-rebuild/log/msgs/b20186.md:71`（b20186・`log/events.log:145`）
  - `projects/p8-viewer-rebuild/log/user-inbox.yaml:1`
  - `job:company/system/ai-org/README.md:28`（別の出どころ。数えない）
  - `job:company/system/ai-org/README.md:36`（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i25"></a>

### 25. 画面を撮るとき、作業者の待ち受けを使うのか自分で立てるのかが screen-check.md に無い（ビルドし直すと 404）

- 分類: 道具
- 回数: 1 プロジェクト（p8）・記録 5
- 状態: 不明 — 直した記録が見つからない。p9 は画面を撮るチームでなかった
- 起きたこと: p8 のレビュアー・リーダーは 2 人とも dist を python の http.server で自分のポートに立てて撮った。astro preview はビルドし直すと新しいファイルを 404 で返し、作業者はビルドのたびに待ち受けを立て直した。
- 参照元:
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml:407`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-kawasaki-d30b4812.yaml:400`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:434`
  - `projects/p8-viewer-rebuild/log/msgs/3df696.md:95`（3df696・`log/events.log:134`）
  - `projects/p8-viewer-rebuild/log/msgs/b20186.md:72`（b20186・`log/events.log:145`）

[↑ 目次へ](#目次)

<a id="i26"></a>

### 26. screen-probe が本文の Markdown の表も折り返しの候補に数え、印を押して出る引き出しを撮れない

- 分類: 道具
- 回数: 1 プロジェクト（p8）・記録 5
- 状態: 不明 — 直した記録が見つからない。p9 は画面を撮るチームでなかった
- 起きたこと: p8 で、screen-probe は td・th の折り返しを一律に数え、本文パネルの表も C-11 の候補に出した。「開いた状態」は details・aria-expanded だけで、引き出しは別のスクリプトで撮った。
- 参照元:
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml:408`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:435`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__worker-ui-6155b5d5.yaml:436`
  - `projects/p8-viewer-rebuild/log/msgs/3df696.md:96`（3df696・`log/events.log:134`）
  - `projects/p8-viewer-rebuild/log/msgs/b20186.md:73`（b20186・`log/events.log:145`）

[↑ 目次へ](#目次)

<a id="i27"></a>

### 27. チェックリストの設計の段（B）に「押せる大きさと間隔」が無く、設計で通した配置が画面で押せない印になった

- 分類: レビュー
- 回数: 1 プロジェクト（p8）・記録 5
- 状態: 不明 — 直した記録が見つからない。p9 は画面を撮るチームでなかった
- 起きたこと: p8 で、設計の段で同じ時刻の印を 4px ずらす案を通したが、画面の段で重なった印の下に隠れて押せない印になり、review_ng で差し戻した。
- 参照元:
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__leader-18b4f46a.yaml:409`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-kawasaki-d30b4812.yaml:399`
  - `projects/p8-viewer-rebuild/log/msgs/3df696.md:97`（3df696・`log/events.log:134`）
  - `projects/p8-viewer-rebuild/log/msgs/931330.md:10`（931330・`log/events.log:91`）
  - `projects/p8-viewer-rebuild/log/msgs/b20186.md:74`（b20186・`log/events.log:145`）

[↑ 目次へ](#目次)

<a id="i28"></a>

### 28. 作業者が手書きデータの版で先に review_request を出し、実物の版と 2 通になって往復が 1 回増えた

- 分類: レビュー
- 回数: 1 プロジェクト（p5）・記録 5
- 状態: 不明 — 直した記録が見つからない。p6 以降の記録には同じ申告が無い
- 起きたこと: p5 のビューアの作業者が、手書きの snapshot で作った版を先にレビューへ出し、実物が届いて差し替えた版をもう 1 通出した。レビュアーはどれを判定するかをリーダーの start を読むまで決められず、リーダーも判定させるかで迷った。
- 参照元:
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__leader-6f1c1b6b.yaml:78`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__reviewer-11df580d.yaml:63`
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-viewer-3cf48c51.yaml:94`
  - `projects/p5-org-viewer/log/msgs/146e61.md:41`（146e61・`log/events.log:110`）
  - `projects/p5-org-viewer/log/msgs/2140aa.md:37`（2140aa・`log/events.log:120`）

[↑ 目次へ](#目次)

<a id="i29"></a>

### 29. レビュアーの承認のあとにリーダーが rework を出したとき、レビュアーがもう一度見るかが決まりに無かった

- 分類: レビュー
- 回数: 1 プロジェクト（p2）・記録 5
- 状態: 直った — レビュアーとリーダーの決まりに rework のあとの流れが入った（df25d5b、PR #1、10-23 12:51）。p3〜p9 に同じ迷いの記録が無い（p3 の監査役も繰り返していないと照合）
- 起きたこと: p2 で review_ok のあとにリーダーが rework を出し、作業者の第3版がレビュアーに来た。レビュアーは 2 回目の review_ok を出すかを迷い、出した。PM・リーダーも同じ点を書いた。
- 参照元:
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__pm-0775601b.yaml:69`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__leader-70bafeda.yaml:67`
  - `projects/p2-orca-run-use/reports/sessions/p2-orca-run-use__teams__run-use-fix__reviewer-f7de4d8b.yaml:59`
  - `projects/p2-orca-run-use/log/msgs/1f7fb5.md:73`（1f7fb5・`log/events.log:68`）
  - `projects/p2-orca-run-use/log/msgs/7ad811.md:57`（7ad811・`log/events.log:82`）

[↑ 目次へ](#目次)

<a id="i30"></a>

### 30. 「閉じる並び」を review_request に入れるのか最終報告に入れるのかを、作業者がパックから読み取れなかった

- 分類: 文脈パック
- 回数: 1 プロジェクト（p9）・記録 4
- 状態: 印なし — 直した記録が見つからない。p9 が最後に閉じたプロジェクト
- 起きたこと: p9 の worker-audit が、完了条件 4 の「p9 を閉じる並び」の置き場が読み取れず、レビュアーの review_ng（まだ報告に無い）で review_request に入れると分かった。
- 参照元:
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-audit-6bc5c166.yaml:61`
  - `projects/p9-org-watch/log/msgs/26be36.md:38`（26be36・`log/events.log:110`）
  - `projects/p9-org-watch/log/msgs/635d9b.md:53`（635d9b・`log/events.log:121`）
  - `projects/p9-org-watch/log/msgs/f08c2f.md:10`（f08c2f・`log/events.log:59`）

[↑ 目次へ](#目次)

<a id="i31"></a>

### 31. 同じファイル（orgctl.py）を 2 人で同時に直し、Edit の衝突と受け持ちの外への手入れが起きた

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p9）・記録 4
- 状態: 印なし — 直した記録が見つからない。p9 が最後に閉じたプロジェクト
- 起きたこと: p9 で作業者 2 人が orgctl.py を関数で分けて同時に直した。worker-watch は Edit が「読んだあとに変わった」で止まり続け、1 度 Python でファイルを読み書きして置き換えた（パックは Edit で差分だけ）。試しのために受け持ちの関数の外（projects_dir）にも手を入れた。どちらも unclear に書かれ、escalate は出ていない。
- 参照元:
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-watch-f06de01a.yaml:70`
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__teams__watch__worker-watch-f06de01a.yaml:71`
  - `projects/p9-org-watch/log/msgs/26be36.md:37`（26be36・`log/events.log:110`）
  - `projects/p9-org-watch/log/msgs/635d9b.md:52`（635d9b・`log/events.log:121`）
  - `projects/p9-org-watch/reports/audit/p9-org-watch.md:13`（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i32"></a>

### 32. 指摘の回数（3 回まで）を、design.md の段と画面の段で通算するかが決まりに無い

- 分類: レビュー
- 回数: 1 プロジェクト（p8）・記録 4
- 状態: 不明 — 直した記録が見つからない。p9 は 2 段で見るチームでなかった
- 起きたこと: p8 で 2 段（設計・画面）で見たチームのレビュアーが、指摘の回数を通算で数えた（差し戻し 2・承認 2）。コーディネーター・リーダーも、2 段で見るチームでは上限に早く当たりうると書いた。
- 参照元:
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__coordinator-087f6e79.yaml:69`
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-kawasaki-d30b4812.yaml:398`
  - `projects/p8-viewer-rebuild/log/msgs/3df696.md:98`（3df696・`log/events.log:134`）
  - `projects/p8-viewer-rebuild/log/msgs/b20186.md:75`（b20186・`log/events.log:145`）

[↑ 目次へ](#目次)

<a id="i33"></a>

### 33. 往復の「合意」と「返し」が同じ report の種類で、種類だけでは見分けられない

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p7）・記録 4
- 状態: 印なし — 直した記録が見つからず、p8・p9 でも合意は report で出ている（log/msgs/c03dcf.md・log/msgs/544cc1.md）
- 起きたこと: p7 で PM が合意を report で出したので、コーディネーターの返しと合意が種類だけでは見分けられず、本文の先頭で見分けた。job の控えにも残ったこととして書かれている。
- 参照元:
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__pm-1c125b2e.yaml:73`
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__teams__coordinator-flow__leader-e917435e.yaml:67`
  - `projects/p7-coordinator-role/log/msgs/2e8018.md:54`（2e8018・`log/events.log:65`）
  - `projects/p7-coordinator-role/log/msgs/be01fb.md:46`（be01fb・`log/events.log:76`）
  - `job:company/system/ai-org/README.md:53`（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i34"></a>

### 34. コーディネーターの終わり方と、返しに書くもの（実現できる理由・崩れる前提）が規範に無かった

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p7）・記録 4
- 状態: 直った — 終わり方（wrap_up で終わる）と返すもの 3 が PR #11（5c1bcd2）で規範に入り、p8・p9 に同じ申告が無い
- 起きたこと: p7 のコーディネーターは、合意のあと PM の作成・assign が済むまで残って wrap_up で終えた。返しに「この編成で実現できる理由」と「崩れる前提」を書く決まりが無く、自分で足した。
- 参照元:
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:68`
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:71`
  - `projects/p7-coordinator-role/log/msgs/4d25e4.md:40`（4d25e4・`log/events.log:13`）
  - `projects/p7-coordinator-role/log/msgs/4d25e4.md:43`（4d25e4・`log/events.log:13`）

[↑ 目次へ](#目次)

<a id="i35"></a>

### 35. パックの deny に $TMPDIR のパスを書くと /tmp のまま入り、ヒントの deny は /private/tmp になる

- 分類: 文脈パック
- 回数: 1 プロジェクト（p7）・記録 4
- 状態: 不明 — 直した記録が見つからない。p8 以降の記録には同じ申告が無い
- 起きたこと: p7 で、パックの deny とヒントの deny とで /tmp と /private/tmp（macOS のリンク）が食い違った。試しの場所だけの話で直していない。
- 参照元:
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__teams__coordinator-flow__worker-1-32df2698.yaml:74`
  - `projects/p7-coordinator-role/log/msgs/2e8018.md:44`（2e8018・`log/events.log:65`）
  - `projects/p7-coordinator-role/log/msgs/891118.md:66`（891118・`log/events.log:33`）
  - `projects/p7-coordinator-role/log/msgs/be01fb.md:47`（be01fb・`log/events.log:76`）

[↑ 目次へ](#目次)

<a id="i36"></a>

### 36. リーダーの `wait --cc` が、作業者 → 未起動のレビュアーの review_request を拾わず、約 10 分止まった

- 分類: 連絡
- 回数: 1 プロジェクト（p1）・記録 4
- 状態: 直った — wait が「宛先がまだ起きていない配下宛て」で目を覚ます処理（orgctl.py の pending）が PR #1（130f642、10-23 12:51）で main に入り、p3〜p9 に同じ申告が無い
- 起きたこと: p1 で作業者がレビュアーへ review_request を出したが、レビュアーはまだ起きておらず、リーダーの `wait --cc` はそれを拾わずに 9 分の時間切れで戻った。レビュアーの起動が約 10 分遅れ、PM の確認で気づいた。
- 参照元:
  - `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:70`
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__leader.yaml:66`
  - `projects/p1-org-status/log/msgs/803ffb.md:45`（803ffb・`log/events.log:75`）
  - `projects/p1-org-status/log/msgs/d9ba25.md:39`（d9ba25・`log/events.log:61`）

[↑ 目次へ](#目次)

<a id="i37"></a>

### 37. プランの「立場」の表と P3 の完了の目安が、監査役の新しい形（起きたことだけを書く）と食い違ったまま

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p9）・記録 3
- 状態: 印なし — 今の dev-tools のプラン（docs/todo/ai-org-plan.md の 125・258 行）も改訂案のまま
- 起きたこと: p9 で監査役の出力を「起きたことと参照元」に変えたが、プランの「立場」の表（監査役の上げること: 雛形の改訂案）と P3 の完了の目安（改訂案が雛形に 1 回以上入る）は元のまま残った。リーダー・PM・レビュアーが書いている。
- 参照元:
  - `projects/p9-org-watch/log/msgs/26be36.md:32`（26be36・`log/events.log:110`）
  - `projects/p9-org-watch/log/msgs/5904f6.md:11`（5904f6・`log/events.log:86`）
  - `projects/p9-org-watch/log/msgs/635d9b.md:47`（635d9b・`log/events.log:121`）

[↑ 目次へ](#目次)

<a id="i38"></a>

### 38. `orgctl export --check` を `--out` と一緒に打つと、書き出し直してから検査する

- 分類: 道具
- 回数: 1 プロジェクト（p8）・記録 3
- 状態: 不明 — 直した記録が見つからない。p9 の記録には同じ申告が無い
- 起きたこと: p8 で、壊した写しを検査しようとして `--check` と `--out` を併用すると写しが上書きされ、`--check <path>` 単独で打つ必要があった。
- 参照元:
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__teams__viewer__reviewer-export-baf05c27.yaml:388`
  - `projects/p8-viewer-rebuild/log/msgs/3df696.md:99`（3df696・`log/events.log:134`）
  - `projects/p8-viewer-rebuild/log/msgs/b20186.md:76`（b20186・`log/events.log:145`）

[↑ 目次へ](#目次)

<a id="i39"></a>

### 39. 文脈の台帳（context.yaml）に、題材が組織そのもの（ai-org・dev-tools の org）のときに読む先が無い

- 分類: 文脈パック
- 回数: 1 プロジェクト（p5）・記録 3
- 状態: 不明 — 今の context.yaml にも行は無い（直した記録なし）。p6 以降の記録には同じ申告が無い
- 起きたこと: p5 のコーディネーターが、台帳の allow が job だけなので、charter の範囲を根拠に ai-org・dev-tools を読ませた。
- 参照元:
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__coordinator-viewer-2d6b3d7c.yaml:60`
  - `projects/p5-org-viewer/log/msgs/17b6a4.md:33`（17b6a4・`log/events.log:15`）
  - `projects/p5-org-viewer/log/msgs/2140aa.md:41`（2140aa・`log/events.log:120`）

[↑ 目次へ](#目次)

<a id="i40"></a>

### 40. 見本の id が根っこの親ディレクトリ基準（rel_id）で、見本のディレクトリ名を揃える必要が決まりに書かれていない

- 分類: 道具
- 回数: 1 プロジェクト（p1）・記録 3
- 状態: 不明 — 直した記録が見つからない。p2 以降の記録には同じ申告が無い
- 起きたこと: p1 の作業者が、最初のテストで失敗して気づいた。
- 参照元:
  - `projects/p1-org-status/reports/sessions/p1-org-status__teams__status-tool__worker-1.yaml:56`
  - `projects/p1-org-status/log/msgs/803ffb.md:50`（803ffb・`log/events.log:75`）
  - `projects/p1-org-status/log/msgs/d9ba25.md:43`（d9ba25・`log/events.log:61`）

[↑ 目次へ](#目次)

<a id="i41"></a>

### 41. p9 のチームの完了条件で、閉じる側を PM と書いていた（根っこなので閉じるのは user）

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p9）・記録 2
- 状態: 印なし — 直した記録が見つからない。p9 が最後に閉じたプロジェクト
- 起きたこと: p9 の PM がチームの charter の完了条件 4 に「PM がそのとき打つコマンド」を足して渡し、作業者はその文のとおり「閉じる側＝PM」の並びを出した。リーダーが後から「閉じるのは根っこのセッション（user）」と直させた。PM は、誰が打つかの線が charter から読み取りにくかったと書いた。
- 参照元:
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__pm-f743150d.yaml:70`
  - `projects/p9-org-watch/log/msgs/299393.md:15`（299393・`log/events.log:65`）
  - `projects/p9-org-watch/reports/audit/p9-org-watch.md:5`（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i42"></a>

### 42. 監査役の参照元の形（1 行に複数・バッククォート付き）が、export の refs で 1 件に潰れる

- 分類: 道具
- 回数: 1 プロジェクト（p9）・記録 2
- 状態: 不明 — p9 の中で直したが、マージ（PR #14）のあとに閉じたプロジェクトが無い
- 起きたこと: p9 のレビュアーが、position.md の形どおりに書いた参照元が audit_findings の refs で 1 件（バッククォートと「・」が中に残る）になると指摘した。監査役本人も、括弧で添えた形がどう割れるかは確かめていないと書いた。
- 参照元:
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__auditor-272c70db.yaml:48`
  - `projects/p9-org-watch/log/msgs/f08c2f.md:8`（f08c2f・`log/events.log:59`）

[↑ 目次へ](#目次)

<a id="i43"></a>

### 43. 文脈パックが charter より先に書かれ、まだ無い charter を指した

- 分類: 文脈パック
- 回数: 1 プロジェクト（p7）・記録 2
- 状態: 直った — コーディネーターの返すもの 4「チームごとに charter に入れてほしいこと」が PR #11（5c1bcd2、10-24 15:30）で入り、p8・p9 に同じ申告が無い
- 起きたこと: p7 のコーディネーターが、チームの charter ができる前にパックを書いた。パックと完了条件がずれないよう、自分で「charter に入れてほしいこと」を添えた。
- 参照元:
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:66`
  - `projects/p7-coordinator-role/log/msgs/4d25e4.md:38`（4d25e4・`log/events.log:13`）

[↑ 目次へ](#目次)

<a id="i44"></a>

### 44. コーディネーターと PM の往復で使う event の種類が決まっていなかった

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p7）・記録 2
- 状態: 直った — コーディネーターの決まりに「往復のしかた（event の種類）」の表が PR #11（5c1bcd2）で入り、p8・p9 に同じ申告が無い
- 起きたこと: p7 で、相談を start、返しを report で出した。PM が視点を足して返すときの種類も決まっていなかった。
- 参照元:
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:67`
  - `projects/p7-coordinator-role/log/msgs/4d25e4.md:39`（4d25e4・`log/events.log:13`）

[↑ 目次へ](#目次)

<a id="i45"></a>

### 45. orgctl new がチームにも packs/ を作り、新しい流れでは空のまま残った

- 分類: 道具
- 回数: 1 プロジェクト（p7）・記録 2
- 状態: 直った — orgctl new が packs/ をプロジェクトにだけ作る直しが PR #11（5c1bcd2）で入り、p8・p9 に同じ申告が無い
- 起きたこと: p7 で、チームの packs/ が使われず空のままになった。
- 参照元:
  - `projects/p7-coordinator-role/reports/sessions/p7-coordinator-role__coordinator-d243a674.yaml:70`
  - `projects/p7-coordinator-role/log/msgs/4d25e4.md:42`（4d25e4・`log/events.log:13`）

[↑ 目次へ](#目次)

<a id="i46"></a>

### 46. p5 の画面の確かめが、明るい表示・幅 1400px の 1 枚だけだった

- 分類: レビュー
- 回数: 1 プロジェクト（p6）・記録 2
- 状態: 直った — 撮る幅・ダークを含む screen-check.md が PR #10（54385d3、10-24 15:05）で入り、p8 のレビュアーは 900・1800px・ダークで撮った（log/msgs/931330.md:4）
- 起きたこと: p6 の研究チームが p5 の画面の判定を見直すと、撮影は明るい表示・1400px の 1 枚だけで、900／1800px・cursor・フォーカスの項目は未取得、1800px の問いも 1400px の画像から判定していた。
- 参照元:
  - `projects/p6-org-build/log/msgs/dd1184.md:28`（dd1184・`log/events.log:128`）
  - `projects/p6-org-build/log/msgs/dd1184.md:30`（dd1184・`log/events.log:128`）

[↑ 目次へ](#目次)

<a id="i47"></a>

### 47. 調べもの・出典の裏取りが本業の職種が台帳に無く、リーダーの職種なしが許されるかも書かれていない

- 分類: 文脈パック
- 回数: 1 プロジェクト（p6）・記録 2
- 状態: 不明 — 直した記録が見つからない（PR #10 で足した職種は ui-designer）。p7 以降の記録には同じ申告が無い
- 起きたこと: p6 のコーディネーターは調べものの職種が無いので strategy で代えた。PM は研究チームのリーダーを職種なし（-）で起こしたが、それが台帳の上で許されるか決まりに無かった。
- 参照元:
  - `projects/p6-org-build/reports/sessions/p6-org-build__coordinator-uiux-research-057eafed.yaml:66`
  - `projects/p6-org-build/reports/sessions/p6-org-build__pm-16bc79bc.yaml:88`

[↑ 目次へ](#目次)

<a id="i48"></a>

### 48. assign でペルソナを重ねて指定すると、黙って 1 つにまとめる（README に書かれていない）

- 分類: 道具
- 回数: 1 プロジェクト（p6）・記録 2
- 状態: 不明 — 直した記録が見つからない。p7 以降の記録には同じ申告が無い
- 起きたこと: p6 で、同名のペルソナを重ねたときに黙って 1 つにまとめる動きが文書に無いと、レビュアーと PM が書いた。
- 参照元:
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__reviewer-b8082b46.yaml:75`
  - `projects/p6-org-build/log/msgs/25786e.md:67`（25786e・`log/events.log:186`）

[↑ 目次へ](#目次)

<a id="i49"></a>

### 49. 規範から org/ の資料を辿る書き方が「orgctl のパスから scripts/orgctl.py を外した所」になった

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p6）・記録 2
- 状態: 不明 — 直した記録が見つからない。p7 以降の記録には同じ申告が無い
- 起きたこと: p6 で、規範から org/common/... を指すのに、システムプロンプトの orgctl のパスから辿る書き方になった。雛形の場所が台帳の行で出ているのはコーディネーターだけだった。
- 参照元:
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-norms-7bbd0aab.yaml:93`
  - `projects/p6-org-build/log/msgs/25786e.md:74`（25786e・`log/events.log:186`）

[↑ 目次へ](#目次)

<a id="i50"></a>

### 50. JavaScript で描くページを WebFetch で読めず、出典の裏取りがほかの道頼みになった

- 分類: 環境
- 回数: 1 プロジェクト（p6）・記録 2
- 状態: 不明 — 直した記録が見つからない。p7 以降の記録には同じ申告が無い
- 起きたこと: p6 の研究チームの作業者が、Material Design・NN/g の一部のページを WebFetch で取れず（JavaScript 描画・404）、K-02 の値は Gemini の回答だけになった。WebFetch 以外の道（ブラウザ）を使ってよいかは決まりに無かった。
- 参照元:
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__worker-1-833d6b72.yaml:71`
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__uiux-research__worker-1-833d6b72.yaml:74`

[↑ 目次へ](#目次)

<a id="i51"></a>

### 51. 承認のときにも thread.md に追記するかが決まりに無かった

- 分類: レビュー
- 回数: 1 プロジェクト（p3）・記録 2
- 状態: 直った — レビュアーの決まりの 4 に承認のときの追記が PR #2（f394306）で入り、p4〜p9 に同じ申告が無い
- 起きたこと: p3 のレビュアー 2 人が、承認のときに thread.md へ追記するかが決まりに無い（指摘のときだけ）と同じ迷いを書き、どちらも自分の判断で追記した。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__reviewer-10b48465.yaml:62`
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__reviewer-8d87b16a.yaml:63`
  - `projects/p3-org-visibility/log/msgs/95df09.md:16`（95df09・`log/events.log:126`）（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i52"></a>

### 52. 並行する別チームの成果物を、できる前に前提にして書いた

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p3）・記録 2
- 状態: 不明 — 直した記録が見つからない。p4 以降の記録には同じ申告が無い
- 起きたこと: p3 の readme-guide の作業者は、別チームが作成中の tools/org_timeline.py を確かめられず、charter の形を前提に README を書いた。最終形が変わったら合わせると申し送った。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__worker-1-7f90e6d2.yaml:64`
  - `projects/p3-org-visibility/log/msgs/258cd4.md:23`（258cd4・`log/events.log:50`）

[↑ 目次へ](#目次)

<a id="i53"></a>

### 53. 同じ人が 2 回起動すると、セッション報告が 1 ファイルに上書きされた

- 分類: 道具
- 回数: 1 プロジェクト（p3）・記録 2
- 状態: 直った — セッション報告のファイル名にセッション id を付ける形が PR #1（00ee87a、10-23 12:51）で main に入り、p2〜p9 はその形。p3〜p9 に同じ申告が無い
- 起きたこと: p1 の PM は 2 回起動したが、セッション報告は p1-org-status__pm.yaml 1 つに上書きされ、2 回目の分しか残っていなかった（p3 の時系列の道具を作るときに分かった）。
- 参照元:
  - `projects/p3-org-visibility/log/msgs/c76d01.md:31`（c76d01・`log/events.log:110`）
  - `projects/p3-org-visibility/log/msgs/f315e9.md:13`（f315e9・`log/events.log:70`）

[↑ 目次へ](#目次)

<a id="i54"></a>

### 54. PM の入れ替えで、前の PM の状況が新しい PM に引き継がれなかった

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p1）・記録 2
- 状態: 直った — 入れ替えは元のパックに経緯の 1 枚（--digest）を付けて渡す形が PR #5（6642b87、10-24 00:25）で入り、p4〜p9 に同じ申告が無い
- 起きたこと: p1 の最初の PM は 11 分で入れ替えになり（自己申告なし、charter.md だけ変えていた）、新しい PM には前の PM の状況の引き継ぎが来なかった。新しい PM はセッション報告の files_changed_in_window から推した。
- 参照元:
  - `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:75`
  - `projects/p1-org-status/log/msgs/803ffb.md:49`（803ffb・`log/events.log:75`）

[↑ 目次へ](#目次)

<a id="i55"></a>

### 55. PM が検収で、本物の ai-org/projects に書き込みのある patrol --dry を打った

- 分類: 人の操作
- 回数: 1 プロジェクト（p9）・記録 1
- 状態: 印なし — 直した記録が見つからない。p9 が最後に閉じたプロジェクト
- 起きたこと: `patrol --dry` は受け箱と .patrol.json に書く作り。p9 のリーダーはそれを理由に本物の projects/ には打たなかったが、PM は検収で `patrol --projects <ai-org>/projects --once --dry` を打った（何も出なかった）。チームの範囲では projects/ は読むだけ。
- 参照元:
  - `projects/p9-org-watch/reports/sessions/p9-org-watch__pm-f743150d.yaml:71`
  - `projects/p9-org-watch/reports/audit/p9-org-watch.md:17`（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i56"></a>

### 56. プロジェクトの charter の完了条件が記録と食い違うとき、PM が子の charter で補ってよいかがはっきりしない

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p8）・記録 1
- 状態: 不明 — 直した記録が見つからない。p9 の記録には同じ申告が無い
- 起きたこと: p8 の PM が、プロジェクトの charter の完了条件が記録と食い違うのを見つけ、補ってよい範囲と判断して子の charter で直し、上への report に書いた。
- 参照元:
  - `projects/p8-viewer-rebuild/reports/sessions/p8-viewer-rebuild__pm-129ad682.yaml:416`

[↑ 目次へ](#目次)

<a id="i57"></a>

### 57. 別の作業者へ送った文案が、相手の成果物に入ったか確かめられなかった

- 分類: 連絡
- 回数: 1 プロジェクト（p6）・記録 1
- 状態: 不明 — 直した記録が見つからない。p7 以降の記録には同じ申告が無い
- 起きたこと: p6 の worker-norms が、context.yaml の ui-designer の行の文案を担当の worker-orgctl へ送ったが、入ったかは未確認のまま終わった。
- 参照元:
  - `projects/p6-org-build/reports/sessions/p6-org-build__teams__org-build__worker-norms-7bbd0aab.yaml:91`

[↑ 目次へ](#目次)

<a id="i58"></a>

### 58. zsh で `echo =====` と打つと「==== not found」で失敗する

- 分類: 環境
- 回数: 1 プロジェクト（p5）・記録 1
- 状態: 不明 — 直した記録が見つからない。p6 以降の記録には同じ申告が無い
- 起きたこと: p5 の作業者が、区切りの行を出そうとして zsh の = の展開で失敗し、別の文字にした。
- 参照元:
  - `projects/p5-org-viewer/reports/sessions/p5-org-viewer__teams__viewer__worker-export-098dcfca.yaml:74`

[↑ 目次へ](#目次)

<a id="i59"></a>

### 59. 台帳の deny（**/_archive/）が、案件の成果物の置き場と重なった

- 分類: 文脈パック
- 回数: 1 プロジェクト（p4）・記録 1
- 状態: 不明 — 直した記録が見つからない（job の README も文脈の台帳の改善を未着手としている）。p5 以降の記録には同じ申告が無い
- 起きたこと: p4 で、job.deny の **/_archive/ が成果物の置き場と重なり、台帳に例外の書き方が無かった。
- 参照元:
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__coordinator-run-use-thin-ad0d46dd.yaml:59`

[↑ 目次へ](#目次)

<a id="i60"></a>

### 60. サンドボックスの中で Bash のパイプ（git show | diff）が Operation not permitted になる

- 分類: 環境
- 回数: 1 プロジェクト（p4）・記録 1
- 状態: 不明 — 直した記録が見つからない。p5 以降の記録には同じ申告が無い
- 起きたこと: p4 の PM が、一度ファイルに書き出して diff した。
- 参照元:
  - `projects/p4-job-run-use/reports/sessions/p4-job-run-use__pm-7fcade93.yaml:72`

[↑ 目次へ](#目次)

<a id="i61"></a>

### 61. 起こした直後の相手にも「wait で待っているので知らせは出さない」と出た

- 分類: 連絡
- 回数: 1 プロジェクト（p3）・記録 1
- 状態: 不明 — 直した記録が見つからない。p4 以降の記録には同じ申告が無い
- 起きたこと: p3 の PM が監査役を起こした直後に start を出すと、orgctl が「相手は wait で待っているので知らせは出さない」と出した。監査役は届いて動いたが、PM は起動直後でも wait 中と判定される根拠を確かめていない。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__pm-8512c441.yaml:86`

[↑ 目次へ](#目次)

<a id="i62"></a>

### 62. PM の wrap_up に、PM が自分で確かめたことが書かれていなかった

- 分類: レビュー
- 回数: 1 プロジェクト（p3）・記録 1
- 状態: 直った — PM の決まりの 4 に「wrap_up に自分で確かめたことを書く」が PR #2（f394306、10-23 14:07）で入り、p4〜p9 に同じ申告が無い（p8 の PM は「PM が自分で開いて見たもの」を書いている）
- 起きたこと: p3 の PM の wrap_up は子の report から 13 秒・17 秒で出ていて、本文は「完了条件を満たしているので通します」だけだった。PM 本人も、確かめてはいたが記録から追えないと書いた。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__pm-8512c441.yaml:85`
  - `projects/p3-org-visibility/log/msgs/95df09.md:8`（95df09・`log/events.log:126`）（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i63"></a>

### 63. リーダーの残る不明点がセッション報告の unclear にだけあり、PM への report に無かった

- 分類: レビュー
- 回数: 1 プロジェクト（p3）・記録 1
- 状態: 直った — リーダーの report に「目的に照らして残る不明点」の節を置く決まりが PR #2（f394306）で入り、p4 以降の report にその節がある。同じ申告は無い
- 起きたこと: p3 の readme-guide のリーダーは、README の 2 章・5 章のコマンドを打つのが誰かがはっきりしないと unclear に書いたが、PM への report には無く、PM は知らずに通した。セッション報告は teardown の後にできる。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__leader-4d653d8e.yaml:77`
  - `projects/p3-org-visibility/log/msgs/95df09.md:12`（95df09・`log/events.log:126`）（別の出どころ。数えない）

[↑ 目次へ](#目次)

<a id="i64"></a>

### 64. 監査役の見るものに、セッション報告の machine 欄（files_changed_in_window など）の正しさが入るかがはっきりしない

- 分類: 規範の書き方
- 回数: 1 プロジェクト（p3）・記録 1
- 状態: 不明 — 直した記録が見つからない（今の org/positions/auditor/position.md に machine・files_changed の語は無い）。p4 以降の記録には同じ申告が無い
- 起きたこと: p3 の監査役が、machine 欄の正しさを見るものに入れてよいかが分からず、orgctl の記録の取り方の話として改訂案に入れた。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__auditor-074c4759.yaml:50`

[↑ 目次へ](#目次)

<a id="i65"></a>

### 65. teardown の files_changed_in_window に、並行チームの変更が混じる

- 分類: 道具
- 回数: 1 プロジェクト（p3）・記録 1（監査・job の控えだけが書いているので、それを数えた）
- 状態: 不明 — 兄弟のコンポーネントを除く直しは PR #2（f394306）で入ったが、同じ時間帯の他のメンバーの変更は混ざると注記したまま。p4 以降に同じ申告は無い
- 起きたこと: p3 の timeline-tool のリーダーのセッション報告に README.md と teams/readme-guide/ の 3 ファイルが、readme-guide のリーダーに tools/org_timeline.py などが入っていた。p1 の PM は前の PM がしたことをこの欄から推していた（p3 の監査役）。
- 参照元:
  - `projects/p3-org-visibility/log/msgs/95df09.md:24`（95df09・`log/events.log:126`）

[↑ 目次へ](#目次)

<a id="i66"></a>

### 66. tools/org_timeline.py に --help が無く、打つとディレクトリとして扱われて例外で止まる

- 分類: 道具
- 回数: 1 プロジェクト（p3）・記録 1
- 状態: 不明 — 直した記録が見つからない。p4 以降の記録には同じ申告が無い
- 起きたこと: p3 のレビュアーが --help を打つと例外で止まった（ファイルは作られなかった）。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__readme-guide__reviewer-10b48465.yaml:63`

[↑ 目次へ](#目次)

<a id="i67"></a>

### 67. Claude in Chrome の拡張が繋がらず、実ブラウザで確かめられなかった

- 分類: 環境
- 回数: 1 プロジェクト（p3）・記録 1
- 状態: 不明 — 直した記録が見つからない。p4 以降の記録には同じ申告が無い
- 起きたこと: p3 の作業者が、ヘッドレス Chrome のスクリーンショットで代用した。
- 参照元:
  - `projects/p3-org-visibility/reports/sessions/p3-org-visibility__teams__timeline-tool__worker-1-969f0ba1.yaml:70`

[↑ 目次へ](#目次)

<a id="i68"></a>

### 68. PM がリーダーへ催促・確認するための種類が無く、report で代用した

- 分類: 連絡
- 回数: 1 プロジェクト（p1）・記録 1
- 状態: 不明 — メンバー向けの種類は増えていない（nudge は根っこが使い、ASK_KINDS に入ったのは PR #14 のあと）。p2 以降に同じ申告は無い
- 起きたこと: p1 の PM が、止まっているリーダーへの確認を report の種類で出した。event の種類の一覧に催促・確認に当たるものが無かった。
- 参照元:
  - `projects/p1-org-status/reports/sessions/p1-org-status__pm.yaml:74`

[↑ 目次へ](#目次)

## 作り方

- 読んだ場所: 閉じた p1〜p9 の `reports/sessions/*.yaml` の `self` の `unclear`・`not_done`、`log/msgs/*.md` の「うまくいかなかったこと」系・「申し送り」「残る不明点」「未確認」系の節と見出しでない「申し送り:」の札、`log/events.log` で種類が review_ng・rework・blocked・escalate・nudge の本文（blocked・escalate は 0 行）、`log/user-inbox.yaml` の report でない項、監査役の出力（p3 の `log/msgs/95df09.md`・p9 の `reports/audit/p9-org-watch.md`）、events.log の監査役の assign の有無（無いまま閉じたプロジェクトを 1 件ずつ）、job の `company/system/ai-org/README.md` の「組織の直し待ち」（p10 以降の行は除く）と「の時点」の残ったこと・申し送り（job の README は git の管理外で外の人が書き足すので、読んだ版の指紋を `counts.md` に残した: sha1 5060bd4ae884・更新 2026-10-24 19:41）。p10 と会話ログは読まない。抜き出しは `scripts/extract.py`（1 行 1 件、`teams/issues/work/extract.tsv`・件数表 `counts.md`）。
- まとめ方: 言い方でなく中身（誰が・何をして・どうなったか）が同じものを 1 件にした。成果物の中身への指摘、何も起きなかった行、直し方の選択肢、これからの段取り、未実施・〔仮〕の申告は入れなかった。各行の行き先と入れなかった理由は `teams/issues/work/mapping.md`。判断は `scripts/issues_def.py`。
- 回数: 「プロジェクト数」はその件の記録があるプロジェクトの数、「記録の数」は寄せた抜き出しの行の数（同じ人の unclear と報告の節は別に数える）。監査役の出力と job の控えは、同じ出来事を別の出どころが書いたものなので参照元に足すが数えない（その件にほかの出どころが無いときだけ数える）。
- 並び: **プロジェクト数**の多い順。同じなら記録の数の多い順、それも同じなら新しい順（数えた記録のうち一番新しいプロジェクト）。
- 状態: 「直った」は dev-tools の main にマージ済みの直した記録があり、かつそのマージより後に始まって閉じたプロジェクトの記録に同じ申告が無いもの。片方しか無いものは「不明」（何が足りないかを書いた）。直した記録が無く最後のプロジェクトまで起きているもの、直したあとにも起きているものは印なし。照合に使ったのは `git -C dev-tools log main` の PR のマージ時刻と、各プロジェクトの events.log の最初と最後の時刻。
- 数え直し: `python3 projects/p11-issue-list/scripts/extract.py && python3 projects/p11-issue-list/scripts/build.py`（抜き出しの指紋 563ad1937973）。

[↑ 目次へ](#目次)
