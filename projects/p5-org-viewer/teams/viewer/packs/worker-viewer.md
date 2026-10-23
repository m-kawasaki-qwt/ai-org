---
deny:
  - /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/**
---

# 文脈パック: 作業者（viewer）— viewer

workdir は ai-org の worktree `/Users/maka343noshi/orca/workspaces/ai-org/viewer`。書くのはここ（ビューア・README）と、スクリーンショットの置き場 `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/screenshots/`。ai-org 本体の `projects/` は読むだけ。job は読まない。

## 読む資料

| # | パス | 何のため・どこまで |
|---|---|---|
| 1 | ai-org `projects/p5-org-viewer/teams/viewer/charter.md` | 完了条件（とくに 2〜4）と範囲。全部 |
| 2 | リーダーから渡るスキーマ | これが正。ビューアは `snapshot.json` だけを読む。足りない項目はリーダーへ（自分で記録を読みに行かない） |
| 3 | worktree `CLAUDE.md`・`README.md` | repo の決まりと、立ち上げ方を書き足す先 |
| 4 | ai-org `policy.md` | 1・4・5 節。画面の判断の基準（認知負荷を減らす・選ぶだけ・記録が調べられる） |
| 5 | ai-org `tools/org_timeline.py` と、それが書いた `projects/p1-org-status/timeline.html`・`projects/p2-orca-run-use/timeline.html` | 時系列の画面の前例。docstring と出力の見た目。何を帯に畳み、何を落としたか |
| 6 | dev-tools `claude/plugins/dev-tools/skills/playwright/SKILL.md` | スクリーンショットの撮り方。「前提」と「ローカルキャプチャ」の節 |

## 事業の文脈の要約

- 見る人は川崎さん 1 人、PC。目的は認知負荷を減らすこと: 開いて 10 秒で「どこを見ればいいか」が分かる。各画面はまず数字・状態・一言、詳細は `<details>` などで畳む。全部見られるが全部並べない。
- 画面は charter の 5 つ（一覧・プロジェクトの中・受け箱・パフォーマンス・監査の改訂案と unclear）。サイドメニューで行き来。読むだけ。
- Astro の静的な書き出し（`astro build`）で動く形にする。将来 Cloudflare Pages に載せる見込みだが、設定・公開はしない。

## これまでの経緯

- p3 で `org_timeline.py` が 1 プロジェクト 1 枚の静的 HTML を作った。p5 はその後継で、全プロジェクトを 1 か所で見る。PM の指定でスキーマが先、export と並べて作る。

## 作業の注意

- 入れた npm パッケージと理由を報告に書く（Astro と、要るなら最小限）。
- スクリーンショット: dev server（`astro dev` か `astro preview`）を立ててから Playwright で撮る。`localhost` への通信はサンドボックスで落ちることがある（スキルの「前提」）。撮れないときは、何で落ちたかを添えてリーダーへ。Chrome の拡張（claude-in-chrome）は川崎さんのブラウザを使うので使わない。
- README の立ち上げ方は 1 コマンド 1 行（`\` の行継続・heredoc を使わない）。`orgctl export` → ビューアの起動 の順。
- export がまだできていない間は、スキーマに沿った手書きの小さな `snapshot.json` で作り始めてよい。最後は実物（p1〜p4）で表示を確かめる。
