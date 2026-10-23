# ヒント: worker-export

- 形の正はリーダーのスキーマ `/Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects/p5-org-viewer/teams/viewer/schema.md`。最初にこれを JSON Schema（`org/schema/snapshot.schema.json`）に起こし、それに合わせて export を書く。形に迷ったら自分で変えずリーダーへ。
- orgctl.py に `cmd_export` を足すのがいちばん素直。`read_events`・`NOISE_KINDS`・`member_state`・`load` をそのまま呼ぶ（写さない）。ファイルが長くなるのが気になるなら、組み立ては関数に分けるだけでよく、別モジュールにしなくてよい。
- 読むだけを守る: `inbox` 系（offset・ack を書く）・`append_event` を呼ばない。`member_state` は会話ログの mtime を見るだけなので呼んでよい。
- YAML は全部を読まない。セッション報告の `machine:` は orgctl 自身が `yaml_dump` で書いた形（2 スペース字下げ・値は JSON の文字列か数・null）なので、その形だけを読む小さな関数で足りる。`self:` は `unclear:` などの下の `- ` 行を拾い、原文も残す。`user-inbox.yaml` も `yaml_dump` の形。
- 本番のデータで試す: `--projects /Users/maka343noshi/ghq/github.com.qwt/m-kawasaki-qwt/ai-org/projects --out /Users/maka343noshi/orca/workspaces/ai-org/viewer/viewer/data/snapshot.json`。p1（ファイル名に session の頭が無い）・p3（監査役の改訂案 5 件・rework・review_ng）・p4（user-inbox）・p5（開いている。報告ゼロ）で、それぞれ値が実物と合うかを自分で突き合わせる。
- スキーマの確かめ（`--check` など）も標準ライブラリだけで。最初に一度 snapshot.json を出したら、ビューアの作業者が使えるので早めに出してよい（リーダーへ一言 report をくれると助かる）。
- 自分で確かめたこと（各プロジェクトの数・監査の件数・unclear の件数）を review_request の本文に書く。
