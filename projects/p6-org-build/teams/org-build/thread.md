
## 作業者 第1版
- org/scripts/orgctl.py に --persona（複数可・存在確認は mkdir 前・無指定は出力不変）、org/context.yaml に personas 節。確かめは review_request（c4cc0d）本文。README 文案は worker-norms へ送付済み。

## レビュアー 第1回（orgctl の --persona と context.yaml）
- 承認（前半の orgctl 部分のみ。後半は research 待ち）。scratchpad の仮 repo で worktree の orgctl を実際に打って確かめた: `assign --persona kawasaki --persona sales` は rc=0、system.md の「あなたについて」に「職種: engineer・ペルソナ: kawasaki, sales」、職種の後ろに「# ペルソナ: …（この目線で見る）」が指定順で入る。events に `personas=kawasaki,sales`。`--persona kawasaki --persona nobody --persona ../x` は rc=1、「使えるペルソナ: end-user, kawasaki, sales」つきで止まり、メンバーのディレクトリは作られない。`--persona` 無しは system.md に「ペルソナ」の語が出ず、events の行も従来の形。標準ライブラリのみ・既存関数は不変。
- 未確認: ui-designer 職種は未着のため、職種つきの組み合わせは engineer でのみ確認。

## 作業者 第1版（worker-norms・前半: ペルソナと受け口）
- 新規 org/personas/{kawasaki,end-user,sales}.md（32〜38 行・形を揃えた: 誰か／何をしに開くか／最初の数秒／嫌うこと・離れる理由／判定の問い）。kawasaki はフィードバックの言葉を引用。end-user・sales は観点だけで、具体はコーディネーターがパックで足す・無ければ判定前に escalate。orgctl が「# ペルソナ: <名前>」の見出しを付けるので、ファイル側の H1 は「**目線:**」の 1 行にした。
- 新規 org/common/screen-check.md（誰が・いつ撮り・何で・何に照らし・通らなければどうするか、p5 の撮り方の注意 4 点）。システムプロンプトに入れず、立場の規範から参照（画面の無いチームを重くしないため）。チェックリストの参照先は〔後半で確定〕。
- 変更 positions/{reviewer,leader,pm,coordinator}/position.md に「画面を作るチームでは」の節。レビュアーは review_ok の前に自分で撮ってペルソナの判定を通すのが必須（通らないまま 4 回目でも承認せず escalate）。

## レビュアー 第2回（worker-norms 前半: personas・立場・screen-check.md）
- 承認（前半のみ）。完了条件 2（3 ペルソナ・1 ファイルずつ、kawasaki はフィードバックの言葉で認知負荷・全部並べない・開いて回らず・明るい画面は嫌・900〜1800px が入っている）と、完了条件 4 のうち、レビュアー・リーダー・PM・コーディネーターの受け口と撮り方（サンドボックスの外・scratchpad・`--cache`・`名前,/パス`）を確かめた。手順の本体を `org/common/screen-check.md` 1 か所にして立場には 4〜5 行だけ置いた点は、システムプロンプトを膨らませない目的に合っている。p5 の筋（承認後にリーダーが rework）を、レビュアーの段（毎回自分で撮る・通らないまま 4 回目でも承認せず escalate）で止める形になっている。
- 後半で見る: チェックリストの参照先の確定（screen-check.md の〔後半で確定〕の印が消えること）、ui-designer の規範、org-project-new、README・プラン、対応表。

## 作業者 第2版（worker-norms・後半）
- 新規 org/common/ui/（research の checklist・principles・sources・tools/png_contrast.py を写して正に。冒頭に元と写した日。checklist の B の答え方を design.md に合わせた）。新規 org/common/ui/tools/screen-probe.mjs（初期表示・全体・開いた・フォーカスの画像と、背景色・はみ出し・折り返し・cursor・24px 未満の値。仕込んだ欠陥を全部拾うのを確かめた）。
- 新規 org/occupations/ui-designer/occupation.md（design.md に B-01〜B-09 を先に書く手順・U-xx の番号と要約）。screen-check.md の〔後半で確定〕を消して checklist の参照・値の読み方・design.md の照らし方・置き場の辿り方を入れた。立場・ペルソナの判定の問いに C の番号。
- 変更 org-project-new（根っこが伝える前に同じ基準で見る）・README（ペルソナ・画面を作るチーム・置き場）・プラン「立場と職種」。対応表は teams/org-build/feedback-map.md（24 行）。context.yaml の ui-designer の行は worker-orgctl へ依頼（1b9273）。

## レビュアー 第3回（後半: ui-designer・common/ui・org-project-new・README・プラン・対応表）
- 承認。完了条件 1・3・4・5・6・7・8 を確かめた。指摘なし。
- 1: ui-designer は B-01〜B-09 を 8 手の「組み立てる前に design.md」にし、各手に U-/B- 番号が付いて `common/ui/` に辿れる。G-01・K-02 の数値は規範に無い（sources と checklist の出典欄のみ）。
- 7: 仮の repo で、worktree の orgctl で `assign worker --occupation ui-designer --persona kawasaki` rc=0（CLAUDE.md に職種 41 行・ペルソナ 76 行）。存在しない `designer` は rc=1、一覧つき、ディレクトリ無し。system.md は engineer 約 13.7KB に対し ui-designer 約 20.8KB。checklist などの全文はシステムプロンプトに入らない。
- 8: 対応表は、フィードバックの画面ごと・UI 全体・組織の側の原因・監査のまとめ方の全行に、組み込み先（ファイルと節）がある。防げないもの（監査のまとめ方の仕組み・前の版との比較）は「防げない」と書いてある。
