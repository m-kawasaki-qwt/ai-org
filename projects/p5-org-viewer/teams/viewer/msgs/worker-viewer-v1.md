# 作業者 第1版（手書き snapshot.json で作ったもの）

実物（p1〜p4）の snapshot.json はまだ無いので、完了条件 3 の「実物で表示」は未確認。export が出たら差し替えて確かめる。

## 成果物（ai-org worktree `/Users/maka343noshi/orca/workspaces/ai-org/viewer`）
- `viewer/`（Astro。依存は astro のみ）: `src/pages/{index,inbox,performance,audit}.astro`・`src/pages/projects/[id].astro`・`src/components/Tree.astro`・`src/layouts/Layout.astro`・`src/lib/snap.ts`・`data/snapshot.json`（手書きのサンプル。開いている 1・閉じた 1。往復・NG・unclear・監査案あり）
- `README.md` の「ビューア」節（export → npm install → dev / build → preview。1 行ずつ）
- スクリーンショット: `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/screenshots/` の 1-projects・2-project-detail・3-inbox・4-performance・5-audit（.png）

## 完了条件ごとの確かめ
- 2（5 画面・要点→詳細は畳む）: `astro build` 後に preview を立て、Playwright で 5 画面を撮って目視。冒頭は 1 段の数字（一覧は 開いている・未読・判断待ち、中は いま／最後・動いているメンバー・往復・作り直し）。時系列は lifecycle を帯に畳み、message だけ `<details>`。null は「—（片づけ前）」。サイドメニューに受け箱の未読バッジ。
- 3: `astro build` は通った（6 ページ）。実物 4 プロジェクトでの表示は未（export 待ち）。スクリーンショットは手書きデータ分。
- 4: README に記載。

## 入れたパッケージ
- astro のみ（ビューアの dependencies）。UI・CSS フレームワークは入れていない。撮影用の playwright は scratchpad に入れ、repo には入れていない。

## 気づき（unclear）
- npm の既定キャッシュ（~/.npm）の権限が壊れていて `--cache` を TMPDIR に向けた。README の `npm install` は、その環境では同じ指定が要るかもしれない。
- `astro preview` と Playwright はサンドボックスの外で実行した（localhost の待ち受け・接続）。
- Astro は 7.x が入った。
