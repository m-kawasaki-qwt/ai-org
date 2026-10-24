// 時系列の図（design.md の「時系列の図」）。データはページの <script id="tl-data"> から読み、幅に合わせて SVG を描く。
// 横: 時刻（5 分以上の空白は 96px に詰める）。縦: 入れ子の帯（川崎さん → プロジェクト → チーム → メンバー）。

type Run = { a: number | null; l: number | null; c: number | null };
type Row = {
  key: string; type: 'user' | 'head' | 'member'; label: string; sub?: string; mid?: string; depth: number;
  tpl?: string; runs?: Run[]; ancestors: string[]; collapsible?: boolean; span?: [number, number]; count?: number;
};
type Ev = { t: number; from: string; tos: string[]; glyph: string; role: string; title: string; tpl: string; evs: string[] };
type Data = {
  start: number; end: number; times: number[]; msgTimes: number[]; rows: Row[]; events: Ev[];
  stalls: { member: string; from: number; to: number; note: string }[];
  loops: { member: string; from: number; to: number; label: string }[];
  rts: { a: string; b: string; from: number; to: number; n: number }[];
  memberOf: Record<string, string>; // メンバー id → 行の key
};

const NS = 'http://www.w3.org/2000/svg';
const GAP_MS = 5 * 60_000;
const GAP_W = 96;
const ROW_H = 30;
const RT_PAD = 18;
const LOOP_PAD = 14;
const AXIS_H = 40;
const PAD_L = 16;
const PAD_R = 40;

function el<K extends keyof SVGElementTagNameMap>(tag: K, attrs: Record<string, string | number>, parent?: Element) {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, String(v));
  parent?.appendChild(e);
  return e;
}

const pad2 = (n: number) => String(n).padStart(2, '0');
const hm = (t: number) => { const d = new Date(t); return `${pad2(d.getHours())}:${pad2(d.getMinutes())}`; };
const md = (t: number) => { const d = new Date(t); return `${pad2(d.getMonth() + 1)}-${pad2(d.getDate())}`; };

// 横の目盛り: 区切りの時刻ごとに、空白は GAP_W、ほかは時間に比例。
// 同じ帯の印どうしは MARK_GAP 以上離す（重なって押せない印を作らない）。収まらなければ図の中だけ横に流す
const MARK_GAP = 24;
function scale(d: Data, avail: number, lanesAt: Map<number, string[]>) {
  const ts = d.times;
  const layout = (k: number) => {
    const xs: number[] = [];
    const last = new Map<string, number>();
    ts.forEach((t, i) => {
      let x = PAD_L;
      if (i > 0) {
        const dt = t - ts[i - 1];
        x = xs[i - 1] + (dt >= GAP_MS ? GAP_W : dt > 0 ? Math.max(1, dt * k) : 0);
      }
      for (const l of lanesAt.get(t) ?? []) if (last.has(l)) x = Math.max(x, last.get(l)! + MARK_GAP);
      const here = lanesAt.get(t) ?? [];
      for (const l of here) last.set(l, x + (here.filter((v) => v === l).length - 1) * MARK_GAP);
      xs.push(x);
    });
    return xs;
  };
  const room = avail - PAD_R;
  let lo = 0, hi = 1;
  while (layout(hi)[ts.length - 1] < room && hi < 1e3) hi *= 2;
  for (let i = 0; i < 40; i++) { const m = (lo + hi) / 2; if (layout(m)[ts.length - 1] > room) hi = m; else lo = m; }
  const xs = layout(lo);
  const x = (t: number) => {
    if (t <= ts[0]) return xs[0];
    if (t >= ts[ts.length - 1]) return xs[xs.length - 1];
    let a = 0, b = ts.length - 1;
    while (b - a > 1) { const m = (a + b) >> 1; if (ts[m] <= t) a = m; else b = m; }
    const dt = ts[a + 1] - ts[a];
    return dt ? xs[a] + ((t - ts[a]) / dt) * (xs[a + 1] - xs[a]) : xs[a];
  };
  const gaps = ts.slice(0, -1).map((t, i) => ({ t0: t, t1: ts[i + 1], dt: ts[i + 1] - t, x0: xs[i], x1: xs[i + 1] })).filter((g) => g.dt >= GAP_MS);
  return { x, width: xs[xs.length - 1] + PAD_R, gaps };
}

