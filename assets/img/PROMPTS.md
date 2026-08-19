# Prompts de generación de imágenes

Cada lámina del sitio tiene un espacio reservado con su proporción exacta.
Para llenarlo: copia el prompt, genéralo en ChatGPT (o el modelo que prefieras),
exporta el resultado y guárdalo en `assets/img/generated/` con **exactamente**
el nombre de archivo indicado. La página lo toma sola, sin tocar código.

Los prompts están en inglés a propósito: los modelos de imagen siguen mejor
un brief en inglés. La paleta y las restricciones de estilo ya vienen incluidas
en cada uno para que todas las piezas se vean como un mismo sistema.

| # | Archivo | Proporción | Página | Qué es |
|---|---|---|---|---|
| 1 | `home-corridor.png` | 16:9 | Inicio | Mapa del corredor Tijuana–San Diego |
| 2 | `home-stack.png` | 4:3 | Inicio | Las tres capas de servicio |
| 3 | `svc-scope.png` | 16:9 | Servicios | Alcance de cada servicio sobre la cadena |
| 4 | `imp-tree.png` | 16:9 | — | Árbol de decisión: temporal o definitiva |
| 5 | `imp-321.png` | 16:9 | — | Flujo Sección 321 |
| 6 | `imp-yard.jpg` | 3:2 | — | Patio de contenedores |
| 7 | `wh-plan.png` | 16:9 | — | Planta del almacén por zonas |
| 8 | `wh-wms.png` | 16:10 | — | Tablero de inventario |
| 9 | `wh-racks.jpg` | 3:2 | — | Interior de nave |
| 10 | `shl-split.png` | 16:9 | — | Reparto de responsabilidades |
| 11 | `shl-ramp.png` | 21:9 | — | Rampa de arranque |
| 12 | `shl-floor.jpg` | 3:2 | — | Piso de producción |
| 13 | `near-lanes.png` | 16:9 | — | Comparativa de carriles de suministro |
| 14 | `near-crossing.jpg` | 21:9 | — | La frontera desde el aire |
| 15 | `ops-flow.png` | 21:9 | — | Anatomía de un cruce |
| 16 | `ops-docs.png` | 4:3 | — | El expediente |
| 17 | `ops-track.png` | 16:10 | — | Seguimiento de embarque |
| 18 | `fac-site.png` | 16:9 | — | Plano de conjunto |
| 19 | `fac-aerial.jpg` | 21:9 | — | Vista aérea del conjunto |
| 20 | `fac-security.png` | 16:9 | — | Capas de seguridad CTPAT |
| 21 | `cert-matrix.png` | 16:9 | — | Qué habilita cada programa |
| 22 | `abt-team.jpg` | 3:2 | — | El equipo |
| 23 | `abt-arc.png` | 21:9 | — | Treinta años en una línea |
| 24 | `cli-sectors.png` | 16:9 | — | Sectores atendidos |
| 25 | `con-locate.png` | 16:9 | — | Cómo llegar |

---

## 1. `home-corridor.png` — Mapa del corredor Tijuana–San Diego

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/home-corridor.png`
- **Pie de figura:** FIG. 01 — El corredor: tres naves en Tijuana a minutos de dos garitas comerciales.

```text
A minimal schematic map diagram of the Tijuana–San Diego cross-border corridor, viewed top-down like a transit map, not a satellite image. Show the international border as a single bright cyan dashed horizontal line running across the frame, labeled 'MEXICO' below and 'UNITED STATES' above in small uppercase type. Below the line place three small square building markers labeled 'NAVE 1', 'NAVE 2', 'NAVE 3' clustered in a zone labeled 'TIJUANA, B.C.'. Mark two border gateways crossing the line, labeled 'OTAY MESA' and 'SAN YSIDRO', each drawn as a small gate glyph. Above the line draw three thin routes fanning north to nodes labeled 'SAN DIEGO', 'LOS ANGELES' and 'US DISTRIBUTION'. Add a faint dotted background grid and small corner tick marks like a technical drawing. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 2. `home-stack.png` — Las tres capas de servicio

- **Proporción:** 4:3
- **Guardar en:** `assets/img/generated/home-stack.png`
- **Pie de figura:** FIG. 02 — Importación/exportación, almacenaje y shelter operan como capas de una misma cadena.

