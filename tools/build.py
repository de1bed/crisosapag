#!/usr/bin/env python3
"""
CRISOSA Logistic Solutions — static site builder.

The site ships as plain HTML: no server, no runtime, no npm. This script
only exists so the shared shell (header, mega-menu, footer, pager) stays
identical across the twelve routes. It reads the per-page body from
tools/parts/<slug>.html and writes <route>/index.html.

    python3 tools/build.py

Editing copy: you can edit the generated HTML directly — it is normal,
readable HTML. Re-running the build regenerates the shell only if you
also update tools/parts/, so keep body edits in tools/parts/.
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PARTS = ROOT / "tools" / "parts"
sys.path.insert(0, str(ROOT / "tools"))
from plates import PLATES  # noqa: E402

# ── Site map ────────────────────────────────────────────────────────
# slug, directory, ES title, EN title, ES nav label, EN nav label,
# ES menu blurb, EN menu blurb
PAGES = [
    ("home", "", "Inicio", "Home",
     "Inicio", "Home",
     "Treinta años cruzando, almacenando y despachando carga en la frontera.",
     "Thirty years crossing, storing and clearing freight at the border."),
    ("servicios", "servicios", "Servicios", "Services",
     "Servicios", "Services",
     "Las tres líneas de servicio y cuál corresponde a tu operación.",
     "The three service lines and which one fits your operation."),
    ("importacion-exportacion", "importacion-exportacion",
     "Importación y Exportación", "Import & Export",
     "Importación y Exportación", "Import & Export",
     "Importación temporal y definitiva, exportación y Sección 321.",
     "Temporary and definitive import, export and Section 321."),
    ("almacenaje", "almacenaje", "Almacenaje", "Warehousing",
     "Almacenaje", "Warehousing",
     "22,000 m² en tres naves: recepción, inventario, surtido y devoluciones.",
     "22,000 m² across three buildings: receiving, inventory, fulfillment, returns."),
    ("shelter", "shelter", "Shelter", "Shelter",
     "Shelter", "Shelter",
     "Manufactura en México sin constituir la entidad legal primero.",
     "Manufacture in Mexico without incorporating an entity first."),
    ("nearshoring", "nearshoring", "Nearshoring", "Nearshoring",
     "Nearshoring", "Nearshoring",
     "Por qué Tijuana: el corredor con más cruces comerciales del mundo.",
     "Why Tijuana: the busiest commercial crossing corridor in the world."),
    ("operacion", "operacion", "Operación", "Operations",
     "Operación", "Operations",
     "Los siete pasos de un cruce, del pickup a la última milla.",
     "The seven steps of a crossing, from pickup to last mile."),
    ("instalaciones", "instalaciones", "Instalaciones", "Facilities",
     "Instalaciones", "Facilities",
     "Naves, andenes, racking y seguridad certificada CTPAT.",
     "Buildings, dock doors, racking and CTPAT-certified security."),
    ("certificaciones", "certificaciones", "Certificaciones", "Certifications",
     "Certificaciones", "Certifications",
     "IMMEX, IVA/IEPS AAA, CTPAT y OEA — qué habilita cada una.",
     "IMMEX, IVA/IEPS AAA, CTPAT and OEA — what each one unlocks."),
    ("nosotros", "nosotros", "Nosotros", "About us",
     "Nosotros", "About us",
     "De 1994 a hoy: la historia, el equipo y la forma de trabajar.",
     "From 1994 to today: the history, the team and how we work."),
    ("clientes", "clientes", "Clientes", "Clients",
     "Clientes", "Clients",
     "Las empresas que mueven su carga con CRISOSA.",
     "The companies that move their freight with CRISOSA."),
    ("contacto", "contacto", "Contacto", "Contact",
     "Contacto", "Contact",
     "Cuéntanos qué necesitas mover, guardar o fabricar en México.",
     "Tell us what you need to move, store or manufacture in Mexico."),
]

# Condensed header navigation — the mega-menu carries the full index.
HEADER_NAV = ["servicios", "nearshoring", "operacion", "instalaciones", "nosotros"]

# ── Per-page metadata: <title> and meta description, both languages ──
META = {
 "home": (
  "CRISOSA Logistic Solutions — Logística transfronteriza en Tijuana",
  "CRISOSA Logistic Solutions — Cross-border logistics in Tijuana",
  "Importación, exportación, almacenaje y shelter en la frontera México–EE. UU. "
  "Empresa certificada IVA/IEPS AAA, CTPAT e IMMEX. Tijuana, B.C. desde 1994.",
  "Import, export, warehousing and shelter services on the U.S.–Mexico border. "
  "IVA/IEPS AAA, CTPAT and IMMEX certified. Tijuana, B.C. since 1994."),
 "servicios": (
  "Servicios — CRISOSA Logistic Solutions",
  "Services — CRISOSA Logistic Solutions",
  "Tres líneas de servicio sobre una sola cadena: importación/exportación, "
  "almacenaje y shelter. Compara alcances y elige la que corresponde a tu operación.",
  "Three service lines on one supply chain: import/export, warehousing and shelter. "
  "Compare scopes and pick the one that fits your operation."),
 "importacion-exportacion": (
  "Importación y Exportación — CRISOSA Logistic Solutions",
  "Import & Export — CRISOSA Logistic Solutions",
  "Importación temporal bajo IMMEX, importación definitiva, exportación a EE. UU. "
  "y envíos bajo Sección 321 con cumplimiento aduanero completo.",
  "Temporary import under IMMEX, definitive import, export to the U.S. and "
  "Section 321 shipments with full customs compliance."),
 "almacenaje": (
  "Almacenaje — CRISOSA Logistic Solutions",
  "Warehousing — CRISOSA Logistic Solutions",
  "22,000 m² de almacenaje en tres naves en Tijuana: recepción, control de "
  "inventario, surtido de pedidos y manejo de devoluciones.",
  "22,000 m² of warehouse space across three buildings in Tijuana: receiving, "
  "inventory control, order fulfillment and returns handling."),
 "shelter": (
  "Shelter — CRISOSA Logistic Solutions",
  "Shelter — CRISOSA Logistic Solutions",
  "Establece manufactura en México bajo el programa de maquiladora sin constituir "
  "una entidad legal: infraestructura, logística y cumplimiento normativo.",
  "Set up manufacturing in Mexico under the maquiladora program without "
  "incorporating an entity: infrastructure, logistics and compliance."),
 "nearshoring": (
  "Nearshoring — CRISOSA Logistic Solutions",
  "Nearshoring — CRISOSA Logistic Solutions",
  "Por qué Tijuana–San Diego es el corredor de nearshoring más eficiente de "
  "Norteamérica y cómo entrar a él sin construir la operación desde cero.",
  "Why Tijuana–San Diego is North America's most efficient nearshoring corridor "
  "and how to enter it without building the operation from scratch."),
 "operacion": (
  "Operación — CRISOSA Logistic Solutions",
  "Operations — CRISOSA Logistic Solutions",
  "Los siete pasos de un cruce transfronterizo, del pickup en origen a la entrega "
  "de última milla, con los documentos y controles de cada etapa.",
  "The seven steps of a cross-border crossing, from origin pickup to last-mile "
  "delivery, with the documents and controls at every stage."),
 "instalaciones": (
  "Instalaciones — CRISOSA Logistic Solutions",
  "Facilities — CRISOSA Logistic Solutions",
  "Tres naves en Tijuana, B.C. con 22,000 m², andenes de carga, racking selectivo "
  "y seguridad bajo estándar CTPAT.",
  "Three buildings in Tijuana, B.C. with 22,000 m², loading docks, selective "
  "racking and CTPAT-standard security."),
 "certificaciones": (
  "Certificaciones — CRISOSA Logistic Solutions",
  "Certifications — CRISOSA Logistic Solutions",
  "IMMEX, IVA/IEPS AAA, CTPAT y OEA: qué es cada programa, qué habilita y cómo "
  "se traduce en tiempo y costo para tu carga.",
  "IMMEX, IVA/IEPS AAA, CTPAT and OEA: what each program is, what it unlocks and "
  "how it translates into time and cost for your freight."),
 "nosotros": (
  "Nosotros — CRISOSA Logistic Solutions",
  "About us — CRISOSA Logistic Solutions",
  "Fundada en 1994 en Tijuana, B.C. Treinta años adaptando la operación a las "
  "necesidades de fabricantes de ambos lados de la frontera.",
  "Founded in 1994 in Tijuana, B.C. Thirty years adapting operations to the needs "
  "of manufacturers on both sides of the border."),
 "clientes": (
  "Clientes — CRISOSA Logistic Solutions",
  "Clients — CRISOSA Logistic Solutions",
  "Hisense, Steelcase, Cardinal Health, Hanes, Enovis y más empresas que confían "
  "su carga transfronteriza a CRISOSA.",
  "Hisense, Steelcase, Cardinal Health, Hanes, Enovis and more companies that "
  "trust CRISOSA with their cross-border freight."),
 "contacto": (
  "Contacto — CRISOSA Logistic Solutions",
  "Contact — CRISOSA Logistic Solutions",
  "Escríbenos o llámanos en México y Estados Unidos. Respondemos con una "
  "propuesta concreta para tu operación.",
  "Write or call us in Mexico and the United States. We reply with a concrete "
  "proposal for your operation."),
}


# ── Shell ───────────────────────────────────────────────────────────
SHELL = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title_es}</title>
<meta name="description" content="{desc_es}">
<meta name="theme-color" content="#050C1A">
<meta name="author" content="CRISOSA Logistic Solutions">
<link rel="icon" href="{b}assets/logos/crisosa.png">
<meta property="og:site_name" content="CRISOSA Logistic Solutions">
<meta property="og:title" content="{title_es}">
<meta property="og:description" content="{desc_es}">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_MX">
<meta property="og:locale:alternate" content="en_US">
<link rel="stylesheet" href="{b}assets/css/styles.css">
</head>
<body
  data-es-doctitle="{title_es}" data-en-doctitle="{title_en}"
  data-es-docdesc="{desc_es}" data-en-docdesc="{desc_en}">

<a class="skip" href="#main" data-es="Ir al contenido" data-en="Skip to content">Ir al contenido</a>

{header}
{mega}

<main id="main">
{body}
{pager}
</main>

{footer}

<script src="{b}assets/js/main.js"></script>
</body>
</html>
"""