export function mount(root: HTMLElement) {
  const d: Data = JSON.parse(document.getElementById('tl-data')!.textContent!);
  const labels = root.querySelector('.tl-labels') as HTMLElement;
  const plot = root.querySelector('.tl-plot') as HTMLElement;
  const collapsed = new Set<string>();
  let selected: string | null = null;

  function render() {
    const vis = d.rows.filter((r) => !r.ancestors.some((a) => collapsed.has(a)));
    const rowOf = new Map(d.rows.map((r) => [r.key, r]));
    // メンバー id → 描く行（畳んだチームの中なら、その括りの見出しの行）
    const laneKey = (mid: string): string | null => {
      const k = d.memberOf[mid];
      if (!k) return null;
      const r = rowOf.get(k)!;
      const c = r.ancestors.find((a) => collapsed.has(a));
      return c ?? k;
    };
    const hosts = new Set<string>();
    for (const rt of d.rts) {
      const ka = laneKey(rt.a), kb = laneKey(rt.b);
      const ia = vis.findIndex((r) => r.key === ka), ib = vis.findIndex((r) => r.key === kb);
      if (ia >= 0 && ib >= 0) hosts.add(vis[Math.min(ia, ib)].key);
    }
    const loopRows = new Set(d.loops.map((l) => laneKey(l.member)).filter((k): k is string => !!k && !collapsed.has(k) && vis.some((r) => r.key === k && r.type === 'member')));
    const top = new Map<string, number>();
    const mid = new Map<string, number>();
    const bottom = new Map<string, number>();
    const pads = new Map<string, [number, number]>();
    let y = AXIS_H;
    for (const r of vis) {
      // 往復の括りを載せる行は上に、起動が 2 回以上ある行は下（「2 回目」の文字）に余白
      const pt = (hosts.has(r.key) ? RT_PAD : 0) + (loopRows.has(r.key) ? LOOP_PAD : 0);
      const pb = (r.runs?.length ?? 0) > 1 ? 14 : 0;
      pads.set(r.key, [pt, pb]);
      top.set(r.key, y);
      mid.set(r.key, y + pt + ROW_H / 2);
      y += ROW_H + pt + pb;
      bottom.set(r.key, y);
    }
    const H = y + 8;
    const yOf = (m: string) => { const k = laneKey(m); return k !== null ? mid.get(k) : undefined; };

    // 帯の名前（HTML。押せるものはボタン）
    const focusKey = (document.activeElement as HTMLElement | null)?.dataset?.key;
    labels.replaceChildren();
    labels.style.height = H + 'px';
    const axisLab = document.createElement('div');
    axisLab.className = 'lab lab-axis';
    axisLab.style.height = AXIS_H + 'px';
    axisLab.textContent = '時刻 →';
    labels.appendChild(axisLab);
    for (const r of vis) {
      const h = bottom.get(r.key)! - top.get(r.key)!;
      const [pt, pb] = pads.get(r.key)!;
      let n: HTMLElement;
      if (r.type === 'member') {
        n = document.createElement('button');
        n.className = 'lab lab-m';
        n.dataset.panel = r.tpl!;
        n.innerHTML = `<span class="u"></span>`;
        (n.firstChild as HTMLElement).textContent = r.label;
        n.title = `${r.label}の中身（起動の区間・時間・迷った点）を開く`;
      } else if (r.type === 'head' && r.collapsible) {
        n = document.createElement('button');
        n.className = 'lab lab-h';
        const isC = collapsed.has(r.key);
        n.setAttribute('aria-expanded', String(!isC));
        n.innerHTML = `<span class="tw" aria-hidden="true">${isC ? '▶' : '▼'}</span><span class="nm"></span><span class="sub"></span>`;
        n.querySelector('.nm')!.textContent = r.label;
        n.querySelector('.sub')!.textContent = isC ? `${r.count} 人を畳んだ` : '';
        n.title = `${r.label}（${r.sub ?? ''}）を${isC ? '開く' : '畳む'}`;
        n.addEventListener('click', () => { collapsed.has(r.key) ? collapsed.delete(r.key) : collapsed.add(r.key); render(); });
      } else {
        n = document.createElement('div');
        n.className = r.type === 'head' ? 'lab lab-h static' : 'lab lab-user';
        n.innerHTML = `<span class="nm"></span>`;
        n.firstChild!.textContent = r.label;
      }
      n.dataset.key = r.key;
      n.style.height = h + 'px';
      n.style.paddingTop = pt + 'px';
      n.style.paddingBottom = pb + 'px';
      n.style.paddingLeft = 8 + r.depth * 14 + 'px';
      if (r.depth > 0) n.style.setProperty('--depth', String(r.depth));
      labels.appendChild(n);
    }
    if (focusKey) labels.querySelector<HTMLElement>(`[data-key="${CSS.escape(focusKey)}"]`)?.focus();

    // 図
    const avail = Math.max(200, plot.clientWidth);
    const lanesAt = new Map<number, string[]>();
    for (const e of d.events) {
      const k = laneKey(e.from);
      if (k) lanesAt.set(e.t, [...(lanesAt.get(e.t) ?? []), k]);
    }
    const sc = scale(d, avail, lanesAt);
    const W = Math.max(avail, sc.width);
    const x = sc.x;
    const svg = el('svg', { width: W, height: H, viewBox: `0 0 ${W} ${H}`, role: 'img', 'aria-label': '時系列の図' });
    svg.classList.toggle('has-sel', !!selected);
    const defs = el('defs', {}, svg);
    const hatch = el('pattern', { id: 'hatch', width: 6, height: 6, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(45)' }, defs);
    el('rect', { width: 6, height: 6, class: 'hatch-bg' }, hatch);
    el('line', { x1: 0, y1: 0, x2: 0, y2: 6, class: 'hatch-line' }, hatch);
    const gapP = el('pattern', { id: 'gapp', width: 8, height: 8, patternUnits: 'userSpaceOnUse', patternTransform: 'rotate(-45)' }, defs);
    el('line', { x1: 0, y1: 0, x2: 0, y2: 8, class: 'gap-line' }, gapP);

    // 詰めた空白
    for (const g of sc.gaps) {
      el('rect', { x: g.x0 + 4, y: AXIS_H - 6, width: g.x1 - g.x0 - 8, height: H - AXIS_H + 6, fill: 'url(#gapp)', class: 'gap' }, svg);
      const tx = el('text', { x: (g.x0 + g.x1) / 2, y: 26, 'text-anchor': 'middle', class: 'ax gapt' }, svg);
      tx.textContent = `⋯ ${Math.round(g.dt / 60000)} 分 ⋯`;
    }
    // 目盛り
    let lastX = -1e9, lastDay = '';
    const gapStarts = new Set(sc.gaps.map((g) => g.t1));
    for (const t of d.msgTimes) {
      const xx = x(t);
      if (xx - lastX < 64 && !gapStarts.has(t)) continue;
      if (sc.gaps.some((g) => xx > g.x0 - 30 && xx < g.x1 - 2 && t !== g.t1)) continue;
      const dd = md(t);
      if (dd !== lastDay) { const t1 = el('text', { x: xx, y: 13, 'text-anchor': 'middle', class: 'ax' }, svg); t1.textContent = dd; }
      const t2 = el('text', { x: xx, y: 27, 'text-anchor': 'middle', class: 'ax' }, svg);
      t2.textContent = hm(t);
      el('line', { x1: xx, x2: xx, y1: AXIS_H - 6, y2: AXIS_H, class: 'tick' }, svg);
      lastX = xx; lastDay = dd;
    }
    el('line', { x1: 0, x2: W, y1: AXIS_H, y2: AXIS_H, class: 'axis' }, svg);

    // 行（括り・区切り・生きている区間）
    for (const r of vis) {
      const t0 = top.get(r.key)!, cy = mid.get(r.key)!, bot = bottom.get(r.key)!;
      if (r.type === 'head') {
        el('rect', { x: 0, y: t0, width: W, height: bot - t0, class: 'row-head' }, svg);
        if (r.span) {
          if (collapsed.has(r.key)) el('rect', { x: x(r.span[0]), y: cy - 4, width: Math.max(2, x(r.span[1]) - x(r.span[0])), height: 8, rx: 2, class: 'run' }, svg);
          else el('rect', { x: x(r.span[0]), y: cy - 1, width: Math.max(2, x(r.span[1]) - x(r.span[0])), height: 2, class: 'span' }, svg);
        }
      }
      el('line', { x1: 0, x2: W, y1: bot, y2: bot, class: 'sep' }, svg);
      if (r.type === 'user') el('rect', { x: x(d.start), y: cy - 2, width: x(d.end) - x(d.start), height: 4, rx: 2, class: 'run user' }, svg);
      (r.runs ?? []).forEach((run, i) => {
        const a = run.a ?? run.l, l = run.l, c = run.c ?? d.end;
        if (a !== null && (l === null || l > a)) el('rect', { x: x(a), y: cy - 5, width: Math.max(2, x(l ?? c) - x(a)), height: 10, rx: 2, class: 'unlaunched' }, svg);
        if (l !== null) el('rect', { x: x(l), y: cy - 4, width: Math.max(3, x(c) - x(l)), height: 8, rx: 2, class: 'run' }, svg);
        if (i > 0 && l !== null) {
          el('line', { x1: x(l), x2: x(l), y1: cy - 8, y2: cy + 10, class: 'run-cut' }, svg);
          const t = el('text', { x: x(l) + 3, y: cy + 19, class: 'note-s run-n' }, svg);
          t.textContent = `${i + 1} 回目の起動`;
        }
      });
    }
    // 括りの枠（開いたチーム）
    for (const r of vis) {
      if (r.type !== 'head' || !r.collapsible || collapsed.has(r.key)) continue;
      const inner = vis.filter((v) => v.ancestors.includes(r.key));
      const last = inner[inner.length - 1] ?? r;
      el('rect', { x: 1, y: top.get(r.key)!, width: W - 2, height: bottom.get(last.key)! - top.get(r.key)!, rx: 4, class: 'box' }, svg);
    }
    // 直しの輪
    for (const l of d.loops) {
      const k = laneKey(l.member);
      if (!k || k !== d.memberOf[l.member]) continue;
      const cy = mid.get(k)!;
      const yTop = cy - ROW_H / 2 - LOOP_PAD + 2;
      el('rect', { x: x(l.from), y: yTop, width: Math.max(4, x(l.to) - x(l.from)), height: cy + ROW_H / 2 - 2 - yTop, rx: 3, class: 'loop' }, svg);
      const t = el('text', { x: x(l.from) + 4, y: yTop + 11, class: 'note-s loop-t' }, svg);
      t.textContent = l.label;
    }
    // 待ち・止まっていた所
    const notes: SVGElement[] = [];
    for (const s of d.stalls) {
      const cy = yOf(s.member);
      if (cy === undefined) continue;
      const x0 = x(s.from), x1 = x(s.to);
      el('rect', { x: x0, y: cy - 9, width: Math.max(4, x1 - x0), height: 18, fill: 'url(#hatch)', class: 'stall' }, svg);
      const g = el('g', { class: 'note' });
      const txt = el('text', { x: 0, y: cy + 4, class: 'note-t' }, g);
      txt.textContent = s.note;
      notes.push(g);
      (g as any)._pos = { x0, x1 };
    }
    // やりとりの線
    const lines = el('g', { class: 'lines' }, svg);
    const marks = el('g', { class: 'marks' }, svg);
    const markX = new Map<string, number>();
    for (const e of d.events) {
      const ys = yOf(e.from);
      if (ys === undefined) continue;
      const lk = laneKey(e.from)!;
      const xx = Math.max(x(e.t), (markX.get(lk) ?? -1e9) + MARK_GAP);
      markX.set(lk, xx);
      const evs = ' ' + e.evs.join(' ') + ' ';
      for (const to of e.tos) {
        const yr = yOf(to);
        if (yr === undefined || Math.abs(yr - ys) <= 2) continue;
        const dir = yr > ys ? 1 : -1;
        const g = el('g', { class: `ln r-${e.role}`, 'data-id': e.tpl, 'data-evs': evs }, lines);
        el('line', { x1: xx, x2: xx, y1: ys, y2: yr - dir * 7 }, g);
        el('path', { d: `M${xx - 4},${yr - dir * 8} L${xx + 4},${yr - dir * 8} L${xx},${yr - dir * 1} Z` }, g);
      }
      const g = el('g', { class: `mk r-${e.role}`, role: 'button', tabindex: 0, 'data-panel': e.tpl, 'data-id': e.tpl, 'data-evs': evs, 'aria-label': e.title }, marks);
      el('title', {}, g).textContent = e.title;
      el('circle', { cx: xx, cy: ys, r: 13, class: 'hit' }, g);
      el('circle', { cx: xx, cy: ys, r: 13, class: 'ring' }, g);
      el('circle', { cx: xx, cy: ys, r: 8.5, class: 'dot' }, g);
      const gl = el('text', { x: xx, y: ys + 4, 'text-anchor': 'middle', class: 'gl' }, g);
      gl.textContent = e.glyph;
      if (e.tos.length > 1) { const n = el('text', { x: xx + 9, y: ys - 9, class: 'note-s multi' }, g); n.textContent = `×${e.tos.length}`; }
    }
    // 往復の括り
    for (const rt of d.rts) {
      const ka = laneKey(rt.a), kb = laneKey(rt.b);
      const host = vis.find((r) => r.key === ka || r.key === kb);
      if (!host || ka === kb) continue;
      const yy = top.get(host.key)! + 8;
      const x0 = x(rt.from) - 8, x1 = x(rt.to) + 8;
      el('path', { d: `M${x0},${yy + 6} L${x0},${yy} L${x1},${yy} L${x1},${yy + 6}`, class: 'rt' }, svg);
      const t = el('text', { x: x1 + 6, y: yy + 5, class: 'rt-t' }, svg);
      t.textContent = `往復 ${rt.n}`;
    }
    // 注記の札は最後に（線と印の上に読めるように）
    plot.replaceChildren(svg);
    for (const g of notes) {
      svg.appendChild(g);
      const t = g.querySelector('text') as SVGTextElement;
      const w = t.getComputedTextLength();
      const { x0, x1 } = (g as any)._pos;
      const cx = x1 - x0 >= w + 12 ? (x0 + x1) / 2 - w / 2 : x0 + 4;
      t.setAttribute('x', String(cx));
      const bb = t.getBBox();
      const bg = el('rect', { x: bb.x - 5, y: bb.y - 2, width: bb.width + 10, height: bb.height + 4, rx: 4, class: 'note-bg' });
      g.insertBefore(bg, t);
    }
    applySel();
  }

  function applySel() {
    const svg = plot.querySelector('svg');
    if (!svg) return;
    svg.classList.toggle('has-sel', !!selected);
    svg.querySelectorAll('.sel').forEach((n) => n.classList.remove('sel'));
    if (selected) svg.querySelectorAll(`[data-id="${CSS.escape(selected)}"], [data-evs~="${CSS.escape(selected)}"]`).forEach((n) => n.classList.add('sel'));
  }

  document.addEventListener('panel:select', (e: any) => {
    const id = e.detail.id as string | null;
    selected = id && (id.startsWith('tpl-e-') || id.startsWith('tpl-g-')) ? id : null;
    applySel();
  });
  let raf = 0;
  new ResizeObserver(() => { cancelAnimationFrame(raf); raf = requestAnimationFrame(render); }).observe(plot);
  render();
}

const root = document.querySelector<HTMLElement>('.tl');
if (root) mount(root);
