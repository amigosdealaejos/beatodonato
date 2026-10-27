#!/usr/bin/env python3
"""Genera las páginas del sitio a partir de los fragmentos de _fuente/paginas/.

Uso:  python3 _fuente/construir.py
Cambia URL_BASE cuando el sitio tenga su dirección definitiva (dominio propio).
"""
from pathlib import Path
from datetime import date

RAIZ = Path(__file__).resolve().parent.parent
FRAG = RAIZ / "_fuente" / "paginas"

URL_BASE = "https://beatodonato.com/"
NOMBRE = "Beato Donato Jiménez Bibiano"

# (archivo, etiqueta del menú, título, descripción, numeral)
PAGINAS = [
    ("index.html", "Portada", "Beato Donato Jiménez Bibiano (1873–1936) · Mártir redentorista de Alaejos",
     "Vida, martirio y memoria del beato Donato Jiménez Bibiano (Alaejos, 1873 – Madrid, 1936), sacerdote y misionero redentorista, beatificado en 2022. Contado desde las fuentes.", None),
    ("vida.html", "Su vida", "Su vida · " + NOMBRE,
     "Infancia en Alaejos, la misión de 1887, la vocación redentorista y más de treinta años de misionero y superior, contados desde sus propios escritos y los de su amigo el P. Saturnino Martín.", "I"),
    ("martirio.html", "Martirio", "El martirio · " + NOMBRE,
     "Dos meses escondido, la detención en la calle Mayor, la celda número 5 de la checa de Fomento y su muerte el 18 de septiembre de 1936, con los testimonios de quienes lo vieron.", "II"),
    ("cronologia.html", "Cronología", "Cronología · " + NOMBRE,
     "La vida del beato Donato Jiménez Bibiano y su causa de beatificación en veinticinco fechas, cada una con su fuente.", "III"),
    ("los-12.html", "Los doce", "Los doce mártires redentoristas de Madrid · " + NOMBRE,
     "Los doce redentoristas mártires de Madrid (1936), beatificados en la catedral de la Almudena el 22 de octubre de 2022.", "IV"),
    ("memoria.html", "Memoria", "Memoria · " + NOMBRE,
     "Sin sepultura conocida: Alaejos, quienes guardaron su memoria y la galería de fotografías del beato Donato Jiménez Bibiano.", "V"),
    ("fuentes.html", "Fuentes y oración", "Fuentes y oración · " + NOMBRE,
     "Documentos originales de la causa del beato Donato Jiménez Bibiano, publicaciones, criterios de cita y oración para pedir su intercesión.", "VI"),
]

CLASES = {"index.html": "cap-portada", "vida.html": "cap-vida", "martirio.html": "cap-martirio",
          "cronologia.html": "cap-cronologia", "los-12.html": "cap-doce", "memoria.html": "cap-memoria",
          "fuentes.html": "cap-fuentes"}

CABEZA = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#1f4e8c">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="{nombre}">
<meta property="og:title" content="{titulo_og}">
<meta property="og:description" content="{descripcion}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}assets/img/og-portada.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Beato Donato Jiménez Bibiano, sacerdote redentorista y mártir (Alaejos, 1873 – Madrid, 1936).">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="preload" href="assets/fonts/ibarra-real-nova-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/estilo.css">
<script>document.documentElement.classList.add('js');</script>
</head>
<body class="{clase}">
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <div class="envoltorio">
    <a class="marca" href="index.html"><span>Donato Jiménez Bibiano</span><small>Beato mártir, 1873–1936</small></a>
    <nav class="menu" id="menu" aria-label="Apartados del sitio">
      <button class="menu-boton" type="button" aria-expanded="false" aria-controls="menu-lista">Menú</button>
      <ul id="menu-lista">
{menu}
      </ul>
    </nav>
  </div>
