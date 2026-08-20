#!/usr/bin/env python3
"""
CRISOSA Logistic Solutions — static site builder.

The site ships as plain HTML: no server, no runtime, no npm. This script
exists so the shared shell (header, index overlay, footer) stays identical
across the seven routes. It reads each page body from tools/parts/<slug>.html
and writes <route>/index.html.

    python3 tools/build.py

Editing copy: the generated HTML is normal readable HTML and can be edited
directly. Keep edits in tools/parts/ if you want them to survive a rebuild.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PARTS = ROOT / "tools" / "parts"
sys.path.insert(0, str(ROOT / "tools"))
from plates import PLATES  # noqa: E402

WHATSAPP = "526646072000"

# slug, directory, ES name, EN name
PAGES = [
    ("home",            "",                "Inicio",          "Home"),
    ("servicios",       "servicios",       "Servicios",       "Services"),
    ("certificaciones", "certificaciones", "Certificaciones", "Certifications"),
    ("clientes",        "clientes",        "Clientes",        "Clients"),
    ("instalaciones",   "instalaciones",   "Instalaciones",   "Facilities"),
    ("nosotros",        "nosotros",        "Nosotros",        "About us"),
    ("contacto",        "contacto",        "Contacto",        "Contact"),
]

NAV = ["servicios", "certificaciones", "clientes", "instalaciones", "nosotros", "contacto"]

META = {
 "home": (
  "CRISOSA Logistic Solutions — Certificada AAA · CTPAT · IMMEX · Tijuana",
  "CRISOSA Logistic Solutions — AAA · CTPAT · IMMEX certified · Tijuana",
  "Empresa certificada IVA/IEPS AAA, CTPAT e IMMEX. 22,000 m² de almacenaje en Tijuana, "
  "B.C. y 30 años cruzando carga para Hisense, Steelcase, Cardinal Health y Hanes.",
  "IVA/IEPS AAA, CTPAT and IMMEX certified. 22,000 m² of warehousing in Tijuana, B.C. and "
  "30 years crossing freight for Hisense, Steelcase, Cardinal Health and Hanes."),
 "servicios": (
  "Servicios — CRISOSA Logistic Solutions",
  "Services — CRISOSA Logistic Solutions",
  "Importación y exportación, almacenaje y shelter en la frontera México–Estados Unidos, "
  "bajo un solo operador certificado.",
  "Import and export, warehousing and shelter on the U.S.–Mexico border, under one "
  "certified operator."),
 "certificaciones": (
  "Certificaciones — CRISOSA Logistic Solutions",
  "Certifications — CRISOSA Logistic Solutions",
  "IVA/IEPS nivel AAA, CTPAT, IMMEX y OEA en proceso. Las acreditaciones que permiten "
  "cruzar más rápido y con menos capital inmovilizado.",
  "IVA/IEPS AAA level, CTPAT, IMMEX and OEA in progress. The accreditations that let "
  "freight cross faster with less capital tied up."),
 "clientes": (
  "Clientes — CRISOSA Logistic Solutions",
  "Clients — CRISOSA Logistic Solutions",
  "Hisense, Steelcase, Cardinal Health, Hanes, Enovis y once empresas más confían su carga "
  "transfronteriza a CRISOSA.",
  "Hisense, Steelcase, Cardinal Health, Hanes, Enovis and eleven more companies trust "
  "CRISOSA with their cross-border freight."),
 "instalaciones": (
  "Instalaciones — CRISOSA Logistic Solutions",
  "Facilities — CRISOSA Logistic Solutions",
  "22,000 m² en tres naves en Tijuana, B.C., con patio propio, andenes de carga y "
  "seguridad bajo estándar CTPAT.",
  "22,000 m² across three buildings in Tijuana, B.C., with our own yard, loading docks "
  "and CTPAT-standard security."),
 "nosotros": (
  "Nosotros — CRISOSA Logistic Solutions",
  "About us — CRISOSA Logistic Solutions",
  "Fundada en 1994 en Tijuana, B.C. Treinta años creciendo al ritmo que la carga de "
  "nuestros clientes lo ha exigido.",
  "Founded in 1994 in Tijuana, B.C. Thirty years growing at the pace our customers' "
  "freight demanded."),
 "contacto": (
  "Contacto — CRISOSA Logistic Solutions",
  "Contact — CRISOSA Logistic Solutions",
  "Escríbenos o llámanos en México y Estados Unidos. Respondemos con una propuesta "
  "concreta para tu operación.",
  "Write or call us in Mexico and the United States. We reply with a concrete proposal "
  "for your operation."),
}

# ── Photograph slots ────────────────────────────────────────────────
PLATE_PAGE = {}
SLOT_RE = re.compile(r"\{\{(BG|CARD|SHOT|PORTRAIT):([a-z0-9\-]+)\}\}")
SVG_RE = re.compile(r"\{\{SVG:([a-z0-9\-]+)\}\}")


def slot(kind, key, b):
    d = PLATES[key]
    src = f"{b}assets/img/generated/{d['file']}"
    ratio = d["ar"].replace("/", ":")
    eager = ' fetchpriority="high"' if kind == "BG" else ' loading="lazy"'
    img = {
        "BG":   f'<img class="panel__bg" src="{src}" alt=""{eager} decoding="async">',
        "CARD": f'<img class="tcard__bg" src="{src}" alt=""{eager} decoding="async">',
        "SHOT": f'<img src="{src}" alt=""{eager} decoding="async">',
        "PORTRAIT": f'<img src="{src}" alt=""{eager} decoding="async">',
    }[kind]
    ph_class = "ph ph--light" if kind in ("SHOT", "PORTRAIT") else "ph"
    scrim = '\n      <div class="panel__scrim"></div>' if kind == "BG" else ""
    return f"""{img}
      <div class="{ph_class}" data-prompt="{html.escape(d['prompt'], quote=True)}">
        <p class="ph__note">
          <b data-es="Fotografía · {d['file']} · {ratio}" data-en="Photograph · {d['file']} · {ratio}">Fotografía · {d['file']} · {ratio}</b>
          <span data-es="{html.escape(d['t_es'], quote=True)}" data-en="{html.escape(d['t_en'], quote=True)}">{d['t_es']}</span>
          <button type="button" class="ph__copy" data-es="Copiar prompt" data-en="Copy prompt">Copiar prompt</button>
        </p>
      </div>{scrim}"""


def expand(body, b, page=""):
    def sub(m):
        PLATE_PAGE.setdefault(m.group(2), page)
        return slot(m.group(1), m.group(2), b)
    body = SLOT_RE.sub(sub, body)
    # figures are inlined, not linked: they inherit the page's type and colours
    return SVG_RE.sub(
        lambda m: (ROOT / "assets" / "svg" / f"{m.group(1)}.svg").read_text(encoding="utf-8").strip(),
        body)


# ── Shell ───────────────────────────────────────────────────────────
SHELL = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_es}</title>
<meta name="description" content="{desc_es}">
<meta name="theme-color" content="#0E1116">
<link rel="icon" href="{b}assets/logos/crisosa.png">
<link rel="canonical" href="{canonical}">
<meta property="og:site_name" content="CRISOSA Logistic Solutions">
<meta property="og:title" content="{title_es}">
<meta property="og:description" content="{desc_es}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{site}/assets/img/generated/home-hero.jpg">
<meta property="og:locale" content="es_MX">
<meta property="og:locale:alternate" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="{b}assets/css/styles.css">
{ld}
</head>
<body
  data-es-doctitle="{title_es}" data-en-doctitle="{title_en}"
  data-es-docdesc="{desc_es}" data-en-docdesc="{desc_en}">

<a class="skip" href="#main" data-es="Ir al contenido" data-en="Skip to content">Ir al contenido</a>

{header}
{mega}

<main id="main" class="panels">
{body}
</main>

{footer}

<a class="wa" href="https://wa.me/{wa}" target="_blank" rel="noopener"
   data-es-label="Escribir por WhatsApp" data-en-label="Message us on WhatsApp" aria-label="Escribir por WhatsApp">
  <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12.04 2C6.6 2 2.18 6.42 2.18 11.86c0 1.74.46 3.44 1.32 4.94L2.1 22l5.35-1.4a9.8 9.8 0 0 0 4.59 1.17h.01c5.43 0 9.85-4.42 9.85-9.86C21.9 6.42 17.47 2 12.04 2Zm5.77 14.09c-.24.68-1.42 1.31-1.95 1.36-.5.05-.96.22-3.23-.68-2.72-1.07-4.44-3.85-4.57-4.03-.13-.18-1.09-1.45-1.09-2.76s.69-1.96.93-2.23c.24-.27.53-.34.7-.34h.5c.16 0 .38-.06.59.45.24.57.8 1.98.87 2.12.07.14.12.3.02.48-.1.18-.15.29-.29.45-.14.16-.3.35-.43.47-.14.14-.29.29-.12.57.17.28.74 1.22 1.59 1.98 1.09.97 2.01 1.27 2.29 1.41.28.14.45.12.61-.07.17-.2.71-.83.9-1.11.19-.28.38-.23.63-.14.26.09 1.66.78 1.94.93.28.14.47.21.54.32.07.12.07.66-.17 1.34Z"/></svg>
  <span data-es="WhatsApp" data-en="WhatsApp">WhatsApp</span>
</a>

<script src="{b}assets/js/main.js"></script>
</body>
</html>
"""

