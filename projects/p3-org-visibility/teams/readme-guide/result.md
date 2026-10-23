# readme-guide の結果

成果物: ai-org の [README.md](../../../../README.md)（作業者 worker-1＝Sonnet、レビュアー＝Opus。第 1 版で承認、往復なし）

## 完了条件ごと

1. 節はそろっている。節の一覧（上から）:
   - 0 表記（`$DEV_TOOLS_REPO_PATH` と `orgctl` の呼び方、`ORG_ROOT=… ORG_MEMBER=user`）
   - 1 はじめに人がやること（`sh $DEV_TOOLS_REPO_PATH/setup.sh`・Google Chat の webhook を `.secrets/gchat-webhook.url` に置く（任意。無ければ `log/notify-outbox.log` に溜まる）・Orca で ai-org を開く）
   - 2 プロジェクトを立ち上げる（`org-project-new` がやる 4 手順と、そのあと PM 以下で起きること・川崎さんに来るもの）
   - 3 いまの状況を見る（`orgctl watch`・`tools/org_status.py [--json]`・`tools/org_timeline.py`・`orgctl notify-stats`・`orgctl patrol`）
   - 4 記録の在り処（`log/events.log`・`log/msgs/`・`reports/sessions/`・`thread.md`・`result.md`・`timeline.html` のツリーと grep の例）
   - 5 閉じる（wrap_up → wait → teardown → 出た close・git の行を打つ）
   - 6 コミットの決まり（CLAUDE.md の要約とリンク）
2. 準備 → 立ち上げ → 状況 → 記録 → 閉じる → コミット の順。上から順にたどれる。
3. `\` の行継続・heredoc なし。orgctl のサブコマンドを `--help` と突き合わせた（下）。`tools/org_status.py` は `root [--json]` で実物と一致（レビュアーが p2-orca-run-use で実行して確認）。
4. `tools/org_timeline.py` は「プロジェクトのディレクトリを渡すと `<そのディレクトリ>/timeline.html` を書く」（`python3 tools/org_timeline.py projects/<slug>`）**この形を前提に書いた。** レビュー時点で tools/ に実物があり、位置引数のディレクトリを取って `<dir>/timeline.html` を書く形だった（`--help` は無い）。timeline-tool チームの最終形が変わったら README 3 章の行を合わせる。
5. このファイルと report に一覧を書いた。

## 突き合わせた orgctl のサブコマンド（`orgctl <sub> --help`）

orgctl 全体: new, assign, launch, attach, event, inbox, wait, watch, notify-stats, patrol, teardown, whoami。

README が使うもの（11 個）と引数:
- `new project <dir> --root --charter <file>`
- `assign <dir> pm --model opus`
- `launch <member>`
- `attach <member> <handle>`
- `event start|wrap_up --to <id> --body "…"`
- `inbox`（名前だけ）
- `wait`
- `watch <dir>`
- `notify-stats --root <dir>`
- `patrol <dir>`（`--once`・`--dry`・`--stuck-min`）
- `teardown <dir> --summary "…"`

`whoami` は使っていない。

## リーダーとして確かめたこと

- `sh $DEV_TOOLS_REPO_PATH/setup.sh` は、dev-tools の README と同じ打ち方。
- `orgctl` はプラグインの `bin/orgctl` として PATH にある（`which orgctl` で確認）。
- 2 章の手順は `org-project-new` の SKILL.md の手順 1〜6 と合っている。

## 申し送り（軽微。直していない）

- 0 章の「人として打つときは `ORG_ROOT=… ORG_MEMBER=user` を付ける」が実際に要るのは event / inbox / wait だけ。ほかは付けなくても動く（README の各コマンドもその書き方なので、害はない）。
- 5 章の「見張りも止める」: patrol は根っこが closed になると自分で終わるので、止めなくてもよい。
