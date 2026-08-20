# Imágenes del sitio

El sitio tiene **21 espacios de imagen**. Hoy faltan **13**.

Mientras un archivo no exista, su pantalla conserva la composición sobre un
degradado y muestra abajo una línea con el nombre del archivo y un botón
**«Copiar prompt»**. Para llenarla: genera o toma la imagen y guárdala en
`assets/img/generated/` **con exactamente el nombre indicado**. La página la
toma sola, sin tocar código.

Hay dos tipos de espacio y no se resuelven igual:

- **9 para generar** con un modelo de imagen. El prompt va en inglés a
  propósito: los modelos siguen mejor un brief en inglés. Todos terminan con la
  misma dirección fotográfica para que parezcan una sola sesión, y todos piden
  **espacio vacío en el tercio superior**, que es donde va el titular.
- **12 para fotografiar de verdad.** Son la gente y los activos de
  CRISOSA; ninguna imagen generada los sustituye. El texto es la guía de toma.

> Los diagramas del sitio —planta y corte de la nave, las naves a escala y el
> mapa del corredor— **no son imágenes**: están dibujados en SVG y viven en
> `assets/svg/`. Se editan en `tools/diagrams.py`, no se generan.

| # | Archivo | Proporción | Página | Tipo | Estado |
|---|---|---|---|---|---|
| 1 | `home-hero.jpg` | 16:9 | Inicio | Generar | ✅ puesta |
| 2 | `home-certs.jpg` | 16:9 | Inicio | Generar | ⬜ falta |
| 3 | `home-why.jpg` | 16:9 | Inicio | Generar | ✅ puesta |
| 4 | `home-facility.jpg` | 21:9 | Inicio | Fotografiar | ⬜ falta |
| 5 | `svc-hero.jpg` | 16:9 | Servicios | Generar | ✅ puesta |
| 6 | `svc-import.jpg` | 3:4 | Inicio | Generar | ✅ puesta |
| 7 | `svc-storage.jpg` | 3:4 | Inicio | Generar | ✅ puesta |
| 8 | `svc-shelter.jpg` | 3:4 | Inicio | Generar | ⬜ falta |
| 9 | `cert-hero.jpg` | 16:9 | Certificaciones | Generar | ⬜ falta |
| 10 | `cli-hero.jpg` | 16:9 | Clientes | Fotografiar | ⬜ falta |
| 11 | `fac-hero.jpg` | 21:9 | Instalaciones | Fotografiar | ⬜ falta |
| 12 | `fac-docks.jpg` | 16:9 | Instalaciones | Generar | ✅ puesta |
| 13 | `fac-security.jpg` | 16:9 | Instalaciones | Fotografiar | ⬜ falta |
| 14 | `abt-hero.jpg` | 16:9 | Nosotros | Fotografiar | ⬜ falta |
| 15 | `abt-truck.jpg` | 3:2 | Nosotros | Fotografiar | ✅ puesta |
| 16 | `abt-team.jpg` | 3:2 | Nosotros | Fotografiar | ✅ puesta |
| 17 | `lead-1.jpg` | 4:5 | Nosotros | Fotografiar | ⬜ falta |
| 18 | `lead-2.jpg` | 4:5 | Nosotros | Fotografiar | ⬜ falta |
| 19 | `lead-3.jpg` | 4:5 | Nosotros | Fotografiar | ⬜ falta |
| 20 | `lead-4.jpg` | 4:5 | Nosotros | Fotografiar | ⬜ falta |
| 21 | `lead-5.jpg` | 4:5 | Nosotros | Fotografiar | ⬜ falta |

---

# Para generar con un modelo de imagen

Copia el bloque completo, pégalo en ChatGPT y exporta el resultado.

## `home-hero.jpg` — Portada — el conjunto al atardecer

- **Proporción:** 16:9
- **Página:** Inicio
- **Guardar en:** `assets/img/generated/home-hero.jpg`  ·  **ya puesta** (se puede reemplazar)

```text
Aerial photograph at blue hour of a large logistics complex in Tijuana, Baja California, seen from about 300 metres and slightly angled, not straight down. Three long flat-roofed warehouses with lit loading bays, a row of white dry-van trailers backed into the docks, a wide clean concrete yard, and beyond them the lights of the border city fading into dry hills under a deep blue sky with the last warm band of sunset at the horizon. Quiet, orderly, monumental. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

## `home-certs.jpg` — Certificaciones — inspección nocturna en andén

- **Proporción:** 16:9
- **Página:** Inicio
- **Guardar en:** `assets/img/generated/home-certs.jpg`

```text
Night photograph of a single white dry-van trailer backed into a warehouse loading dock, lit from inside the building so light spills out around the trailer doors. A closed security seal is visible on the door latch. Wet concrete apron reflecting the dock lights, the rest of the frame falling into darkness. The mood is controlled and serious, like a secure facility at 3 a.m. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

## `home-why.jpg` — Por qué CRISOSA — interior de nave

