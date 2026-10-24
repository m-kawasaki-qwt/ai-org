import snapshot from '../../data/snapshot.json';
import { marked } from 'marked';

export const snap: any = snapshot;
export const NOW = new Date(snap.generated_at).getTime();

export function tok(n: number | null | undefined): string {
  if (n === null || n === undefined) return '—';
  if (n >= 1_000_000) return (n / 1_000_000).toFixed(1) + 'M';
  if (n >= 1_000) return Math.round(n / 1_000) + 'k';
  return String(n);
}

export function min(n: number | null | undefined): string {
  if (n === null || n === undefined) return '—';
  if (n >= 120) return (n / 60).toFixed(1) + ' 時間';
  return Math.round(n) + ' 分';
}

// 10-24 13:23（日時は全画面でこの書式）
export function when(ts: string | null | undefined): string {
  if (!ts) return '—';
  return ts.slice(5, 16).replace('T', ' ');
}

export const day = (ts: string) => ts.slice(5, 10);
export const hm = (ts: string) => ts.slice(11, 16);
export const hms = (ts: string) => ts.slice(11, 19);

// 本文（Markdown）を整形して出す。本文の 1 行目のコメント（<!-- from → to kind ts -->）は外す
export function md(s: string | null | undefined): string {
  if (!s) return '';
  const html = marked.parse(s.replace(/^<!--.*?-->\s*/s, ''), { async: false }) as string;
  // 表の短いセル（名前・状態・数値）は折り返さない。文章のセルは折り返す
  return html.replace(/<(td|th)([^>]*)>([^<]{1,14})<\/\1>/g, (_m, t, a, x) => `<${t}${a} class="nw">${x}</${t}>`);
}

export function mdInline(s: string | null | undefined): string {
  if (!s) return '';
  return marked.parseInline(s, { async: false }) as string;
}