</header>
<main id="contenido">
"""

PASO = """<nav class="paso envoltorio" aria-label="Siguiente apartado">
{ant}
{sig}
</nav>
"""

PIE = """</main>
<footer class="pie">
  <div class="envoltorio">
    <p class="quien-pie">Beato Donato Jiménez Bibiano<small>Alaejos, 21 de marzo de 1873 · Fuencarral, Madrid, 18 de septiembre de 1936</small></p>
    <ul>
{menu_pie}
    </ul>
    <div class="aviso">
      <p>Sitio conmemorativo sin ánimo de lucro. No es una publicación oficial de los Misioneros Redentoristas ni de ninguna institución eclesiástica.</p>
      <p>Las fotografías y los documentos proceden del archivo de la causa y se reproducen con permiso de los Misioneros Redentoristas. Los textos citan siempre su fuente; las correcciones y aportaciones documentales son bienvenidas.</p>
    </div>
  </div>
</footer>
<script>
(function () {{
  var nav = document.getElementById('menu');
  var boton = nav.querySelector('.menu-boton');
  boton.addEventListener('click', function () {{
    var abierto = nav.classList.toggle('abierto');
    boton.setAttribute('aria-expanded', abierto ? 'true' : 'false');
  }});
  document.addEventListener('keydown', function (e) {{
    if (e.key === 'Escape' && nav.classList.contains('abierto')) {{
      nav.classList.remove('abierto'); boton.setAttribute('aria-expanded', 'false'); boton.focus();
    }}
  }});
}})();
</script>
</body>
</html>
"""


def esc(t):
    return t.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def menu(actual, sangria):
    filas = []
    for archivo, etiqueta, *_ in PAGINAS:
        cur = ' aria-current="page"' if archivo == actual else ""
        clase = CLASES[archivo].replace('cap-', 'c-')
        filas.append(f'{sangria}<li class="{clase}"><a href="{archivo}"{cur}>{etiqueta}</a></li>')
    return "\n".join(filas)


def construir():
    for i, (archivo, etiqueta, titulo, desc, num) in enumerate(PAGINAS):
        cuerpo = (FRAG / archivo).read_text(encoding="utf-8")
        url = URL_BASE + ("" if archivo == "index.html" else archivo)
        html = CABEZA.format(
            titulo=esc(titulo), descripcion=esc(desc), url=url, base=URL_BASE,
            nombre=NOMBRE, titulo_og=esc(titulo.split(" · ")[0] if archivo != "index.html" else NOMBRE + " (1873–1936)"),
            menu=menu(archivo, " " * 8),
            clase=CLASES[archivo],
        )
        html += cuerpo
        if num:
            ant = PAGINAS[i - 1]
            sig = PAGINAS[i + 1] if i + 1 < len(PAGINAS) else None
            a = f'  <a class="ant" href="{ant[0]}"><span>Anterior</span><strong>{ant[1]}</strong></a>'
            s = (f'  <a class="sig" href="{sig[0]}"><span>Siguiente</span><strong>{sig[1]}</strong></a>'
                 if sig else '  <a class="sig" href="index.html"><span>Volver al principio</span><strong>Portada</strong></a>')
            html += PASO.format(ant=a, sig=s)
        html += PIE.format(menu_pie=menu(archivo, " " * 6))
        (RAIZ / archivo).write_text(html, encoding="utf-8")

    hoy = date.today().isoformat()
    mapa = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for archivo, *_ in PAGINAS:
        loc = URL_BASE + ("" if archivo == "index.html" else archivo)
        mapa.append(f"  <url><loc>{loc}</loc><lastmod>{hoy}</lastmod></url>")
    mapa.append("</urlset>")
    (RAIZ / "sitemap.xml").write_text("\n".join(mapa) + "\n", encoding="utf-8")
    (RAIZ / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {URL_BASE}sitemap.xml\n", encoding="utf-8")

    (RAIZ / "404.html").write_text(f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Página no encontrada · {NOMBRE}</title><meta name="robots" content="noindex">
<link rel="stylesheet" href="{URL_BASE}assets/css/estilo.css"></head>
<body><main class="envoltorio" style="padding-block: 5rem;">
<p class="acta">Esta dirección no corresponde a ninguna página del sitio.</p>
<h1 style="font-size: var(--t-h1); margin-top: .5rem;">Página no encontrada</h1>
<p style="margin-top: 1.5rem;"><a href="{URL_BASE}">Ir a la portada</a></p>
</main></body></html>
""", encoding="utf-8")
    print("Sitio generado:", ", ".join(p[0] for p in PAGINAS))


if __name__ == "__main__":
    construir()
