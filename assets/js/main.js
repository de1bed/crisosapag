/* ══════════════════════════════════════════════════════════════════
   CRISOSA Logistic Solutions — site behaviour
   Bilingual EN/ES, mega-menu, hero canvas, image plates with
   copyable generation prompts, section rail, flow stepper,
   service picker, counters, meters and the mailto contact form.
   No dependencies. Every module is optional: each one checks for
   its own markup before binding.
   ══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* Inbox that receives the contact form. Change to the address
     CRISOSA wants to publish (e.g. ventas@crisosa.com). */
  var CONTACT_EMAIL = 'info@crisosa.com';

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ════ 1. Language ═══════════════════════════════════════════════
     Text lives in data-en / data-es on leaf elements. Attributes use
     the -ph / -alt / -label suffixes. Editing copy means editing both
     versions in the HTML — there is no separate string file. */
  var STORE = 'crisosa-lang';
  var ATTRS = { ph: 'placeholder', alt: 'alt', label: 'aria-label', title: 'title' };

  function setLang(lang) {
    var other = lang === 'es' ? 'en' : 'es';
    document.documentElement.lang = lang;

    $$('[data-' + lang + ']').forEach(function (el) {
      el.textContent = el.getAttribute('data-' + lang);
    });
    Object.keys(ATTRS).forEach(function (k) {
      $$('[data-' + lang + '-' + k + ']').forEach(function (el) {
        el.setAttribute(ATTRS[k], el.getAttribute('data-' + lang + '-' + k));
      });
    });

    var t = document.body.getAttribute('data-' + lang + '-doctitle');
    if (t) document.title = t;
    var d = document.body.getAttribute('data-' + lang + '-docdesc');
    var meta = $('meta[name="description"]');
    if (d && meta) meta.setAttribute('content', d);

    $$('.lang button').forEach(function (b) {
      var on = b.getAttribute('data-lang') === lang;
      b.classList.toggle('is-on', on);
      b.setAttribute('aria-pressed', String(on));
    });

    try { localStorage.setItem(STORE, lang); } catch (e) { /* private mode */ }
    document.documentElement.setAttribute('data-other-lang', other);
  }

  var saved = null;
  try { saved = localStorage.getItem(STORE); } catch (e) { /* ignore */ }
  setLang(saved || (/^es/i.test(navigator.language || '') ? 'es' : 'en'));

  $$('.lang button').forEach(function (b) {
    b.addEventListener('click', function () { setLang(b.getAttribute('data-lang')); });
  });

  /* ════ 2. Header state ═══════════════════════════════════════════ */
  var hdr = $('#hdr');
  if (hdr) {
    var stick = function () { hdr.classList.toggle('is-stuck', window.scrollY > 12); };
    stick();
    window.addEventListener('scroll', stick, { passive: true });
  }

  /* ════ 3. Mega-menu ══════════════════════════════════════════════ */
  var mega = $('#mega'), mtrig = $('#mtrig');
  if (mega && mtrig) {
    var items = $$('.mega__item', mega);
    items.forEach(function (el, i) { el.style.animationDelay = (0.04 * i + 0.06) + 's'; });

    var openMega = function (open) {
      mega.classList.toggle('is-open', open);
      mtrig.setAttribute('aria-expanded', String(open));
      document.body.classList.toggle('is-locked', open);
      mega.setAttribute('aria-hidden', String(!open));
      if (open) { var f = items[0]; if (f) setTimeout(function () { f.focus(); }, 260); }
      else mtrig.focus();
    };
    mtrig.addEventListener('click', function () {
      openMega(mtrig.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mega.classList.contains('is-open')) openMega(false);
    });
    mega.addEventListener('click', function (e) {
      if (e.target.closest('a')) openMega(false);
    });
  }

  /* ════ 4. Image plates ═══════════════════════════════════════════
     A plate starts empty and only shows its picture once the file
     named in the <img> actually loads. Until then it renders the
     blueprint state carrying the prompt that produces it. */
  $$('.plate').forEach(function (plate) {
    var img = $('img', plate);
    if (!img) return;
    var miss = function () { plate.classList.add('is-empty'); };
    if (img.complete) { if (!img.naturalWidth) miss(); }
    else { img.addEventListener('error', miss); }

    var btn = $('.plate__act', plate);
    if (!btn) return;
    btn.addEventListener('click', function () {
      var text = plate.getAttribute('data-prompt') || '';
      var done = function () {
        var es = document.documentElement.lang === 'es';
        btn.textContent = es ? 'Prompt copiado' : 'Prompt copied';
        btn.classList.add('is-done');
        setTimeout(function () {
          btn.textContent = btn.getAttribute('data-' + (document.documentElement.lang) ) ||
                            (es ? 'Copiar prompt' : 'Copy prompt');
          btn.classList.remove('is-done');
        }, 2200);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, done);
      } else {
        var ta = document.createElement('textarea');
        ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
        document.body.appendChild(ta); ta.select();
        try { document.execCommand('copy'); } catch (e) { /* ignore */ }
        document.body.removeChild(ta); done();
      }
    });
  });

  /* ════ 5. Scroll reveal ══════════════════════════════════════════ */
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window && !reduce) {
    var rio = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); rio.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -10% 0px', threshold: 0.06 });
    reveals.forEach(function (el) { rio.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ════ 6. Counters & meters ══════════════════════════════════════ */
  function count(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    if (isNaN(target)) return;
    var dec = parseInt(el.getAttribute('data-dec') || '0', 10);
    var t0 = null, dur = 1200;
    function step(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var v = target * (1 - Math.pow(1 - p, 3));
      // data-plain: years and codes are not quantities — never group them
      el.textContent = el.hasAttribute('data-plain')
        ? String(Math.round(v))
        : v.toLocaleString('en-US', { minimumFractionDigits: dec, maximumFractionDigits: dec });
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }

  var animated = $$('[data-count],.meter__bar[data-pct]');
  if ('IntersectionObserver' in window && !reduce) {
    var aio = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target;
        if (el.hasAttribute('data-count')) count(el);
        else el.style.width = el.getAttribute('data-pct') + '%';
        aio.unobserve(el);
      });
    }, { threshold: 0.45 });
    animated.forEach(function (el) { aio.observe(el); });
  } else {
    animated.forEach(function (el) {
      if (el.hasAttribute('data-pct')) el.style.width = el.getAttribute('data-pct') + '%';
    });
  }

  /* ════ 7. Section rail scroll-spy ════════════════════════════════ */
  var railLinks = $$('.rail a[href^="#"]');
  if (railLinks.length && 'IntersectionObserver' in window) {
    var targets = railLinks
      .map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); })
      .filter(Boolean);
    var sio = new IntersectionObserver(function (es) {
      es.forEach(function (en) {
        if (!en.isIntersecting) return;
        railLinks.forEach(function (a) {
          a.classList.toggle('is-active', a.getAttribute('href') === '#' + en.target.id);
        });
      });
    }, { rootMargin: '-20% 0px -68% 0px' });
    targets.forEach(function (t) { sio.observe(t); });
  }

  /* ════ 8. Flow stepper ═══════════════════════════════════════════ */
  var flow = $('#flow');
  if (flow) {
    var tabs = $$('.flow__btn', flow);
    var panels = $$('.flow__panel', flow);
    var select = function (i) {
      tabs.forEach(function (t, n) { t.setAttribute('aria-selected', String(n === i)); });
      panels.forEach(function (p, n) { p.classList.toggle('is-on', n === i); });
    };
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { select(i); });
      t.addEventListener('keydown', function (e) {
        var d = e.key === 'ArrowDown' || e.key === 'ArrowRight' ? 1
              : e.key === 'ArrowUp'   || e.key === 'ArrowLeft'  ? -1 : 0;
        if (!d) return;
        e.preventDefault();
        var n = (i + d + tabs.length) % tabs.length;
        tabs[n].focus(); select(n);
      });
    });
    select(0);
  }

  /* ════ 9. Service picker ═════════════════════════════════════════ */
  var pick = $('#pick');
  if (pick) {
    var opts = $$('.pick__opt', pick);
    var out = $('.pick__out', pick);
    var results = $$('[data-result]', pick);
    opts.forEach(function (o) {
      o.addEventListener('click', function () {
        var key = o.getAttribute('data-pick');
        opts.forEach(function (x) { x.setAttribute('aria-pressed', String(x === o)); });
        results.forEach(function (r) { r.hidden = r.getAttribute('data-result') !== key; });
        out.hidden = false;
      });
    });
  }

  /* ════ 10. Hero canvas ═══════════════════════════════════════════
     The border, drawn as data: a hairline node field with the
     frontier as a bright horizontal, and shipments crossing it. */
  var cv = $('#heroCanvas');
  if (cv && !reduce) {
    var ctx = cv.getContext('2d');
    var W = 0, H = 0, dpr = Math.min(window.devicePixelRatio || 1, 2);
    var nodes = [], routes = [], raf = null;

    function build() {
      var r = cv.getBoundingClientRect();
      W = r.width; H = r.height;
      cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      var cols = Math.max(7, Math.round(W / 118));
      var rows = Math.max(5, Math.round(H / 108));
      nodes = [];
      for (var y = 0; y <= rows; y++) {
        for (var x = 0; x <= cols; x++) {
          nodes.push({
            x: (x / cols) * W + (Math.random() - .5) * 30,
            y: (y / rows) * H + (Math.random() - .5) * 26,
            p: Math.random() * Math.PI * 2
          });
        }
      }
      // four shipment routes crossing the frontier line at 52% height
      routes = [];
      for (var i = 0; i < 4; i++) {
        var x0 = W * (0.08 + 0.24 * i + Math.random() * .08);
        routes.push({
          pts: [
            { x: x0, y: H * 1.02 },
            { x: x0 + (Math.random() - .5) * W * .14, y: H * .74 },
            { x: x0 + (Math.random() - .5) * W * .10, y: H * .52 },
            { x: x0 + (Math.random() - .5) * W * .20, y: H * .26 },
            { x: x0 + (Math.random() - .5) * W * .26, y: -H * .04 }
          ],
          t: Math.random(),
          v: 0.0016 + Math.random() * 0.0013
        });
      }
    }

    function at(pts, t) {
      var n = pts.length - 1, i = Math.min(Math.floor(t * n), n - 1), f = t * n - i;
      return { x: pts[i].x + (pts[i + 1].x - pts[i].x) * f,
               y: pts[i].y + (pts[i + 1].y - pts[i].y) * f };
    }

    function frame(ts) {
      ctx.clearRect(0, 0, W, H);

      // node field
      for (var i = 0; i < nodes.length; i++) {
        var n = nodes[i];
        var a = 0.16 + 0.16 * Math.sin(ts / 1400 + n.p);
        ctx.fillStyle = 'rgba(120,180,235,' + a.toFixed(3) + ')';
        ctx.fillRect(n.x, n.y, 1.6, 1.6);
      }

      // the frontier
      var fy = H * 0.52;
      ctx.strokeStyle = 'rgba(69,215,255,.20)';
      ctx.lineWidth = 1;
      ctx.setLineDash([2, 7]);
      ctx.beginPath(); ctx.moveTo(0, fy); ctx.lineTo(W, fy); ctx.stroke();
      ctx.setLineDash([]);

      // routes + shipments
      for (var r = 0; r < routes.length; r++) {
        var ro = routes[r];
        ctx.strokeStyle = 'rgba(120,180,235,.13)';
        ctx.beginPath();
        ctx.moveTo(ro.pts[0].x, ro.pts[0].y);
        for (var p = 1; p < ro.pts.length; p++) ctx.lineTo(ro.pts[p].x, ro.pts[p].y);
        ctx.stroke();

        ro.t += ro.v; if (ro.t > 1) ro.t = 0;
        var pos = at(ro.pts, ro.t);
        var tail = at(ro.pts, Math.max(0, ro.t - .07));
        var g = ctx.createLinearGradient(tail.x, tail.y, pos.x, pos.y);
        g.addColorStop(0, 'rgba(69,215,255,0)');
        g.addColorStop(1, 'rgba(69,215,255,.85)');
        ctx.strokeStyle = g; ctx.lineWidth = 1.6;
        ctx.beginPath(); ctx.moveTo(tail.x, tail.y); ctx.lineTo(pos.x, pos.y); ctx.stroke();
        ctx.lineWidth = 1;

        ctx.fillStyle = 'rgba(69,215,255,.95)';
        ctx.beginPath(); ctx.arc(pos.x, pos.y, 2.1, 0, Math.PI * 2); ctx.fill();
      }
      raf = requestAnimationFrame(frame);
    }

    var start = function () { if (raf === null) raf = requestAnimationFrame(frame); };
    var stop  = function () { if (raf !== null) { cancelAnimationFrame(raf); raf = null; } };

    build(); start();
    var rt = null;
    window.addEventListener('resize', function () {
      clearTimeout(rt); rt = setTimeout(function () { build(); }, 180);
    });
    document.addEventListener('visibilitychange', function () {
      document.hidden ? stop() : start();
    });
  }

  /* ════ 11. Contact form → mailto ═════════════════════════════════ */
  var form = $('#form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.reportValidity()) return;
      var d = new FormData(form);
      var es = document.documentElement.lang === 'es';
      var subject = (es ? 'Solicitud de información — ' : 'Information request — ') + d.get('service');
      var body = [
        (es ? 'Nombre: '   : 'Name: ')    + (d.get('name')    || ''),
        (es ? 'Empresa: '  : 'Company: ') + (d.get('company') || ''),
        (es ? 'Correo: '   : 'Email: ')   + (d.get('email')   || ''),
        (es ? 'Teléfono: ' : 'Phone: ')   + (d.get('phone')   || ''),
        (es ? 'Servicio: ' : 'Service: ') + (d.get('service') || ''),
        '',
        d.get('message') || ''
      ].join('\n');
      window.location.href = 'mailto:' + CONTACT_EMAIL +
        '?subject=' + encodeURIComponent(subject) +
        '&body='    + encodeURIComponent(body);
    });
  }

  /* ════ 12. Footer year ═══════════════════════════════════════════ */
  var yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();
})();
