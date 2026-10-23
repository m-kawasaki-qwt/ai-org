# ai-org

AI 組織（コンポーネント: プロジェクト・チーム）の実行場所。プロジェクトは `projects/<slug>/` に置く。

- メンバーの決まりは、起動のときのシステムプロンプトにある（各メンバーのディレクトリの CLAUDE.md と同じ中身）。この repo の CLAUDE.md には足さない。
- 雛形と CLI（orgctl）は dev-tools の `org/`、プランは dev-tools の `docs/todo/ai-org-plan.md`。

## コミットとプッシュ

- **コミット・プッシュするのは根っこの側（プロジェクトを立ち上げ、`ORG_MEMBER=user` で動かしているセッション）だけ。** メンバー（PM・リーダー・作業者・レビュアー・監査役）は git を触らない。
- **根っこの側がコンポーネントを閉じたら、指示を待たずにコミットしてプッシュする**（全 repo の共通規範「git は指示があるときだけ」に対する、この repo だけの例外）。`orgctl teardown` が出す `git add`・`git commit`・`git push` の行を、1 行ずつ単独で打つ。子のコンポーネントは PM が閉じるので、その分は根っこの側が次に閉じるときにまとめて入る。
- ブランチは `main` に直接積む。ここに入るのは組織の記録と組織内の道具だけ。プロダクトの repo の成果物は、その repo の決まり（PR）に従う。
- 残すもの: `charter.md`・`component.json`・`log/`（1 行報告と本文）・`reports/sessions/`・`thread.md`・チームの結果・`tools/`。残さないもの（`.gitignore`）: 起動中のメンバーの足場。
