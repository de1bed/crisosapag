#!/usr/bin/env python3
"""
CRISOSA — image plate catalogue.

Single source of truth for every custom image on the site. Each entry
carries the file the page expects, the aspect ratio the layout reserves,
the caption, and the generation prompt that produces it.

Prompts are written in English on purpose: image models follow English
briefs more reliably. Paste one into ChatGPT / DALL·E / Midjourney,
export the result, and save it in assets/img/generated/ under the exact
`file` name — the plate picks it up with no code change.

build.py expands {{PLATE:key}} in tools/parts/*.html and regenerates
assets/img/PROMPTS.md from this same dictionary.
"""

BRAND = ("Strict brand palette only: navy #0A357F, corporate blue #0F62B4, "
         "cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. "
         "No other hues. Flat vector, no gradients except a single subtle cyan glow, "
         "no drop shadows, no 3D bevels, no stock-photo collage, no clip art. "
         "Thin 1.5px strokes, geometric precision, generous negative space, "
         "square corners. Any text must be short, in uppercase sans-serif, "
         "and spelled exactly as given.")

PHOTO = ("Documentary photograph, natural light, wide depth of field, "
         "cool blue-leaning color grade, no people looking at camera, "
         "no visible third-party brand logos, no text overlays, "
         "photorealistic, 35mm look.")

