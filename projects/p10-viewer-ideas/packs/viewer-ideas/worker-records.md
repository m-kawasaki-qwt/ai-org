---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`R` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`、`P` = `R/projects/p10-viewer-ideas`、`T` = `P/teams/viewer-ideas`、`O` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/org`（雛形。読むだけ）。

1. `T/charter.md` 全体 — 照らす完了条件。
2. `P/charter.md` の「材料」 — 叩き台 8 件の原文。1 件ずつ 採る／採らない／形を変える を付ける。
3. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/job/company/system/ai-org/feedback/2026-10-24-viewer.md` の「画面ごとの指摘」「UI 全体の指摘」 — 川崎さんが何に困ったかの原文（p5 のビューアへの指摘。p8 で直ったものと残るものを分ける）。
4. `O/personas/kawasaki.md` 全体 — 読み手。案の価値は「川崎さんの何の判断が早くなるか」で書く。
5. `O/common/ui/principles.md`（U-01〜U-12）と `O/common/ui/checklist.md` の B — 見せ方の案の基準。とくに U-03（概観と詳細）・U-05（時間の変化は帯・折れ線、比較は棒）・U-06（数字の比べる相手）。
6. `R/projects/p8-viewer-rebuild/teams/viewer/design.md` の「画面の一覧と行き来」「要素ごとの理由」「外す画面」「snapshot に要るもの」 — いまの画面がなぜその形か。案がこの決めごとを壊すなら、そう書く。
7. `R/projects/p8-viewer-rebuild/log/msgs/b20186.md` の「申し送り」「うまくいかなかったこと」 — p8 が残した問題。
8. 根拠の記録: `R/projects/p1-*`〜`p9-*` の `log/events.log`（1 行報告）・`log/msgs/<hash>.md`（本文）・`reports/sessions/*.yaml`（`machine` に時間 `span_min`・トークン `tokens_total`、`self` に `unclear`・`not_done`）・`R/projects/p9-org-watch/reports/audit/` — 「困った・分からなかった」の根拠。どのプロジェクトのどのファイル・hash かを必ず控える。
9. いまのビューアのコード `R/viewer/src/`（`pages/index.astro`・`pages/p/[id].astro`・`pages/rules.astro`・`lib/model.ts`）とデータの形 `O/schema/snapshot.schema.json` — 案ごとの「作る重さ」（いまのデータにあるか・足すなら orgctl export を変えるか）を判断する。読むだけ。
10. `O/common/screen-check.md` の「何で撮るか」「撮り方の注意」 — いまの画面を撮る手順。

`T/research.md` は `worker-research` が書く。リーダーから `start` でパスが来たら読み、「外のリサーチから取り入れた考え方」に使う。来る前は待たずに 1〜10 で進める。

## 事業の文脈の要約

事業の案件ではない。読み手は川崎さん 1 人（PC・900〜1800px・ダーク）。**このチームは画面を組み立てない**ので、`ui-designer` の規範の `design.md` は書かない。U-01〜U-12 と B は、見せ方の案を書くときの基準として使う。

- 書くもの: **`P/report.md`**（プロジェクトの直下。チームのディレクトリではない）。画像は `T/screenshots/` に置き、report.md からは `teams/viewer-ideas/screenshots/<名前>.png` の相対パスで貼る。根拠の一覧が長くなるなら `T/evidence.md` に分け、report.md からリンクする。
- report.md の形（kawasaki の目線で「長すぎず、要点から先に、開いて回らずに掴める」）:
  - 冒頭に Summary（1 画面に収まる量）と、推奨する上位 3〜5 件（名前は 10 字程度・なぜ先か 1 行）。
  - 案ごとに同じ欄: 問題（記録の根拠: プロジェクト・ファイルか hash）／見せ方／川崎さんにとっての価値／作る重さ（データの足し・画面の足し・orgctl の変更の有無）／優先度と理由／いまの画面のどこを変えるか（画像）。根拠を示せない案は「根拠なし（推測）」と書く。
  - 叩き台 8 件の判定は 1 つの表（番号・判定・理由 1 行・本文のどの案になったか）。
  - 外のリサーチから取り入れた考え方は、出典（URL）付き。
- 画面を撮る: `http://localhost:4390` を**見るだけ**（止めない・再起動しない）。待ち受けを別に立てる必要があれば 4391〜4399 を使い、終わったら止める。Playwright はサンドボックスの外・scratchpad に入れる（10 の手順）。撮るのは ホーム・プロジェクトの画面（動いているもの 1 つと閉じたもの 1 つ。p8 か p9）・決まりの直し候補。どこを変えるかは、画像に枠を描く（scratchpad の Python で）か、画像の下に「どの要素か」を 1 行で書く。新しい画面の絵は要らない。
- 数（介入の回数・差し戻しの回数・時間・トークンなど）はスクリプトで数え、スクリプトは `T/scripts/` に残す。暗算しない。
- 範囲の外: 監査の指摘・unclear の一覧づくりは p11（`R/projects/p11-issue-list`）が並行でやる。叩き台 7（直し待ちの画面）は「その一覧をどう見せるか」までにする。p11 の `issues.md` ができていれば形の参考にしてよいが、待たない。
- 書いてよい場所は `P` の中だけ。ai-org の `viewer/`・dev-tools・job は読むだけ。git は触らない。

## これまでの経緯

- p5 のビューアは記録の形から作り、川崎さんに届かなかった（3 の原文）。p8 で 3 画面（いま／プロジェクト／決まりの直し候補）に作り直し、川崎さんが「わかりやすい。時系列と往復が分かりやすい」と判定した。良いと言われた所（時系列の図と往復の線）を崩す案は、崩す理由を書く。
- 叩き台 2（データの時刻と古い写しの警告）は、古い写しで「動いている」と出て川崎さんが混乱したことが元（根っこのセッションの申告）。記録の中に根拠が見つかれば、その場所を書く。見つからなければそう書く。
- 叩き台 3（誰が誰を待っているか）は、p8 で全員が待ちに入って止まったことが元（`R/projects/p9-org-watch/charter.md` の「問題 1」に経緯がある。p6 でも同じ形。p9 で見張りが検知するようにしたので、ビューアに出す意味が残るかも判定する）。
