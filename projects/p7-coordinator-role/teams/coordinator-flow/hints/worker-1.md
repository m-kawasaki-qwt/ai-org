# worker-1 へのヒント

- まずコーディネーターの `position.md` を新しい流れで書き直し、そこで決めた言葉（相談・返し・視点を足して返す・合意の event の種類、パックの置き場 `<親>/packs/<チーム名>/<立場>.md`、`wrap_up` で終わる）を正にして、PM・org-team-setup・リーダー・README・プランへ同じ言葉で写すと、用語がぶれにくいと思う。
- event の種類は、既存の種類（`start`・`report`・`rework` など）で足りるならそれを使い、orgctl に新しい種類を足すのは要るときだけ。足すなら理由を報告に書く。
- `orgctl new` がチームにも `packs/` を作る件と、`digest` が名前だと引けない件は、直すか直さないかを決めて、理由を報告に書く（完了条件 3）。直すなら W の orgctl だけ。本体は触らない。
- 完了条件 4 の grep は、打ったコマンドと出た行をそのまま報告に貼る。過去の記録として残した行は「残した理由」を添える。
- 完了条件 7 の CLI の試しは、`$TMPDIR` の下の仮の根っこに対して W の orgctl（`/Users/maka343noshi/orca/workspaces/dev-tools/coordinator-role/org/scripts/orgctl.py`）で打つ。`launch` は打たない。打ったコマンドと、`CLAUDE.md`・`pack.md`・`.claude/settings.json` に何が入ったかを報告に残す（レビュアーが同じ手順で打ち直せるように）。
- 書いてよいのは W の中と `$TMPDIR` だけ。git は触らない。
