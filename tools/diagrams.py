#!/usr/bin/env python3
"""
CRISOSA — hand-built SVG figures.

Three drawings the site needs and no photograph can give it: a cutaway of
the warehouse, the buildings drawn to relative scale, and the corridor the
company sits in. Generated rather than hand-typed so the geometry stays
honest and a fourth building is a one-line change.

    python3 tools/diagrams.py     → assets/svg/*.svg

build.py inlines them into the pages with {{SVG:name}}.
"""
import math
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "svg"

INK   = "#0E1116"
BODY  = "#5C6673"
MUTE  = "#8B95A3"
LINE  = "#C9D4E2"
NAVY  = "#0A357F"
BLUE  = "#0F62B4"
CYAN  = "#1CA0E0"

# The buildings. Add one here and every figure below follows.
NAVES = [("Nave 1", 9000), ("Nave 2", 7500), ("Nave 3", 5500)]


def svg(w, h, body, label):
    return (f'<svg viewBox="0 0 {w} {h}" role="img" aria-label="{label}" '
            f'xmlns="http://www.w3.org/2000/svg" fill="none" '
            f'font-family="Manrope, system-ui, sans-serif">\n{body}\n</svg>\n')


# The figures are inlined into the page, so the site's data-es/data-en swap
# reaches SVG <text> too — the drawings change language with everything else.
EN = {
    "PLANTA": "PLAN",
    "CORTE A–A": "SECTION A–A",
    "Recepción": "Receiving",
    "Racking selectivo": "Selective racking",
    "Surtido y despacho": "Picking and dispatch",
    "Una sola envolvente: la carga no sale del perímetro":
        "One envelope: freight never leaves the perimeter",
    "Cajas en espera": "Trailers waiting",
    "Andén a nivel de caja": "Dock at trailer height",
    "Altura libre": "Clear height",
    "para racking en altura": "for high-bay racking",
    "Recorrido de la mercancía, de andén a andén": "The path goods take, dock to dock",
    "ESTADOS UNIDOS": "UNITED STATES",
    "MÉXICO": "MEXICO",
    "Los Ángeles": "Los Angeles",
    "Tijuana, Baja California": "Tijuana, Baja California",
    "Aeropuerto de Tijuana": "Tijuana Airport",
}
for _i in range(1, 12):
    EN[f"Nave {_i}"] = f"Building {_i}"


def txt(x, y, s, size=13, fill=BODY, anchor="start", weight=500, ls=0):
    en = EN.get(str(s))
    bi = f' data-es="{s}" data-en="{en}"' if en and en != str(s) else ""
    return (f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill}" '
            f'text-anchor="{anchor}" font-weight="{weight}" '
            f'letter-spacing="{ls}"{bi}>{s}</text>')


