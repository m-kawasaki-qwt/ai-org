後半を始めてください。research が届いた: /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p6-org-build/research/（principles.md U-01〜U-12・checklist.md B 9 項目/C 27 項目と撮り方・feedback-map.md 19 行・sources.md・tools/png_contrast.py。研究チームの報告は log/msgs/dd1184.md）。

やること: org/occupations/ui-designer/・screen-check.md の〔後半で確定〕を checklist の参照に・org-project-new のスキル・org/README.md（worker-orgctl の --persona 文案 9232e0 を入れる。org/common/screen-check.md と org/personas/ の置き場も書く）・プランの「立場と職種」・対応表（feedback-map.md の 19 行に「組み込んだ先＝ファイルと節」を足したもの。チームのディレクトリ teams/org-build/ に置き、review_request にパス）。

研究チームからの申し送り（反映してください）:

1. 900/1800px の崩れ・cursor・フォーカスは画像に写らないので、Playwright で値を読む（要素の幅・はみ出し・computed style の cursor）・状態（ホバー・フォーカス・開いたアコーディオン）を撮る手順を screen-check.md に入れる。
2. checklist の B（作る前に決めること）を誰がどこに書くか → リーダーが決めた: UI デザイナー（画面を作る作業者）が、組み立てる前にチームのディレクトリの design.md に B-01〜B-09 への答えを書き、review_request の本文にそのパスを書く。レビュアーは C に加えて design.md を B に照らし、画面が design.md どおりか（理由の書けない要素が出ていないか）を見る。charter には書かない。ui-designer の規範・レビュアーの受け口・screen-check.md に、この形で入れる。
3. G-01（データインク比）・K-02（#121212）は出典の照合が △。規範に数値として写さない。
4. 置き場（PM の決定 46481e）: 雛形から ai-org の projects/p6-org-build/research/ を参照先にしない（プロジェクトの記録で、道具の置き場ではない）。checklist.md・sources.md（要るなら principles.md と tools/png_contrast.py も）を worktree の org/ の中（例: org/common/ui/）へ写して正にし、ui-designer の規範・screen-check.md・ペルソナ・立場の受け口は、そこを番号（U-xx・B-xx・C の番号）とパスで参照する。システムプロンプトに入る規範（occupation.md・position.md・personas）には全文を入れず、番号と短い要約だけ。写した先の冒頭に、元（research のパス）と写した日を書く。

前半で出たレビュアーの申し送りも合わせて: 立場の文の「orgctl と同じ org/ の下」を辿れる書き方に。coordinator が ui-designer を参照しているので、職種を作ってから `assign --occupation ui-designer` が通ることを確かめる。