```text
An isometric line diagram of three stacked translucent horizontal layers, seen from a low 30-degree angle, each layer a thin outlined slab. Bottom layer labeled 'IMPORT / EXPORT' contains a tiny truck and a customs gate glyph. Middle layer labeled 'WAREHOUSING' contains tiny racking rows and pallet glyphs. Top layer labeled 'SHELTER' contains a tiny factory silhouette and worker glyphs. A single vertical cyan line pierces all three layers to show they are one continuous chain, with small connector dots where it meets each slab. Labels in small uppercase sans-serif to the right of each layer. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 3. `svc-scope.png` — Alcance de cada servicio sobre la cadena

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/svc-scope.png`
- **Pie de figura:** FIG. 01 — Los tres servicios sobre la misma línea: dónde empieza y termina cada uno.

```text
A horizontal span diagram, like a Gantt chart stripped to its essentials. Across the top, seven evenly spaced stage labels in small uppercase: 'SUPPLIER', 'PICKUP', 'CUSTOMS', 'WAREHOUSE', 'PRODUCTION', 'DISPATCH', 'CUSTOMER'. Below them three horizontal bars of different lengths, each starting and ending under different stage labels, with a small round cap at each end: bar one labeled 'IMPORT / EXPORT' spanning SUPPLIER to WAREHOUSE and again DISPATCH to CUSTOMER; bar two labeled 'WAREHOUSING' spanning CUSTOMS to DISPATCH; bar three labeled 'SHELTER' spanning PICKUP all the way to CUSTOMER. Thin vertical guide lines drop from each stage label through all bars. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 4. `imp-tree.png` — Árbol de decisión: temporal o definitiva

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/imp-tree.png`
- **Pie de figura:** FIG. 01 — La mercancía elige su régimen: qué preguntas lo determinan.

```text
A clean top-down decision tree diagram with square nodes and right-angled connector lines. Root node at top labeled 'GOODS ENTERING MEXICO'. First branch on the question 'WILL IT BE RE-EXPORTED?' splitting left to 'YES' and right to 'NO'. The YES path leads to a node 'TEMPORARY IMPORT' and below it a node 'IMMEX PROGRAM', then a final outcome node 'NO IMPORT TAX ON ENTRY'. The NO path leads to 'DEFINITIVE IMPORT' and a final outcome node 'DUTIES AND VAT PAID'. A second small branch from TEMPORARY IMPORT labeled 'IVA/IEPS AAA' leads to 'VAT CREDIT'. Outcome nodes drawn with a filled cyan left edge; question nodes drawn as outlined diamonds. Small uppercase sans-serif labels inside every node. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 5. `imp-321.png` — Flujo Sección 321

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/imp-321.png`
- **Pie de figura:** FIG. 02 — Sección 321: consolidar en Tijuana, entregar en EE. UU. como envío individual.

```text
A left-to-right horizontal process flow with five square outlined stages connected by thin arrows, drawn on a faint dotted grid. Stage 1 'E-COMMERCE ORDER' with a small cart glyph. Stage 2 'TIJUANA WAREHOUSE' with a small warehouse glyph and a stack of three small parcels. Stage 3 'CONSOLIDATED MANIFEST' with a document glyph listing three tiny lines. Stage 4 'BORDER CROSSING' drawn as a gate straddling a bright cyan vertical dashed border line. Stage 5 'US LAST MILE' with a small van glyph and a house glyph. Above stage 4 add a small callout box reading 'DE MINIMIS THRESHOLD PER PARCEL'. Below the flow, a thin timeline axis with tick marks labeled 'D+0', 'D+1', 'D+2'. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 6. `imp-yard.jpg` — Patio de contenedores

- **Proporción:** 3:2
- **Guardar en:** `assets/img/generated/imp-yard.jpg`
- **Pie de figura:** FIG. 03 — Patio de maniobras: consolidación y desconsolidación antes del cruce.

```text
Wide documentary photograph of a cross-border logistics container yard at golden hour in Tijuana, Baja California. Rows of stacked shipping containers in muted blues and greys, a tractor unit hooking a dry van trailer in the middle ground, dry hills and industrial rooflines on the horizon. Clean, orderly, professional. Documentary photograph, natural light, wide depth of field, cool blue-leaning color grade, no people looking at camera, no visible third-party brand logos, no text overlays, photorealistic, 35mm look.
```

---

## 7. `wh-plan.png` — Planta del almacén por zonas

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/wh-plan.png`
- **Pie de figura:** FIG. 01 — Recorrido de la mercancía dentro de la nave, de andén a andén.

