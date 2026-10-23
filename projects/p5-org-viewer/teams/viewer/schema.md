# snapshot.json のスキーマ（v1）— リーダーが確定

export（orgctl）とビューア（Astro）の両方がこれを正とする。形を変えたくなったら、自分で変えずリーダーへ（`escalate` か `report`）。変えるときはリーダーが両方へ同じ差分を渡す。

## 置き場所とコマンド

- 書き出し: `python3 <dev-tools>/org/scripts/orgctl.py export --projects <ai-org>/projects --out <ai-org>/viewer/data/snapshot.json`
  - `--projects` は `projects/` のディレクトリ（`ORG_MEMBER` などの環境変数に頼らない）。読むだけ。offset・ack・events.log に何も書かない。
- 確かめ: `orgctl export ... --check <snapshot.json>`（または別のサブコマンド）で、下の JSON Schema に合うかを標準ライブラリだけで確かめる（型と必須の確認でよい）。
- JSON Schema の実体: dev-tools の `org/schema/snapshot.schema.json`（export の作業者が、この md から書く）。この md が説明、JSON Schema が機械の正。
- ビューア: ai-org の `viewer/`（Astro のプロジェクト）。`viewer/data/snapshot.json` をビルドのときに読む。ほかのファイル（`projects/` の記録）を読まない。

## 共通の約束

- 時刻はすべて ISO 8601（オフセット付き。記録の値をそのまま）。
- 時間は分（`*_min`、小数 1 桁）。トークンは整数。
- **分からない値は `null`。0 と区別する**（例: 開いているプロジェクトのトークン）。
- 数えるための行（`orgctl.py` の `NOISE_KINDS`）は、`timeline`・回数の集計のどれにも入れない。export は `NOISE_KINDS` を import して使い、自前の集合を持たない。
- パスは `projects/` からの相対（例: `p3-org-visibility/log/msgs/95df09.md`）。
- 並び順: 一覧は新しい順（プロジェクトは `created_at` の降順、受け箱は時刻の降順）。`timeline` だけは古い順（時系列）。

## 決めたこと（リーダーの判断。PM の指定どおりここに書く）

1. **川崎さん宛ての未読の数（`unread_to_user`）**: events.log の、宛先が `user` で種類が `NOISE_KINDS` に無い行のうち、行番号が `log/.inbox_user`（ユーザーの既読の位置＝ events.log の行番号）より大きいものの数。`.inbox_user` が無ければ 0 行目（全部未読）。`user-inbox.yaml` の `read` は常に false で既読にする仕組みが無いため、数えるのに使わない。
   - 受け箱の 1 件の `unread` も同じ基準: `ref` の行の番号 > 既読の位置。`ref` が無い件（`kind: stuck` など）は、`at` が「既読の位置の行の時刻」より後なら未読。
2. **監査の改訂案（`audit_proposals`）**: 立場が `auditor` のメンバー（id の最後の段が `auditor`、またはセッション報告の `machine.position` が `auditor`）が出した `report` の本文から拾う。本文の `## ` 見出しに「改訂案」を含む節の中の、`1. **題** — 対象` の形の番号付きの項目を 1 件ずつにする（項目の下の行は `body` に markdown のまま入れる）。その形で 1 件も取れなければ、本文全体を 1 件（`number: null`・`title` は本文の最初の `# ` 見出し）として入れ、`parsed: false` にする。改訂案の節に入らない部分（観察・好みで決まる点）は `report_body` に原文で持つ。
3. **開いているプロジェクト・片づけ前のメンバーのトークンと時間**: セッション報告が無いメンバーのトークン・時間は `null`。プロジェクトの合計は、報告のあるメンバーの分だけを足し、`metrics_complete: false`（報告の無いメンバーが 1 人でもいる）を付ける。報告が 1 件も無ければ合計も `null`。ビューアは `null` を「—（片づけ前）」と出し、0 と書かない。

## 全体

```jsonc
{
  "schema_version": 1,
  "generated_at": "2026-10-24T02:00:00+09:00",
  "source": "/Users/.../ai-org/projects",      // --projects の絶対パス
  "noise_kinds": ["ack", "notify_recv", ...],   // NOISE_KINDS をそのまま（ソート）。表示の説明用
  "totals": Totals,                              // 一覧の上に出す要点
  "projects": [Project],                         // created_at の降順
  "inbox": [InboxItem],                          // 全プロジェクトの受け箱。時刻の降順
  "audit_proposals": [AuditReport],              // 監査の report ごと
  "unclear": [UnclearItem],                      // 全セッション報告の unclear
  "performance": Performance
}
```

