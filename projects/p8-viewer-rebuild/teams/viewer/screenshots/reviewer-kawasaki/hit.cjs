const { chromium } = require('/private/tmp/claude-501/-Users-maka343noshi-ghq-github-com-qwt-m-kawasaki-qwt-ai-org/d30b4812-44c4-49eb-97d9-81b19e1a5107/scratchpad/pw/node_modules/playwright');
(async () => {
  const b = await chromium.launch();
  for (const w of [900, 1800]) for (const id of ['p1-org-status','p2-orca-run-use','p3-org-visibility','p5-org-viewer','p6-org-build','p7-coordinator-role','p8-viewer-rebuild']) {
    const p = await b.newPage({ viewport: { width: w, height: 1000 }, colorScheme: 'dark' });
    await p.goto(`http://127.0.0.1:4392/p/${id}/`); await p.waitForTimeout(400);
    const r = await p.evaluate(() => {
      const ms = [...document.querySelectorAll('g.mk')];
      const lost = [];
      for (const g of ms) {
        const shape = g.querySelector('circle,path,polygon,rect,text') || g;
        const bb = g.getBoundingClientRect();
        let ok = false;
        for (const [fx, fy] of [[0.5,0.5],[0.3,0.5],[0.7,0.5],[0.5,0.3],[0.5,0.7]]) {
          const el = document.elementFromPoint(bb.x + bb.width*fx, bb.y + bb.height*fy);
          if (el && el.closest('g.mk') === g) { ok = true; break; }
        }
        if (!ok) lost.push(g.getAttribute('aria-label'));
      }
      return { n: ms.length, unclickable: lost.length, ex: lost.slice(0, 4) };
    });
    console.log(w, id, JSON.stringify(r));
    await p.close();
  }
  await b.close();
})();
