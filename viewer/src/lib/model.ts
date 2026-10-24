// snapshot.json から、画面に出すもの（判断待ち・止まっているかもしれないもの・往復・直し・起動の区間）を組む。
// 決め方は teams/viewer/design.md（画面 1・時系列の図）。ここは snapshot を引数に取る純粋な関数だけ。

export type Ev = {
  n: number; ts: string; id: string; from: string; to: string; kind: string;
  group: 'lifecycle' | 'message'; component: string | null; msg: string | null;
  summary: string; body: string | null; unread: boolean; subject?: string | null;
};
export type Run = { assigned_at: string | null; launched_at: string | null; closed_at: string | null };

const MIN = 60_000;
export const T_MANAGER = 5 * MIN; // 規則イ
export const T_REVIEW = 10 * MIN; // 規則ウ
export const T_UNLAUNCHED = 1 * MIN; // 規則ア（起動までの待ちは普段 18 秒以内）
export const GAP_MS = 5 * MIN; // 図で詰める空白

export const ms = (ts: string) => new Date(ts).getTime();

// ---- 言葉（design.md の B-09） ----

export const POS_LABEL: Record<string, string> = {
  user: '川崎さん', pm: 'PM', coordinator: 'コーディネーター', auditor: '監査役',
  leader: 'リーダー', worker: '作業者', reviewer: 'レビュアー',
};
const POS_ORDER = ['user', 'pm', 'coordinator', 'auditor', 'leader', 'worker', 'reviewer'];

export function posOf(mid: string): string {
  if (mid === 'user') return 'user';
  const name = mid.split('/').slice(-1)[0];
  return POS_ORDER.find((p) => name === p || name.startsWith(p + '-')) ?? name;
}

// 「作業者 ui」「コーディネーター org-build」。`-1` のような番号だけなら立場だけ
export function who(mid: string): string {
  if (mid === 'user') return '川崎さん';
  const name = mid.split('/').slice(-1)[0];
  const p = posOf(mid);
  const rest = name.startsWith(p + '-') ? name.slice(p.length + 1) : name === p ? '' : name;
  const label = POS_LABEL[p] ?? name;
  return rest && !/^\d+$/.test(rest) ? `${label} ${rest}` : label;
}

export const KIND: Record<string, { label: string; glyph: string; role: string }> = {
  start: { label: '依頼', glyph: '▶', role: 'start' },
  report: { label: '報告', glyph: '●', role: 'report' },
  review_request: { label: 'レビュー依頼', glyph: '?', role: 'request' },
  review_ok: { label: '承認', glyph: '✓', role: 'ok' },
  review_ng: { label: '差し戻し', glyph: '✕', role: 'danger' },
  rework: { label: 'やり直し', glyph: '↺', role: 'danger' },
  reassign: { label: '入れ替え', glyph: '⇄', role: 'danger' },
  escalate: { label: '判断の依頼', glyph: '▲', role: 'warn' },
  blocked: { label: '止まっている', glyph: '■', role: 'danger' },
  wrap_up: { label: '終わりの指示', glyph: '◎', role: 'muted' },
  done: { label: '終わった', glyph: '◆', role: 'muted' },
};
export const kindOf = (k: string) => KIND[k] ?? { label: k, glyph: '·', role: 'muted' };

// ---- 木 ----

export function flatten(c: any): any[] {
  return [c, ...c.children.flatMap(flatten)];
}

export function allMembers(p: any): any[] {
  return flatten(p.tree).flatMap((c: any) => c.members.map((m: any) => ({ ...m, comp: c })));
}

// チームの短い名前: short_title → component.json の title（目的の頭を切ったものでなければ）→ id の末尾
export function compName(c: any): string {
  if (c.short_title) return c.short_title;
  if (c.kind === 'project' && c.title) return c.title;
  return c.id.split('/').slice(-1)[0];
}

// ---- 起動の区間 ----

// ライフサイクルの行の対象メンバー（subject が無い古い snapshot は summary の頭・teardown は to）
export function subjectOf(e: Ev): string | null {
  if (e.subject !== undefined && e.subject !== null) return e.subject;
  if (e.kind === 'teardown') return e.to !== '-' ? e.to : null;
  if (e.kind === 'assign' || e.kind === 'launch') return e.summary.split(' ')[0] || null;
  return null;
}

export function runsFromTimeline(tl: Ev[]): Map<string, Run[]> {
  const out = new Map<string, Run[]>();
  for (const e of tl) {
    if (!['assign', 'launch', 'teardown'].includes(e.kind)) continue;
    const s = subjectOf(e);
    if (!s) continue;
    const rs = out.get(s) ?? [];
    out.set(s, rs);
    const last = rs[rs.length - 1];
    if (e.kind === 'assign') rs.push({ assigned_at: e.ts, launched_at: null, closed_at: null });
    else if (e.kind === 'launch') {
      if (last && !last.launched_at && !last.closed_at) last.launched_at = e.ts;
      else rs.push({ assigned_at: null, launched_at: e.ts, closed_at: null });
    } else if (last && !last.closed_at) last.closed_at = e.ts;
  }
  return out;
}