LD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "CRISOSA Logistic Solutions",
  "url": "%(site)s/",
  "logo": "%(site)s/assets/logos/crisosa.png",
  "foundingDate": "1994",
  "description": "Importación, exportación, almacenaje y shelter en la frontera México–Estados Unidos. Empresa certificada IVA/IEPS AAA, CTPAT e IMMEX.",
  "address": { "@type": "PostalAddress", "addressLocality": "Tijuana", "addressRegion": "Baja California", "addressCountry": "MX" },
  "contactPoint": [
    { "@type": "ContactPoint", "telephone": "+52-664-607-2000", "contactType": "sales", "areaServed": "MX", "availableLanguage": ["es","en"] },
    { "@type": "ContactPoint", "telephone": "+1-619-270-2229", "contactType": "sales", "areaServed": "US", "availableLanguage": ["en","es"] }
  ],
  "email": "info@crisosa.com",
  "hasCredential": ["IMMEX", "IVA/IEPS AAA", "CTPAT"]
}
</script>"""


def header(b, home, slug):
    links = "\n".join(
        '      <a href="{h}"{cur} data-es="{es}" data-en="{en}">{es}</a>'.format(
            h=f"{b}{p[1]}/", es=p[2], en=p[3],
            cur=' aria-current="page"' if p[0] == slug else "")
        for s in NAV for p in PAGES if p[0] == s)
    return f"""<header class="hdr" id="hdr" data-on="dark">
  <div class="hdr__in">
    <a class="hdr__logo" href="{home}" aria-label="CRISOSA Logistic Solutions">
      <img class="logo--light" src="{b}assets/logos/crisosa-white.png" alt="CRISOSA Logistic Solutions" width="140" height="26">
      <img class="logo--dark" src="{b}assets/logos/crisosa.png" alt="CRISOSA Logistic Solutions" width="140" height="26">
    </a>
    <nav class="hdr__nav" aria-label="Principal">
{links}
    </nav>
    <div class="hdr__tools">
      <div class="lang" role="group" aria-label="Idioma / Language">
        <button type="button" data-lang="es" class="is-on">ES</button><i aria-hidden="true">/</i><button type="button" data-lang="en">EN</button>
      </div>
      <button class="mtrig" id="mtrig" type="button" aria-expanded="false" aria-controls="mega"
        data-open-es="Índice" data-close-es="Cerrar" data-open-en="Index" data-close-en="Close"
        data-es="Índice" data-en="Index">Índice</button>
    </div>
  </div>
