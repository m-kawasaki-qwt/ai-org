// いまの画面を撮り、変える所に枠と番号の札を描く（4390 は見るだけ。ページの中に重ねた div で描く）
import { chromium } from 'playwright';
const out = process.argv[2];
const shots = [
  { name: 'home-1800', url: '/', w: 1800, marks: [
    { sel: 'header.top .fresh', label: '② 古さは右上に小さく出るが、警告は無い', pos: 'below-right' },
    { sel: '.kps', label: '③ 全員待ち（p6・p8 の形）はここに出ない', pad: 4 },
    { pred: "[document.querySelectorAll('section.plist')[0]]", label: '② 写しが古くても「動いている」「—」のまま', pad: 2, pos: 'inside-right' },
    { pred: "[...document.querySelectorAll('section.plist')[1].querySelectorAll('.prow .c-note')]", label: '⑥ 「直し 2 回」か「—」だけ。重かったものが分からない', first: true },
  ]},
  { name: 'p9-1800', url: '/p/p9-org-watch/', w: 1800, marks: [
    { sel: 'h1.lead', label: '① 結論が PM の結果ではなく監査役の「4 件書いた」になる', pos: 'inside-right' },
    { sel: '#panel', label: '① 指摘 4 件の中身は出ず、ファイルの場所だけ', pos: 'below' },
  ]},
  { name: 'p8-1800', url: '/p/p8-viewer-rebuild/', w: 1800, marks: [
    { pred: "[...document.querySelectorAll('g.mk')].filter(g => /nudge/.test(g.getAttribute('aria-label')||''))", label: '⑤ 根っこの促し。凡例に無い「·」で、名前も英語のまま', pos: 'left' },
    { pred: "[...document.querySelectorAll('g.mk')].filter(g => /16:2[56].*リーダー/.test(g.getAttribute('aria-label')||''))", label: '③ ここから 5 分、リーダーも PM も待ちのまま。印が無い', pad: 10, group: true, pos: 'below-right' },
  ]},
  { name: 'p10-1800', url: '/p/p10-viewer-ideas/', w: 1800, marks: [
    { sel: 'h1.lead', label: '② 写しは 19:14。記録はその後も進んでいるのに「最後の動き 0 分前」', pos: 'inside-right' },
    { sel: '.tl', label: '② メンバー 6 人のうち、写しにある 2 人しか出ない', pos: 'inside-right' },
  ]},
  { name: 'rules-1800', url: '/rules/', w: 1800, marks: [
    { sel: 'main h1', label: '④ p9 の閉じるときの監査（指摘 4 件）が出ていない' },
    { sel: 'details.ugroup', all: true, label: '④ 迷った点はプロジェクトごと。似たもの・回数で束ねていない', first: true, group: true, pos: 'inside-right' },
  ]},
];
const b = await chromium.launch();
for (const s of shots) {
  const pg = await b.newPage({ viewport: { width: s.w, height: 1000 }, colorScheme: 'dark' });
  await pg.goto('http://localhost:4390' + s.url, { waitUntil: 'networkidle' });
  await pg.waitForTimeout(600);
  const res = await pg.evaluate((marks) => {
    // Astro の開発用ツールバーは画面の一部ではないので隠す
    document.querySelectorAll('astro-dev-toolbar').forEach((n) => n.remove());
    const log = [];
    const box = (r, label, pad, showLabel, pos) => {
      const d = document.createElement('div');
      Object.assign(d.style, { position: 'absolute', left: (r.left + scrollX - pad) + 'px', top: (r.top + scrollY - pad) + 'px', width: (r.width + pad * 2) + 'px', height: (r.height + pad * 2) + 'px', border: '3px solid #ff5ad1', borderRadius: '6px', zIndex: 99999, pointerEvents: 'none', boxSizing: 'border-box' });
      document.body.appendChild(d);
      if (!showLabel) return;
      const t = document.createElement('div');
      t.textContent = label;
      Object.assign(t.style, { position: 'absolute', left: (r.left + scrollX - pad) + 'px', top: Math.max(0, r.top + scrollY - pad - 26) + 'px', visibility: 'hidden', background: '#ff5ad1', color: '#111', font: '700 14px/22px -apple-system, "Hiragino Sans", sans-serif', padding: '1px 8px', borderRadius: '4px', zIndex: 100000, whiteSpace: 'nowrap', pointerEvents: 'none' });
      document.body.appendChild(t);
      // 見出しは指す所に重ねない: 枠の外の空いた所か、枠の中の右の空いた所に置く
      const w = t.offsetWidth, L = r.left + scrollX - pad, T = r.top + scrollY - pad, R = L + r.width + pad * 2, B = T + r.height + pad * 2;
      const at = { 'above': [L, T - 26], 'below': [L, B + 4], 'below-right': [R - w, B + 4], 'left': [L - w - 6, T], 'inside-right': [R - w - 8, T + 6] }[pos || 'above'];
      t.style.left = Math.max(0, at[0]) + 'px'; t.style.top = Math.max(0, at[1]) + 'px'; t.style.visibility = 'visible';
    };
    for (const m of marks) {
      let els = m.pred ? eval(m.pred) : (m.all ? [...document.querySelectorAll(m.sel)] : [document.querySelector(m.sel)].filter(Boolean));
      log.push(`${m.label}: ${els.length}`);
      if (!els.length) continue;
      if (m.group) {
        const rs = els.map((e) => e.getBoundingClientRect());
        const r = { left: Math.min(...rs.map((x) => x.left)), top: Math.min(...rs.map((x) => x.top)), width: Math.max(...rs.map((x) => x.right)) - Math.min(...rs.map((x) => x.left)), height: Math.max(...rs.map((x) => x.bottom)) - Math.min(...rs.map((x) => x.top)) };
        box(r, m.label, m.pad ?? 4, true, m.pos);
      } else els.forEach((e, i) => box(e.getBoundingClientRect(), m.label, m.pad ?? 4, !m.first || i === 0, m.pos));
    }
    return log;
  }, s.marks);
  console.log(s.name, res.join(' | '));
  await pg.screenshot({ path: `${out}/${s.name}.png`, fullPage: false });
  await pg.close();
}
await b.close();