export function runsOf(p: any): Map<string, Run[]> {
  const fromTl = runsFromTimeline(p.timeline);
  for (const m of allMembers(p)) if (Array.isArray(m.runs)) fromTl.set(m.id, m.runs);
  return fromTl;
}

function runningAt(runs: Run[] | undefined, t: number): boolean {
  return (runs ?? []).some((r) => r.launched_at && ms(r.launched_at) <= t && (!r.closed_at || ms(r.closed_at) > t));
}

function nextLaunch(runs: Run[] | undefined, t: number): number | null {
  const ls = (runs ?? []).map((r) => (r.launched_at ? ms(r.launched_at) : null)).filter((x): x is number => x !== null && x > t);
  return ls.length ? Math.min(...ls) : null;
}

// 図の終わり（閉じていれば閉じた時刻、動いていれば書き出し時刻）
export function endOf(p: any, now: number): number {
  return p.closed_at ? ms(p.closed_at) : now;
}

// ---- 止まっているかもしれないもの（規則ア〜エ） ----

export type Stall = {
  rule: 'ア' | 'イ' | 'ウ' | 'エ'; member: string; ev: Ev;
  from: number; to: number; ongoing: boolean; // 図に塗る区間（受けた・届いた時刻から、消えるまで）
};

export function stallText(s: Stall): string {
  const m = Math.round((s.to - s.from) / MIN);
  const w = who(s.member);
  if (s.rule === 'ア') return `${w} が未起動のまま、${kindOf(s.ev.kind).label}が届いている`;
  if (s.rule === 'イ') return `${w} が依頼を受けて ${m} 分、動きが無い`;
  if (s.rule === 'ウ') return `レビュー依頼に ${m} 分、${w} から返事が無い`;
  return `${w}への${kindOf(s.ev.kind).label}に返事が無い`;
}

export function stallNote(s: Stall): string {
  const m = Math.max(1, Math.round((s.to - s.from) / MIN));
  return { ア: `未起動で待ち ${m} 分`, イ: `動き無し ${m} 分`, ウ: `返事無し ${m} 分`, エ: `返事待ち ${m} 分` }[s.rule];
}

export function stalls(p: any, now: number): Stall[] {
  const tl: Ev[] = p.timeline;
  const runs = runsOf(p);
  const end = endOf(p, now);
  const out: Stall[] = [];
  tl.forEach((e, i) => {
    if (e.group !== 'message' || e.to === '-' || e.to === 'user') return;
    const r = e.to;
    const t0 = ms(e.ts);
    const next = tl.slice(i + 1).find((x) => x.from === r);
    const t1 = next ? ms(next.ts) : null;
    const replied = t1 ?? end;
    const running = runningAt(runs.get(r), t0);
    if (!running) {
      // ア: 起動していない相手に届いた。起動するまで
      if (e.kind === 'done' || e.kind === 'wrap_up') return; // 片づけの手続きは待ちではない
      const l = nextLaunch(runs.get(r), t0);
      const until = Math.min(l ?? end, end);
      if (until - t0 >= T_UNLAUNCHED) out.push({ rule: 'ア', member: r, ev: e, from: t0, to: until, ongoing: l === null && !p.closed_at });
      return;
    }
    if (e.kind === 'start' && ['pm', 'leader'].includes(posOf(r)) && replied - t0 >= T_MANAGER)
      out.push({ rule: 'イ', member: r, ev: e, from: t0, to: replied, ongoing: t1 === null && !p.closed_at });
    else if (e.kind === 'review_request' && replied - t0 >= T_REVIEW)
      out.push({ rule: 'ウ', member: r, ev: e, from: t0, to: replied, ongoing: t1 === null && !p.closed_at });
    else if (['escalate', 'blocked'].includes(e.kind) && replied > t0)
      out.push({ rule: 'エ', member: r, ev: e, from: t0, to: replied, ongoing: t1 === null && !p.closed_at });
  });
  return out;
}

// いま止まっているかもしれないもの（動いているプロジェクトだけ）
export function openStalls(p: any, now: number): Stall[] {
  if (p.status !== 'open') return [];
  return stalls(p, now).filter((s) => s.ongoing);
}

// ---- 判断待ち ----

export function decisions(p: any): Ev[] {
  const tl: Ev[] = p.timeline;
  return tl.filter((e, i) =>
    e.group === 'message' && e.to === 'user' && ['report', 'escalate', 'blocked'].includes(e.kind) &&
    !tl.slice(i + 1).some((x) => x.from === 'user' && x.to === e.from));
}

