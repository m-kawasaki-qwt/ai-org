# ai-org

AI 組織（コンポーネント: プロジェクト・チーム）を実際に回す場所。プロジェクトは `projects/<slug>/` に置き、その記録（1 行報告・本文・セッション報告・チームの結果）がこの repo に残る。雛形と CLI（`orgctl`）は dev-tools の `org/` にある。

- 方針（何のための組織か）: [policy.md](policy.md)
- コミットの決まり: [CLAUDE.md](CLAUDE.md)
- このページは、初めて触る人が上から順にたどれば「立ち上げ → 状況を見る → 閉じる」まで行けるように並べてある。

## 0. 表記

dev-tools の場所は環境変数 `DEV_TOOLS_REPO_PATH` に入っている。このページのコマンドは、orgctl を次の形で呼ぶ（短く `orgctl` と書く）。

```
python3 $DEV_TOOLS_REPO_PATH/org/scripts/orgctl.py
```

- `<ai-org>` は、この repo の絶対パス（`$HOME/ghq/github.com.qwt/m-kawasaki-qwt/ai-org`）。
- 人（川崎さん）として orgctl を打つときは、先頭に `ORG_ROOT=<ai-org>/projects/<slug> ORG_MEMBER=user` を付ける（メンバーは起動時に自動で入る）。
- コマンドは 1 行ずつ、単独で打つ。`orca ...` の行も、そのまま単独で打つ。

## 1. はじめに人がやること（準備。1 回だけ）

川崎さん（人）の仕事。AI は代わりにやらない。

1. **dev-tools の `setup.sh` を打つ。** orgctl とスキル（`org-project-new` など）は dev-tools プラグインに入っていて、`setup.sh` がこの Mac に反映する。dev-tools を更新したあとも打ち直す。

   ```
   sh $DEV_TOOLS_REPO_PATH/setup.sh
   ```
2. **Google Chat の通知用 webhook を置く（任意）。** 見張り（`patrol`、3 章）が、川崎さん宛ての報告・判断の依頼と、止まったメンバーを Google Chat の通知専用スペースへ知らせる。送るのは dev-tools の道具 `gchat-notify` で、送り先は slug `ai-org`（dev-tools の `gchat-spaces.json`）。そのスペースの webhook の URL を、1 行だけ dev-tools の `.secrets/gchat/ai-org.url` に書く（git に入らない）。`gchat-notify list` で「URL あり」になれば届く。
   - 置かなくても動く。送らずに、プロジェクトの受け箱 `log/user-inbox.yaml` に残る（送ったときも同じ中身が残る）。
3. **Orca で `ai-org` の repo を開いておく。** メンバーは Orca のタブとして起こされる。

## 2. プロジェクトを立ち上げる

**この章と 5 章のコマンドを打つのは、根っこのセッション（Claude。`ORG_MEMBER=user` として動く）。** 川崎さんは「これをプロジェクトにしよう」と言うだけで、コマンドは打たない。

入口は `org-project-new` スキル（dev-tools プラグイン。中身は dev-tools の `claude/plugins/dev-tools/skills/org-project-new/SKILL.md`）。ai-org のセッションで「これをプロジェクトにしよう」と言うと、スキルが次を行う。**プロジェクトにするかは川崎さんが決める**（AI から持ちかけない）。

1. 目的・完了条件・範囲を `charter.md` の下書きにする。
2. `orgctl new project <ai-org>/projects/<slug> --root --charter <下書き>` で、根っこのプロジェクトを作る。
3. `orgctl assign <ai-org>/projects/<slug> pm --model opus` と `orgctl launch <ai-org>/projects/<slug>/pm` で PM（プロジェクトマネージャー）を用意する。出た `orca terminal create ...` を打ち、`orgctl attach <ai-org>/projects/<slug>/pm <handle>` でタブを台帳に結ぶ。続けて `ORG_ROOT=<ai-org>/projects/<slug> ORG_MEMBER=user orgctl event start --to <slug>/pm --body "charter を読んで始めてください"` で PM に始めさせる。
4. 見張りを裏で回す（3 章）。

**その後に起きること。** PM は charter を読み、規模（チームをいくつ・子プロジェクトにするか・作業者を何人）を自分で決める。チームは リーダー・作業者・レビュアー で組まれ、作業者が作り、レビュアーが目的と完了条件に照らして見て、通るまで往復する。リーダーが PM へ、PM が川崎さんへ `report` を上げる。川崎さんに来るのは、推奨付きの 2〜5 択の判断（`escalate`）と、完了の報告だけ。立ち上げたあと、川崎さんは待つだけでよい。

待つときは、次を打つ。9 分で戻るので、続けるならもう一度。PM の `report`・`escalate` が来たら読んで、判断を返す。

```
ORG_ROOT=<ai-org>/projects/<slug> ORG_MEMBER=user orgctl wait
```

## 3. いまの状況を見る

| 見たいもの | コマンド | 出るもの |
|---|---|---|
| 直下のメンバーと子が、進んでいるか・止まっているか・ループしているか | `orgctl watch <ai-org>/projects/<slug>` | メンバーごとの状態と最後の報告 |
| コンポーネントの木と、メンバーごとの最後の 1 行報告・状態 | `python3 tools/org_status.py projects/<slug>`（`--json` で JSON） | 状態は 動いている／終わった／未起動／片づけ済み |
| 時系列の見取り図 | `python3 tools/org_timeline.py projects/<slug>` | `projects/<slug>/timeline.html`（ブラウザで開く） |
| Orca の知らせの届き方 | `orgctl notify-stats --root <ai-org>/projects/<slug>` | 届いた割合・誤配・遅れ |