```text
A top-down architectural floor plan of a distribution warehouse, drawn as a thin-line technical blueprint. Rectangular building outline. On the left edge four dock doors labeled 'RECEIVING'; on the right edge four dock doors labeled 'DISPATCH'. Inside, from left to right: a hatched zone 'INBOUND STAGING', a large area of parallel racking rows drawn as repeated thin double lines labeled 'SELECTIVE RACKING', a zone 'PICKING', a zone 'PACKING', and a smaller separated zone 'RETURNS'. A single continuous cyan line traces the flow of goods through all zones, with small directional arrowheads. Add a scale bar in the lower left reading '0 10 20 30 M' and a north arrow in the upper right. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 8. `wh-wms.png` — Tablero de inventario

- **Proporción:** 16:10
- **Guardar en:** `assets/img/generated/wh-wms.png`
- **Pie de figura:** FIG. 02 — Visibilidad de inventario: existencias, ubicación y movimiento en un solo tablero.

```text
A flat UI mockup of a warehouse inventory dashboard on a dark near-black navy background, shown straight-on with no perspective, no browser chrome, no mouse cursor. Top row: four KPI tiles with large numbers and small uppercase labels reading 'SKUS', 'PALLET POSITIONS', 'INBOUND TODAY', 'ORDERS SHIPPED'. Left two thirds: a data table with a header row 'SKU / DESCRIPTION / LOCATION / QTY / STATUS' and six rows of monospaced placeholder data, one row highlighted with a thin cyan left edge. Right third: a simple vertical bar chart titled 'OCCUPANCY BY AISLE' with eight cyan bars of varying height, and below it a compact stacked list titled 'RECENT MOVEMENTS'. All type small, uppercase for labels, monospaced for numbers. Crisp 1px separators. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 9. `wh-racks.jpg` — Interior de nave

- **Proporción:** 3:2
- **Guardar en:** `assets/img/generated/wh-racks.jpg`
- **Pie de figura:** FIG. 03 — Racking selectivo: acceso directo a cada posición de pallet.

```text
Wide documentary photograph inside a modern distribution warehouse in Mexico. Tall blue selective racking in long converging rows, wrapped pallets on every level, a clean sealed concrete floor with painted aisle markings, bright even LED high-bay lighting, a forklift small in the far background. Orderly, spacious, safety-conscious. Documentary photograph, natural light, wide depth of field, cool blue-leaning color grade, no people looking at camera, no visible third-party brand logos, no text overlays, photorealistic, 35mm look.
```

---

## 10. `shl-split.png` — Reparto de responsabilidades

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/shl-split.png`
- **Pie de figura:** FIG. 01 — El cliente conserva el producto y el proceso; CRISOSA absorbe la entidad y el cumplimiento.

```text
A two-column comparison diagram divided by a single vertical line. Left column headed 'YOUR COMPANY KEEPS' listing five items each with a small square bullet: 'PRODUCT DESIGN', 'PROCESS AND QUALITY', 'EQUIPMENT', 'SUPPLIER CHOICE', 'IP AND KNOW-HOW'. Right column headed 'CRISOSA ABSORBS' listing five items each with a small cyan square bullet: 'LEGAL ENTITY', 'IMMEX PERMIT', 'CUSTOMS COMPLIANCE', 'PAYROLL AND HR', 'FACILITY AND LOGISTICS'. Draw a thin bracket beneath both columns joining into a single node at the bottom center labeled 'ONE OPERATING PLANT IN MEXICO'. Column headers in small uppercase sans-serif, items in slightly smaller uppercase. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 11. `shl-ramp.png` — Rampa de arranque

- **Proporción:** 21:9
- **Guardar en:** `assets/img/generated/shl-ramp.png`
- **Pie de figura:** FIG. 02 — De la carta de intención a la primera exportación.

