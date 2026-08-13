# CRISOSA Logistic Solutions — sitio web

Sitio corporativo de **CRISOSA Logistic Solutions** (Tijuana, B.C.), construido a partir de
la presentación *Presentacion Crisosa EN 2026*. Sitio estático: HTML, CSS y JavaScript sin
dependencias ni proceso de build.

## Contenido

| Sección | Origen en la presentación |
|---|---|
| Hero + cifras | Portada, About Us, Storage Service |
| Nosotros | 03 — About Us |
| Servicios | 04 — Our Services |
| Importación / Exportación | 05 — Import/Export Service |
| Almacenaje | 06 — Storage Service |
| Shelter | 07 — Shelter Service |
| Programas y certificaciones | 08–09 — Programs & Certifications + Coming Soon (OEA) |
| Clientes | 10 — Our Business Partners |
| Contacto | Firma del correo de Dirección General |

## Estructura

```
index.html                 Página completa (una sola página con anclas)
assets/css/styles.css      Estilos
assets/js/main.js          Idioma EN/ES, menú móvil, animaciones, formulario
assets/img/                Fotografías extraídas de la presentación
assets/logos/              Logo CRISOSA, certificaciones y logos de clientes
```

Todos los logos e imágenes se extrajeron de la presentación original en su resolución
máxima disponible. Los logos con máscara de transparencia (ACORN, enovis, cubeship,
DirecTex, OMG, OEA) se recompusieron como PNG con canal alfa.

## Verlo en local

No requiere instalación. Desde la raíz del proyecto:

```bash
python3 -m http.server 8080
```

Y abrir <http://localhost:8080>.

> Abrir `index.html` directamente con doble clic también funciona.

## Idiomas

El sitio es bilingüe inglés/español. El texto vive en los atributos `data-en` y `data-es`
del HTML y `assets/js/main.js` los intercambia. El idioma inicial se toma del navegador
(español si el navegador está en español, inglés en cualquier otro caso) y la elección del
visitante se guarda en `localStorage`.

Para editar un texto hay que cambiar **las dos** versiones en el atributo correspondiente.

## Pendientes antes de publicar

- [ ] **Correo de contacto.** El formulario abre el cliente de correo del visitante
      apuntando a `info@crisosa.com`, definido en `CONTACT_EMAIL` al inicio de
      `assets/js/main.js`. Hay que confirmar la dirección real.
- [ ] **Dirección física.** El sitio dice sólo «Tijuana, Baja California, México» porque la
      presentación no incluye domicilio. Falta el domicilio completo y, si se quiere, un mapa.
- [ ] **Logo de cliente sin identificar.** `assets/logos/horse.png` aparece en la
      presentación sin nombre legible; en el sitio lleva el texto alternativo genérico
      «Business partner».
- [ ] **Formulario con backend.** El `mailto:` funciona sin servidor, pero si se quiere
      recibir los mensajes en una bandeja o CRM hay que conectar un servicio de formularios.
- [ ] **Autorización de logos.** Confirmar que los clientes listados autorizan el uso de su
      marca en el sitio público.