// ---- 往復の括り ----

const RT_KINDS = new Set(['start', 'report', 'escalate', 'blocked']);
export type RoundTrip = { a: string; b: string; events: Ev[] };

export function roundTrips(p: any): RoundTrip[] {
  const ms_ = (p.timeline as Ev[]).filter((e) => e.group === 'message' && !['wrap_up', 'done'].includes(e.kind));
  const out: RoundTrip[] = [];
  let i = 0;
  while (i < ms_.length) {
    const a = ms_[i];
    let j = i;
    const pair = (e: Ev) => [e.from, e.to].sort().join('|');
    if (RT_KINDS.has(a.kind)) {
      while (j + 1 < ms_.length && RT_KINDS.has(ms_[j + 1].kind) && pair(ms_[j + 1]) === pair(a) && ms_[j + 1].from !== ms_[j].from) j++;
    }
    if (j - i + 1 >= 3) out.push({ a: a.from, b: a.to, events: ms_.slice(i, j + 1) });
    i = j + 1;
  }
  return out;
}

// ---- 差し戻しの輪 ----

export type Loop = { member: string; from: number; to: number; nth: number[] };

export function reviewLoops(p: any, now: number): Loop[] {
  const tl: Ev[] = p.timeline;
  const end = endOf(p, now);
  const loops: Loop[] = [];
  const count = new Map<string, number>();
  tl.forEach((e, i) => {
    if (!['review_ng', 'rework'].includes(e.kind) || e.to === '-') return;
    const w = e.to;
    const t0 = ms(e.ts);
    // その作業者が出し直したあとの、同じコンポーネントの承認まで
    const rr = tl.slice(i + 1).findIndex((x) => x.from === w && x.kind === 'review_request');
    const ok = rr < 0 ? undefined : tl.slice(i + 1 + rr).find((x) => x.kind === 'review_ok' && x.component === e.component);
    const t1 = ok ? ms(ok.ts) : end;
    const n = (count.get(w) ?? 0) + 1;
    count.set(w, n);
    const last = loops.find((l) => l.member === w && l.to >= t0);
    if (last) {
      last.to = Math.max(last.to, t1);
      last.nth.push(n);
    } else loops.push({ member: w, from: t0, to: t1, nth: [n] });
  });
  return loops;
}

// ---- 数字（閉じたプロジェクトの平均と比べる） ----

export function averages(projects: any[], except?: string) {
  const cl = projects.filter((p) => p.status === 'closed' && p.id !== except);
  const avg = (f: (p: any) => number | null) => {
    const xs = cl.map(f).filter((x): x is number => typeof x === 'number');
    return xs.length ? xs.reduce((a, b) => a + b, 0) / xs.length : null;
  };
  return {
    n: cl.length,
    duration: avg((p) => p.duration_min),
    tokens: avg((p) => p.tokens_total),
    remakes: avg((p) => p.counts.remakes),
  };
}

// 川崎さん宛ての最後の報告（結果）
export function lastReportToUser(p: any): Ev | null {
  const r = [...(p.timeline as Ev[])].reverse().find((e) => e.to === 'user' && e.kind === 'report');
  return r ?? null;
}

export function lastMessage(p: any): Ev | null {
  const r = [...(p.timeline as Ev[])].reverse().find((e) => e.group === 'message');
  return r ?? null;
}

// 報告の本文から、結果を言う 1 文（全角 44 字まで）を取り出す。
// 「## Summary」の最初の箇条、無ければ最初の「##」より前の段落。どちらも無ければ空
export function gist(body: string | null | undefined, max = 44): string {
  if (!body) return '';
  const lines = body.replace(/^<!--.*?-->\s*/s, '').split('\n');
  let para = '';
  const si = lines.findIndex((l) => /^#{2,}\s*Summary/i.test(l));
  if (si >= 0) para = lines.slice(si + 1).find((l) => /^\s*[-*]\s+/.test(l)) ?? '';
  if (!para) {
    for (const l of lines) {
      if (/^#{2,}\s/.test(l) || /^```/.test(l)) break;
      if (/^#\s/.test(l) || !l.trim()) { if (para) break; continue; }
      if (/^\s*([-*]|\d+\.)\s+/.test(l)) { if (!para) para = l.replace(/^\s*\d+\.\s+/, ''); break; } // 箇条は最初の 1 つだけ
      para += l.trim();
    }
  }
  const text = para.replace(/^\s*[-*]\s+/, '').replace(/\[([^\]]*)\]\([^)]*\)/g, '$1').replace(/[`*_]/g, '').trim();
  if (!text) return '';
  const sentences = text.match(/[^。]+。?/g) ?? [text];
  let out = '';
  for (const t of sentences) {
    if ((out + t).length > max) break;
    out += t;
  }
  if (!out) out = sentences[0].slice(0, max - 1) + '…';
  return out;
}
