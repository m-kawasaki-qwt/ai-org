// 本文のパネル: [data-panel="tpl-…"] を押すと、その <template> の中身をパネルに出す。
// 1400px 以上は横に張り付いたパネル、それ未満は押した所と反対の側から出る引き出し（design.md の B-07）。
const panel = document.getElementById('panel');

if (panel) {
  const title = panel.querySelector('.p-title') as HTMLElement;
  const content = panel.querySelector('.p-content') as HTMLElement;
  const nav = panel.querySelector('.p-nav') as HTMLElement;
  const prev = panel.querySelector('.p-prev') as HTMLButtonElement;
  const next = panel.querySelector('.p-next') as HTMLButtonElement;
  const closeBtn = panel.querySelector('.p-close') as HTMLButtonElement;
  const emptyHtml = title.innerHTML;
  const wide = () => matchMedia('(min-width: 1400px)').matches;
  let returnTo: HTMLElement | null = null;

  const trigger = (id: string) => document.querySelector<HTMLElement>(`[data-panel="${id}"]`);

  function open(id: string, from: HTMLElement | null, focus = true, setHash = true) {
    const t = document.getElementById(id) as HTMLTemplateElement | null;
    if (!t) return;
    const box = document.createElement('div');
    box.innerHTML = t.innerHTML;
    title.innerHTML = box.querySelector('.t-title')?.innerHTML ?? '';
    content.innerHTML = box.querySelector('.t-body')?.innerHTML ?? '';
    panel!.removeAttribute('data-empty');
    const p = t.dataset.prev, n = t.dataset.next;
    nav.hidden = !p && !n;
    prev.disabled = !p;
    next.disabled = !n;
    prev.dataset.to = p ?? '';
    next.dataset.to = n ?? '';
    if (!wide()) {
      const r = from?.getBoundingClientRect();
      const left = r ? r.left + r.width / 2 > innerWidth / 2 : false;
      panel!.classList.toggle('left', left);
      panel!.classList.add('open');
    }
    panel!.scrollTop = 0;
    if (from) returnTo = from;
    if (focus) panel!.focus({ preventScroll: true });
    if (setHash) history.replaceState(null, '', '#' + id.replace(/^tpl-/, ''));
    document.dispatchEvent(new CustomEvent('panel:select', { detail: { id } }));
  }

  function close() {
    if (wide()) {
      title.innerHTML = emptyHtml;
      content.innerHTML = '';
      nav.hidden = true;
      panel!.setAttribute('data-empty', '');
    }
    panel!.classList.remove('open');
    history.replaceState(null, '', location.pathname);
    document.dispatchEvent(new CustomEvent('panel:select', { detail: { id: null } }));
    returnTo?.focus();
  }

  document.addEventListener('click', (e) => {
    const el = (e.target as Element).closest<HTMLElement>('[data-panel]');
    if (!el) return;
    e.preventDefault();
    open(el.dataset.panel!, el);
  });
  document.addEventListener('keydown', (e) => {
    const el = (e.target as Element).closest?.<HTMLElement>('[role="button"][data-panel]');
    if (el && (e.key === 'Enter' || e.key === ' ')) {
      e.preventDefault();
      open(el.dataset.panel!, el);
    }
    if (e.key === 'Escape' && (panel.classList.contains('open') || (wide() && !panel.hasAttribute('data-empty')))) close();
  });
  closeBtn.addEventListener('click', close);
  for (const b of [prev, next]) b.addEventListener('click', () => b.dataset.to && open(b.dataset.to, trigger(b.dataset.to)));

  // 開いたとき: URL の #… があればそれ、無ければ 1400px 以上で初期の中身
  const fromHash = location.hash ? 'tpl-' + decodeURIComponent(location.hash.slice(1)) : '';
  if (fromHash && document.getElementById(fromHash)) requestAnimationFrame(() => open(fromHash, trigger(fromHash), false));
  else if (wide() && panel.dataset.initial) open(panel.dataset.initial, null, false, false);
  (window as any).__panelOpen = open;
}
