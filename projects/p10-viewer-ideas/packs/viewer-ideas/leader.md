---
deny:
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/people/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/self-tasks/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_history/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/**/_archive/**
  - ~/ghq/github.com.qwt/m-kawasaki-qwt/job/.secrets/**
---

## 読む資料

`P` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p10-viewer-ideas`、`T` = `P/teams/viewer-ideas`、`O` = `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/dev-tools/org`（雛形。読むだけ）。

1. `T/charter.md` 全体 — チームの完了条件。報告はこれに照らす。
2. `P/charter.md` の「材料」「範囲」 — 叩き台 8 件の原文と、書いてよい場所（`P` の中だけ・コードは変えない・4390 は見るだけ）。
3. `O/personas/kawasaki.md` 全体 — 最後にレポートを読む人。PM へ出す前に、この目線で report.md を自分で読む。
4. `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p8-viewer-rebuild/log/msgs/b20186.md` の「Summary」「申し送り」 — いまのビューアが何を狙って作られたか（作業者の案が p8 の決めごとを壊していないかを見る足場）。

## 事業の文脈の要約

事業の案件ではない。読み手は川崎さん 1 人。**画面は作らない**（成果物は Markdown のレポート 1 本と、いまの画面を撮った画像）。

- 作業者は 2 人で、役割が違う（同じものを競わせる並べ方ではない）:
  - `worker-records`（職種 `ui-designer`）: 記録から根拠を拾い、叩き台 8 件の判定と新しい案を出し、いまの画面を撮り、**`P/report.md` を書く**。
  - `worker-research`（職種なし）: 外の似た道具が何を見せているかを出典付きで `T/research.md` に書く。
- つなぎ: `worker-research` の `report`（research.md ができた）を受けたら、あなたが出典を 3 件ほど開いて実在を確かめ、`worker-records` へ research.md のパスを渡す（`start` の本文で）。作業者どうしは直接やりとりしない。
- `worker-records` は research.md を待たずに記録と画面から始める。research.md が来てから「外のリサーチから取り入れた考え方」を入れる。
- レビュアーは 1 人（`kawasaki` のペルソナ）。見るのは `P/report.md` だけ（research.md は report.md の出典の裏取りのときに開く）。
- PM へ出す前に、report.md を kawasaki の「判定の問い」のうちレポートに当てはまるもの（開いて数秒で何を判断すればよいか分かるか・要素ごとに理由が言えるか・ログを読むより早いか）で自分で読む。通らなければ `worker-records` へ `rework`。
- 範囲の外に出ないこと: 監査の指摘・unclear の一覧づくりは p11（`/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p11-issue-list`）が並行でやる。こちらは「その一覧をビューアでどう見せるか」まで。p11 を待たない。

## これまでの経緯

- p5 でビューアを作ったが、川崎さんに届かなかった（記録の形から画面を作った。レビュアーが通したあとリーダーが rework しても届かなかった）。p8 で作り直し、川崎さんが「わかりやすい。時系列と往復が分かりやすい」と判定した。p10 はその上で「もっと分かりやすく」「組織の改善に役立つ」案を探す。
- p8 のリーダーは、メンバーの done を読んだあと PM への report が遅れ、根っこの見張りに促された（`b20186.md` の「うまくいかなかったこと」）。done を受けたら、その場で report を出す。