PLATES = {

# ══ HOME ══════════════════════════════════════════════════════════
"home-corridor": dict(
  file="home-corridor.png", ar="16/9", fig="FIG. 01",
  t_es="Mapa del corredor Tijuana–San Diego",
  t_en="Tijuana–San Diego corridor map",
  b_es="Mapa esquemático del corredor con las tres naves, las garitas de Otay Mesa y San Ysidro, y las rutas hacia distribución en EE. UU.",
  b_en="Schematic corridor map with the three warehouses, the Otay Mesa and San Ysidro ports of entry, and the routes into U.S. distribution.",
  c_es="El corredor: tres naves en Tijuana a minutos de dos garitas comerciales.",
  c_en="The corridor: three warehouses in Tijuana, minutes from two commercial ports of entry.",
  prompt=(
    "A minimal schematic map diagram of the Tijuana–San Diego cross-border corridor, "
    "viewed top-down like a transit map, not a satellite image. "
    "Show the international border as a single bright cyan dashed horizontal line "
    "running across the frame, labeled 'MEXICO' below and 'UNITED STATES' above in small uppercase type. "
    "Below the line place three small square building markers labeled 'NAVE 1', 'NAVE 2', 'NAVE 3' "
    "clustered in a zone labeled 'TIJUANA, B.C.'. "
    "Mark two border gateways crossing the line, labeled 'OTAY MESA' and 'SAN YSIDRO', "
    "each drawn as a small gate glyph. "
    "Above the line draw three thin routes fanning north to nodes labeled 'SAN DIEGO', "
    "'LOS ANGELES' and 'US DISTRIBUTION'. "
    "Add a faint dotted background grid and small corner tick marks like a technical drawing. "
    + BRAND)),

"home-stack": dict(
  file="home-stack.png", ar="4/3", fig="FIG. 02",
  t_es="Las tres capas de servicio",
  t_en="The three service layers",
  b_es="Diagrama isométrico de las tres líneas de servicio apiladas como capas de una sola cadena.",
  b_en="Isometric diagram of the three service lines stacked as layers of a single chain.",
  c_es="Importación/exportación, almacenaje y shelter operan como capas de una misma cadena.",
  c_en="Import/export, warehousing and shelter operate as layers of one chain.",
  prompt=(
    "An isometric line diagram of three stacked translucent horizontal layers, "
    "seen from a low 30-degree angle, each layer a thin outlined slab. "
    "Bottom layer labeled 'IMPORT / EXPORT' contains a tiny truck and a customs gate glyph. "
    "Middle layer labeled 'WAREHOUSING' contains tiny racking rows and pallet glyphs. "
    "Top layer labeled 'SHELTER' contains a tiny factory silhouette and worker glyphs. "
    "A single vertical cyan line pierces all three layers to show they are one continuous chain, "
    "with small connector dots where it meets each slab. "
    "Labels in small uppercase sans-serif to the right of each layer. "
    + BRAND)),

# ══ SERVICIOS ═════════════════════════════════════════════════════
"svc-scope": dict(
  file="svc-scope.png", ar="16/9", fig="FIG. 01",
  t_es="Alcance de cada servicio sobre la cadena",
  t_en="Where each service starts and ends",
  b_es="Diagrama de barras horizontales mostrando en qué tramo de la cadena interviene cada servicio.",
  b_en="Horizontal span diagram showing which stretch of the chain each service covers.",
  c_es="Los tres servicios sobre la misma línea: dónde empieza y termina cada uno.",
  c_en="The three services on one line: where each begins and ends.",
  prompt=(
    "A horizontal span diagram, like a Gantt chart stripped to its essentials. "
    "Across the top, seven evenly spaced stage labels in small uppercase: "
    "'SUPPLIER', 'PICKUP', 'CUSTOMS', 'WAREHOUSE', 'PRODUCTION', 'DISPATCH', 'CUSTOMER'. "
    "Below them three horizontal bars of different lengths, each starting and ending "
    "under different stage labels, with a small round cap at each end: "
    "bar one labeled 'IMPORT / EXPORT' spanning SUPPLIER to WAREHOUSE and again DISPATCH to CUSTOMER; "
    "bar two labeled 'WAREHOUSING' spanning CUSTOMS to DISPATCH; "
    "bar three labeled 'SHELTER' spanning PICKUP all the way to CUSTOMER. "
    "Thin vertical guide lines drop from each stage label through all bars. "
    + BRAND)),

# ══ IMPORTACIÓN / EXPORTACIÓN ═════════════════════════════════════
"imp-tree": dict(
  file="imp-tree.png", ar="16/9", fig="FIG. 01",
  t_es="Árbol de decisión: temporal o definitiva",
  t_en="Decision tree: temporary or definitive",
  b_es="Diagrama de decisión que lleva de la pregunta inicial al régimen de importación correcto.",
  b_en="Decision diagram leading from the opening question to the right import regime.",
  c_es="La mercancía elige su régimen: qué preguntas lo determinan.",
  c_en="The goods pick their regime: the questions that decide it.",
  prompt=(
    "A clean top-down decision tree diagram with square nodes and right-angled connector lines. "
    "Root node at top labeled 'GOODS ENTERING MEXICO'. "
    "First branch on the question 'WILL IT BE RE-EXPORTED?' splitting left to 'YES' and right to 'NO'. "
    "The YES path leads to a node 'TEMPORARY IMPORT' and below it a node 'IMMEX PROGRAM', "
    "then a final outcome node 'NO IMPORT TAX ON ENTRY'. "
    "The NO path leads to 'DEFINITIVE IMPORT' and a final outcome node 'DUTIES AND VAT PAID'. "
    "A second small branch from TEMPORARY IMPORT labeled 'IVA/IEPS AAA' leads to 'VAT CREDIT'. "
    "Outcome nodes drawn with a filled cyan left edge; question nodes drawn as outlined diamonds. "
    "Small uppercase sans-serif labels inside every node. "
    + BRAND)),

"imp-321": dict(
  file="imp-321.png", ar="16/9", fig="FIG. 02",
  t_es="Flujo Sección 321",
  t_en="Section 321 flow",
  b_es="Flujo horizontal de un pedido bajo Sección 321, del almacén en Tijuana al consumidor en EE. UU.",
  b_en="Horizontal flow of a Section 321 order, from the Tijuana warehouse to the U.S. consumer.",
  c_es="Sección 321: consolidar en Tijuana, entregar en EE. UU. como envío individual.",
  c_en="Section 321: consolidate in Tijuana, deliver in the U.S. as individual parcels.",
  prompt=(
    "A left-to-right horizontal process flow with five square outlined stages "
    "connected by thin arrows, drawn on a faint dotted grid. "
    "Stage 1 'E-COMMERCE ORDER' with a small cart glyph. "
    "Stage 2 'TIJUANA WAREHOUSE' with a small warehouse glyph and a stack of three small parcels. "
    "Stage 3 'CONSOLIDATED MANIFEST' with a document glyph listing three tiny lines. "
    "Stage 4 'BORDER CROSSING' drawn as a gate straddling a bright cyan vertical dashed border line. "
    "Stage 5 'US LAST MILE' with a small van glyph and a house glyph. "
    "Above stage 4 add a small callout box reading 'DE MINIMIS THRESHOLD PER PARCEL'. "
    "Below the flow, a thin timeline axis with tick marks labeled 'D+0', 'D+1', 'D+2'. "
    + BRAND)),

"imp-yard": dict(
  file="imp-yard.jpg", ar="3/2", fig="FIG. 03", existing="import-export.jpg",
  t_es="Patio de contenedores",
  t_en="Container yard",
  b_es="Fotografía del patio de maniobras con contenedores y tractocamión en operación.",
  b_en="Photograph of the yard with containers and a tractor unit in operation.",
  c_es="Patio de maniobras: consolidación y desconsolidación antes del cruce.",
  c_en="The yard: consolidation and deconsolidation before the crossing.",
  prompt=(
    "Wide documentary photograph of a cross-border logistics container yard at golden hour "
    "in Tijuana, Baja California. Rows of stacked shipping containers in muted blues and greys, "
    "a tractor unit hooking a dry van trailer in the middle ground, "
    "dry hills and industrial rooflines on the horizon. Clean, orderly, professional. "
    + PHOTO)),

# ══ ALMACENAJE ════════════════════════════════════════════════════
"wh-plan": dict(
  file="wh-plan.png", ar="16/9", fig="FIG. 01",
  t_es="Planta del almacén por zonas",
  t_en="Warehouse floor plan by zone",
  b_es="Plano cenital del almacén con las zonas de recepción, racking, surtido, empaque, devoluciones y despacho.",
  b_en="Top-down warehouse plan with receiving, racking, picking, packing, returns and dispatch zones.",
  c_es="Recorrido de la mercancía dentro de la nave, de andén a andén.",
  c_en="The path goods take inside the building, dock to dock.",
  prompt=(
    "A top-down architectural floor plan of a distribution warehouse, drawn as a thin-line "
    "technical blueprint. Rectangular building outline. On the left edge four dock doors "
    "labeled 'RECEIVING'; on the right edge four dock doors labeled 'DISPATCH'. "
    "Inside, from left to right: a hatched zone 'INBOUND STAGING', "
    "a large area of parallel racking rows drawn as repeated thin double lines labeled 'SELECTIVE RACKING', "
    "a zone 'PICKING', a zone 'PACKING', and a smaller separated zone 'RETURNS'. "
    "A single continuous cyan line traces the flow of goods through all zones, "
    "with small directional arrowheads. "
    "Add a scale bar in the lower left reading '0 10 20 30 M' and a north arrow in the upper right. "
    + BRAND)),

"wh-wms": dict(
  file="wh-wms.png", ar="16/10", fig="FIG. 02",
  t_es="Tablero de inventario",
  t_en="Inventory dashboard",
  b_es="Mockup de interfaz del tablero de inventario: existencias por SKU, ubicaciones y movimientos del día.",
  b_en="UI mockup of the inventory dashboard: stock by SKU, locations and the day's movements.",
  c_es="Visibilidad de inventario: existencias, ubicación y movimiento en un solo tablero.",
  c_en="Inventory visibility: stock, location and movement on one board.",
  prompt=(
    "A flat UI mockup of a warehouse inventory dashboard on a dark near-black navy background, "
    "shown straight-on with no perspective, no browser chrome, no mouse cursor. "
    "Top row: four KPI tiles with large numbers and small uppercase labels reading "
    "'SKUS', 'PALLET POSITIONS', 'INBOUND TODAY', 'ORDERS SHIPPED'. "
    "Left two thirds: a data table with a header row 'SKU / DESCRIPTION / LOCATION / QTY / STATUS' "
    "and six rows of monospaced placeholder data, one row highlighted with a thin cyan left edge. "
    "Right third: a simple vertical bar chart titled 'OCCUPANCY BY AISLE' with eight cyan bars of "
    "varying height, and below it a compact stacked list titled 'RECENT MOVEMENTS'. "
    "All type small, uppercase for labels, monospaced for numbers. Crisp 1px separators. "
    + BRAND)),

"wh-racks": dict(
  file="wh-racks.jpg", ar="3/2", fig="FIG. 03", existing="warehouse.jpg",
  t_es="Interior de nave",
  t_en="Warehouse interior",
  b_es="Fotografía del racking selectivo con pasillos despejados y mercancía paletizada.",
  b_en="Photograph of the selective racking with clear aisles and palletized goods.",
  c_es="Racking selectivo: acceso directo a cada posición de pallet.",
  c_en="Selective racking: direct access to every pallet position.",
  prompt=(
    "Wide documentary photograph inside a modern distribution warehouse in Mexico. "
    "Tall blue selective racking in long converging rows, wrapped pallets on every level, "
    "a clean sealed concrete floor with painted aisle markings, bright even LED high-bay lighting, "
    "a forklift small in the far background. Orderly, spacious, safety-conscious. "
    + PHOTO)),

# ══ SHELTER ═══════════════════════════════════════════════════════
"shl-split": dict(
  file="shl-split.png", ar="16/9", fig="FIG. 01",
  t_es="Reparto de responsabilidades",
  t_en="Split of responsibilities",
  b_es="Diagrama de dos columnas contrastando lo que aporta el cliente y lo que absorbe CRISOSA.",
  b_en="Two-column diagram contrasting what the client brings and what CRISOSA absorbs.",
  c_es="El cliente conserva el producto y el proceso; CRISOSA absorbe la entidad y el cumplimiento.",
  c_en="The client keeps product and process; CRISOSA absorbs entity and compliance.",
  prompt=(
    "A two-column comparison diagram divided by a single vertical line. "
    "Left column headed 'YOUR COMPANY KEEPS' listing five items each with a small square bullet: "
    "'PRODUCT DESIGN', 'PROCESS AND QUALITY', 'EQUIPMENT', 'SUPPLIER CHOICE', 'IP AND KNOW-HOW'. "
    "Right column headed 'CRISOSA ABSORBS' listing five items each with a small cyan square bullet: "
    "'LEGAL ENTITY', 'IMMEX PERMIT', 'CUSTOMS COMPLIANCE', 'PAYROLL AND HR', 'FACILITY AND LOGISTICS'. "
    "Draw a thin bracket beneath both columns joining into a single node at the bottom center "
    "labeled 'ONE OPERATING PLANT IN MEXICO'. "
    "Column headers in small uppercase sans-serif, items in slightly smaller uppercase. "
    + BRAND)),

"shl-ramp": dict(
  file="shl-ramp.png", ar="21/9", fig="FIG. 02",
  t_es="Rampa de arranque",
  t_en="Ramp-up timeline",
  b_es="Línea de tiempo horizontal del arranque de una operación shelter, semana por semana.",
  b_en="Horizontal timeline of a shelter start-up, week by week.",
  c_es="De la carta de intención a la primera exportación.",
  c_en="From letter of intent to first export.",
  prompt=(
    "A wide horizontal timeline diagram spanning the full frame. "
    "A single thin baseline axis with tick marks labeled 'WEEK 0', 'WEEK 2', 'WEEK 4', "
    "'WEEK 8', 'WEEK 12', 'WEEK 16'. "
    "Above the axis, five milestone markers drawn as small squares connected to the axis by short "
    "vertical stems, labeled in small uppercase: 'SCOPE AND LETTER OF INTENT', 'SPACE ASSIGNED', "
    "'IMMEX EXTENSION FILED', 'EQUIPMENT IMPORTED', 'FIRST PRODUCTION RUN'. "
    "Below the axis, three thin overlapping horizontal bars of different lengths labeled "
    "'PERMITS', 'HIRING AND TRAINING', 'FIT-OUT', showing that they run in parallel. "
    "The final milestone marker is filled solid cyan and labeled 'FIRST EXPORT'. "
    + BRAND)),

"shl-floor": dict(
  file="shl-floor.jpg", ar="3/2", fig="FIG. 03", existing="shelter-port.jpg",
  t_es="Piso de producción",
  t_en="Production floor",
  b_es="Fotografía de una línea de ensamble ligera operando dentro de una nave.",
  b_en="Photograph of a light assembly line running inside a plant.",
  c_es="Manufactura ligera operando bajo el permiso IMMEX de CRISOSA.",
  c_en="Light manufacturing running under CRISOSA's IMMEX permit.",
  prompt=(
    "Wide documentary photograph of a clean light-assembly production floor in a Mexican "
    "maquiladora. Rows of workbenches with anti-static mats, component bins, task lighting, "
    "operators in blue smocks and safety glasses seen from behind or in profile, "
    "painted floor lanes, an overhead conveyor line in the background. "
    "Bright, modern, well organized. "
    + PHOTO)),

# ══ NEARSHORING ═══════════════════════════════════════════════════
"near-lanes": dict(
  file="near-lanes.png", ar="16/9", fig="FIG. 01",
  t_es="Comparativa de carriles de suministro",
  t_en="Supply lane comparison",
  b_es="Comparativa esquemática entre el carril transpacífico y el carril fronterizo terrestre.",
  b_en="Schematic comparison of the transpacific lane against the overland border lane.",
  c_es="Dos rutas al mismo anaquel: distancia, tránsito y puntos de falla.",
  c_en="Two routes to the same shelf: distance, transit and failure points.",
  prompt=(
    "A comparison diagram of two supply lanes drawn as two horizontal tracks stacked vertically, "
    "each on its own thin baseline, on a faint dotted grid. "
    "Upper track labeled 'ASIA → US WEST COAST': a long line with five node markers labeled "
    "'FACTORY', 'PORT', 'OCEAN', 'PORT', 'INLAND', and a small callout box reading 'WEEKS IN TRANSIT'. "
    "Lower track labeled 'TIJUANA → US': a much shorter line with three node markers labeled "
    "'PLANT', 'BORDER', 'US DC', and a small callout box reading 'HOURS IN TRANSIT'. "
    "Draw the lower track in solid cyan and the upper track in muted navy so the length "
    "difference reads instantly. "
    "At the right edge align both tracks to a shared endpoint node labeled 'SAME SHELF'. "
    + BRAND)),

"near-crossing": dict(
  file="near-crossing.jpg", ar="21/9", fig="FIG. 02", existing="facility-aerial.jpg",
  t_es="La frontera desde el aire",
  t_en="The border from above",
  b_es="Fotografía aérea del cruce comercial y el parque industrial contiguo.",
  b_en="Aerial photograph of the commercial crossing and the industrial park beside it.",
  c_es="Otay Mesa: el cruce comercial que ordena toda la operación.",
  c_en="Otay Mesa: the commercial crossing the whole operation is arranged around.",
  prompt=(
    "High aerial photograph at dusk of a commercial border crossing between Tijuana and "
    "San Diego. Long queues of dry van trailers on the approach lanes, inspection canopies, "
    "an adjacent industrial park of flat-roofed warehouses with lit yards, "
    "dry hills beyond and the last cool blue light in the sky. Shot from around 400 meters. "
    + PHOTO)),

# ══ OPERACIÓN ═════════════════════════════════════════════════════
"ops-flow": dict(
  file="ops-flow.png", ar="21/9", fig="FIG. 01",
  t_es="Anatomía de un cruce",
  t_en="Anatomy of a crossing",
  b_es="Diagrama maestro de los siete pasos de un cruce, con el documento que gobierna cada uno.",
  b_en="Master diagram of the seven crossing steps, with the document that governs each.",
  c_es="Siete pasos, siete controles: la operación completa en una línea.",
  c_en="Seven steps, seven controls: the whole operation on one line.",
  prompt=(
    "A wide master process diagram spanning the full frame, left to right, in three horizontal registers. "
    "Middle register: seven square outlined stage nodes connected by thin arrows, numbered 01 to 07 "
    "and labeled 'PICKUP', 'CONSOLIDATION', 'DOCUMENTATION', 'BORDER CROSSING', "
    "'WAREHOUSE RECEIPT', 'FULFILLMENT', 'LAST MILE'. "
    "Node 04 straddles a bright cyan vertical dashed line running the full height of the frame, "
    "labeled 'BORDER' vertically. "
    "Upper register: for each stage a small document glyph with a short uppercase label — "
    "'PICKUP ORDER', 'PACKING LIST', 'PEDIMENTO', 'CUSTOMS RELEASE', 'RECEIPT', 'PICK LIST', 'POD'. "
    "Lower register: a thin timeline axis with tick marks and small elapsed-time labels "
    "'H+0', 'H+4', 'H+8', 'H+12', 'H+24', 'H+36', 'H+48'. "
    + BRAND)),

"ops-docs": dict(
  file="ops-docs.png", ar="4/3", fig="FIG. 02",
  t_es="El expediente",
  t_en="The document set",
  b_es="Los documentos que acompañan a la carga, dispuestos como un expediente escalonado.",
  b_en="The documents that travel with the freight, laid out as a stepped file.",
  c_es="Un cruce se detiene por papeles antes que por tráfico.",
  c_en="A crossing is stopped by paperwork long before it is stopped by traffic.",
  prompt=(
    "A flat overhead diagram of six stacked document sheets fanned in a stepped diagonal "
    "so each sheet's top edge and title strip is visible. "
    "Titles in small uppercase from back to front: 'COMMERCIAL INVOICE', 'PACKING LIST', "
    "'BILL OF LADING', 'CARTA PORTE', 'PEDIMENTO', 'CERTIFICATE OF ORIGIN'. "
    "Each sheet drawn as a thin outlined rectangle with three or four short placeholder rule lines "
    "suggesting text, and a small square field block in the upper right. "
    "The frontmost sheet 'PEDIMENTO' has a solid cyan title strip. "
    "Thin leader lines from the right edge point to two small callouts reading "
    "'ONE ERROR STOPS THE LOAD' and 'FILED BEFORE ARRIVAL'. "
    + BRAND)),

"ops-track": dict(
  file="ops-track.png", ar="16/10", fig="FIG. 03",
  t_es="Seguimiento de embarque",
  t_en="Shipment tracking",
  b_es="Mockup de la vista de seguimiento: estado del embarque, hitos y documentos asociados.",
  b_en="UI mockup of the tracking view: shipment status, milestones and attached documents.",
  c_es="El estado del embarque, legible sin llamar por teléfono.",
  c_en="Shipment status, readable without picking up the phone.",
  prompt=(
    "A flat UI mockup of a shipment tracking screen on a dark near-black navy background, "
    "straight-on, no browser chrome, no cursor. "
    "Header strip with a monospaced reference code, a status pill reading 'IN TRANSIT' in cyan, "
    "and a small uppercase label 'ETA'. "
    "Main area: a vertical milestone timeline with seven rows, each a small circular node on a "
    "vertical rule, with a bold uppercase milestone label, a monospaced timestamp, and a short "
    "secondary line. The first four nodes filled cyan (completed), the fifth node a hollow cyan ring "
    "(current), the last two hollow grey. "
    "Right side panel titled 'DOCUMENTS' listing four rows with small file glyphs. "
    "Crisp 1px separators, small uppercase labels, monospaced numerals. "
    + BRAND)),

# ══ INSTALACIONES ═════════════════════════════════════════════════
"fac-site": dict(
  file="fac-site.png", ar="16/9", fig="FIG. 01",
  t_es="Plano de conjunto",
  t_en="Site plan",
  b_es="Plano cenital del conjunto: las tres naves, patios de maniobra, andenes y control de acceso.",
  b_en="Top-down site plan: the three buildings, yards, dock doors and access control.",
  c_es="Tres naves, un solo perímetro controlado.",
  c_en="Three buildings, one controlled perimeter.",
  prompt=(
    "A top-down architectural site plan drawn as a thin-line technical blueprint. "
    "A rectangular fenced perimeter drawn as a dashed line, with one gated entrance on the "
    "lower edge labeled 'ACCESS CONTROL' next to a small guard booth square. "
    "Inside, three rectangular building footprints of different sizes labeled 'NAVE 1 — 9,000 M2', "
    "'NAVE 2 — 7,500 M2', 'NAVE 3 — 5,500 M2'. "
    "Along one long edge of each building, a row of short perpendicular ticks representing dock doors, "
    "with a small count label such as 'x8 DOCKS'. "
    "Between the buildings a hatched area labeled 'MANEUVERING YARD' with a dashed turning-circle arc. "
    "Small camera glyphs placed around the perimeter with a legend entry 'CCTV'. "
    "Scale bar reading '0 25 50 M' and a north arrow. "
    + BRAND)),

"fac-aerial": dict(
  file="fac-aerial.jpg", ar="21/9", fig="FIG. 02", existing="facility-aerial.jpg",
  t_es="Vista aérea del conjunto",
  t_en="Aerial view of the site",
  b_es="Fotografía aérea de las naves con patio de maniobras y trailers en andén.",
  b_en="Aerial photograph of the buildings with the yard and trailers at the docks.",
  c_es="El conjunto en operación, a minutos de la garita.",
  c_en="The site in operation, minutes from the port of entry.",
  prompt=(
    "Aerial photograph from around 250 meters of a modern industrial warehouse complex in "
    "Tijuana, Baja California. Three large flat-roofed buildings, a wide concrete maneuvering yard, "
    "a row of dry van trailers backed into dock doors, a fenced perimeter, "
    "dry brown hills in the distance under a clear pale sky. Late afternoon light, long soft shadows. "
    + PHOTO)),

"fac-security": dict(
  file="fac-security.png", ar="16/9", fig="FIG. 03",
  t_es="Capas de seguridad CTPAT",
  t_en="CTPAT security layers",
  b_es="Diagrama concéntrico de los controles de seguridad, del perímetro a la unidad de carga.",
  b_en="Concentric diagram of security controls, from the perimeter to the load unit.",
  c_es="La seguridad como capas, no como candado.",
  c_en="Security as layers, not as a padlock.",
  prompt=(
    "A concentric ring diagram with four nested squares rotated zero degrees, drawn as thin outlines, "
    "with a small solid cyan square at the center. "
    "From outside in, each ring labeled on its own thin leader line to the right: "
    "'PERIMETER — FENCE, LIGHTING, CCTV', 'ACCESS — ID CONTROL, VISITOR LOG', "
    "'PROCESS — SEALS, SEVEN-POINT INSPECTION', 'PARTNERS — VETTED CARRIERS'. "
    "The center square labeled 'THE LOAD'. "
    "In the lower left a small legend box headed 'CTPAT' with three short entries. "
    + BRAND)),

# ══ CERTIFICACIONES ═══════════════════════════════════════════════
"cert-matrix": dict(
  file="cert-matrix.png", ar="16/9", fig="FIG. 01",
  t_es="Qué habilita cada programa",
  t_en="What each program unlocks",
  b_es="Matriz que cruza los cuatro programas contra los beneficios operativos que habilitan.",
  b_en="Matrix crossing the four programs against the operational benefits they unlock.",
  c_es="Los programas no son sellos: cada uno abre una puerta distinta.",
  c_en="These programs are not badges: each one opens a different door.",
  prompt=(
    "A clean matrix grid diagram. Four column headers across the top in small uppercase: "
    "'IMMEX', 'IVA/IEPS AAA', 'CTPAT', 'OEA'. "
    "Six row labels down the left side: 'DUTY-FREE TEMPORARY ENTRY', 'VAT CREDIT', "
    "'FASTER VAT REFUND', 'EXTENDED STAY OF GOODS', 'PRIORITY INSPECTION LANE', "
    "'MUTUAL RECOGNITION ABROAD'. "
    "Cells filled with a small solid cyan square where the benefit applies and left empty otherwise. "
    "Thin 1px grid rules, generous cell padding. "
    "The 'OEA' column header carries a small outlined pill label reading 'IN PROGRESS'. "
    + BRAND)),

# ══ NOSOTROS ══════════════════════════════════════════════════════
"abt-team": dict(
  file="abt-team.jpg", ar="3/2", fig="FIG. 01", existing="team.jpg",
  t_es="El equipo",
  t_en="The team",
  b_es="Fotografía del equipo de CRISOSA en las instalaciones de Tijuana.",
  b_en="Photograph of the CRISOSA team at the Tijuana facility.",
  c_es="El equipo que sostiene la operación en Tijuana.",
  c_en="The team that keeps the operation running in Tijuana.",
  prompt=(
    "Documentary group photograph of a logistics company team of about twelve people "
    "standing informally in front of a warehouse dock door in Tijuana, Mexico. "
    "Mixed ages, business-casual and hi-vis vests, relaxed natural posture, "
    "warm late-afternoon side light, the building's blue steel structure behind them. "
    "Authentic and unposed rather than corporate-stock. "
    + PHOTO)),

"abt-arc": dict(
  file="abt-arc.png", ar="21/9", fig="FIG. 02",
  t_es="Treinta años en una línea",
  t_en="Thirty years on one line",
  b_es="Línea de tiempo horizontal de 1994 a hoy con los hitos de crecimiento y certificación.",
  b_en="Horizontal timeline from 1994 to today with growth and certification milestones.",
  c_es="Cada certificación llegó cuando la operación ya la exigía.",
  c_en="Every certification arrived when the operation already demanded it.",
  prompt=(
    "A wide horizontal timeline spanning the full frame on a single thin baseline. "
    "Year ticks labeled '1994', '2000', '2008', '2015', '2020', '2024', 'TODAY'. "
    "Above the line, milestone markers as small squares on short stems with short uppercase labels: "
    "'FOUNDED IN TIJUANA', 'FIRST DEDICATED WAREHOUSE', 'IMMEX PROGRAM', "
    "'THREE BUILDINGS — 22,000 M2', 'CTPAT CERTIFIED', 'IVA/IEPS AAA', 'OEA IN PROGRESS'. "
    "Below the line, a thin area band that grows in height from left to right, labeled at its "
    "right end 'CAPACITY'. The final marker is filled solid cyan. "
    + BRAND)),

# ══ CLIENTES ══════════════════════════════════════════════════════
"cli-sectors": dict(
  file="cli-sectors.png", ar="16/9", fig="FIG. 01",
  t_es="Sectores atendidos",
  t_en="Sectors served",
  b_es="Diagrama radial de los sectores industriales que cruzan carga con CRISOSA.",
  b_en="Radial diagram of the industrial sectors that move freight with CRISOSA.",
  c_es="Seis sectores con exigencias distintas sobre la misma infraestructura.",
  c_en="Six sectors with different demands on the same infrastructure.",
  prompt=(
    "A radial hub-and-spoke diagram. A small square node at the center labeled 'CRISOSA'. "
    "Six thin spokes radiating outward at even angles, each ending in an outlined square node "
    "with a small line glyph above a short uppercase label: "
    "'ELECTRONICS' with a circuit glyph, 'MEDICAL DEVICES' with a cross glyph, "
    "'APPAREL AND TEXTILES' with a garment glyph, 'FURNITURE' with a chair glyph, "
    "'METALS AND COATINGS' with a beam glyph, 'CONSUMER GOODS' with a box glyph. "
    "Each spoke carries a small tick mark near the center. "
    "Faint concentric guide circles behind the spokes. "
    + BRAND)),

# ══ CONTACTO ══════════════════════════════════════════════════════
"con-locate": dict(
  file="con-locate.png", ar="16/9", fig="FIG. 01",
  t_es="Cómo llegar",
  t_en="How to find us",
  b_es="Mapa esquemático de la ubicación en Tijuana respecto a las dos garitas comerciales.",
  b_en="Schematic map of the Tijuana location relative to the two commercial ports of entry.",
  c_es="Ubicación respecto a las garitas y al aeropuerto.",
  c_en="Location relative to the ports of entry and the airport.",
  prompt=(
    "A minimal schematic locator map, top-down, transit-map style, not satellite. "
    "A bright cyan dashed horizontal line across the upper third labeled 'BORDER'. "
    "Two gate markers on it labeled 'OTAY MESA' and 'SAN YSIDRO'. "
    "Below, a solid cyan square marker labeled 'CRISOSA' with a short leader line reading "
    "'TIJUANA, BAJA CALIFORNIA'. "
    "Two thin route lines from the CRISOSA marker to each gate, each carrying a small "
    "distance pill such as 'MIN' in uppercase. "
    "A third route to a small plane glyph labeled 'TIJUANA AIRPORT'. "
    "Three or four unlabeled thin grey road lines for context. Faint dotted grid, corner tick marks. "
    + BRAND)),
}