### Totals

| 項目 | 型 | 説明 |
|---|---|---|
| `projects_open` / `projects_closed` | int | 状態ごとの数 |
| `unread_to_user` | int | 全プロジェクトの `unread_to_user` の合計 |
| `escalations_open` | int | 宛先が `user` の `escalate`・`blocked` で、既読の位置より後のもの |
| `tokens_total` | int\|null | 全プロジェクトの合計（報告のある分） |
| `unclear_count` / `audit_proposal_count` | int | 件数 |

### Project

| 項目 | 型 | 説明 |
|---|---|---|
| `id` | string | `p3-org-visibility`（slug） |
| `purpose` | string | charter.md の「# 目的」直後の最初の段落の 1 文目（`。` まで。無ければ段落を 120 字で切る） |
| `status` | `"open"`\|`"closed"` | component.json |
| `created_at` / `closed_at` | string / string\|null | component.json |
| `duration_min` | number | 閉じていれば closed−created、開いていれば generated_at−created |
| `tokens_total` | int\|null | 決めたこと 3 |
| `session_span_min_total` | number\|null | セッション報告の `span_min` の合計（決めたこと 3 と同じ扱い） |
| `metrics_complete` | bool | 決めたこと 3 |
| `unread_to_user` | int | 決めたこと 1 |
| `counts` | Counts | プロジェクト全体の回数 |
| `last_event` | Event\|null | `timeline` の最後（「いま何が起きているか」の一言用） |
| `tree` | Component | 根のコンポーネント（プロジェクト自身）。子は `children` に入れ子 |
| `timeline` | [Event] | NOISE_KINDS を除いた全行。古い順 |

### Counts（プロジェクトとチームで同じ形）

| 項目 | 型 | 説明 |
|---|---|---|
| `events` | int | NOISE_KINDS を除いた行数 |
| `round_trips` | int | `review_request` の数（作業者 → レビュアーの往復の回数） |
| `review_ng` / `review_ok` / `rework` / `reassign` / `escalate` / `blocked` | int | その種類の行数 |
| `remakes` | int | 作り直し＝ `review_ng` + `rework` + `reassign` |

### Component

| 項目 | 型 | 説明 |
|---|---|---|
| `id` | string | `p3-org-visibility/teams/timeline-tool` |
| `kind` | `"project"`\|`"team"` | |
| `status` / `created_at` / `closed_at` | | component.json |
| `purpose` | string\|null | そのコンポーネントの charter.md の目的の 1 文目（Project と同じ切り方） |
| `counts` | Counts | from か to がこのコンポーネント配下（id がこの id で始まる）の行だけで数える。プロジェクトの根では Project の counts と同じ |
| `members` | [Member] | component.json の `members` の順 |
| `children` | [Component] | component.json の `children` の順 |

### Member

| 項目 | 型 | 説明 |
|---|---|---|
| `name` / `id` | string | component.json の members のキーと値 |
| `position` | string | セッション報告の `machine.position`、無ければ member.json、どちらも無ければ name から数字と `-…` を落としたもの |
| `occupation` / `model` | string\|null | セッション報告（`model_requested`）か member.json |
| `state` | string | 下の表 |
| `state_note` | string | `member_state` の note（無ければ空） |
| `session` | Session\|null | このメンバーのセッション報告（入れ替えで複数あるときは最後のもの。全部は `performance.sessions` にある） |

`state`: member.json があれば orgctl の `member_state()` の戻り値をそのまま（「進んでいる」「止まっている?」「終わった」「未起動」「片づけ済み」など）。member.json が無くセッション報告があれば「片づけ済み」。どちらも無ければ「不明」。

### Event

| 項目 | 型 | 説明 |
|---|---|---|
| `n` | int | events.log の行番号 |
| `ts` / `id` / `from` / `to` / `kind` | string | `read_events` の値 |
| `group` | `"lifecycle"`\|`"message"` | `component_new`・`component_closed`・`assign`・`launch`・`teardown` は lifecycle（帯に畳む対象）、ほかは message |
| `component` | string\|null | from（無ければ to）が属するコンポーネントの id（メンバー id の親）。`user` は null |
| `msg` | string\|null | 本文のパス（`kv.msg` を projects 相対に） |
| `summary` | string | 本文の最初の空でない行（注記 `<!-- -->` を除き、先頭の `#` を落とす）。本文が無ければ detail |
| `body` | string\|null | 本文の markdown 全文（1 行目の注記を除く）。本文が無ければ null |
| `unread` | bool | 宛先が `user` で決めたこと 1 の未読なら true。ほかは false |