</header>"""


def mega(b, home):
    rows = "\n".join(
        '      <a class="mega__item" href="{h}"><span data-es="{es}" data-en="{en}">{es}</span></a>'.format(
            h=(home if p[1] == "" else f"{b}{p[1]}/"), es=p[2], en=p[3])
        for p in PAGES)
    return f"""<div class="mega" id="mega" role="dialog" aria-modal="true" aria-hidden="true" aria-label="Índice">
  <div class="mega__in">
    <nav class="mega__list">
{rows}
    </nav>
    <div class="mega__foot">
      <a href="tel:+526646072000">+52 (664) 607-20-00</a>
      <a href="tel:+16192702229">+1 (619) 270-22-29</a>
      <a href="mailto:info@crisosa.com">info@crisosa.com</a>
      <span>Tijuana, Baja California, México</span>
    </div>
  </div>
</div>"""


def footer(b, home):
    def li(slug):
        p = next(x for x in PAGES if x[0] == slug)
        h = home if p[1] == "" else f"{b}{p[1]}/"
        return f'          <li><a href="{h}" data-es="{p[2]}" data-en="{p[3]}">{p[2]}</a></li>'
    nav1 = "\n".join(li(s) for s in ["servicios", "certificaciones", "clientes"])
    nav2 = "\n".join(li(s) for s in ["instalaciones", "nosotros", "contacto"])
    return f"""<footer class="ftr">
  <div class="ftr__in">
    <div class="ftr__top">
      <div>
        <img class="ftr__logo" src="{b}assets/logos/crisosa-white.png" alt="CRISOSA Logistic Solutions" width="160" height="30">
        <p class="small" data-es="Empresa certificada IVA/IEPS AAA · CTPAT · IMMEX" data-en="Certified company IVA/IEPS AAA · CTPAT · IMMEX">Empresa certificada IVA/IEPS AAA · CTPAT · IMMEX</p>
        <p class="small" style="margin-top:.4rem">Tijuana, Baja California, México</p>
      </div>
      <div>
        <h4 data-es="Sitio" data-en="Site">Sitio</h4>
        <ul>
{nav1}
{nav2}
        </ul>
      </div>
      <div>
        <h4 data-es="Contacto" data-en="Contact">Contacto</h4>
        <ul>
          <li><a href="tel:+526646072000">MX +52 (664) 607-20-00</a></li>
          <li><a href="tel:+16192702229">US +1 (619) 270-22-29</a></li>
          <li><a href="mailto:info@crisosa.com">info@crisosa.com</a></li>
          <li><a href="https://wa.me/{WHATSAPP}" target="_blank" rel="noopener">WhatsApp</a></li>
        </ul>
      </div>
    </div>
    <div class="ftr__bar">
      <span>© <span id="yr">2026</span> CRISOSA Logistic Solutions.</span>
      <span data-es="Siempre superando expectativas" data-en="Always exceeding expectations">Siempre superando expectativas</span>
    </div>
  </div>
