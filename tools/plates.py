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

# kind="ai"   → paste the prompt into an image model
# kind="foto" → a photograph someone has to take; the text is the shooting brief
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
  file="home-facility.jpg", ar="21/9", kind="foto",
  t_es="Instalaciones — patio de maniobras",
  t_en="Facilities — the maneuvering yard",
  prompt='Fotografía del patio de maniobras a ras de suelo, a última hora de la tarde, mirando a lo largo del patio para que las sombras vengan hacia la cámara. Que entre una unidad maniobrando entre dos filas de cajas estacionadas. Cámara baja, a la altura del pecho, gran angular. Encuadre 21:9 con espacio de cielo arriba. Sin gente posando y sin coches particulares en cuadro.'),

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
  file="cli-hero.jpg", ar="16/9", kind="foto",
  t_es="Clientes — mercancía lista para salir",
  t_en="Clients — freight ready to leave",
  prompt='Fotografía dentro de la nave, cerca de los andenes de salida: una fila larga de tarimas emplayadas y etiquetadas, alineadas en el piso esperando carga, con los portones abiertos al fondo dejando entrar luz de día. Cámara a la altura del pecho, mirando a lo largo de la fila para que se vea la perspectiva. Etiquetas ilegibles a esa distancia. Piso barrido. Encuadre 16:9.'),

# ══ INSTALACIONES ═════════════════════════════════════════════════
"fac-hero": dict(
  file="fac-hero.jpg", ar="21/9", kind="foto",
  t_es="Instalaciones — vista aérea del conjunto",
  t_en="Facilities — aerial view of the site",
  prompt='Fotografía aérea del conjunto, con dron, a unos 120–150 metros y en ángulo inclinado (no cenital), de modo que se vean los techos, el patio de maniobras y las cajas estacionadas en fila. Volar a última hora de la tarde, con el sol bajo: las sombras largas son lo que da volumen al conjunto. Encuadre horizontal muy panorámico (21:9) con el edificio en el tercio inferior y cielo limpio arriba, que es donde va el titular. Patio despejado y ordenado antes de volar.'),

"fac-docks": dict(
  file="fac-docks.jpg", ar="16/9",
  t_es="Instalaciones — andenes de carga",
  t_en="Facilities — the loading docks",
  prompt=(
    "Photograph along the dock face of a large warehouse: a receding row of loading bays with "
    "dock levellers and bumpers, two trailers docked and the rest of the bays open and empty, "
    "strong perspective, clean concrete apron in the foreground, overcast even light. " + LOOK)),

"fac-security": dict(
  file="fac-security.jpg", ar="16/9", kind="foto",
  t_es="Instalaciones — control de acceso",
  t_en="Facilities — access control",
  prompt='Fotografía del acceso vehicular al anochecer: la caseta de vigilancia encendida, la pluma abajo, la barda perimetral alejándose de la cámara y el patio al fondo en penumbra con luz cálida. Tomar en el momento en que todavía hay algo de azul en el cielo. Que no se lea ningún letrero ni placa. La idea es que se vea controlado y tranquilo, no intimidante. Encuadre 16:9.'),

# ══ NOSOTROS ══════════════════════════════════════════════════════
"abt-hero": dict(
  file="abt-hero.jpg", ar="16/9", kind="foto",
  t_es="Nosotros — la nave al amanecer",
  t_en="About — the building at first light",
  prompt='Fotografía exterior de la nave a primera hora de la mañana, desde el otro lado del patio vacío: la fachada recibiendo el primer sol cálido mientras el cielo todavía está azul frío. Una sola caja en andén, nadie en cuadro, sombras largas y quietas. Encuadre 16:9, amplio, casi de naturaleza muerta. Es el retrato del edificio, no una foto de operación.'),

"abt-truck": dict(
  file="abt-truck.jpg", ar="3/2", kind="foto",
  t_es="Nosotros — la unidad de reparto",
  t_en="About — the delivery unit",
  prompt=(
    "Photograph one of the CRISOSA box trucks, three-quarter front view, with the "
    "dolphin logo and the phone number clearly readable on the side. "
    "Shoot late afternoon with the sun behind you so the white body is bright and the "
    "logo has contrast; put the truck against a plain wall or the warehouse facade, not "
    "against parked cars or a busy street. Stand about 8 metres away at chest height and "
    "leave a little empty space above the roof. Clean the unit first: this is the piece of "
    "the brand that drives around the city.")),

"abt-team": dict(
  file="abt-team.jpg", ar="3/2", kind="foto",
  t_es="Nosotros — el equipo",
  t_en="About — the team",
  prompt=(
    "Group photograph of a logistics company team of about twelve people standing informally "
    "in front of an open warehouse dock door in Tijuana, Mexico. Mixed ages, business-casual "
    "clothing and hi-vis vests, relaxed natural posture and easy expressions, "
    "warm late-afternoon side light, the blue steel structure of the building behind them. "
    "Authentic and unposed rather than corporate stock. " + LOOK)),

# ══ NOSOTROS — retratos de líderes de área ════════════════════════
"lead-1": dict(
  file="lead-1.jpg", ar="4/5", kind="foto",
  t_es="Retrato — Dirección General",
  t_en="Portrait — General Management",
  prompt='Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.'),

"lead-2": dict(
  file="lead-2.jpg", ar="4/5", kind="foto",
  t_es="Retrato — Dirección de Operaciones",
  t_en="Portrait — Operations",
  prompt='Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.'),

"lead-3": dict(
  file="lead-3.jpg", ar="4/5", kind="foto",
  t_es="Retrato — Comercio Exterior",
  t_en="Portrait — Foreign Trade",
  prompt='Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.'),

"lead-4": dict(
  file="lead-4.jpg", ar="4/5", kind="foto",
  t_es="Retrato — Almacén y Distribución",
  t_en="Portrait — Warehousing & Distribution",
  prompt='Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.'),

"lead-5": dict(
  file="lead-5.jpg", ar="4/5", kind="foto",
  t_es="Retrato — Atención a Clientes",
  t_en="Portrait — Customer Service",
  prompt='Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.'),
}
