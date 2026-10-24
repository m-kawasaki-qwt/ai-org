# org-build の結果

## Summary

- 雛形（dev-tools の worktree `/Users/maka343noshi/orca/workspaces/dev-tools/org-build` の `org/`）と orgctl に、UI デザイナーの職種・ペルソナで見るレビュアー（`--persona`）・撮って「出せる水準か」を判定する基準を足した。完了条件 1〜8 は全部満たした（レビュアーが承認し、リーダーも仮の repo で打って中身を読んで確かめた）。
- 決めたこと: `--persona` は複数可（何度でも）。ペルソナは `org/personas/<名前>.md`（kawasaki・end-user・sales。end-user と sales は観点だけで、具体はコーディネーターがパックに書く）。作る前の決めごと（checklist の B）は、UI デザイナーがチームの `design.md` に書く。research は `org/common/ui/` に写して正にした（PM の決定）。
- 編成: worker-orgctl（engineer・sonnet）・worker-norms（engineer・opus）・reviewer（engineer・sonnet）。指摘は 0 回、rework は 0 回、入れ替えは無し。

## 目次

- [触ったファイル](#触ったファイル)
- [完了条件ごとの結果](#完了条件ごとの結果)
- [申し送り](#申し送り)
- [目的に照らして残る不明点](#目的に照らして残る不明点)
- [うまくいかなかったこと](#うまくいかなかったこと)

## 触ったファイル

```
worktree（dev-tools/org-build）
├── org/
│   ├── scripts/orgctl.py                     変更  assign に --persona（何度でも）。存在確認・一覧つきで止まる・member.json と events に personas
│   ├── context.yaml                          変更  occupations に ui-designer、personas の節
│   ├── README.md                             変更  ペルソナ（--persona）・画面を作るチーム・置き場の tree・足すとき
│   ├── personas/{kawasaki,end-user,sales}.md 新規  1 ファイル 1 ペルソナ。判定の問いに checklist の C 番号
│   ├── occupations/ui-designer/occupation.md 新規  組み立てる前に design.md（B-01〜B-09）→ 組み立てる → 出す前に撮って C
│   ├── common/screen-check.md                新規  誰が・いつ撮るか／撮り方（p5 の注意 + Chromium もサンドボックスの外）／何に照らすか／通らなければ
│   ├── common/ui/                            新規  research の写し（checklist・principles・sources・tools/png_contrast.py）と screen-probe.mjs（画像に写らない値を読む）
│   └── positions/{reviewer,leader,pm,coordinator}/position.md  変更  「画面を作るチームでは」の受け口
├── claude/plugins/dev-tools/skills/org-project-new/SKILL.md     変更  根っこがユーザーへ伝える前に同じ基準で見る（手順 5）
└── docs/todo/ai-org-plan.md                  変更  「立場と職種」に UI デザイナー・ペルソナ・出せる水準か
ai-org
└── projects/p6-org-build/teams/org-build/feedback-map.md  新規  完了条件 8 の対応表
```

[↑ 目次へ](#目次)

## 完了条件ごとの結果

| # | 結果 | どこで確かめたか |
|---|---|---|
| 1 | 満たした。`occupation.md` の手順が U-xx・B-xx の番号つきで `org/common/ui/` の原文に辿れる。「組み立てる前に: design.md を書く（要素ごとに何のために、誰に出すか）」が手順の本体。G-01・K-02 の数値は写していない | リーダーが読んだ |
| 2 | 満たした。kawasaki はフィードバックの言葉（認知負荷・全部並べない・開いて回らず掴む・明るい画面は嫌・PC 900〜1800px・10 文字程度）のまま | リーダーが読んだ |
| 3 | 満たした。複数可を README に記載。存在しない名前は「ペルソナ zzz の雛形が無い（…/org/personas）。使えるペルソナ: end-user, kawasaki, sales」で rc=1、ディレクトリも component.json も作らない。context.yaml に personas の節 | 下の 7 |
| 4 | 満たした。レビュアー（review_ok の前に毎回自分で撮りペルソナで判定・design.md を B に照らす・4 回目でも通らなければ escalate）／リーダー（承認後に撮り直し kawasaki で判定）／PM（画像を開いてから上げる）／コーディネーター（編成案で「画面を作るか」→ UI デザイナーの有無・ペルソナ別のレビュアー、end-user・sales の具体をパックへ）。撮り方は `screen-check.md` に、p5 の 4 点と、Chromium もサンドボックスの外で動かすこと | リーダーが diff を読んだ |
| 5 | 満たした。org-project-new の手順 5 | レビュアー |
| 6 | 満たした。README とプランの「立場と職種」 | レビュアー |
| 7 | 満たした（下） | リーダーとレビュアーがそれぞれ打った |
| 8 | 満たした。`feedback-map.md`。research の 19 行に「組み込んだ先（ファイルと節）」を足し、組織の側の原因 4 つと監査のまとめ方を 5 行足した（全 24 行: 防げる 17・一部 3・項目に分けて拾う 2・防げない 1・対象外 1。数は作業者がスクリプトで数えた） | リーダーが読んだ |

**完了条件 7（リーダーが打った分。scratchpad の仮の repo、worktree の orgctl）:**

- `new project <仮>/pX --root` → `new team <仮>/pX/teams/t`
- `assign <仮>/pX/teams/t reviewer --occupation engineer --persona kawasaki --persona end-user` → rc=0。system.md に「立場: reviewer・職種: engineer・ペルソナ: kawasaki, end-user」、129 行目「# ペルソナ: kawasaki（この目線で見る）」、172 行目「# ペルソナ: end-user（この目線で見る）」
- `assign <仮>/pX/teams/t worker --name ud --occupation ui-designer --persona kawasaki` → rc=0。見出しの順は「# 立場: 作業者」→ 106 行目「# 職種: UI デザイナー（UI・UX）」→ 141 行目「# ペルソナ: kawasaki」
- `assign ... worker --name w2 --persona kawasaki --persona nope`、`assign ... reviewer --name rz --occupation ui-designer --persona zzz` → どちらも rc=1、一覧つきのメッセージ、メンバーのディレクトリは作られない
- 作業者の確認（変更前の orgctl と並べて）: `--persona` 無しの assign で system.md・CLAUDE.md・member.json（created_at を除く）に差なし

[↑ 目次へ](#目次)

## 申し送り

- 本体の dev-tools へ入るまで（根っこの側が PR にしてマージするまで）、動いている組織の orgctl には `--persona` も ui-designer も無い。
- `org/common/ui/` は research の写し（約 46KB）で、正はこちら。research が更新されても自動では追わない（README に記載）。
- `screen-probe.mjs` は worker-norms が欠陥を仕込んだ HTML で動かした（900px で横スクロール・折り返し・cursor・24px 未満・フォーカスを検出）。レビュアーとリーダーは再実行していない。
- 同じペルソナを重ねて指定すると黙って 1 つにまとめる。README には書いていない。

[↑ 目次へ](#目次)

## 目的に照らして残る不明点

- 規範に入れた手順が、実際の画面のチームで p5 の指摘を止められるかは、まだ試していない（今回は雛形と orgctl を作っただけ）。次に画面を作るチームを回したときに、`design.md` → 撮影 → ペルソナで判定、の流れが回るかを見る必要がある。
- 規範から `org/common/...` を辿る書き方が「システムプロンプトの orgctl のパスから `scripts/orgctl.py` を外した所」になった。orgctl の「あなたについて」に雛形の場所を 1 行出せば短くできるが、今回はやっていない（orgctl の変更になるので、別の作業として判断してほしい）。

[↑ 目次へ](#目次)

## うまくいかなかったこと

- 文脈パックの撮り方の注意は「localhost のためサンドボックスの外」という理由だけだった。実際は Chromium もサンドボックスの中では起動しない（mach port の権限）。`screen-check.md` に足した。
- review_ok はリーダー宛てなので、作業者は自分の前半が承認されたことを `thread.md` でしか知れなかった（worker-norms の申告）。
- リーダーの `event --body-file /dev/stdin` は directory-guard に止められた。本文はチームの `msgs/` にファイルで書いて渡した。

[↑ 目次へ](#目次)