</footer>"""


# Absolute base for canonical URLs, og:image and the sitemap. Change this
# to the real domain before publishing — social previews and Google both
# need an absolute URL and will silently do nothing with the wrong one.
SITE = "https://www.crisosa.com"


def build():
    written = []
    for p in PAGES:
        slug, d = p[0], p[1]
        b = "" if d == "" else "../"
        home = "index.html" if d == "" else "../"
        canonical = f"{SITE}/" + (f"{d}/" if d else "")
        body = expand((PARTS / f"{slug}.html").read_text(encoding="utf-8"), b, p[2])
        body = body.replace("{b}", b).replace("{home}", home).replace("{wa}", WHATSAPP)
        t_es, t_en, d_es, d_en = META[slug]
        page = SHELL.format(
            b=b, wa=WHATSAPP, site=SITE, canonical=canonical,
            ld=(LD % {"site": SITE}) if slug == "home" else "",
            title_es=html.escape(t_es, quote=True), title_en=html.escape(t_en, quote=True),
            desc_es=html.escape(d_es, quote=True), desc_en=html.escape(d_en, quote=True),
            header=header(b, home, slug), mega=mega(b, home), footer=footer(b, home),
            body=body.rstrip(),
        )
        out = ROOT / (d if d else ".") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        written.append(str(out.relative_to(ROOT)))

    nf = PARTS / "404.html"
    if nf.exists():
        body = expand(nf.read_text(encoding="utf-8"), "/").replace("{b}", "/").replace("{home}", "/")
        page = SHELL.format(
            b="/", wa=WHATSAPP, site=SITE, canonical=f"{SITE}/404.html", ld="",
            title_es="Página no encontrada — CRISOSA", title_en="Page not found — CRISOSA",
            desc_es="La página que buscas no existe.", desc_en="The page you are looking for does not exist.",
            header=header("/", "/", ""), mega=mega("/", "/"), footer=footer("/", "/"),
            body=body.rstrip())
        (ROOT / "404.html").write_text(page, encoding="utf-8")
        written.append("404.html")

    write_sitemap(); written += ["sitemap.xml", "robots.txt"]
    write_prompts(); written.append("assets/img/PROMPTS.md")
    print("\n".join(written) + f"\n\n{len(written)} files written.")


def write_sitemap():
    urls = "\n".join(
        f"  <url><loc>{SITE}/{p[1] + '/' if p[1] else ''}</loc>"
        f"<changefreq>monthly</changefreq>"
        f"<priority>{'1.0' if not p[1] else '0.8'}</priority></url>"
        for p in PAGES)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{urls}\n</urlset>\n", encoding="utf-8")
    (ROOT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")


def write_prompts():
    """Regenerate assets/img/PROMPTS.md from the catalogue."""
    have = {f.name for f in (ROOT / "assets" / "img" / "generated").glob("*")}
    ai = [(k, d) for k, d in PLATES.items() if d.get("kind") != "foto"]
    photo = [(k, d) for k, d in PLATES.items() if d.get("kind") == "foto"]
    pending = [k for k, d in PLATES.items() if d["file"] not in have]

    L = [
        "# Imágenes del sitio",
        "",
        f"El sitio tiene **{len(PLATES)} espacios de imagen**. "
        f"Hoy faltan **{len(pending)}**.",
        "",
        "Mientras un archivo no exista, su pantalla conserva la composición sobre un",
        "degradado y muestra abajo una línea con el nombre del archivo y un botón",
        "**«Copiar prompt»**. Para llenarla: genera o toma la imagen y guárdala en",
        "`assets/img/generated/` **con exactamente el nombre indicado**. La página la",
        "toma sola, sin tocar código.",
        "",
        "Hay dos tipos de espacio y no se resuelven igual:",
        "",
        f"- **{len(ai)} para generar** con un modelo de imagen. El prompt va en inglés a",
        "  propósito: los modelos siguen mejor un brief en inglés. Todos terminan con la",
        "  misma dirección fotográfica para que parezcan una sola sesión, y todos piden",
        "  **espacio vacío en el tercio superior**, que es donde va el titular.",
        f"- **{len(photo)} para fotografiar de verdad.** Son la gente y los activos de",
        "  CRISOSA; ninguna imagen generada los sustituye. El texto es la guía de toma.",
        "",
        "> Los diagramas del sitio —planta y corte de la nave, las naves a escala y el",
        "> mapa del corredor— **no son imágenes**: están dibujados en SVG y viven en",
        "> `assets/svg/`. Se editan en `tools/diagrams.py`, no se generan.",
        "",
        "| # | Archivo | Proporción | Página | Tipo | Estado |",
        "|---|---|---|---|---|---|",
    ]
    for i, (k, d) in enumerate(PLATES.items(), 1):
        kind = "Fotografiar" if d.get("kind") == "foto" else "Generar"
        state = "✅ puesta" if d["file"] in have else "⬜ falta"
        L.append(f"| {i} | `{d['file']}` | {d['ar'].replace('/', ':')} | "
                 f"{PLATE_PAGE.get(k, '—')} | {kind} | {state} |")
    L.append("")

    for title, group, note in (
        ("Para generar con un modelo de imagen", ai,
         "Copia el bloque completo, pégalo en ChatGPT y exporta el resultado."),
        ("Para fotografiar", photo,
         "Estas no se generan: son personas y activos reales de CRISOSA."),
    ):
        L += ["---", "", f"# {title}", "", note, ""]
        for k, d in group:
            state = "" if d["file"] not in have else "  ·  **ya puesta** (se puede reemplazar)"
            L += [
                f"## `{d['file']}` — {d['t_es']}", "",
                f"- **Proporción:** {d['ar'].replace('/', ':')}",
                f"- **Página:** {PLATE_PAGE.get(k, '—')}",
                f"- **Guardar en:** `assets/img/generated/{d['file']}`{state}",
                "", "```text", d["prompt"], "```", "",
            ]
    (ROOT / "assets" / "img" / "PROMPTS.md").write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    build()
