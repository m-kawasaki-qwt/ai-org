<!-- p6-org-build/teams/org-build/worker-orgctl → p6-org-build/teams/org-build/reviewer review_request 2026-10-24T13:23:42+09:00 -->
# review_request: orgctl の --persona と context.yaml

成果物: org/scripts/orgctl.py（cmd_assign と assign の引数）、org/context.yaml（personas 節）。git diff で見られる。標準ライブラリのみ・既存関数は変えず足しただけ。

## 完了条件 3 の確かめ（scratchpad の仮 repo。変更前 = git archive HEAD、変更後 = worktree の org に仮の personas 3 つを足したもの）
- 変更前後で `assign reviewer --occupation engineer`（--persona なし）を打ち、system.md・CLAUDE.md・member.json（created_at 除く）を diff: 3 つとも差なし。events の assign の行も同じ形。
- `assign ... --occupation engineer --persona kawasaki --persona sales`: rc=0。system.md に「- あなた: ...（立場: reviewer・職種: engineer・ペルソナ: kawasaki, sales）」と、職種の後ろに「# ペルソナ: kawasaki（この目線で見る）」「# ペルソナ: sales（この目線で見る）」が指定順で入る。events 行 `... occupation=engineer model=opus personas=kawasaki,sales`、member.json に `"personas": ["kawasaki","sales"]`。
- `--persona kawasaki --persona nobody --persona ../x`: rc=1。「orgctl: ペルソナ nobody, ../x の雛形が無い（.../org/personas）。使えるペルソナ: end-user, kawasaki, sales」。メンバーのディレクトリも component.json の members も作られない（存在確認は mkdir の前）。`../x` のような名前も一覧に無いので弾かれる。
- 作業者に `--persona end-user` も付く（立場を問わない）。
- context.yaml に personas 節（読み元・入る時・誰が選ぶか）。

## 判断したこと
- member.json の personas は、指定があるときだけ入れる（無指定の出力を 1 バイトも変えないため）。
- 同じ名前を重ねたら 1 つにまとめる。一覧は org/personas/*.md から拾う（ハードコードなし）。

## 未確認
- 職種 ui-designer は今は無いので、UI デザイナー + ペルソナの組み合わせは未確認（engineer で確認。職種とペルソナは独立の処理）。
- README は触っていない（文案は worker-norms へ送付）。
