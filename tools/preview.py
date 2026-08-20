#!/usr/bin/env python3
"""
Build a single self-contained HTML file that carries the whole site.

Every route's <main> is inlined and a tiny hash router swaps between them,
so the twelve pages stay clickable inside one file with no server. Fonts,
logos and photographs are embedded as data URIs. Useful for sending the
site to someone before it is deployed anywhere.

    python3 tools/preview.py            → dist/crisosa-preview.html

The deployed site does not use this file: it serves the real routes.
"""
import base64
import mimetypes
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from build import PAGES  # noqa: E402

_cache = {}


def data_uri(rel):
    rel = rel.lstrip("./")
    if rel in _cache:
        return _cache[rel]
    p = ROOT / rel
    if not p.exists():
        # undecodable on purpose: fires the img error handler that reveals the
        # blueprint state, without issuing a request
        return "data:image/gif;base64,"
    mime = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
    uri = "data:%s;base64,%s" % (mime, base64.b64encode(p.read_bytes()).decode())
    _cache[rel] = uri
    return uri


ROUTE = {p[1]: ("#/" + p[1] if p[1] else "#/") for p in PAGES}


def rewrite(html, b):
    """Point every internal link at a hash route and every asset at a data URI."""
    # asset references → data URIs
    html = re.sub(r'(src|href)="%sassets/([^"]+)"' % re.escape(b),
                  lambda m: '%s="%s"' % (m.group(1), data_uri("assets/" + m.group(2))), html)
    # route links (strip any deep anchor: one hash per URL)
    for d, r in ROUTE.items():
        if not d:
            continue
        html = re.sub(r'href="%s%s/(#[a-z0-9\-]+)?"' % (re.escape(b), re.escape(d)),
                      'href="%s"' % r, html)
    # home
    html = html.replace('href="index.html"', 'href="#/"').replace('href="../"', 'href="#/"')
    return html


def build():
    # ── shell pieces come from the built home page ──────────────────
    home = (ROOT / "index.html").read_text(encoding="utf-8")
    head = re.search(r'<header class="hdr".*?</header>', home, re.S).group(0)
    mega = re.search(r'<div class="mega".*?\n</div>', home, re.S).group(0)
    foot = re.search(r'<footer class="ftr".*?</footer>', home, re.S).group(0)
    wa = re.search(r'<a class="wa".*?</a>', home, re.S).group(0)
    head, mega, foot, wa = (rewrite(x, "") for x in (head, mega, foot, wa))

    # ── every route's <main> ────────────────────────────────────────
    routes, titles = {}, {}
    for p in PAGES:
        d, b = p[1], ("" if p[1] == "" else "../")
        src = (ROOT / (d if d else ".") / "index.html").read_text(encoding="utf-8")
        body = re.search(r'<main id="main"[^>]*>(.*)</main>', src, re.S).group(1)
        routes[ROUTE[d]] = rewrite(body, b)
        titles[ROUTE[d]] = (
            re.search(r'data-es-doctitle="([^"]+)"', src).group(1),
            re.search(r'data-en-doctitle="([^"]+)"', src).group(1),
        )

    css = (ROOT / "assets/css/styles.css").read_text(encoding="utf-8")
    css = re.sub(r'url\(\.\./fonts/([^)]+)\)',
                 lambda m: "url(%s)" % data_uri("assets/fonts/" + m.group(1)), css)
    js = (ROOT / "assets/js/main.js").read_text(encoding="utf-8")

    import json
    out = f"""<title>CRISOSA Logistic Solutions</title>
<style>
{css}
</style>

{head}
{mega}

<main id="main" class="panels">
{routes['#/']}
</main>

{foot}

{wa}

<script>
{js}
</script>
<script>
/* Single-file router: the twelve routes live in one document. Only hashes
   that start with "#/" are routes — in-page anchors keep working. */
(function () {{
  var ROUTES = {json.dumps(routes, ensure_ascii=False)};
  var TITLES = {json.dumps(titles, ensure_ascii=False)};
  var main = document.getElementById('main');

  function show(hash, push) {{
    var html = ROUTES[hash];
    if (!html) return false;
    main.innerHTML = html;
    var t = TITLES[hash];
    if (t) document.title = document.documentElement.lang === 'en' ? t[1] : t[0];
    if (window.CRISOSA) {{
      window.CRISOSA.bindPage();
      window.CRISOSA.setLang(document.documentElement.lang || 'es');
    }}
    document.querySelectorAll('.hdr__nav a').forEach(function (a) {{
      a.toggleAttribute('aria-current', a.getAttribute('href') === hash);
    }});
    if (push) window.scrollTo(0, 0);
    return true;
  }}

  window.addEventListener('hashchange', function () {{
    if (location.hash.indexOf('#/') === 0) show(location.hash, true);
  }});
  if (location.hash.indexOf('#/') === 0) show(location.hash, false);
}})();
</script>
"""
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)

    # body-only: for hosts that supply their own <head> skeleton
    body = dist / "crisosa-body.html"
    body.write_text(out, encoding="utf-8")

    # standalone: opens correctly from disk or from any static host
    doc = dist / "crisosa-preview.html"
    doc.write_text(
        '<!DOCTYPE html>\n<html lang="es">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="theme-color" content="#050C1A">\n'
        '</head>\n<body>\n' + out + '\n</body>\n</html>\n',
        encoding="utf-8")

    for f in (doc, body):
        print(f"{f.relative_to(ROOT)} — {f.stat().st_size / 1048576:.2f} MB")
    print(f"{len(routes)} routes, {len(_cache)} assets embedded")


if __name__ == "__main__":
    build()
