# 目的

job（川崎さんの業務のナレッジベース）の手順書 `.claude/skills/manager/sources/orca/run-use.md` を、dev-tools の共通スキル orca-multi-agent の直し（2026-10-23。`run-use` は依頼の直前と引き取るときだけ・戻りは結ばずに `inbox` で見る）に合わせて、**job 固有の差分だけ**に薄くする。共通の手順は dev-tools 側を指し、job にしか無いもの（Run の ID・引き取るまでの時間・automation の印・観察ログ・誤配の扱いの job での運用）だけを残す。同じことが 2 か所に書かれて食い違うのを防ぐため。

出発点の記録: job の `.claude/plans/tmp/2026-10-22-orca-multi-agent-run-use-handover.md`（「dev-tools に上げずに job に残すもの」「job 側で直したもの」の節）。

AI 組織の P2.5 の試走でもある。今回は job の事業・運用の文脈が要る題材で、チームコーディネーターが組む文脈パックが効くかを見る。

# 完了条件

1. `run-use.md` が、共通の手順（いつ結ぶか・結ばずに見る分岐・依頼していない戻りの扱い）を dev-tools の `claude/plugins/dev-tools/skills/orca-multi-agent/SKILL.md` の該当の節への参照に置き換え、job 固有のもの（上の目的に挙げたもの）だけを持つ。
2. job の決まり「情報を消さない」に従う: 置き換えで外した文は消さず、同じディレクトリの `_archive/2026-10-24-run-use-before.md` に元の全文を退避し、`run-use.md` の冒頭から 1 行で指す。
3. job の中で `run-use.md` を参照している箇所（`grep` で探す）が、薄くした後も矛盾しない。直す必要があれば、その箇所の直しも同じ形（外した文は退避）で行う。直した箇所の一覧を報告に書く。
4. dev-tools の SKILL.md と job の `run-use.md` で、同じ事柄について食い違う記述が無い（突き合わせた結果を報告に書く）。

# 範囲

- 書いてよい場所: job の `.claude/skills/manager/sources/orca/`（`run-use.md`・`_archive/`）と、完了条件 3 で直す必要が出た job のファイル、このプロジェクトのディレクトリの中。
- 読んでよい場所: dev-tools（読むだけ）、job（文脈の台帳 `org/context.yaml` の範囲）。
- 触らないもの: dev-tools、job の台帳（`tasks/`）・`self-tasks/`・`people/`、git の操作。
- job は川崎さんの他のセッションも同時に書いている。書く前に読み直し、追記・置き換えは最小の差分で行う。
- うまくいかなかったこと（文脈パックの過不足・連絡・決まり）は、隠さずセッション報告の `unclear` と最後の報告に書く。とくに「パックに無くて自分で探した資料」「パックにあって要らなかった資料」を書く。
