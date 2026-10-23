# 目的

川崎さんが、AI 組織（ai-org）の中で何が起きているか・何が起きたかを、ファイルを開いて回らずに掴めるビューアを作る。**この組織を作った目的は、川崎さんがボトルネックにならずに仕事が回り、間違いが分かり、直ることにある（ai-org の `policy.md`）。ビューアの目的は、川崎さんの認知負荷を減らすこと。** 全部を見られるようにはするが、全部を並べない。要点を先に、抽象から見せ、詳細は畳んで、必要なときだけ開ける形にする。

決まっている作り方（dev-tools の `docs/todo/ai-org-plan.md` の決まったこと 24・決定ログ）:

- **データの形を先に決め、表示はそこから機械的に作る。** 記録（`projects/*/` の `log/events.log`・`log/msgs/`・`component.json`・`reports/sessions/*.yaml`・`log/user-inbox.yaml`）を読む正は orgctl の 1 か所。orgctl に `export` を足し、正規化した `snapshot.json`（スキーマ付き）を書き出す。ビューアはそれを描くだけで、記録を自分で解釈しない。
- **画面は Astro。** PC で見る前提（スマホは当面考えない）。サイドメニューで行き来する。読むだけで、編集はしない。
- **当面はローカル**（`astro dev` か、書き出した静的なファイル）。将来、他のメンバーへ配る段で Cloudflare Pages に載せることを考えて、Astro の静的な書き出しで動く形にしておく（Cloudflare への設定・公開はしない）。

# 完了条件

1. dev-tools の orgctl に `export` があり、ai-org の全プロジェクト（`projects/*`）の記録から `snapshot.json` を書き出せる。スキーマ（JSON Schema か、型の定義と説明の md）がある。1 行報告の種類の扱い（数えるための行を外す等）は orgctl の既存の定義（`NOISE_KINDS` など）を使い、二重に定義しない。
2. ai-org に Astro のビューアがあり、`snapshot.json` だけを読んで次を見せる。どれも、まず要点（数字・状態・一言）を見せ、詳細は畳む。
   - プロジェクトの一覧（状態・期間・トークン・川崎さん宛ての未読の数）
   - プロジェクトの中: コンポーネントの木とメンバーの状態、時系列（今の `tools/org_timeline.py` の後継）、往復の回数・作り直し
   - 川崎さん宛ての受け箱（`user-inbox.yaml`）
   - パフォーマンス（時間・トークン・往復・作り直し。プロジェクトごと・立場ごと）
   - 監査の改訂案と、セッション報告の `unclear`（決まりで分からなかった点）の一覧
3. 今ある記録（p1〜p4 の 4 プロジェクト）で実際に表示でき、画面のスクリーンショット（主要な画面ごとに 1 枚）を報告に付ける。
4. 立ち上げ方（`orgctl export` → ビューアの起動）が、ai-org の README に 1 行ずつのコマンドで書いてある。

# 範囲

- 書いてよい場所:
  - dev-tools の worktree `/Users/maka343noshi/orca/workspaces/dev-tools/org-viewer`（orgctl の export とスキーマ）。dev-tools の本体（`~/ghq/.../dev-tools`）は読むだけ。動いている組織はそちらの orgctl を使っているので、本体を書き換えない。
  - ai-org の worktree `/Users/maka343noshi/orca/workspaces/ai-org/viewer`（ビューア・README）。ai-org の本体の `projects/` は読むだけ（記録はここにある。export の入力として読む）。
  - このプロジェクトのディレクトリの中。
- 作業者は、それぞれの worktree を `--workdir` にして起動する（その repo の CLAUDE.md・スキルが効く）。
- git の操作はしない（worktree のブランチへのコミットと PR は根っこの側がやる）。Cloudflare への設定・公開はしない。
- npm のパッケージを入れてよい（Astro と、要るなら最小限）。入れたものと理由を報告に書く。
- うまくいかなかったこと（文脈パックの過不足・連絡・決まり・worktree での起動）は、隠さずセッション報告の `unclear` と最後の報告に書く。
