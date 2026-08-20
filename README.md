# CRISOSA Logistic Solutions — sitio web

Sitio corporativo de **CRISOSA Logistic Solutions** (Tijuana, B.C.). HTML, CSS y
JavaScript estáticos: sin dependencias, sin servidor de aplicación, sin proceso de
build para servirlo. Se sube tal cual a cualquier hosting.

---

## La idea

El sitio es una **secuencia de pantallas completas**. Cada una lleva una fotografía,
un titular, una línea y dos botones. La fotografía hace el 80% del trabajo y el texto
el 20% — no al revés.

El orden de la portada es deliberado: **primero lo que se presume.**

1. Quiénes somos, en una frase
2. **Certificaciones** — IVA/IEPS AAA, CTPAT, IMMEX, OEA en proceso
3. **Clientes** — dieciséis marcas, a color y con espacio
4. Las cifras — 1994 · 22,000 m² · 3 naves · 30+ años
5. Los tres servicios
6. Instalaciones
7. Contacto

No explicamos la operación paso a paso: quien contrata logística transfronteriza ya
sabe cómo funciona un pedimento. Lo que no sabe es por qué CRISOSA.

---

## Rutas

Siete páginas reales, cada una con su URL, título y descripción.

| Ruta | Pantallas | Qué presume |
|---|---|---|
| `/` | 7 | Certificaciones, clientes, cifras, servicios, instalaciones |
| `/servicios/` | 5 | Importación y exportación, almacenaje, shelter |
| `/certificaciones/` | 5 | Una pantalla por acreditación, con el sello en grande |
| `/clientes/` | 3 | Las dieciséis marcas y los seis sectores |
| `/instalaciones/` | 4 | Capacidad, andenes, seguridad CTPAT |
| `/nosotros/` | 4 | Historia, forma de trabajar, dirección general |
| `/contacto/` | 2 | Formulario, datos directos, ubicación |

`404.html` cubre lo que no existe. Los enlaces internos son relativos, así que el
sitio funciona igual en la raíz de un dominio o en un subdirectorio.

El **índice** (botón arriba a la derecha) abre las siete rutas a pantalla completa.

---

## Fotografías y sus prompts

Cada pantalla tiene reservado su espacio con la proporción exacta. Mientras el archivo
no exista, la pantalla **conserva su composición** sobre un degradado y muestra abajo
una línea discreta con el nombre del archivo y un botón **«Copiar prompt»**.

Para llenar una:

1. Pulsa **Copiar prompt** en la pantalla que quieras.
2. Pégalo en ChatGPT (o el modelo de imagen que uses) y genera la fotografía.
3. Guárdala en `assets/img/generated/` **con el nombre exacto** que muestra la línea.
4. Recarga. Aparece sola: no hay que tocar código.

Las dieciséis fotografías, con proporción, nombre y prompt, están en
**[`assets/img/PROMPTS.md`](assets/img/PROMPTS.md)**, generado desde `tools/plates.py`.

Los prompts están en inglés a propósito —los modelos de imagen siguen mejor un brief
en inglés— y **todos terminan con la misma dirección fotográfica**, para que las
dieciséis piezas parezcan una sola sesión y no un banco de imágenes. Cada uno pide
además **espacio vacío en el tercio superior**: ahí va el titular.

Siete espacios ya vienen llenos con las fotografías de la presentación original.
Se reemplazan usando el mismo nombre de archivo.

---

## Diseño

- **Color.** Blanco y `#0E1116` (negro con una insinuación de azul) como fondos;
  `#F4F6F9` para las pantallas claras; el navy corporativo `#0A357F` en los botones.
  Los grises están sesgados a azul, no son neutros de fábrica.
- **Tipografía.** `Manrope`, **una sola familia**, pesos 200 a 800. Nada de
  monoespaciada. Auto-alojada en `assets/fonts/` (39 KB): el sitio no hace ninguna
  petición a terceros.
- **Composición.** Titular arriba, botones abajo, todo centrado, mucho aire. Los
  titulares se limitan a 19 caracteres por línea para que nunca lean como párrafo.
- **Movimiento.** Aparición suave al entrar en pantalla y contadores en las cifras.
  Nada más. Todo respeta `prefers-reduced-motion`.

