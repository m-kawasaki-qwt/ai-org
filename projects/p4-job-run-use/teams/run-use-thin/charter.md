# 目的

job の手順書 `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.claude/skills/manager/sources/orca/run-use.md` を、dev-tools の共通スキル orca-multi-agent（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/claude/plugins/dev-tools/skills/orca-multi-agent/SKILL.md`。2026-10-23 の直し: `run-use` は依頼の直前と引き取るときだけ・戻りは結ばずに `inbox` で見る）に合わせて、job 固有の差分だけに薄くする。共通の手順は dev-tools 側の該当の節を指し、job にしか無いもの（Run の ID・引き取るまでの時間・automation の印・観察ログ・誤配の扱いの job での運用）だけを残す。同じことが 2 か所に書かれて食い違うのを防ぐため。上のプロジェクト p4-job-run-use の目的そのもの。

出発点の記録: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/.claude/plans/tmp/2026-10-22-orca-multi-agent-run-use-handover.md`（「dev-tools に上げずに job に残すもの」「job 側で直したもの」の節）。

# 完了条件

1. `run-use.md` が、共通の手順（いつ結ぶか・結ばずに見る分岐・依頼していない戻りの扱い）を SKILL.md の該当の節（節の見出し名で指す）への参照に置き換え、job 固有のもの（Run の ID・引き取るまでの時間・automation の印・観察ログ・誤配の扱いの job での運用）だけを持つ。
2. 置き換えの前の `run-use.md` の全文が、同じディレクトリの `_archive/2026-10-24-run-use-before.md` に一字も欠けずに退避されていて（diff で確かめる）、`run-use.md` の冒頭の 1 行がそのファイルを指している。
3. job の中で `run-use.md` を参照している箇所を `grep -rn --exclude='.env*' "run-use" /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job` で洗い出し、薄くした後も矛盾しない。直した箇所があれば、外した文は同じ形（元の全文を `_archive/` などに退避）で残す。洗い出した箇所と、直した／直さなかった理由の一覧が報告にある。
4. SKILL.md と `run-use.md` で、同じ事柄について食い違う記述が無い。突き合わせた事柄ごとの結果（一致／job 固有で SKILL.md に無い／食い違い→直した）の表が報告にある。
5. 報告に、文脈パックの過不足（パックに無くて自分で探した資料・パックにあって要らなかった資料）が書かれている。

# 範囲

- 書いてよい場所: job の `.claude/skills/manager/sources/orca/`（`run-use.md`・`_archive/`）と、完了条件 3 で直す必要が出た job のファイル、このチームのディレクトリの中。
- 読んでよい場所: dev-tools（読むだけ）、job（文脈パックと台帳 dev-tools `org/context.yaml` の範囲）。
- 触らないもの: dev-tools、job の `tasks/`・`self-tasks/`・`people/`、git の操作（add・commit・push・branch・worktree）。
- job は川崎さんの他のセッションも同時に書いている。書く直前に読み直し、置き換えは最小の差分で行う。
- 人にしかできない操作が要ったら: 手順を書いて escalate。