def header(b, home, slug):
    links = []
    for s in HEADER_NAV:
        p = next(x for x in PAGES if x[0] == s)
        cur = ' aria-current="page"' if s == slug else ""
        links.append(
            f'      <a href="{b}{p[1]}/"{cur} data-es="{p[4]}" data-en="{p[5]}">{p[4]}</a>'
        )
    nav = "\n".join(links)
    return f"""<header class="hdr" id="hdr">
  <div class="wrap wrap--w hdr__in">
    <a class="hdr__logo" href="{home}" aria-label="CRISOSA Logistic Solutions — inicio">
      <img src="{b}assets/logos/crisosa-white.png" alt="CRISOSA Logistic Solutions" width="150" height="30">
    </a>
    <nav class="hdr__nav" aria-label="Principal">
{nav}
    </nav>
    <div class="hdr__tools">
      <div class="lang" role="group" aria-label="Idioma / Language">
        <button type="button" data-lang="es" class="is-on">ES</button><span aria-hidden="true">/</span><button type="button" data-lang="en">EN</button>
      </div>
      <button class="mtrig" id="mtrig" type="button" aria-expanded="false" aria-controls="mega">
        <span class="mtrig__ico" aria-hidden="true"><i></i><i></i><i></i></span>
        <span data-es="Índice" data-en="Index">Índice</span>
      </button>
    </div>
  </div>
</header>"""


