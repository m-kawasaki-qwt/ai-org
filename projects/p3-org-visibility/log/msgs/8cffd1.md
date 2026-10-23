<!-- p3-org-visibility/teams/readme-guide/worker-1 → p3-org-visibility/teams/readme-guide/reviewer review_request 2026-10-23T13:28:44+09:00 -->
# review_request 第1版

成果物: /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/README.md

## README の節
0 表記 / 1 はじめに人がやること（setup.sh・webhook・Orca） / 2 プロジェクトを立ち上げる（org-project-new と、その後に起きること） / 3 いまの状況を見る（watch・org_status.py・org_timeline.py・notify-stats・patrol） / 4 記録の在り処 / 5 閉じる / 6 コミットの決まり

## 突き合わせた orgctl のサブコマンド（`orgctl <sub> --help` で実在を確認）
new（--root --charter）/ assign（--model ほか）/ launch / attach / event（--to --body）/ wait / watch / patrol（--once --dry --stuck-min）/ teardown（--summary）/ notify-stats（--root）。orgctl.py 全体の一覧: new, assign, launch, attach, event, inbox, wait, watch, notify-stats, patrol, teardown, whoami。README が使うのは inbox（記録の節で名前だけ）まで含め 11 個、whoami は不使用。
tools/org_status.py: `org_status.py <root> [--json]` を実行して p2-orca-run-use で出力を確認。

## 完了条件ごと
1. 5 節（立ち上げ・状況・記録・コミット・人がやること）すべてある。人がやること＝1 章。
2. 上から 準備 → 立ち上げ → 状況 → 記録 → 閉じ → コミット の順。
3. コマンドは 1 行 1 コマンド、`\` と heredoc なし（`\` 行末は grep で 0）。dev-tools のパスは `$DEV_TOOLS_REPO_PATH` に統一。
4. org_timeline.py は `python3 tools/org_timeline.py projects/<slug>` → `projects/<slug>/timeline.html` を前提に記載（未確認・並行チーム作成中）。
5. 本メッセージが一覧。

## 未確認・判断した点
- setup.sh が org のために何かするかは、プラグイン（orgctl の bin と org-project-new スキル）の導入までを根拠にした。webhook は patrol の実装（`.secrets/gchat-webhook.url`・`ORG_GCHAT_WEBHOOK_FILE`）から。
- 閉じる節の `wrap_up` の本文例は私が書いた文言。PM が wrap_up で配下を閉じる動きは SKILL.md の記述（wrap_up → done を待つ → teardown）に従った。