La cabecera **lee la pantalla que tiene debajo** y cambia de color: blanca sobre
fotografía, oscura sobre fondo claro.

---

## Idiomas

Bilingüe español/inglés. El texto vive en los atributos `data-es` y `data-en` del
HTML; `assets/js/main.js` los intercambia, y también cambia el `<title>`, la meta
descripción y los `placeholder` del formulario.

El idioma inicial se toma del navegador y la elección del visitante se guarda en
`localStorage`.

> **Al editar un texto hay que cambiar las dos versiones**, `data-es` y `data-en`.

---

## Estructura

```
index.html                  Portada
<ruta>/index.html           Las seis páginas restantes
404.html · sitemap.xml · robots.txt
assets/css/styles.css       Sistema de diseño completo (~470 líneas)
assets/js/main.js           Todo el comportamiento (~230 líneas)
assets/fonts/               Manrope (auto-alojada)
assets/img/generated/       Fotografías — aquí van las nuevas
assets/img/PROMPTS.md       Catálogo de prompts
assets/logos/               Logo CRISOSA, certificaciones y clientes
tools/build.py              Compone las rutas desde el shell compartido
tools/plates.py             Catálogo de fotografías y prompts
tools/parts/*.html          Cuerpo de cada página
tools/trim_logos.py         Recorta el margen muerto de los logos
tools/preview.py            Empaqueta todo en un solo archivo
```

### Editar el sitio

- **Un texto:** edítalo en el HTML generado, o en `tools/parts/<ruta>.html` si quieres
  que sobreviva a la siguiente compilación.
- **Cabecera, índice o pie:** están en `tools/build.py`, en un solo lugar para las
  siete páginas. Después: `python3 tools/build.py`
- **Una fotografía:** edita `tools/plates.py` y recompila. `PROMPTS.md` se regenera solo.
- **Un logo nuevo:** ponlo en `assets/logos/` y corre `python3 tools/trim_logos.py`
  para que quede ópticamente al mismo peso que los demás.

### Verlo en local

```bash
python3 -m http.server 8080
```

Y abrir <http://localhost:8080>.

Para mandárselo a alguien sin publicarlo: `python3 tools/preview.py` genera
`dist/crisosa-preview.html`, un solo archivo con las siete rutas navegables dentro.

---

## Pendientes antes de publicar

- [ ] **Generar las fotografías.** Nueve espacios siguen vacíos. Los prompts están en
      `assets/img/PROMPTS.md`.
- [ ] **Dominio real.** `SITE` al final de `tools/build.py` dice
      `https://www.crisosa.com`. De ahí salen la URL canónica, el `og:image` y el
      `sitemap.xml`: **con el dominio equivocado, las vistas previas al compartir el
      enlace no funcionan.**
- [ ] **WhatsApp.** El botón flotante apunta a `+52 664 607 2000` (`WHATSAPP` en
      `tools/build.py`). Confirmar que ese número tiene WhatsApp Business, o cambiarlo.
- [ ] **Correo de contacto.** El formulario abre el cliente de correo apuntando a
      `info@crisosa.com` (`CONTACT_EMAIL` en `assets/js/main.js`). Confirmar.
- [ ] **Domicilio completo.** El sitio dice sólo «Tijuana, Baja California». Falta el
      domicilio y, si se quiere, un mapa en `/contacto/`.
- [ ] **Casos de éxito.** Los logos son presencia, no evidencia. Dos o tres casos con
      números —aunque sean anónimos— valdrían más que los dieciséis logos juntos.
- [ ] **Datos por confirmar.** El reparto de superficie por nave
      (9,000 / 7,500 / 5,500 m²) está puesto como referencia y así se declara en la
      página. Falta validarlo.
- [ ] **Logo de cliente sin identificar.** `assets/logos/horse.png` aparece en la
      presentación sin nombre legible; lleva el alt genérico «Socio comercial».
- [ ] **Formulario con backend.** El `mailto:` funciona sin servidor, pero pierde
      contactos. Si se quiere recibirlos en una bandeja o CRM hay que conectar un
      servicio de formularios.
- [ ] **Autorización de logos.** Confirmar que los clientes autorizan el uso de su
      marca en el sitio público.