def mega(b, home):
    rows = []
    for i, p in enumerate(PAGES, start=1):
        href = home if p[1] == "" else f"{b}{p[1]}/"
        rows.append(f"""      <a class="mega__item" href="{href}">
        <span class="mega__i">{i:02d}</span>
        <span class="mega__t" data-es="{p[2]}" data-en="{p[3]}">{p[2]}</span>
        <span class="mega__d" data-es="{p[6]}" data-en="{p[7]}">{p[6]}</span>
      </a>""")
    items = "\n".join(rows)
    return f"""<div class="mega" id="mega" role="dialog" aria-modal="true" aria-hidden="true" aria-label="Índice del sitio">
  <div class="wrap wrap--w">
    <div class="mega__grid">
{items}
    </div>
    <div class="mega__foot">
      <span>MX <a href="tel:+526646072000">+52 (664) 607-20-00</a></span>
      <span>US <a href="tel:+16192702229">+1 (619) 270-22-29</a></span>
      <span>Tijuana, Baja California, México</span>
      <span data-es="Siempre superando expectativas" data-en="Always exceeding expectations">Siempre superando expectativas</span>
    </div>
  </div>
</div>"""


def footer(b, home):
    def li(slug):
        p = next(x for x in PAGES if x[0] == slug)
        href = home if p[1] == "" else f"{b}{p[1]}/"
        return f'        <li><a href="{href}" data-es="{p[2]}" data-en="{p[3]}">{p[2]}</a></li>'

    servicios = "\n".join(li(s) for s in
                          ["servicios", "importacion-exportacion", "almacenaje", "shelter"])
    compania = "\n".join(li(s) for s in
                         ["nosotros", "nearshoring", "operacion", "instalaciones",
                          "certificaciones", "clientes"])
    return f"""<footer class="ftr">
  <div class="wrap wrap--w">
    <div class="ftr__in">
      <div>
        <img class="ftr__logo" src="{b}assets/logos/crisosa-white.png" alt="CRISOSA Logistic Solutions" width="170" height="34">
        <p class="ftr__tag" data-es="Logística · Almacenaje · Seguridad · Empaque" data-en="Logistics · Warehousing · Security · Packaging">Logística · Almacenaje · Seguridad · Empaque</p>
        <p class="ftr__tag" data-es="Empresa certificada IVA/IEPS AAA · CTPAT · IMMEX" data-en="Certified company IVA/IEPS AAA · CTPAT · IMMEX">Empresa certificada IVA/IEPS AAA · CTPAT · IMMEX</p>
      </div>
      <div class="ftr__col">
        <h4 data-es="Servicios" data-en="Services">Servicios</h4>
        <ul>
{servicios}
        </ul>
      </div>
      <div class="ftr__col">
        <h4 data-es="Compañía" data-en="Company">Compañía</h4>
        <ul>
{compania}
        </ul>
      </div>
      <div class="ftr__col">
        <h4 data-es="Contacto" data-en="Contact">Contacto</h4>
        <ul>
          <li><a href="tel:+526646072000">MX +52 (664) 607-20-00</a></li>
          <li><a href="tel:+16192702229">US +1 (619) 270-22-29</a></li>
          <li><a href="mailto:info@crisosa.com">info@crisosa.com</a></li>
          <li><span>Tijuana, Baja California, México</span></li>
          <li><a href="{b}contacto/" data-es="Escríbenos" data-en="Write to us">Escríbenos</a></li>
        </ul>
      </div>
    </div>
    <div class="ftr__bar">
      <span>© <span id="yr">2026</span> CRISOSA Logistic Solutions. <span data-es="Todos los derechos reservados." data-en="All rights reserved.">Todos los derechos reservados.</span></span>
      <span data-es="Siempre superando expectativas" data-en="Always exceeding expectations">Siempre superando expectativas</span>
    </div>
  </div>
</footer>"""