```text
A wide horizontal timeline diagram spanning the full frame. A single thin baseline axis with tick marks labeled 'WEEK 0', 'WEEK 2', 'WEEK 4', 'WEEK 8', 'WEEK 12', 'WEEK 16'. Above the axis, five milestone markers drawn as small squares connected to the axis by short vertical stems, labeled in small uppercase: 'SCOPE AND LETTER OF INTENT', 'SPACE ASSIGNED', 'IMMEX EXTENSION FILED', 'EQUIPMENT IMPORTED', 'FIRST PRODUCTION RUN'. Below the axis, three thin overlapping horizontal bars of different lengths labeled 'PERMITS', 'HIRING AND TRAINING', 'FIT-OUT', showing that they run in parallel. The final milestone marker is filled solid cyan and labeled 'FIRST EXPORT'. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 12. `shl-floor.jpg` — Piso de producción

- **Proporción:** 3:2
- **Guardar en:** `assets/img/generated/shl-floor.jpg`
- **Pie de figura:** FIG. 03 — Manufactura ligera operando bajo el permiso IMMEX de CRISOSA.

```text
Wide documentary photograph of a clean light-assembly production floor in a Mexican maquiladora. Rows of workbenches with anti-static mats, component bins, task lighting, operators in blue smocks and safety glasses seen from behind or in profile, painted floor lanes, an overhead conveyor line in the background. Bright, modern, well organized. Documentary photograph, natural light, wide depth of field, cool blue-leaning color grade, no people looking at camera, no visible third-party brand logos, no text overlays, photorealistic, 35mm look.
```

---

## 13. `near-lanes.png` — Comparativa de carriles de suministro

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/near-lanes.png`
- **Pie de figura:** FIG. 01 — Dos rutas al mismo anaquel: distancia, tránsito y puntos de falla.

```text
A comparison diagram of two supply lanes drawn as two horizontal tracks stacked vertically, each on its own thin baseline, on a faint dotted grid. Upper track labeled 'ASIA → US WEST COAST': a long line with five node markers labeled 'FACTORY', 'PORT', 'OCEAN', 'PORT', 'INLAND', and a small callout box reading 'WEEKS IN TRANSIT'. Lower track labeled 'TIJUANA → US': a much shorter line with three node markers labeled 'PLANT', 'BORDER', 'US DC', and a small callout box reading 'HOURS IN TRANSIT'. Draw the lower track in solid cyan and the upper track in muted navy so the length difference reads instantly. At the right edge align both tracks to a shared endpoint node labeled 'SAME SHELF'. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 14. `near-crossing.jpg` — La frontera desde el aire

- **Proporción:** 21:9
- **Guardar en:** `assets/img/generated/near-crossing.jpg`
- **Pie de figura:** FIG. 02 — Otay Mesa: el cruce comercial que ordena toda la operación.

```text
High aerial photograph at dusk of a commercial border crossing between Tijuana and San Diego. Long queues of dry van trailers on the approach lanes, inspection canopies, an adjacent industrial park of flat-roofed warehouses with lit yards, dry hills beyond and the last cool blue light in the sky. Shot from around 400 meters. Documentary photograph, natural light, wide depth of field, cool blue-leaning color grade, no people looking at camera, no visible third-party brand logos, no text overlays, photorealistic, 35mm look.
```

---

## 15. `ops-flow.png` — Anatomía de un cruce

- **Proporción:** 21:9
- **Guardar en:** `assets/img/generated/ops-flow.png`
- **Pie de figura:** FIG. 01 — Siete pasos, siete controles: la operación completa en una línea.

```text
A wide master process diagram spanning the full frame, left to right, in three horizontal registers. Middle register: seven square outlined stage nodes connected by thin arrows, numbered 01 to 07 and labeled 'PICKUP', 'CONSOLIDATION', 'DOCUMENTATION', 'BORDER CROSSING', 'WAREHOUSE RECEIPT', 'FULFILLMENT', 'LAST MILE'. Node 04 straddles a bright cyan vertical dashed line running the full height of the frame, labeled 'BORDER' vertically. Upper register: for each stage a small document glyph with a short uppercase label — 'PICKUP ORDER', 'PACKING LIST', 'PEDIMENTO', 'CUSTOMS RELEASE', 'RECEIPT', 'PICK LIST', 'POD'. Lower register: a thin timeline axis with tick marks and small elapsed-time labels 'H+0', 'H+4', 'H+8', 'H+12', 'H+24', 'H+36', 'H+48'. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 16. `ops-docs.png` — El expediente

- **Proporción:** 4:3
- **Guardar en:** `assets/img/generated/ops-docs.png`
- **Pie de figura:** FIG. 02 — Un cruce se detiene por papeles antes que por tráfico.

