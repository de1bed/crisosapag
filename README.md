# CRISOSA Logistic Solutions — sitio web

Sitio corporativo de **CRISOSA Logistic Solutions** (Tijuana, B.C.). HTML, CSS y
JavaScript estáticos: sin dependencias, sin proceso de build para servirlo, sin
servidor de aplicación. Se sube tal cual a cualquier hosting.

---

## Rutas

El sitio son doce páginas reales, cada una con su propia URL, título y descripción.
No es una sola página con scroll infinito.

| # | Ruta | Qué contiene |
|---|---|---|
| 01 | `/` | Portada: corredor, tres servicios, operación, certificaciones, clientes |
| 02 | `/servicios/` | Comparativa de las tres líneas + selector «¿cuál te corresponde?» |
| 03 | `/importacion-exportacion/` | Regímenes temporal/definitivo, Sección 321, alcance |
| 04 | `/almacenaje/` | Flujo interno, seis operaciones, capacidad por nave, visibilidad |
| 05 | `/shelter/` | Reparto de responsabilidades, rampa de arranque, riesgo, salida |
| 06 | `/nearshoring/` | Comparativa de carriles, por qué Tijuana, cómo entrar, límites |
| 07 | `/operacion/` | Los siete pasos de un cruce (interactivo), expediente, seguimiento |
| 08 | `/instalaciones/` | Plano de conjunto, capacidades, seguridad CTPAT |
| 09 | `/certificaciones/` | IMMEX, IVA/IEPS AAA, CTPAT, OEA — qué habilita cada uno |
| 10 | `/nosotros/` | Historia, forma de trabajar, dirección general |
| 11 | `/clientes/` | Socios comerciales y sectores atendidos |
| 12 | `/contacto/` | Formulario, datos directos, ubicación |

`404.html` cubre las rutas que no existen. Los enlaces internos son relativos,
así que el sitio funciona igual en la raíz de un dominio o en un subdirectorio.

---

## Espacios de imagen y sus prompts

Cada figura del sitio es un **espacio reservado con proporción exacta**. Mientras
el archivo no exista, el espacio se dibuja como una lámina técnica que muestra qué
imagen va ahí y trae un botón **«Copiar prompt»**.

Para llenar un espacio:

1. Abre la página, pulsa **Copiar prompt** en la lámina que quieras.
2. Pégalo en ChatGPT (o el modelo de imagen que uses) y genera la imagen.
3. Guarda el resultado en `assets/img/generated/` **con el nombre exacto** que
   muestra la lámina (por ejemplo `ops-flow.png`).
4. Recarga. La imagen aparece sola: no hay que tocar código.

El catálogo completo —25 láminas con su proporción, su nombre de archivo y su
prompt— está en **[`assets/img/PROMPTS.md`](assets/img/PROMPTS.md)**, generado
desde `tools/plates.py`.

Los prompts están escritos en inglés a propósito: los modelos de imagen siguen
mejor un brief en inglés. Cada uno ya trae dentro la paleta y las restricciones de
estilo, para que todas las piezas se vean como un mismo sistema y no como
ilustraciones sueltas.

Seis láminas ya vienen llenas con las fotografías extraídas de la presentación
original. Pueden reemplazarse con material propio usando el mismo nombre de archivo.

---

## Diseño

El sistema se llama **«Manifiesto»**: un manifiesto aduanal tratado como producto
de software.

- **Color.** Paleta corporativa —navy `#0A357F`, azul `#0F62B4`, cian `#1CA0E0`—
  sobre dos fondos: papel frío `#F5F8FC` para lectura y navy casi negro `#050C1A`
  para las bandas. Los grises están sesgados a azul, no son neutros de fábrica.
- **Tipografía.** `Archivo` variable (se usa su eje de anchura: titulares
  expandidos, acentos condensados) e `IBM Plex Mono` para etiquetas, cifras y
  códigos. Ambas **auto-alojadas** en `assets/fonts/`: el sitio no hace ninguna
  petición a terceros.
- **Estructura.** Cada sección es un *registro numerado* sobre una regla capilar.
  Los datos se leen como readouts monoespaciados. Las figuras van numeradas
  `FIG. n` porque el orden es información, no adorno.

### Navegación

