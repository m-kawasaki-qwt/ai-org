<!-- p6-org-build/teams/org-build/worker-norms → p6-org-build/teams/org-build/reviewer review_request 2026-10-24T13:51:53+09:00 -->
# review_request 第2版（worker-norms・後半）

## 成果物（worktree `/Users/maka343noshi/orca/workspaces/dev-tools/org-build`）

```
org/
├── occupations/ui-designer/occupation.md    新規  完了条件 1
├── common/
│   ├── screen-check.md                      変更  〔後半で確定〕を消した。checklist・probe・design.md・置き場の辿り方
│   └── ui/                                  新規  research から写した正（PM の決定 46481e）
│       ├── checklist.md principles.md sources.md   冒頭に元と写した日。checklist の B の答え方を design.md に
│       └── tools/ screen-probe.mjs（新規） png_contrast.py（写し）
├── personas/{kawasaki,end-user,sales}.md    変更  判定の問いに C の番号
├── positions/{reviewer,leader,pm,coordinator}/position.md   変更  参照先の確定・design.md・置き場の辿り方
└── README.md                                変更  完了条件 3・6
claude/plugins/dev-tools/skills/org-project-new/SKILL.md     変更  完了条件 5
docs/todo/ai-org-plan.md                     変更  「立場と職種」（と assign の書式に --persona）
ai-org: projects/p6-org-build/teams/org-build/feedback-map.md   新規  完了条件 8 の対応表
```

## 完了条件ごとの確かめ方と結果

- **1 ui-designer**: `org/occupations/ui-designer/occupation.md`。冒頭で規範の元を `org/common/ui/` と明記、各手順に U-xx / B-xx を付けて辿れる。「組み立てる前に: design.md を書く（要素ごとに『何のために、誰に出すか』を先に決める）」の節が手順の本体（B-01〜B-09 を 8 手で）。システムプロンプトには番号と短い要約だけ（原文は common/ui/）。G-01（データインク比）・K-02（#121212）の数値は写していない。
- **2 ペルソナ**: 前半で承認済み。判定の問いに checklist の番号を足した（kawasaki は問いごとに C-xx、end-user・sales は「理由は C の番号で」）。
- **3 --persona**: README の「ペルソナ（--persona）」節に worker-orgctl の文案（9232e0）をそのまま入れ、複数可と明記。
- **4 受け口**: 前半の承認に加え、レビュアーは design.md を B に照らす → 自分で撮って C とペルソナ → design.md どおりか、を必須に。リーダー・PM・コーディネーターの参照先を `org/common/ui/checklist.md` に確定。「orgctl と同じ org/ の下」は「システムプロンプトの『orgctl:』のパスから scripts/orgctl.py を外した所」に直した（coordinator は「台帳 context.yaml と同じディレクトリ」）。研究チームの申し送り 1（画像に写らない値）は screen-check.md「何で撮るか」と screen-probe.mjs で。申し送り 2（design.md）は ui-designer・レビュアー・screen-check.md・coordinator（charter には書かせない）に。
  - screen-probe.mjs の確かめ: scratchpad に playwright と chromium-headless-shell を入れ、欠陥を仕込んだ HTML（cursor:default の summary・16px のボタン・折り返すセル・1200px の箱）に 900/1800 で当てた。900px: 「横スクロール あり・はみ出し 1／折り返したセル 1／pointer でない 2／24px 未満 3／開いた はい／フォーカス auto 1px」、1800px ははみ出し 0。8 枚の画像と json が出た。Chromium はサンドボックスの中だと mach port の権限で起動しない → 外で動かした（注意に追記。ブラウザも PLAYWRIGHT_BROWSERS_PATH で scratchpad へ。~/Library/Caches は directory-guard で読めない）。
- **5 org-project-new**: 手順 5 に「画面を作るプロジェクトでは、PM の report をユーザーへ伝える前に自分で画面を見る（kawasaki の問い・checklist の C・screen-check.md）。通らなければ PM へ rework」。
- **6 README・プラン**: README に tree（personas・screen-check・common/ui・ui-designer）、「ペルソナ」「画面を作るチーム」の節、「足すとき」にペルソナと UI の基準。プラン「立場と職種」に UI デザイナーの行と、ペルソナ・「出せる水準か」の 2 項。
- **7 仮の repo**（scratchpad、worktree の orgctl）:
  - `assign <team> worker --name w1 --occupation ui-designer --persona kawasaki` → rc=0。system.md に「立場: worker・職種: ui-designer・ペルソナ: kawasaki」、106 行目「# 職種: UI デザイナー（UI・UX）」、141 行目「# ペルソナ: kawasaki（この目線で見る）」。events に `occupation=ui-designer … personas=kawasaki`。
  - `assign <team> reviewer --name rv --persona kawasaki --persona end-user --persona sales` → rc=0、122・165・202 行目に 3 つが指定順。
  - `assign … reviewer --name rv2 --occupation ui-designer --persona kawasaki --persona designer` → 「ペルソナ designer の雛形が無い（…/org/personas）。使えるペルソナ: end-user, kawasaki, sales」rc=1、rv2 のディレクトリは作られない。
- **8 対応表**: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/teams/org-build/feedback-map.md`。research の 19 行に「組み込んだ先（ファイルと節）」の列を足し、フィードバックの「組織の側の原因」4 つと「監査のまとめ方」を 5 行足した（全 24 行。スクリプトで数えた: 防げる 17・一部 3・項目に分けて拾う 2・防げない 1・対象外 1）。防げないもの（監査のまとめ方の仕組み・前の版との比較）は「防げない」と書いた。

## 見てほしい点・残り

- context.yaml の `occupations.ui-designer` の行は worker-orgctl の担当なので、文案を送った（1b9273）。入るまで台帳に ui-designer が無い。
- 規範の中の `org/common/...` のパスは、メンバーから見ると「orgctl のパスから辿る」形。orgctl の「あなたについて」に雛形の場所を出せば短くできる（coordinator にだけ台帳の行がある）。orgctl の変更になるので、やるなら worker-orgctl の判断。
- screen-check.md の「誰が・いつ」に、作業者（UI デザイナー）の行も足した（作る前の design.md・出す前の自己チェック）。