# ══ 1. Warehouse: plan and section ════════════════════════════════
# An isometric of racking reads as one solid mass; a drawing set does not.
# Plan on top, section below, with the section line marked on the plan.
def cutaway():
    W, H = 1200, 770
    p = []
    L, R, T, B = 150.0, 1050.0, 70.0, 330.0     # plan extents
    DOORS = [(95, 30), (140, 30), (185, 30), (230, 30), (275, 30)]

    def dim(x1, x2, y, label):
        return "".join([
            f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{MUTE}" stroke-width=".9"/>',
            f'<line x1="{x1}" y1="{y-5}" x2="{x1}" y2="{y+5}" stroke="{MUTE}" stroke-width=".9"/>',
            f'<line x1="{x2}" y1="{y-5}" x2="{x2}" y2="{y+5}" stroke="{MUTE}" stroke-width=".9"/>',
            txt((x1+x2)/2, y - 9, label, 12, BODY, "middle", 600),
        ])

    # ── PLAN ──
    p.append(txt(L, T - 26, "PLANTA", 11, MUTE, "start", 700, "1.8"))
    p.append(f'<rect x="{L}" y="{T}" width="{R-L}" height="{B-T}" fill="#EEF2F8" stroke="{NAVY}" stroke-width="2"/>')

    # dock doors cut into both end walls, with trailers waiting outside
    for i, (dy, dh) in enumerate(DOORS):
        p.append(f'<rect x="{L-4}" y="{dy}" width="8" height="{dh}" fill="{NAVY}"/>')
        p.append(f'<rect x="{R-4}" y="{dy}" width="8" height="{dh}" fill="{BLUE}"/>')
    for dy in (95, 230):
        p.append(f'<rect x="{L-96}" y="{dy}" width="88" height="30" rx="3" fill="#fff" stroke="{LINE}" stroke-width="1.4"/>')
        p.append(f'<rect x="{R+8}" y="{dy}" width="88" height="30" rx="3" fill="#fff" stroke="{LINE}" stroke-width="1.4"/>')

    # racking runs, drawn as paired lines with the aisle between them
    rows = [110, 152, 194, 236, 278]
    for y in rows:
        p.append(f'<rect x="360" y="{y}" width="500" height="9" fill="{NAVY}" fill-opacity=".55"/>')
        p.append(f'<rect x="360" y="{y+13}" width="500" height="9" fill="{NAVY}" fill-opacity=".55"/>')

    # the claim: goods enter one end, are worked, and leave the other
    p.append('<path d="M150 215 H330 V142 H886 V290 H1050" stroke="%s" stroke-width="2.6" '
             'fill="none" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#head)"/>' % CYAN)
    p.append(f'<circle cx="150" cy="215" r="4.5" fill="{CYAN}"/>')

    # zones
    for x0, x1, name in ((L, 350, "Recepción"), (360, 869, "Racking selectivo"), (880, R, "Surtido y despacho")):
        p.append(f'<line x1="{x0+4}" y1="{B+14}" x2="{x1-4}" y2="{B+14}" stroke="{LINE}" stroke-width="1.4"/>')
        p.append(txt((x0+x1)/2, B + 32, name, 12.5, BODY, "middle", 600))
    p.append(dim(L, R, B + 74, "Una sola envolvente: la carga no sale del perímetro"))

    # section line A–A
    p.append(f'<line x1="430" y1="{T-14}" x2="430" y2="{B+14}" stroke="{BLUE}" stroke-width="1.2" stroke-dasharray="7 5"/>')
    for y, dy in ((T - 14, -1), (B + 14, 1)):
        p.append(f'<path d="M424 {y+7*dy} L430 {y} L436 {y+7*dy}" stroke="{BLUE}" stroke-width="1.6" fill="none"/>')
    p.append(txt(444, T - 12, "A", 12, BLUE, "start", 700))
    p.append(txt(444, B + 28, "A", 12, BLUE, "start", 700))
    p.append(txt(L - 96, 82, "Cajas en espera", 11.5, MUTE, "start", 500))

    # ── SECTION ──
    GY, RY = 690.0, 470.0                        # ground line, roof line
    p.append(txt(L, 452 - 26, "CORTE A–A", 11, MUTE, "start", 700, "1.8"))
    p.append(f'<line x1="{L-110}" y1="{GY}" x2="{R+110}" y2="{GY}" stroke="{INK}" stroke-width="1.6"/>')
    p.append(f'<path d="M{L} {GY} V{RY} H{R} V{GY}" stroke="{NAVY}" stroke-width="2" fill="#EEF2F8"/>')

    # racking elevation: four levels, five bays
    for i in range(5):
        x0 = 372 + i * 100
        p.append(f'<line x1="{x0}" y1="{GY}" x2="{x0}" y2="{GY-140}" stroke="{NAVY}" stroke-width="1.6" opacity=".8"/>')
        p.append(f'<line x1="{x0+72}" y1="{GY}" x2="{x0+72}" y2="{GY-140}" stroke="{NAVY}" stroke-width="1.6" opacity=".8"/>')
        for lv in range(4):
            y = GY - 22 - lv * 39
            p.append(f'<rect x="{x0}" y="{y-7}" width="72" height="7" fill="{NAVY}" fill-opacity=".5"/>')
            p.append(f'<rect x="{x0+8}" y="{y-22}" width="24" height="15" fill="{BLUE}" fill-opacity=".25"/>')
            p.append(f'<rect x="{x0+40}" y="{y-22}" width="24" height="15" fill="{BLUE}" fill-opacity=".25"/>')

    # a trailer docked at the left, at dock height
    p.append(f'<rect x="{L-150}" y="{GY-86}" width="140" height="62" rx="4" fill="#fff" stroke="{LINE}" stroke-width="1.6"/>')
    p.append(f'<circle cx="{L-118}" cy="{GY-18}" r="9" fill="none" stroke="{MUTE}" stroke-width="1.6"/>')
    p.append(f'<circle cx="{L-42}" cy="{GY-18}" r="9" fill="none" stroke="{MUTE}" stroke-width="1.6"/>')
    p.append(f'<rect x="{L-6}" y="{GY-86}" width="10" height="62" fill="{NAVY}"/>')
    p.append(txt(L - 80, GY + 26, "Andén a nivel de caja", 11.5, MUTE, "middle", 500))

    # clear-height dimension
    DX = 968.0
    p.append(f'<line x1="{DX}" y1="{RY}" x2="{DX}" y2="{GY}" stroke="{MUTE}" stroke-width=".9"/>')
    p.append(f'<line x1="{DX-6}" y1="{RY}" x2="{DX+6}" y2="{RY}" stroke="{MUTE}" stroke-width=".9"/>')
    p.append(f'<line x1="{DX-6}" y1="{GY}" x2="{DX+6}" y2="{GY}" stroke="{MUTE}" stroke-width=".9"/>')
    p.append(txt(DX - 14, (RY + GY) / 2 - 4, "Altura libre", 12, BODY, "end", 600))
    p.append(txt(DX - 14, (RY + GY) / 2 + 14, "para racking en altura", 11.5, MUTE, "end", 500))

    defs = (f'<defs><marker id="head" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
            f'markerHeight="5" orient="auto-start-reverse"><path d="M0 1 L9 5 L0 9 z" fill="{CYAN}"/></marker>'
            f'<marker id="tick" viewBox="0 0 4 4" refX="2" refY="2" markerWidth="3" markerHeight="3">'
            f'<circle cx="2" cy="2" r="1.4" fill="{MUTE}"/></marker></defs>')
    legend = (f'<g><line x1="{L}" y1="738" x2="{L+34}" y2="738" stroke="{CYAN}" stroke-width="2.6" stroke-linecap="round"/>'
              + txt(L + 44, 742, "Recorrido de la mercancía, de andén a andén", 12.5, BODY, "start", 500) + "</g>")
    return svg(W, H, defs + "\n" + "\n".join(p) + "\n" + legend,
               "Planta y corte de una nave: la mercancía entra por los andenes de recepción, "
               "recorre el racking y sale por los de despacho sin dejar el perímetro")