- **Índice completo** en un overlay a pantalla completa (botón `Índice`), con las
  doce rutas numeradas y descritas. Se cierra con `Esc`.
- **Barra lateral** en las páginas largas, con seguimiento de la sección activa.
- **Paginador** anterior/siguiente al pie: el sitio se puede leer en orden, como
  un documento.

### Elementos dinámicos

| Dónde | Qué hace |
|---|---|
| Portada | Canvas del corredor fronterizo con embarques cruzando la línea |
| Portada, Almacenaje | Contadores y barras de capacidad animadas al entrar en pantalla |
| `/servicios/` | Selector que recomienda servicio según la situación del visitante |
| `/operacion/` | Recorrido por los siete pasos del cruce, navegable con teclado |
| Todas | Láminas con prompt copiable, revelado al hacer scroll, cambio EN/ES |

Todo respeta `prefers-reduced-motion` y funciona con teclado.

---

## Idiomas

Bilingüe español/inglés. El texto vive en los atributos `data-es` y `data-en` del
HTML; `assets/js/main.js` los intercambia, y también cambia el `<title>`, la
meta descripción y los `placeholder` de los formularios.

El idioma inicial se toma del navegador —español si el navegador está en español,
inglés en cualquier otro caso— y la elección del visitante se guarda en
`localStorage`.

> **Al editar un texto hay que cambiar las dos versiones**, `data-es` y `data-en`.

---

## Estructura de archivos

```
index.html                  Portada
<ruta>/index.html           Las once páginas restantes
404.html
assets/css/styles.css       Sistema de diseño completo
assets/js/main.js           Todo el comportamiento
assets/fonts/               Archivo + IBM Plex Mono (auto-alojadas)
assets/img/generated/       Imágenes generadas — aquí van las nuevas
assets/img/PROMPTS.md       Catálogo de prompts
assets/logos/               Logo CRISOSA, certificaciones y clientes
tools/build.py              Compone las rutas desde el shell compartido
tools/plates.py             Catálogo de imágenes y prompts
tools/parts/*.html          Cuerpo de cada página
```

### Editar el sitio

- **Cambiar un texto:** edítalo directamente en el HTML generado, o en
  `tools/parts/<ruta>.html` si quieres que sobreviva a la siguiente compilación.
- **Cambiar cabecera, menú, pie o paginador:** están en `tools/build.py`, en un
  solo lugar para las doce páginas. Después:

  ```bash
  python3 tools/build.py
  ```

- **Añadir o cambiar una imagen:** edita `tools/plates.py` y recompila. El
  `PROMPTS.md` se regenera solo.

### Verlo en local

```bash
python3 -m http.server 8080
```

Y abrir <http://localhost:8080>.

---

## Pendientes antes de publicar

- [ ] **Generar las imágenes.** 19 láminas siguen vacías. Están listadas en
      `assets/img/PROMPTS.md` con su prompt.
- [ ] **Correo de contacto.** El formulario abre el cliente de correo del
      visitante apuntando a `info@crisosa.com`, definido en `CONTACT_EMAIL` al
      inicio de `assets/js/main.js`. Hay que confirmar la dirección real.
- [ ] **Domicilio completo.** El sitio dice sólo «Tijuana, Baja California,
      México». Falta el domicilio y, si se quiere, un mapa embebido en
      `/contacto/`.
- [ ] **Datos de instalaciones.** El reparto de superficie por nave
      (9,000 / 7,500 / 5,500 m²), el número de andenes y la altura libre están
      puestos como referencia y deben confirmarse.
- [ ] **Cifras de la ficha técnica.** Igual con los tiempos `H+n` de
      `/operacion/`: hoy describen un cruce estándar, conviene validarlos contra
      la operación real.
- [ ] **Logo de cliente sin identificar.** `assets/logos/horse.png` aparece en la
      presentación sin nombre legible; lleva el texto alternativo genérico
      «Socio comercial».
- [ ] **Formulario con backend.** El `mailto:` funciona sin servidor; si se
      quiere recibir los mensajes en una bandeja o CRM hay que conectar un
      servicio de formularios.
- [ ] **Autorización de logos.** Confirmar que los clientes listados autorizan el
      uso de su marca en el sitio público.
