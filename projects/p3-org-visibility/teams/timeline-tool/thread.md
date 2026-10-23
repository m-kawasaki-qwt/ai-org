
## 作業者 第1版
- 成果物: tools/org_timeline.py、tools/tests/test_org_timeline.py、tools/tests/fixtures/tl/、projects/p1-org-status/timeline.html、projects/p2-orca-run-use/timeline.html
- テスト: python3 -m unittest discover -s tools/tests → 15 件通過（既存 7 + 新規 8）
- 出す/まとめる/落とす: 人の報告と未知の種類は列に出す。assign・launch・teardown は帯の頭の「起動〜終了」に畳む。component_new/closed は出さない。ack・notify_sent・notify_recv は件数のみ。

## レビュアー 第1回
- 承認（review_ok f315e9）。指摘なし。完了条件 1〜5 を確かめた（打ち直すとバイト一致・外部参照 0・ヘッドレス Chrome で表示を目視・本文 p1 14 件／p2 18 件・テスト 15 件 OK）。
- 申し送り: p1 の pm は 2 回起動したがセッション報告は上書きされて 1 回分しかない／「畳んだもの」の文言で component_new・component_closed も畳んだと書いてあるが、実際は出していない。
## 作業者 第2版
- rework 2点を直した: 起動2回以上は「最後の起動分のみ」を帯の頭と表に表示／「畳んだもの」の文言を実装どおりに／done 行末の「-」を消した。
- p1・p2 再生成、unittest 16 件通過。

## レビュアー 第2回（第2版へ）
- rework の 3 点は直っていることを確かめた。テストは 16 件 OK、打ち直すとバイト一致。
- 指摘（review_ng 6acb52）1. 完了条件3／目的: いまの orgctl が書く notify_skipped が NOISE に入っておらず、人の報告として列に出る（p3 では 31 件中 11 件）。notify_ で始まる種類を件数だけの扱いにし、fixture とテストを足せば通す。
## 作業者 第3版
- notify_ で始まる種類と ack を件数のみの扱いに（is_noise）。fixture に notify_skipped を足し、列に出ず件数に出ることをテスト。unittest 16 件通過、p1・p2 再生成。

## レビュアー 第3回（第3版へ）
- 承認（review_ok dc84e7）。notify_ で始まる種類と ack を件数だけの扱いにしたことを確かめた（p3 で列に 0 件、件数欄に 13 件）。テスト 16 件 OK、p1・p2 はバイト一致。
