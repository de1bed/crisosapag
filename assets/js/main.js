/* ══════════════════════════════════════════════════════════════════
   CRISOSA Logistic Solutions — site behaviour
   Bilingual EN/ES, index overlay, a header that reads the panel
   beneath it, photograph placeholders carrying their own prompt,
   figure counters, scroll reveal and the mailto contact form.
   No dependencies. Every module checks for its markup before binding.
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
     Copy lives in data-es / data-en on leaf elements; attributes use
     the -ph / -alt / -label suffixes. Both versions live in the HTML,
     so editing a line means editing it twice. */
  var STORE = 'crisosa-lang';
  var ATTRS = { ph: 'placeholder', alt: 'alt', label: 'aria-label', title: 'title' };

  function setLang(lang) {
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
  }

  var saved = null;
  try { saved = localStorage.getItem(STORE); } catch (e) { /* ignore */ }
  setLang(saved || (/^es/i.test(navigator.language || '') ? 'es' : 'en'));

  $$('.lang button').forEach(function (b) {
    b.addEventListener('click', function () { setLang(b.getAttribute('data-lang')); });
  });

  /* Set by bindPage; the overlay calls it to restore the header tone. */
  var refreshTone = function () {};

  /* ════ 2. Index overlay ══════════════════════════════════════════ */
  var mega = $('#mega'), mtrig = $('#mtrig');
  if (mega && mtrig) {
    var items = $$('.mega__item', mega);
    items.forEach(function (el, i) { el.style.animationDelay = (0.05 * i + 0.08) + 's'; });

    var openMega = function (open) {
      mega.classList.toggle('is-open', open);
      mtrig.setAttribute('aria-expanded', String(open));
      mega.setAttribute('aria-hidden', String(!open));
      document.body.classList.toggle('is-locked', open);
      var label = mtrig.getAttribute('data-' + (open ? 'close' : 'open') + '-' + document.documentElement.lang);
      if (label) mtrig.textContent = label;
      // the overlay is the backdrop now, so the header reads it, not the page
      var hdr = $('#hdr');
      if (hdr) {
        if (open) { hdr.setAttribute('data-on', 'dark'); hdr.classList.remove('is-stuck'); }
        else refreshTone();
      }
      if (open) { if (items[0]) setTimeout(function () { items[0].focus(); }, 240); }
      else mtrig.focus();
    };
    mtrig.addEventListener('click', function () {
      openMega(mtrig.getAttribute('aria-expanded') !== 'true');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && mega.classList.contains('is-open')) openMega(false);
    });
    mega.addEventListener('click', function (e) { if (e.target.closest('a')) openMega(false); });
  }

  /* Page-scoped bindings, re-runnable so the single-file preview can
     swap routes in place. Everything above binds once. */
  var navObserver = null;

  function bindPage() {

    /* ════ 3. Header reads the panel beneath it ════════════════════
       Each panel declares data-nav="dark" or "light"; whichever panel
       sits under the header decides the header's colour. */
    var hdr = $('#hdr');
    if (hdr) {
      if (navObserver) { navObserver.disconnect(); navObserver = null; }
      var panels = $$('[data-nav]');
      var setTone = function () {
        // the last panel whose top has passed the header is the one behind it
        var probe = hdr.getBoundingClientRect().height * 0.6;
        var current = panels[0];
        for (var i = 0; i < panels.length; i++) {
          if (panels[i].getBoundingClientRect().top <= probe) current = panels[i];
        }
        hdr.setAttribute('data-on', current ? current.getAttribute('data-nav') : 'dark');
        hdr.classList.toggle('is-stuck', window.scrollY > 8);
      };
      setTone();
      refreshTone = setTone;
      window.addEventListener('scroll', setTone, { passive: true });
      window.addEventListener('resize', setTone);
      navObserver = { disconnect: function () {
        window.removeEventListener('scroll', setTone);
        window.removeEventListener('resize', setTone);
      } };
    }

    /* ════ 4. Photograph placeholders ══════════════════════════════
       A slot holds the real photograph. Until that file exists the
       slot keeps its composition and shows one quiet line naming what
       belongs there, with the prompt that produces it. */
    $$('.ph[data-prompt]').forEach(function (ph) {
      var slot = ph.parentElement;
      var img = $('.panel__bg, .tcard__bg, img', slot);
      if (img) {
        var miss = function () { slot.classList.add('is-empty'); };
        if (img.complete) { if (!img.naturalWidth) miss(); }
        else img.addEventListener('error', miss);
      }
      var btn = $('.ph__copy', ph);
      if (!btn) return;
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        var text = ph.getAttribute('data-prompt') || '';
        var done = function () {
          var es = document.documentElement.lang === 'es';
          btn.textContent = es ? 'Copiado' : 'Copied';
          setTimeout(function () {
            btn.textContent = btn.getAttribute('data-' + document.documentElement.lang) ||
                              (es ? 'Copiar prompt' : 'Copy prompt');
          }, 2000);
        };
        if (navigator.clipboard && navigator.clipboard.writeText) {
          navigator.clipboard.writeText(text).then(done, done);
        } else {
          var ta = document.createElement('textarea');
          ta.value = text; ta.style.position = 'fixed'; ta.style.opacity = '0';
          document.body.appendChild(ta); ta.select();
          try { document.execCommand('copy'); } catch (err) { /* ignore */ }
          document.body.removeChild(ta); done();
        }
      });
    });

    /* ════ 5. Scroll reveal ════════════════════════════════════════ */
    var reveals = $$('.reveal');
    if ('IntersectionObserver' in window && !reduce) {
      var rio = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          if (en.isIntersecting) { en.target.classList.add('is-in'); rio.unobserve(en.target); }
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });
      reveals.forEach(function (el) { rio.observe(el); });
    } else {
      reveals.forEach(function (el) { el.classList.add('is-in'); });
    }

    /* ════ 6. Figure counters ══════════════════════════════════════ */
    function count(el) {
      var target = parseFloat(el.getAttribute('data-count'));
      if (isNaN(target)) return;
      var t0 = null, dur = 1400;
      function step(ts) {
        if (t0 === null) t0 = ts;
        var p = Math.min((ts - t0) / dur, 1);
        var v = target * (1 - Math.pow(1 - p, 3));
        // data-plain: a year is not a quantity, so it is never grouped
        el.textContent = el.hasAttribute('data-plain')
          ? String(Math.round(v))
          : Math.round(v).toLocaleString('en-US');
        if (p < 1) requestAnimationFrame(step);
      }
      requestAnimationFrame(step);
    }
    var nums = $$('[data-count]');
    if ('IntersectionObserver' in window && !reduce) {
      var cio = new IntersectionObserver(function (es) {
        es.forEach(function (en) {
          if (en.isIntersecting) { count(en.target); cio.unobserve(en.target); }
        });
      }, { threshold: 0.5 });
      nums.forEach(function (el) { cio.observe(el); });
    }

    /* ════ 7. Contact form → mailto ════════════════════════════════ */
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

    /* ════ 8. Footer year ══════════════════════════════════════════ */
    var yr = $('#yr'); if (yr) yr.textContent = new Date().getFullYear();
  }

  bindPage();

  /* Exposed for the single-file preview build, which swaps routes in place. */
  window.CRISOSA = { bindPage: bindPage, setLang: setLang };
})();