def pager(b, home, i):
    """Previous / next across the site map — the routes read as a document."""
    if i == 0:
        return ""
    prev_p = PAGES[i - 1]
    next_p = PAGES[i + 1] if i + 1 < len(PAGES) else PAGES[0]
    ph = home if prev_p[1] == "" else f"{b}{prev_p[1]}/"
    nh = home if next_p[1] == "" else f"{b}{next_p[1]}/"
    return f"""
<nav class="pager" aria-label="Páginas">
  <a href="{ph}">
    <span class="pager__k" data-es="← Anterior" data-en="← Previous">← Anterior</span>
    <span class="pager__t" data-es="{prev_p[2]}" data-en="{prev_p[3]}">{prev_p[2]}</span>
  </a>
  <a href="{nh}">
    <span class="pager__k" data-es="Siguiente →" data-en="Next →">Siguiente →</span>
    <span class="pager__t" data-es="{next_p[2]}" data-en="{next_p[3]}">{next_p[2]}</span>
  </a>
</nav>"""


PLATE_PAGE = {}
PLATE_RE = re.compile(r"\{\{PLATE:([a-z0-9\-]+)(\|[a-z|]+)?\}\}")


def plate(key, b, mods=""):
    """Render one image plate. Missing files fall back to the blueprint state."""
    d = PLATES[key]
    src = f"{b}assets/img/generated/{d['file']}"
    cls = "plate reveal"
    if "contain" in mods:
        cls += " plate--contain"
    ar = d["ar"]
    ratio = ar.replace("/", ":")
    return f"""<figure class="{cls}" style="--ar:{ar}" data-prompt="{html.escape(d['prompt'], quote=True)}">
  <div class="plate__box">
    <img src="{src}" decoding="async" alt="{html.escape(d['t_es'], quote=True)}"
         data-es-alt="{html.escape(d['t_es'], quote=True)}" data-en-alt="{html.escape(d['t_en'], quote=True)}">
    <div class="plate__ph">
      <span class="plate__id">IMG · {d['file']} · {ratio}</span>
      <div>
        <p class="plate__brief">
          <b data-es="{html.escape(d['t_es'], quote=True)}" data-en="{html.escape(d['t_en'], quote=True)}">{d['t_es']}</b>
          <span data-es="{html.escape(d['b_es'], quote=True)}" data-en="{html.escape(d['b_en'], quote=True)}">{d['b_es']}</span>
        </p>
        <button type="button" class="plate__act" data-es="Copiar prompt" data-en="Copy prompt">Copiar prompt</button>
      </div>
    </div>
  </div>
  <figcaption class="plate__cap">
    <b>{d['fig']}</b>
    <span data-es="{html.escape(d['c_es'], quote=True)}" data-en="{html.escape(d['c_en'], quote=True)}">{d['c_es']}</span>
  </figcaption>
</figure>"""


