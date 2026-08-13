/* ════════════════════════════════════════════════════════════════
   CRISOSA Logistic Solutions — site behaviour
   Bilingual EN/ES switch, mobile nav, scroll reveal, stat counters,
   scroll-spy and a mailto-based contact form.
   ════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* Inbox that receives the contact form. Change to the address
     CRISOSA wants to publish (e.g. ventas@crisosa.com). */
  var CONTACT_EMAIL = 'info@crisosa.com';

  var $  = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* ── Language ─────────────────────────────────────────────── */
  var STORE = 'crisosa-lang';
  var langBtns = $$('.lang button');

  function setLang(lang) {
    document.documentElement.lang = lang;
    $$('[data-' + lang + ']').forEach(function (el) {
      el.textContent = el.getAttribute('data-' + lang);
    });
    langBtns.forEach(function (b) {
      b.classList.toggle('is-on', b.dataset.lang === lang);
      b.setAttribute('aria-pressed', String(b.dataset.lang === lang));
    });
    try { localStorage.setItem(STORE, lang); } catch (e) { /* private mode */ }
  }

  var saved;
  try { saved = localStorage.getItem(STORE); } catch (e) { saved = null; }
  setLang(saved || (/^es/i.test(navigator.language || '') ? 'es' : 'en'));

  langBtns.forEach(function (b) {
    b.addEventListener('click', function () { setLang(b.dataset.lang); });
  });

  /* ── Header state + mobile nav ────────────────────────────── */
  var hdr = $('#hdr'), nav = $('#nav'), burger = $('#burger');

  burger.addEventListener('click', function () {
    var open = nav.classList.toggle('is-open');
    burger.setAttribute('aria-expanded', String(open));
  });
  nav.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') {
      nav.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
    }
  });

  var onScroll = function () {
    hdr.classList.toggle('is-stuck', window.scrollY > 20);
  };
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ── Scroll reveal ────────────────────────────────────────── */
  var reveals = $$('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: 0.08 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ── Stat counters ────────────────────────────────────────── */
  var stats = $$('[data-count]');
  function runCounter(el) {
    if (el.hasAttribute('data-plain')) return;          // years render as-is
    var target = parseInt(el.getAttribute('data-count'), 10);
    var suffix = el.getAttribute('data-suffix') || '';
    var t0 = null, dur = 1300;
    function step(ts) {
      if (t0 === null) t0 = ts;
      var p = Math.min((ts - t0) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased).toLocaleString('en-US') + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ('IntersectionObserver' in window &&
      !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { runCounter(en.target); cio.unobserve(en.target); }
      });
    }, { threshold: 0.6 });
    stats.forEach(function (el) { cio.observe(el); });
  }

  /* ── Scroll spy ───────────────────────────────────────────── */
  var links = $$('.nav a[href^="#"]');
  var sections = links
    .map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); })
    .filter(Boolean);

  if ('IntersectionObserver' in window && sections.length) {
    var sio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        links.forEach(function (a) {
          a.classList.toggle('is-active', a.getAttribute('href') === '#' + en.target.id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach(function (s) { sio.observe(s); });
  }

  /* ── Contact form → mailto ────────────────────────────────── */
  var form = $('#form');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    if (!form.reportValidity()) return;

    var d = new FormData(form);
    var es = document.documentElement.lang === 'es';
    var subject = (es ? 'Solicitud de información — ' : 'Information request — ') + d.get('service');
    var body = [
      (es ? 'Nombre: '  : 'Name: ')    + (d.get('name')    || ''),
      (es ? 'Empresa: ' : 'Company: ') + (d.get('company') || ''),
      (es ? 'Correo: '  : 'Email: ')   + (d.get('email')   || ''),
      (es ? 'Servicio: ': 'Service: ') + (d.get('service') || ''),
      '',
      d.get('message') || ''
    ].join('\n');

    window.location.href = 'mailto:' + CONTACT_EMAIL +
      '?subject=' + encodeURIComponent(subject) +
      '&body='    + encodeURIComponent(body);
  });

  /* ── Footer year ──────────────────────────────────────────── */
  $('#yr').textContent = new Date().getFullYear();
})();