### InboxItem

`user-inbox.yaml` の各件と、宛先が `user` で NOISE_KINDS に無い行のうち `user-inbox.yaml` に同じ `ref` が無いもの（patrol が入る前の p1〜p3 の分）を合わせる。

| 項目 | 型 | 説明 |
|---|---|---|
| `project` | string | |
| `source` | `"user-inbox"`\|`"events"` | どちらから来たか |
| `at` | string | user-inbox は `at`、events は `ts` |
| `kind` / `from` | string | |
| `ref` | string\|null | |
| `summary` | string | user-inbox の `summary`、events は Event の summary |
| `msg` / `body` | string\|null | Event と同じ |
| `unread` | bool | 決めたこと 1 |

### AuditReport・AuditProposal

| AuditReport | 型 | 説明 |
|---|---|---|
| `project` / `from` / `ts` / `ref` / `msg` | | 監査役の report の行 |
| `title` | string | 本文の最初の `# ` 見出し |
| `proposals` | [AuditProposal] | 決めたこと 2 |
| `report_body` | string | 本文の全文（畳んで出す用） |
| `parsed` | bool | 番号付きの項目が取れたか |

| AuditProposal | 型 | 説明 |
|---|---|---|
| `number` | int\|null | 項目の番号 |
| `title` | string | `**…**` の中 |
| `target` | string\|null | `—` の後ろ（変える先のファイル） |
| `body` | string | 項目の下の行（markdown） |

### UnclearItem

| 項目 | 型 | 説明 |
|---|---|---|
| `project` / `member_id` / `position` | string | |
| `text` | string | unclear の 1 項目 |
| `report` | string | セッション報告のパス（projects 相対） |

`self:` は書き手ごとに形が揺れる。`unclear:` の下の `- "…"`（引用符あり・なし）を 1 件ずつ拾う。読めなければ拾わない（落ちない）。

### Performance

```jsonc
{
  "sessions": [Session],          // 全セッション報告。project・closed_at の順
  "by_project": [PerfRow],        // key = project id
  "by_position": [PerfRow]        // key = position（pm・leader・worker・reviewer・auditor・coordinator）
}
```

| Session | 型 | 説明 |
|---|---|---|
| `project` / `member_id` / `position` / `model` | string | `model` は `model_requested` |
| `launched_at` / `closed_at` | string\|null | |
| `span_min` | number\|null | |
| `tokens_total` | int\|null | |
| `tokens` | object\|null | `input`・`output`・`cache_read`・`cache_write` |
| `api_messages` | int\|null | |
| `events_sent` | object | 種類 → 数 |
| `review_ng_count` | int | |
| `report` | string | セッション報告のパス |
| `self` | SelfReport | |

| SelfReport | 型 | 説明 |
|---|---|---|
| `asked` | string\|null | |
| `unclear` / `escalated` / `not_done` | [string] | 拾えた分 |
| `raw` | string | `self:` の原文（拾えなかった項目はここで読める） |

| PerfRow | 型 | 説明 |
|---|---|---|
| `key` | string | |
| `sessions` | int | セッション報告の数 |
| `span_min_total` | number\|null | |
| `tokens_total` | int\|null | |
| `tokens_per_session` | int\|null | 合計 ÷ sessions（四捨五入） |
| `round_trips` / `remakes` | int | by_project はそのプロジェクトの Counts。by_position は、その立場のメンバーが from の `review_request` の数 / 立場のメンバーが from か to の `review_ng`・`rework`・`reassign` の数 |
| `metrics_complete` | bool | 報告の無いメンバーを含むなら false |

## ビューアの画面と使う項目（対応表）

| 画面 | 使う項目 |
|---|---|
| プロジェクトの一覧 | `totals`、`projects[].{id,purpose,status,created_at,closed_at,duration_min,tokens_total,metrics_complete,unread_to_user,counts,last_event}` |
| プロジェクトの中 | `projects[].tree`（木とメンバーの状態）、`timeline`（lifecycle は帯に畳む）、`counts` と各 Component の `counts` |
| 受け箱 | `inbox` |
| パフォーマンス | `performance` |
| 監査・unclear | `audit_proposals`、`unclear` |