def expand_plates(body, b, page=""):
    def sub(m):
        PLATE_PAGE.setdefault(m.group(1), page)
        return plate(m.group(1), b, (m.group(2) or ""))
    return PLATE_RE.sub(sub, body)


def write_prompts_doc():
    """Regenerate assets/img/PROMPTS.md from the plate catalogue."""
    lines = [
        "# Prompts de generación de imágenes",
        "",
        "Cada lámina del sitio tiene un espacio reservado con su proporción exacta.",
        "Para llenarlo: copia el prompt, genéralo en ChatGPT (o el modelo que prefieras),",
        "exporta el resultado y guárdalo en `assets/img/generated/` con **exactamente**",
        "el nombre de archivo indicado. La página lo toma sola, sin tocar código.",
        "",
        "Los prompts están en inglés a propósito: los modelos de imagen siguen mejor",
        "un brief en inglés. La paleta y las restricciones de estilo ya vienen incluidas",
        "en cada uno para que todas las piezas se vean como un mismo sistema.",
        "",
        "| # | Archivo | Proporción | Página | Qué es |",
        "|---|---|---|---|---|",
    ]
    for i, (k, d) in enumerate(PLATES.items(), 1):
        lines.append(f"| {i} | `{d['file']}` | {d['ar'].replace('/', ':')} | {PLATE_PAGE.get(k, '—')} | {d['t_es']} |")
    lines.append("")
    for i, (k, d) in enumerate(PLATES.items(), 1):
        lines += [
            "---",
            "",
            f"## {i}. `{d['file']}` — {d['t_es']}",
            "",
            f"- **Proporción:** {d['ar'].replace('/', ':')}",
            f"- **Guardar en:** `assets/img/generated/{d['file']}`",
            f"- **Pie de figura:** {d['fig']} — {d['c_es']}",
            "",
            "```text",
            d["prompt"],
            "```",
            "",
        ]
    (ROOT / "assets" / "img" / "PROMPTS.md").write_text("\n".join(lines), encoding="utf-8")


def build():
    written = []
    for i, p in enumerate(PAGES):
        slug, d = p[0], p[1]
        b = "" if d == "" else "../"
        home = "index.html" if d == "" else "../"
        body = (PARTS / f"{slug}.html").read_text(encoding="utf-8")
        body = expand_plates(body, b, p[2])
        body = body.replace("{b}", b).replace("{home}", home)
        t_es, t_en, d_es, d_en = META[slug]
        page = SHELL.format(
            b=b, title_es=html.escape(t_es, quote=True), title_en=html.escape(t_en, quote=True),
            desc_es=html.escape(d_es, quote=True), desc_en=html.escape(d_en, quote=True),
            header=header(b, home, slug), mega=mega(b, home), footer=footer(b, home),
            pager=pager(b, home, i), body=body.rstrip(),
        )
        out = ROOT / (d if d else ".") / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        written.append(str(out.relative_to(ROOT)))

    # 404 reuses the shell with an inline body
    nf = PARTS / "404.html"
    if nf.exists():
        body = expand_plates(nf.read_text(encoding="utf-8"), "/")
        body = body.replace("{b}", "/").replace("{home}", "/")
        page = SHELL.format(
            b="/", title_es="Página no encontrada — CRISOSA", title_en="Page not found — CRISOSA",
            desc_es="La página que buscas no existe.", desc_en="The page you are looking for does not exist.",
            header=header("/", "/", ""), mega=mega("/", "/"), footer=footer("/", "/"),
            pager="", body=body.rstrip(),
        )
        (ROOT / "404.html").write_text(page, encoding="utf-8")
        written.append("404.html")

    write_prompts_doc()
    written.append("assets/img/PROMPTS.md")

    print("\n".join(written))
    print(f"\n{len(written)} files written.")


if __name__ == "__main__":
    build()
