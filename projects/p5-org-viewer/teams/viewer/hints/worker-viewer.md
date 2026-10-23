# ヒント: worker-viewer

- 形の正はリーダーのスキーマ `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/schema.md`。最後の節に、画面ごとに使う項目の対応がある。足りない項目は自分で記録を読みに行かず、リーダーへ。
- Astro のプロジェクトは worktree 直下の `viewer/` に置く（`/Users/maka343noshi/orca/workspaces/ai-org/viewer/viewer/`）。データは `viewer/data/snapshot.json` をビルドのときに import する。export がまだ無い間は、スキーマに沿った手書きの小さな snapshot.json で作ってよい（export の作業者が出したら実物に差し替える。リーダーから知らせる）。
- 依存は Astro だけを目標に。UI フレームワーク・CSS フレームワークは入れない（静的な HTML と少しの CSS、`<details>` で畳む）。グラフも素の CSS の棒で足りる。
- ページ: `/`（一覧）・`/projects/[id]`（中）・`/inbox`・`/performance`・`/audit`。共通のレイアウトにサイドメニュー（受け箱の未読の数をバッジで）。
- 各画面の冒頭は「数字・状態・一言」の 1 段だけにして、10 秒で見る所が分かるようにする。例: 一覧なら「開いている 1・未読 N・判断待ち N」、中なら「いま誰が何をしているか（last_event と動いているメンバー）」。時系列は lifecycle を 1 本の帯に畳み、message だけを並べ、本文は `<details>` で開く。
- `null` は「—（片づけ前）」。0 と書かない。
- スクリーンショットは 5 画面ぶん `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/screenshots/` に。プロジェクトの中は p3（往復と作り直しがある）を撮る。
- README（worktree 直下の README.md）に立ち上げ方を 1 行ずつ: export → `npm install`（初回）→ `npm run dev` か build＋preview。