- **Proporción:** 16:9
- **Página:** Inicio
- **Guardar en:** `assets/img/generated/home-why.jpg`  ·  **ya puesta** (se puede reemplazar)

```text
Wide interior photograph of a very large modern distribution warehouse, looking straight down a long central aisle that converges toward a bright far wall. Tall blue selective racking on both sides, wrapped pallets stacked evenly on every level, a spotless sealed concrete floor with crisp painted aisle lines, even LED high-bay lighting. Almost empty of people. The feeling is precision and scale. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

## `svc-hero.jpg` — Servicios — cruce comercial

- **Proporción:** 16:9
- **Página:** Servicios
- **Guardar en:** `assets/img/generated/svc-hero.jpg`  ·  **ya puesta** (se puede reemplazar)

```text
Elevated photograph of a commercial border crossing between Mexico and the United States at sunrise, looking along the truck approach lanes. Rows of dry-van trailers waiting under inspection canopies, long soft shadows, faint morning haze over the lanes, dry hills behind. Calm and cinematic rather than congested. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

## `svc-import.jpg` — Importación y Exportación — patio de contenedores

- **Proporción:** 3:4
- **Página:** Inicio
- **Guardar en:** `assets/img/generated/svc-import.jpg`  ·  **ya puesta** (se puede reemplazar)

```text
Vertical photograph of a container yard at golden hour, looking up slightly at stacks of shipping containers in muted blues and greys forming a clean geometric wall, a tractor unit small at the base for scale, warm low sun raking across the corrugated metal. Portrait orientation, three by four. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

## `svc-storage.jpg` — Almacenaje — racking selectivo

- **Proporción:** 3:4
- **Página:** Inicio
- **Guardar en:** `assets/img/generated/svc-storage.jpg`  ·  **ya puesta** (se puede reemplazar)

```text
Vertical photograph inside a warehouse, looking straight up a tall run of blue selective racking loaded with wrapped pallets, the aisle receding above, bright even LED lighting along the ceiling line. Strong vertical perspective, clean and orderly. Portrait orientation, three by four. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

## `svc-shelter.jpg` — Shelter — piso de producción

- **Proporción:** 3:4
- **Página:** Inicio
- **Guardar en:** `assets/img/generated/svc-shelter.jpg`

```text
Vertical photograph of a clean light-assembly production floor in a Mexican plant, looking down a row of workbenches with anti-static mats, component bins and task lighting. Two operators in blue smocks and safety glasses at work, seen in profile and slightly out of focus, painted floor lanes leading away. Bright, modern, organised. Portrait orientation, three by four. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

## `cert-hero.jpg` — Certificaciones — sello de seguridad

- **Proporción:** 16:9
- **Página:** Certificaciones
- **Guardar en:** `assets/img/generated/cert-hero.jpg`

```text
Close photograph of a gloved hand fitting a numbered bolt security seal to the latch of a trailer door, shot with a shallow depth of field so the seal is sharp and the ribbed trailer door falls softly out of focus behind. Cool daylight, restrained colour, the seal unbranded and unnumbered. Precision and care. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

## `fac-docks.jpg` — Instalaciones — andenes de carga

- **Proporción:** 16:9
- **Página:** Instalaciones
- **Guardar en:** `assets/img/generated/fac-docks.jpg`  ·  **ya puesta** (se puede reemplazar)