```text
A flat overhead diagram of six stacked document sheets fanned in a stepped diagonal so each sheet's top edge and title strip is visible. Titles in small uppercase from back to front: 'COMMERCIAL INVOICE', 'PACKING LIST', 'BILL OF LADING', 'CARTA PORTE', 'PEDIMENTO', 'CERTIFICATE OF ORIGIN'. Each sheet drawn as a thin outlined rectangle with three or four short placeholder rule lines suggesting text, and a small square field block in the upper right. The frontmost sheet 'PEDIMENTO' has a solid cyan title strip. Thin leader lines from the right edge point to two small callouts reading 'ONE ERROR STOPS THE LOAD' and 'FILED BEFORE ARRIVAL'. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 17. `ops-track.png` — Seguimiento de embarque

- **Proporción:** 16:10
- **Guardar en:** `assets/img/generated/ops-track.png`
- **Pie de figura:** FIG. 03 — El estado del embarque, legible sin llamar por teléfono.

```text
A flat UI mockup of a shipment tracking screen on a dark near-black navy background, straight-on, no browser chrome, no cursor. Header strip with a monospaced reference code, a status pill reading 'IN TRANSIT' in cyan, and a small uppercase label 'ETA'. Main area: a vertical milestone timeline with seven rows, each a small circular node on a vertical rule, with a bold uppercase milestone label, a monospaced timestamp, and a short secondary line. The first four nodes filled cyan (completed), the fifth node a hollow cyan ring (current), the last two hollow grey. Right side panel titled 'DOCUMENTS' listing four rows with small file glyphs. Crisp 1px separators, small uppercase labels, monospaced numerals. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 18. `fac-site.png` — Plano de conjunto

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/fac-site.png`
- **Pie de figura:** FIG. 01 — Tres naves, un solo perímetro controlado.

```text
A top-down architectural site plan drawn as a thin-line technical blueprint. A rectangular fenced perimeter drawn as a dashed line, with one gated entrance on the lower edge labeled 'ACCESS CONTROL' next to a small guard booth square. Inside, three rectangular building footprints of different sizes labeled 'NAVE 1 — 9,000 M2', 'NAVE 2 — 7,500 M2', 'NAVE 3 — 5,500 M2'. Along one long edge of each building, a row of short perpendicular ticks representing dock doors, with a small count label such as 'x8 DOCKS'. Between the buildings a hatched area labeled 'MANEUVERING YARD' with a dashed turning-circle arc. Small camera glyphs placed around the perimeter with a legend entry 'CCTV'. Scale bar reading '0 25 50 M' and a north arrow. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 19. `fac-aerial.jpg` — Vista aérea del conjunto

- **Proporción:** 21:9
- **Guardar en:** `assets/img/generated/fac-aerial.jpg`
- **Pie de figura:** FIG. 02 — El conjunto en operación, a minutos de la garita.

```text
Aerial photograph from around 250 meters of a modern industrial warehouse complex in Tijuana, Baja California. Three large flat-roofed buildings, a wide concrete maneuvering yard, a row of dry van trailers backed into dock doors, a fenced perimeter, dry brown hills in the distance under a clear pale sky. Late afternoon light, long soft shadows. Documentary photograph, natural light, wide depth of field, cool blue-leaning color grade, no people looking at camera, no visible third-party brand logos, no text overlays, photorealistic, 35mm look.
```

---

## 20. `fac-security.png` — Capas de seguridad CTPAT

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/fac-security.png`
- **Pie de figura:** FIG. 03 — La seguridad como capas, no como candado.

```text
A concentric ring diagram with four nested squares rotated zero degrees, drawn as thin outlines, with a small solid cyan square at the center. From outside in, each ring labeled on its own thin leader line to the right: 'PERIMETER — FENCE, LIGHTING, CCTV', 'ACCESS — ID CONTROL, VISITOR LOG', 'PROCESS — SEALS, SEVEN-POINT INSPECTION', 'PARTNERS — VETTED CARRIERS'. The center square labeled 'THE LOAD'. In the lower left a small legend box headed 'CTPAT' with three short entries. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 21. `cert-matrix.png` — Qué habilita cada programa

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/cert-matrix.png`
- **Pie de figura:** FIG. 01 — Los programas no son sellos: cada uno abre una puerta distinta.

```text
A clean matrix grid diagram. Four column headers across the top in small uppercase: 'IMMEX', 'IVA/IEPS AAA', 'CTPAT', 'OEA'. Six row labels down the left side: 'DUTY-FREE TEMPORARY ENTRY', 'VAT CREDIT', 'FASTER VAT REFUND', 'EXTENDED STAY OF GOODS', 'PRIORITY INSPECTION LANE', 'MUTUAL RECOGNITION ABROAD'. Cells filled with a small solid cyan square where the benefit applies and left empty otherwise. Thin 1px grid rules, generous cell padding. The 'OEA' column header carries a small outlined pill label reading 'IN PROGRESS'. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 22. `abt-team.jpg` — El equipo

