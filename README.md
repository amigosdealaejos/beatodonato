# Beato Donato Jiménez Bibiano

Sitio conmemorativo del beato Donato Jiménez Bibiano (Alaejos, 1873 – Madrid, 1936), sacerdote y misionero redentorista, mártir. Contado desde las fuentes de su causa de beatificación.

Es un sitio estático, sin dependencias, pensado para GitHub Pages.

## Estructura

| Ruta | Qué es |
|---|---|
| `index.html`, `vida.html`, `martirio.html`, `cronologia.html`, `los-12.html`, `memoria.html`, `fuentes.html` | Páginas publicadas en español (se generan, no se editan a mano) |
| `en/` | Las mismas páginas en inglés (también generadas) |
| `_fuente/paginas/` | Texto de cada página en español. **Aquí se corrige el contenido.** |
| `_fuente/pages-en/` | Texto de cada página en inglés |
| `_fuente/construir.py` | Une cada texto con la cabecera, el menú y el pie y genera las páginas |
| `_fuente/procesar_fotos.py` | Convierte las fotos de `_originales/` (no se suben al repositorio) en las versiones web de `assets/img/` |
| `_fuente/imagen_redes.py` | Genera `og-portada.jpg`, la imagen que se ve al compartir el enlace |
| `assets/css/estilo.css` | Estilos |
| `assets/fonts/` | Tipografía Ibarra Real Nova (licencia SIL OFL 1.1) |
| `assets/img/` | Fotografías, imagen para redes sociales e iconos |
| `assets/docs/` | Los seis documentos de la causa en PDF |

## Cómo cambiar un texto

1. Edita el archivo correspondiente en `_fuente/paginas/` y, si el cambio afecta al contenido, también su versión en `_fuente/pages-en/`.
2. Ejecuta `python3 _fuente/construir.py`.
3. Sube los cambios.

## Dirección del sitio

La dirección está en `URL_BASE`, al principio de `_fuente/construir.py`. Si se conecta un dominio propio, hay que cambiarla allí, volver a generar el sitio y añadir un archivo `CNAME` con el dominio.

## Criterios

Toda frase entre comillas es una cita de un documento identificado en `fuentes.html`. Donde dos fuentes no coinciden, se dice.

Sitio sin ánimo de lucro. No es una publicación oficial de los Misioneros Redentoristas. Fotografías y documentos reproducidos con su permiso.