```text
Photograph along the dock face of a large warehouse: a receding row of loading bays with dock levellers and bumpers, two trailers docked and the rest of the bays open and empty, strong perspective, clean concrete apron in the foreground, overcast even light. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

---

# Para fotografiar

Estas no se generan: son personas y activos reales de CRISOSA.

## `home-facility.jpg` — Instalaciones — patio de maniobras

- **Proporción:** 21:9
- **Página:** Inicio
- **Guardar en:** `assets/img/generated/home-facility.jpg`

```text
Fotografía del patio de maniobras a ras de suelo, a última hora de la tarde, mirando a lo largo del patio para que las sombras vengan hacia la cámara. Que entre una unidad maniobrando entre dos filas de cajas estacionadas. Cámara baja, a la altura del pecho, gran angular. Encuadre 21:9 con espacio de cielo arriba. Sin gente posando y sin coches particulares en cuadro.
```

## `cli-hero.jpg` — Clientes — mercancía lista para salir

- **Proporción:** 16:9
- **Página:** Clientes
- **Guardar en:** `assets/img/generated/cli-hero.jpg`

```text
Fotografía dentro de la nave, cerca de los andenes de salida: una fila larga de tarimas emplayadas y etiquetadas, alineadas en el piso esperando carga, con los portones abiertos al fondo dejando entrar luz de día. Cámara a la altura del pecho, mirando a lo largo de la fila para que se vea la perspectiva. Etiquetas ilegibles a esa distancia. Piso barrido. Encuadre 16:9.
```

## `fac-hero.jpg` — Instalaciones — vista aérea del conjunto

- **Proporción:** 21:9
- **Página:** Instalaciones
- **Guardar en:** `assets/img/generated/fac-hero.jpg`

```text
Fotografía aérea del conjunto, con dron, a unos 120–150 metros y en ángulo inclinado (no cenital), de modo que se vean los techos, el patio de maniobras y las cajas estacionadas en fila. Volar a última hora de la tarde, con el sol bajo: las sombras largas son lo que da volumen al conjunto. Encuadre horizontal muy panorámico (21:9) con el edificio en el tercio inferior y cielo limpio arriba, que es donde va el titular. Patio despejado y ordenado antes de volar.
```

## `fac-security.jpg` — Instalaciones — control de acceso

- **Proporción:** 16:9
- **Página:** Instalaciones
- **Guardar en:** `assets/img/generated/fac-security.jpg`

```text
Fotografía del acceso vehicular al anochecer: la caseta de vigilancia encendida, la pluma abajo, la barda perimetral alejándose de la cámara y el patio al fondo en penumbra con luz cálida. Tomar en el momento en que todavía hay algo de azul en el cielo. Que no se lea ningún letrero ni placa. La idea es que se vea controlado y tranquilo, no intimidante. Encuadre 16:9.
```

## `abt-hero.jpg` — Nosotros — la nave al amanecer

- **Proporción:** 16:9
- **Página:** Nosotros
- **Guardar en:** `assets/img/generated/abt-hero.jpg`

```text
Fotografía exterior de la nave a primera hora de la mañana, desde el otro lado del patio vacío: la fachada recibiendo el primer sol cálido mientras el cielo todavía está azul frío. Una sola caja en andén, nadie en cuadro, sombras largas y quietas. Encuadre 16:9, amplio, casi de naturaleza muerta. Es el retrato del edificio, no una foto de operación.
```

## `abt-truck.jpg` — Nosotros — la unidad de reparto

- **Proporción:** 3:2
- **Página:** Nosotros
- **Guardar en:** `assets/img/generated/abt-truck.jpg`  ·  **ya puesta** (se puede reemplazar)

```text
Photograph one of the CRISOSA box trucks, three-quarter front view, with the dolphin logo and the phone number clearly readable on the side. Shoot late afternoon with the sun behind you so the white body is bright and the logo has contrast; put the truck against a plain wall or the warehouse facade, not against parked cars or a busy street. Stand about 8 metres away at chest height and leave a little empty space above the roof. Clean the unit first: this is the piece of the brand that drives around the city.
```

## `abt-team.jpg` — Nosotros — el equipo

- **Proporción:** 3:2
- **Página:** Nosotros
- **Guardar en:** `assets/img/generated/abt-team.jpg`  ·  **ya puesta** (se puede reemplazar)

```text
Group photograph of a logistics company team of about twelve people standing informally in front of an open warehouse dock door in Tijuana, Mexico. Mixed ages, business-casual clothing and hi-vis vests, relaxed natural posture and easy expressions, warm late-afternoon side light, the blue steel structure of the building behind them. Authentic and unposed rather than corporate stock. Cinematic documentary photograph, wide angle around 24mm on a full-frame camera, natural light, restrained cool colour grade with deep clean shadows and controlled highlights, calm and premium, nothing cluttered. No text, no watermarks, no third-party brand logos, no lens flare, no one looking at the camera, no heavy HDR. Photorealistic. Compose with generous empty space across the upper third so a headline can sit over it.
```

## `lead-1.jpg` — Retrato — Dirección General

- **Proporción:** 4:5
- **Página:** Nosotros
- **Guardar en:** `assets/img/generated/lead-1.jpg`

```text
Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.
```

## `lead-2.jpg` — Retrato — Dirección de Operaciones

- **Proporción:** 4:5
- **Página:** Nosotros
- **Guardar en:** `assets/img/generated/lead-2.jpg`

```text
Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.
```

## `lead-3.jpg` — Retrato — Comercio Exterior

- **Proporción:** 4:5
- **Página:** Nosotros
- **Guardar en:** `assets/img/generated/lead-3.jpg`

```text
Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.
```

## `lead-4.jpg` — Retrato — Almacén y Distribución

- **Proporción:** 4:5
- **Página:** Nosotros
- **Guardar en:** `assets/img/generated/lead-4.jpg`

```text
Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.
```

## `lead-5.jpg` — Retrato — Atención a Clientes

- **Proporción:** 4:5
- **Página:** Nosotros
- **Guardar en:** `assets/img/generated/lead-5.jpg`

```text
Retrato de medio cuerpo, vertical, proporción 4:5. Fondo liso y neutro —una pared clara de la oficina o de la nave, sin objetos detrás— o el racking desenfocado a un par de metros. Luz natural de una ventana lateral, nunca flash directo ni luz de techo encima. La persona de frente o en tres cuartos, con la mirada a la cámara, expresión relajada, hombros dentro del encuadre y espacio libre arriba de la cabeza. Vestimenta de trabajo real: camisa de la empresa, chaleco o bata según el área. Cámara a la altura de los ojos, a metro y medio. Todos los retratos con el mismo fondo, la misma luz y el mismo encuadre: es lo que hace que la fila se vea como un equipo y no como cinco fotos sueltas.
```
