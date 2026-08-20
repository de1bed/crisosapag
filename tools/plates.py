#!/usr/bin/env python3
"""
CRISOSA — photograph catalogue.

Single source of truth for every image on the site. Each entry carries
the file a slot expects, the aspect ratio it is cropped to, the short
line shown while the slot is empty, and the prompt that produces it.

The site is photograph-led, so almost every entry is a photograph
rather than a diagram: a panel is one picture, one headline and two
buttons. Prompts are written in English on purpose — image models
follow English briefs more reliably.

Paste a prompt into ChatGPT, export the result, and save it in
assets/img/generated/ under the exact `file` name. The slot picks it up
with no code change.

build.py expands {{BG:key}}, {{CARD:key}} and {{SHOT:key}} in
tools/parts/*.html and regenerates assets/img/PROMPTS.md from here.
"""

# Shared photographic direction — every prompt ends with this, so the
# whole site looks like one shoot rather than a stock-image bin.
LOOK = (
    "Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, "
    "natural light, restrained cool colour grade with deep clean shadows and controlled "
    "highlights, calm and premium, nothing cluttered. "
    "No text, no watermarks, no third-party brand logos, no lens flare, "
    "no one looking at the camera, no heavy HDR. Photorealistic. "
    "Compose with generous empty space across the upper third so a headline can sit over it."
)