# ══ 2. Buildings to relative scale ════════════════════════════════
# Equal depth, width proportional to area — so the drawn areas really are
# in proportion. Scaling both axes would exaggerate the largest building.
def scale():
    total = sum(a for _, a in NAVES)
    W, H, GAP = 1000.0, 210.0, 24.0
    avail = W - GAP * (len(NAVES) - 1)
    p, x = [], 0.0
    for name, area in NAVES:
        w = avail * area / total
        p.append(f'<rect x="{x:.1f}" y="0" width="{w:.1f}" height="{H}" rx="7" '
                 f'fill="{NAVY}" fill-opacity=".11" stroke="{NAVY}" stroke-opacity=".40" stroke-width="1.4"/>')
        # dock ticks along the near edge, so the block reads as a building
        n = max(2, int(w // 34))
        for i in range(n):
            tx = x + w * (i + 0.5) / n
            p.append(f'<line x1="{tx:.1f}" y1="{H}" x2="{tx:.1f}" y2="{H-9}" stroke="{NAVY}" stroke-opacity=".45" stroke-width="2"/>')
        p.append(txt(x + w / 2, H / 2 + 2, f"{area:,}", 32, NAVY, "middle", 700))
        p.append(txt(x + w / 2, H / 2 + 26, "m²", 14, BLUE, "middle", 600))
        p.append(txt(x + w / 2, H + 30, name, 13.5, BODY, "middle", 600))
        x += w + GAP
    p.append(f'<path d="M0 {H+54} v9 h{W} v-9" stroke="{LINE}" stroke-width="1.3" fill="none"/>')
    EN[f"{total:,} m² bajo techo"] = f"{total:,} m² under roof"
    p.append(txt(W / 2, H + 90, f"{total:,} m² bajo techo", 17, INK, "middle", 700))
    return svg(W, H + 110, "\n".join(p),
               "Las naves dibujadas a escala relativa: el ancho de cada bloque es "
               "proporcional a su superficie, y juntas suman la superficie total bajo techo")


# ══ 3. The corridor ═══════════════════════════════════════════════
def corridor():
    W, H = 1000.0, 520.0
    BY = 172.0                                   # the border line
    p = []
    for i, (x1, y1, x2, y2) in enumerate(
            [(90, 470, 250, 60), (300, 500, 420, 40), (620, 490, 700, 50), (820, 480, 900, 70)]):
        p.append(f'<path d="M{x1} {y1} C{x1+40} {(y1+y2)/2} {x2-40} {(y1+y2)/2} {x2} {y2}" '
                 f'stroke="{LINE}" stroke-width="1" opacity=".7"/>')

    p.append(f'<line x1="0" y1="{BY}" x2="{W}" y2="{BY}" stroke="{CYAN}" stroke-width="2" stroke-dasharray="3 7"/>')
    p.append(txt(14, BY - 14, "ESTADOS UNIDOS", 11, MUTE, "start", 700, "1.8"))
    p.append(txt(14, BY + 26, "MÉXICO", 11, MUTE, "start", 700, "1.8"))

    gates = [(360, "San Ysidro"), (620, "Otay Mesa")]
    for gx, name in gates:
        p.append(f'<rect x="{gx-15}" y="{BY-13}" width="30" height="26" rx="5" fill="#fff" stroke="{CYAN}" stroke-width="1.6"/>')
        p.append(f'<line x1="{gx}" y1="{BY-7}" x2="{gx}" y2="{BY+7}" stroke="{CYAN}" stroke-width="1.6"/>')
        p.append(txt(gx, BY - 26, name, 13, INK, "middle", 700))

    cx, cy = 470.0, 372.0
    for gx, _ in gates:
        p.append(f'<path d="M{cx} {cy} C{cx} {cy-70} {gx} {BY+90} {gx} {BY+14}" '
                 f'stroke="{BLUE}" stroke-width="2.2" stroke-linecap="round"/>')
    for gx, _ in gates:
        p.append(f'<path d="M{gx} {BY-14} L{gx} {60}" stroke="{BLUE}" stroke-width="1.6" '
                 f'stroke-dasharray="5 5" opacity=".55"/>')
    p.append(txt(360, 46, "San Diego", 13, MUTE, "middle", 600))
    p.append(txt(620, 46, "Los Ángeles", 13, MUTE, "middle", 600))

    p.append(f'<circle cx="{cx}" cy="{cy}" r="26" fill="{NAVY}" fill-opacity=".10"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="11" fill="{NAVY}"/>')
    p.append(f'<circle cx="{cx}" cy="{cy}" r="4.5" fill="#fff"/>')
    p.append(txt(cx, cy + 48, "CRISOSA", 16, INK, "middle", 800, ".6"))
    p.append(txt(cx, cy + 70, "Tijuana, Baja California", 13, BODY, "middle", 500))

    p.append(f'<path d="M{cx} {cy} C{cx+90} {cy+40} {800} {cy+30} {842} {462}" stroke="{LINE}" stroke-width="1.6"/>')
    p.append(f'<path d="M842 444 l7 18 l-7 -4 l-7 4 z M830 468 l24 0" fill="{MUTE}" stroke="{MUTE}" stroke-width="1.4" stroke-linejoin="round"/>')
    p.append(txt(842, 492, "Aeropuerto de Tijuana", 12, MUTE, "middle", 500))
    return svg(W, H, "\n".join(p),
               "Mapa esquemático: CRISOSA en Tijuana, a minutos de las garitas comerciales "
               "de Otay Mesa y San Ysidro, con las rutas hacia Estados Unidos")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in (("cutaway", cutaway), ("scale", scale), ("corridor", corridor)):
        (OUT / f"{name}.svg").write_text(fn(), encoding="utf-8")
        print(f"  assets/svg/{name}.svg  {(OUT / f'{name}.svg').stat().st_size // 1024} KB")


if __name__ == "__main__":
    main()