- **Proporción:** 3:2
- **Guardar en:** `assets/img/generated/abt-team.jpg`
- **Pie de figura:** FIG. 01 — El equipo que sostiene la operación en Tijuana.

```text
Documentary group photograph of a logistics company team of about twelve people standing informally in front of a warehouse dock door in Tijuana, Mexico. Mixed ages, business-casual and hi-vis vests, relaxed natural posture, warm late-afternoon side light, the building's blue steel structure behind them. Authentic and unposed rather than corporate-stock. Documentary photograph, natural light, wide depth of field, cool blue-leaning color grade, no people looking at camera, no visible third-party brand logos, no text overlays, photorealistic, 35mm look.
```

---

## 23. `abt-arc.png` — Treinta años en una línea

- **Proporción:** 21:9
- **Guardar en:** `assets/img/generated/abt-arc.png`
- **Pie de figura:** FIG. 02 — Cada certificación llegó cuando la operación ya la exigía.

```text
A wide horizontal timeline spanning the full frame on a single thin baseline. Year ticks labeled '1994', '2000', '2008', '2015', '2020', '2024', 'TODAY'. Above the line, milestone markers as small squares on short stems with short uppercase labels: 'FOUNDED IN TIJUANA', 'FIRST DEDICATED WAREHOUSE', 'IMMEX PROGRAM', 'THREE BUILDINGS — 22,000 M2', 'CTPAT CERTIFIED', 'IVA/IEPS AAA', 'OEA IN PROGRESS'. Below the line, a thin area band that grows in height from left to right, labeled at its right end 'CAPACITY'. The final marker is filled solid cyan. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 24. `cli-sectors.png` — Sectores atendidos

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/cli-sectors.png`
- **Pie de figura:** FIG. 01 — Seis sectores con exigencias distintas sobre la misma infraestructura.

```text
A radial hub-and-spoke diagram. A small square node at the center labeled 'CRISOSA'. Six thin spokes radiating outward at even angles, each ending in an outlined square node with a small line glyph above a short uppercase label: 'ELECTRONICS' with a circuit glyph, 'MEDICAL DEVICES' with a cross glyph, 'APPAREL AND TEXTILES' with a garment glyph, 'FURNITURE' with a chair glyph, 'METALS AND COATINGS' with a beam glyph, 'CONSUMER GOODS' with a box glyph. Each spoke carries a small tick mark near the center. Faint concentric guide circles behind the spokes. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```

---

## 25. `con-locate.png` — Cómo llegar

- **Proporción:** 16:9
- **Guardar en:** `assets/img/generated/con-locate.png`
- **Pie de figura:** FIG. 01 — Ubicación respecto a las garitas y al aeropuerto.

```text
A minimal schematic locator map, top-down, transit-map style, not satellite. A bright cyan dashed horizontal line across the upper third labeled 'BORDER'. Two gate markers on it labeled 'OTAY MESA' and 'SAN YSIDRO'. Below, a solid cyan square marker labeled 'CRISOSA' with a short leader line reading 'TIJUANA, BAJA CALIFORNIA'. Two thin route lines from the CRISOSA marker to each gate, each carrying a small distance pill such as 'MIN' in uppercase. A third route to a small plane glyph labeled 'TIJUANA AIRPORT'. Three or four unlabeled thin grey road lines for context. Faint dotted grid, corner tick marks. Strict brand palette only: navy #0A357F, corporate blue #0F62B4, cyan #1CA0E0, pale sky #BBDFF5, near-black navy #050C1A, paper white #F5F8FC. No other hues. Flat vector, no gradients except a single subtle cyan glow, no drop shadows, no 3D bevels, no stock-photo collage, no clip art. Thin 1.5px strokes, geometric precision, generous negative space, square corners. Any text must be short, in uppercase sans-serif, and spelled exactly as given.
```
