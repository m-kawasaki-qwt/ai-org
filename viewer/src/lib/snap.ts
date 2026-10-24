import snapshot from '../../data/snapshot.json';

export const snap: any = snapshot;

export const NA = '—（片づけ前）';

export function tok(n: number | null | undefined): string {
  if (n === null || n === undefined) return NA;
  if (n >= 1_000_000) return (n / 1_000_000).toFixed(2) + 'M';
  if (n >= 1_000) return Math.round(n / 1_000) + 'k';
  return String(n);
}

export function min(n: number | null | undefined): string {
  if (n === null || n === undefined) return NA;
  if (n >= 120) return (n / 60).toFixed(1) + ' 時間';
  return n.toFixed(0) + ' 分';
}

export function when(ts: string | null | undefined): string {
  if (!ts) return '—';
  return ts.slice(5, 16).replace('T', ' ');
}

export function flatten(c: any): any[] {
  return [c, ...c.children.flatMap(flatten)];
}

export function leaf(id: string): string {
  return id.split('/').slice(-1)[0];
}

export function cut(s: string | null | undefined, n = 80): string {
  if (!s) return '';
  return s.length > n ? s.slice(0, n) + '…' : s;
}

// 本文の無い done は一言に使わない
export const isEmptyDone = (e: any) => e.kind === 'done' && !e.body;

// 「いま／最後」の一言: lifecycle を除いた最後の message。閉じていれば user 宛ての最後の report を優先
export function headline(p: any): any | null {
  const msgs = p.timeline.filter((e: any) => e.group === 'message' && !isEmptyDone(e));
  if (p.status === 'closed') {
    const r = [...msgs].reverse().find((e: any) => e.to === 'user' && e.kind === 'report');
    if (r) return r;
  }
  return msgs.length ? msgs[msgs.length - 1] : null;
}

import { marked } from 'marked';

// 本文（Markdown）を整形して出す。本文の 1 行目のコメント（<!-- from → to kind ts -->）は外す
export function md(s: string | null | undefined): string {
  if (!s) return '';
  return marked.parse(s.replace(/^<!--.*?-->\s*/s, ''), { async: false }) as string;
}

// 期間を 1 行で: 「16 分・10-24 01:15」
export function span(p: any): string {
  return `${min(p.duration_min)}・${when(p.created_at)}`;
}

// プロジェクトの全メンバー（木を平らに）
export function allMembers(c: any): any[] {
  return [...c.members.map((m: any) => ({ ...m, comp: c })), ...c.children.flatMap(allMembers)];
}

// 立場ごとの色（時系列の図の帯）
export const POS_COLOR: Record<string, string> = {
  user: '#c084fc', pm: '#7aa2ff', coordinator: '#22d3ee', auditor: '#f472b6', leader: '#fbbf24', worker: '#4ade80', reviewer: '#fb923c',
};
// 種類ごとの色（時系列の図の点と線）
export function kindColor(k: string): string {
  if (['review_ng', 'rework', 'reassign', 'blocked', 'escalate'].includes(k)) return '#f87171';
  if (['review_ok', 'done'].includes(k)) return '#4ade80';
  if (k === 'report') return '#7aa2ff';
  if (k === 'review_request') return '#fb923c';
  if (['start', 'wrap_up'].includes(k)) return '#9ca3af';
  return '#6b7280';
}
