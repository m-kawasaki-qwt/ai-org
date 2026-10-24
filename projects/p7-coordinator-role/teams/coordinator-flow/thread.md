
## 作業者 第1版

- coordinator/position.md を新しい流れで書き直し（責任の範囲・返すもの 1〜5・往復の event の表・合意後も残り wrap_up で終わる）、その言葉を PM・org-team-setup・リーダー・org-assign・README・プランへ写した。
- event は既存の種類だけ: 相談／視点を足す＝start、返し＝report、合意＝PM からの report、終わり＝wrap_up。rework は REMAKE_KINDS に入るので使わない。
- パックの置き場は <親>/packs/<チーム名>/<立場>.md。orgctl は new が packs/ を作るのをプロジェクトだけにした（2 行）。digest は直さず、規範で絶対パスと書いた。
- CLI の試しは $TMPDIR/coord-trial.sh（往復 2 回・パック v1→v2・assign --pack で 3 人に v2 と deny が入った）。詳細は review_request の本文。

## レビュアー 第1回

承認。完了条件 1〜8 を照らした。grep（古い流れの残り）は自分で打ち直し、残りは過去の記録の 5 行だけ。CLI は自分の仮の根っこ（$TMPDIR/rv）で new → assign coordinator → 往復 2 回 → 合意 → packs/beta → new team → assign 3 人 --pack → wrap_up まで打ち、3 人の CLAUDE.md・pack.md にパック本文、settings.json に deny が入り、チームに packs/ が無いことを確認した。