PLATES = {

# ══ HOME ══════════════════════════════════════════════════════════
"home-hero": dict(
  file="home-hero.jpg", ar="16/9",
  t_es="Portada — el conjunto al atardecer",
  t_en="Cover — the site at dusk",
  prompt=(
    "Aerial photograph at blue hour of a large logistics complex in Tijuana, Baja California, "
    "seen from about 300 metres and slightly angled, not straight down. "
    "Three long flat-roofed warehouses with lit loading bays, a row of white dry-van trailers "
    "backed into the docks, a wide clean concrete yard, and beyond them the lights of the "
    "border city fading into dry hills under a deep blue sky with the last warm band of sunset "
    "at the horizon. Quiet, orderly, monumental. " + LOOK)),

"home-certs": dict(
  file="home-certs.jpg", ar="16/9",
  t_es="Certificaciones — inspección nocturna en andén",
  t_en="Certifications — night inspection at the dock",
  prompt=(
    "Night photograph of a single white dry-van trailer backed into a warehouse loading dock, "
    "lit from inside the building so light spills out around the trailer doors. "
    "A closed security seal is visible on the door latch. Wet concrete apron reflecting the "
    "dock lights, the rest of the frame falling into darkness. "
    "The mood is controlled and serious, like a secure facility at 3 a.m. " + LOOK)),

"home-why": dict(
  file="home-why.jpg", ar="16/9",
  t_es="Por qué CRISOSA — interior de nave",
  t_en="Why CRISOSA — warehouse interior",
  prompt=(
    "Wide interior photograph of a very large modern distribution warehouse, looking straight "
    "down a long central aisle that converges toward a bright far wall. "
    "Tall blue selective racking on both sides, wrapped pallets stacked evenly on every level, "
    "a spotless sealed concrete floor with crisp painted aisle lines, even LED high-bay lighting. "
    "Almost empty of people. The feeling is precision and scale. " + LOOK)),

"home-facility": dict(
  file="home-facility.jpg", ar="21/9",
  t_es="Instalaciones — patio de maniobras",
  t_en="Facilities — the maneuvering yard",
  prompt=(
    "Wide low-angle photograph across the concrete maneuvering yard of an industrial warehouse "
    "complex in late afternoon, long shadows stretching toward the camera. "
    "A tractor unit turning between two rows of parked trailers, a fenced perimeter with "
    "light masts, dry brown hills on the horizon under a pale clean sky. " + LOOK)),

# ══ SERVICIOS ═════════════════════════════════════════════════════
"svc-hero": dict(
  file="svc-hero.jpg", ar="16/9",
  t_es="Servicios — cruce comercial",
  t_en="Services — the commercial crossing",
  prompt=(
    "Elevated photograph of a commercial border crossing between Mexico and the United States "
    "at sunrise, looking along the truck approach lanes. Rows of dry-van trailers waiting under "
    "inspection canopies, long soft shadows, faint morning haze over the lanes, "
    "dry hills behind. Calm and cinematic rather than congested. " + LOOK)),

"svc-import": dict(
  file="svc-import.jpg", ar="3/4",
  t_es="Importación y Exportación — patio de contenedores",
  t_en="Import & Export — container yard",
  prompt=(
    "Vertical photograph of a container yard at golden hour, looking up slightly at stacks of "
    "shipping containers in muted blues and greys forming a clean geometric wall, "
    "a tractor unit small at the base for scale, warm low sun raking across the corrugated metal. "
    "Portrait orientation, three by four. " + LOOK)),

"svc-storage": dict(
  file="svc-storage.jpg", ar="3/4",
  t_es="Almacenaje — racking selectivo",
  t_en="Warehousing — selective racking",
  prompt=(
    "Vertical photograph inside a warehouse, looking straight up a tall run of blue selective "
    "racking loaded with wrapped pallets, the aisle receding above, bright even LED lighting "
    "along the ceiling line. Strong vertical perspective, clean and orderly. "
    "Portrait orientation, three by four. " + LOOK)),

"svc-shelter": dict(
  file="svc-shelter.jpg", ar="3/4",
  t_es="Shelter — piso de producción",
  t_en="Shelter — production floor",
  prompt=(
    "Vertical photograph of a clean light-assembly production floor in a Mexican plant, "
    "looking down a row of workbenches with anti-static mats, component bins and task lighting. "
    "Two operators in blue smocks and safety glasses at work, seen in profile and slightly out "
    "of focus, painted floor lanes leading away. Bright, modern, organised. "
    "Portrait orientation, three by four. " + LOOK)),

# ══ CERTIFICACIONES ═══════════════════════════════════════════════
"cert-hero": dict(
  file="cert-hero.jpg", ar="16/9",
  t_es="Certificaciones — sello de seguridad",
  t_en="Certifications — the security seal",
  prompt=(
    "Close photograph of a gloved hand fitting a numbered bolt security seal to the latch of a "
    "trailer door, shot with a shallow depth of field so the seal is sharp and the ribbed "
    "trailer door falls softly out of focus behind. Cool daylight, restrained colour, "
    "the seal unbranded and unnumbered. Precision and care. " + LOOK)),

# ══ CLIENTES ══════════════════════════════════════════════════════
"cli-hero": dict(
  file="cli-hero.jpg", ar="16/9",
  t_es="Clientes — mercancía lista para salir",
  t_en="Clients — freight ready to leave",
  prompt=(
    "Photograph inside a warehouse near the outbound docks: a long line of wrapped and labelled "
    "pallets staged in perfect alignment on the floor, waiting to be loaded, with open dock "
    "doors at the end of the row spilling in bright daylight. "
    "Labels blank and unreadable. Order and readiness. " + LOOK)),

# ══ INSTALACIONES ═════════════════════════════════════════════════
"fac-hero": dict(
  file="fac-hero.jpg", ar="21/9",
  t_es="Instalaciones — vista aérea del conjunto",
  t_en="Facilities — aerial view of the site",
  prompt=(
    "High aerial photograph, straight down at a slight angle, of three large flat-roofed "
    "warehouses arranged around a shared concrete yard, surrounded by a fenced perimeter, "
    "with trailers parked in neat rows. Late afternoon light, long clean shadows, "
    "dry brown terrain around the site. Almost architectural in its symmetry. " + LOOK)),

"fac-docks": dict(
  file="fac-docks.jpg", ar="16/9",
  t_es="Instalaciones — andenes de carga",
  t_en="Facilities — the loading docks",
  prompt=(
    "Photograph along the dock face of a large warehouse: a receding row of loading bays with "
    "dock levellers and bumpers, two trailers docked and the rest of the bays open and empty, "
    "strong perspective, clean concrete apron in the foreground, overcast even light. " + LOOK)),

"fac-security": dict(
  file="fac-security.jpg", ar="16/9",
  t_es="Instalaciones — control de acceso",
  t_en="Facilities — access control",
  prompt=(
    "Photograph of the vehicle entrance to a secure industrial facility at dusk: a lit guard "
    "booth beside a lowered barrier arm, a fenced perimeter running away from the camera, "
    "a camera mast overhead, the yard beyond in soft focus with warm interior light. "
    "No readable signage. Controlled and calm rather than intimidating. " + LOOK)),

# ══ NOSOTROS ══════════════════════════════════════════════════════
"abt-hero": dict(
  file="abt-hero.jpg", ar="16/9",
  t_es="Nosotros — la nave al amanecer",
  t_en="About — the building at first light",
  prompt=(
    "Exterior photograph of a large warehouse building at first light, shot from across the "
    "empty yard, the facade catching the first warm sun while the sky is still cool blue. "
    "A single trailer at a dock, no people, long quiet shadows. "
    "The composition is calm and wide, almost still-life. " + LOOK)),

"abt-team": dict(
  file="abt-team.jpg", ar="3/2",
  t_es="Nosotros — el equipo",
  t_en="About — the team",
  prompt=(
    "Group photograph of a logistics company team of about twelve people standing informally "
    "in front of an open warehouse dock door in Tijuana, Mexico. Mixed ages, business-casual "
    "clothing and hi-vis vests, relaxed natural posture and easy expressions, "
    "warm late-afternoon side light, the blue steel structure of the building behind them. "
    "Authentic and unposed rather than corporate stock. " + LOOK)),

# ══ CONTACTO ══════════════════════════════════════════════════════
"con-hero": dict(
  file="con-hero.jpg", ar="16/9",
  t_es="Contacto — Tijuana desde el aire",
  t_en="Contact — Tijuana from the air",
  prompt=(
    "Aerial photograph of the Tijuana industrial district at dusk, the grid of warehouse roofs "
    "and lit streets stretching toward the border, the lights of San Diego visible beyond, "
    "dry hills to one side, deep blue sky. Wide, quiet, cinematic. " + LOOK)),
}