- `tools/` のコマンドは `<ai-org>` で打つ。`org_timeline.py` は「プロジェクトのディレクトリを渡すと、その中に `timeline.html` を書く」形。
- **見張り（`patrol`）。** プロジェクトを立ち上げたら、閉じるまで裏で回しておく（Bash の `run_in_background` など）。止まっている・ループしている状態が半日（`--stuck-min` で変えられる）続いたメンバーと、川崎さん宛ての報告・判断の依頼を、Google Chat へ知らせる。

  ```
  orgctl patrol <ai-org>/projects/<slug>
  ```
  - 試すときは `--once`（1 回だけ）と `--dry`（Google Chat へは送らず、受け箱 `log/user-inbox.yaml` にだけ残す）。

### ビューア（全プロジェクトを 1 か所で見る。`viewer/`）

Astro の静的サイト。`viewer/data/snapshot.json` だけを読む（記録は読まない）。一覧・プロジェクトの中・受け箱・パフォーマンス・監査と unclear の 5 画面。読むだけ。コマンドは 1 行ずつ単独で打つ。`<dev-tools>` は dev-tools の repo。

1. 記録を `snapshot.json` に書き出す（`<ai-org>` で）。`snapshot.json` は生成物で git に入れない（`.gitignore`）。無いとビューアは起動できないので、起動の前に必ず書き出す。

```
python3 <dev-tools>/org/scripts/orgctl.py export --projects projects --out viewer/data/snapshot.json
```

2. 依存を入れる（初回だけ）。

```
npm install --prefix viewer
```

3. 開発サーバーで見る（`http://localhost:4321`）。

```
npm run dev --prefix viewer
```

静的に書き出して見るなら、次の 2 行（出力は `viewer/dist/`。`preview` の URL は起動時に出る）。

```
npm run build --prefix viewer
```

```
npm run preview --prefix viewer
```

- 記録が増えたら 1 の `export` をやり直す。画面を見直すだけなら 3 から。
- `snapshot.json` の形は export とビューアの共通の約束。形を変えるときは両方を揃える。

## 4. 記録の在り処

根っこのプロジェクト `projects/<slug>/` の下に残る。後から `grep` で調べられる形が方針（[policy.md](policy.md) の 5）。

```
projects/<slug>/
├── charter.md                       目的・完了条件・範囲
├── component.json                   メンバー・子の台帳
├── log/
│   ├── events.log                   1 行報告（<時刻> <hash> <from> <kind> <to> ...）。全員分がここ 1 本
│   └── msgs/<hash>.md               1 行報告の本文（長い中身はここ。events.log の msg= が指す）
├── reports/sessions/<id>.yaml       メンバーごとのセッション報告（依頼・やったこと・判断・時間・トークン）
├── timeline.html                    org_timeline.py が作る見取り図
└── teams/<team>/                    チーム（子プロジェクトなら projects/<名前>/ に同じ形）
    ├── charter.md
    ├── thread.md                    作業者とレビュアーのやりとり（追記のみ）
    └── result.md                    チームの結果（成果物・完了条件ごとの結果）
```

- 例: `grep review_ng projects/<slug>/log/events.log`、`cat projects/<slug>/log/msgs/<hash>.md`。実物は `projects/p1-org-status/`・`projects/p2-orca-run-use/`。
- メンバーが読む自分宛ての報告は `orgctl inbox`、待つのは `orgctl wait`。

## 5. 閉じる

ユーザー（川崎さん）が「終わり」と言ったら、PM に `wrap_up`（終わりの指示）を出す。PM が配下を閉じて `done` を返したら、根っこを片づける。

```
ORG_ROOT=<ai-org>/projects/<slug> ORG_MEMBER=user orgctl event wrap_up --to <slug>/pm --body "終わりにしてください"
```

```
ORG_ROOT=<ai-org>/projects/<slug> ORG_MEMBER=user orgctl wait
```

```
orgctl teardown <ai-org>/projects/<slug> --summary "<コミットメッセージに添える 1 行>"
```

`teardown` は、セッション報告を `reports/sessions/` に残し、足場を消して、続きの手順を出す。出た行を **1 行ずつ単独で** 打つ。

- `orca terminal close ...`（タブを閉じる）
- `git add -A`・`git commit`・`git push origin HEAD`（記録を残す）

見張りも止める。

## 6. コミットの決まり

詳しくは [CLAUDE.md](CLAUDE.md)。要点だけ:

- **コミット・プッシュするのは、根っこの側（川崎さん、またはプロジェクトを立ち上げて `ORG_MEMBER=user` で動かしているセッション）だけ。** PM・リーダー・作業者・レビュアー・監査役は git を触らない。
- **コンポーネントを閉じたら、指示を待たずにコミットしてプッシュする。** `teardown` が出す `git add`・`git commit`・`git push` の行をそのまま打つ。子のコンポーネントは PM が閉じるので、その分は根っこの側が次に閉じるときにまとめて入る。
- ブランチは `main` に直接積む。ここに入るのは組織の記録と組織内の道具だけ（プロダクトの repo の成果物は、その repo の決まり＝PR に従う）。
- 残すもの: `charter.md`・`component.json`・`log/`・`reports/sessions/`・`thread.md`・チームの結果・`tools/`。残さないもの: 起動中メンバーの足場・`.secrets/`（`.gitignore`）。
