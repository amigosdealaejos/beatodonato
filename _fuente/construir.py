#!/usr/bin/env python3
"""Genera las páginas del sitio, en español y en inglés, a partir de los fragmentos de _fuente/.

    _fuente/paginas/   texto de las páginas en español  -> raíz del sitio
    _fuente/pages-en/  texto de las páginas en inglés   -> carpeta en/

Uso:  python3 _fuente/construir.py
Cambia URL_BASE si el sitio cambia de dirección.
"""
from pathlib import Path
from datetime import date

RAIZ = Path(__file__).resolve().parent.parent
URL_BASE = "https://beatodonato.com/"

# Cada página: clase de color, numeral y, por idioma, (archivo, etiqueta del menú, título, descripción)
PAGINAS = [
    ("cap-portada", None, {
        "es": ("index.html", "Portada", "Beato Donato Jiménez Bibiano (1873–1936) · Mártir redentorista de Alaejos",
               "Vida, martirio y memoria del beato Donato Jiménez Bibiano (Alaejos, 1873 – Madrid, 1936), sacerdote y misionero redentorista, beatificado en 2022. Contado desde las fuentes."),
        "en": ("index.html", "Home", "Blessed Donato Jiménez Bibiano (1873–1936) · Redemptorist martyr from Alaejos",
               "The life, martyrdom and memory of Blessed Donato Jiménez Bibiano (Alaejos, 1873 – Madrid, 1936), Redemptorist priest and missionary, beatified in 2022. Told from the sources."),
    }),
    ("cap-vida", "I", {
        "es": ("vida.html", "Su vida", "Su vida",
               "Infancia en Alaejos, la misión de 1887, la vocación redentorista y más de treinta años de misionero, contados desde sus propios escritos y los de su amigo el P. Saturnino Martín."),
        "en": ("life.html", "His life", "His life",
               "Childhood in Alaejos, the parish mission of 1887, his Redemptorist vocation and over thirty years as a missionary, told from his own writings and those of his friend Fr Saturnino Martín."),
    }),
    ("cap-martirio", "II", {
        "es": ("martirio.html", "Martirio", "El martirio",
               "Dos meses escondido, la detención en la calle Mayor, la celda número 5 de la checa de Fomento y su muerte el 18 de septiembre de 1936, con los testimonios de quienes lo vieron."),
        "en": ("martyrdom.html", "Martyrdom", "The martyrdom",
               "Two months in hiding, his arrest in Calle Mayor, cell number 5 of the Fomento checa and his death on 18 September 1936, with the testimony of those who saw him."),
    }),
    ("cap-cronologia", "III", {
        "es": ("cronologia.html", "Cronología", "Cronología",
               "La vida del beato Donato Jiménez Bibiano y su causa de beatificación en veinticinco fechas, cada una con su fuente."),
        "en": ("timeline.html", "Timeline", "Timeline",
               "The life of Blessed Donato Jiménez Bibiano and his cause for beatification in twenty-five dates, each with its source."),
    }),
    ("cap-doce", "IV", {
        "es": ("los-12.html", "Los doce", "Los doce mártires redentoristas de Madrid",
               "Los doce redentoristas mártires de Madrid (1936), beatificados en la catedral de la Almudena el 22 de octubre de 2022."),
        "en": ("the-twelve.html", "The Twelve", "The twelve Redemptorist martyrs of Madrid",
               "The twelve Redemptorist martyrs of Madrid (1936), beatified in Almudena Cathedral on 22 October 2022."),
    }),
    ("cap-memoria", "V", {
        "es": ("memoria.html", "Memoria", "Memoria",
               "Sin sepultura conocida: Alaejos, quienes guardaron su memoria y la galería de fotografías del beato Donato Jiménez Bibiano."),
        "en": ("memory.html", "Memory", "Memory",
               "No known grave: Alaejos, those who kept his memory alive, and the photo gallery of Blessed Donato Jiménez Bibiano."),
    }),
    ("cap-fuentes", "VI", {
        "es": ("fuentes.html", "Fuentes y oración", "Fuentes y oración",
               "Documentos originales de la causa del beato Donato Jiménez Bibiano, publicaciones, criterios de cita y oración para pedir su intercesión."),
        "en": ("sources.html", "Sources & prayer", "Sources and prayer",
               "Original documents from the cause of Blessed Donato Jiménez Bibiano, publications, how quotations are handled, and a prayer for his intercession."),
    }),
]

IDIOMAS = {
    "es": dict(
        carpeta="", fragmentos="paginas", locale="es_ES", nombre="Beato Donato Jiménez Bibiano",
        og_imagen="og-portada.jpg",
        og_alt="Beato Donato Jiménez Bibiano, sacerdote redentorista y mártir (Alaejos, 1873 – Madrid, 1936).",
        saltar="Saltar al contenido", marca_sub="Beato mártir, 1873–1936", menu_aria="Apartados del sitio",
        menu="Menú", otro="en", otro_texto="English", otro_titulo="Read this page in English",
        paso_aria="Siguiente apartado", anterior="Anterior", siguiente="Siguiente",
        volver="Volver al principio", portada="Portada",
        pie_quien="Beato Donato Jiménez Bibiano<small>Alaejos, 21 de marzo de 1873 · Fuencarral, Madrid, 18 de septiembre de 1936</small>",
        aviso=("Sitio conmemorativo sin ánimo de lucro. No es una publicación oficial de los Misioneros Redentoristas ni de ninguna institución eclesiástica.",
               "Las fotografías y los documentos proceden del archivo de la causa y se reproducen con permiso de los Misioneros Redentoristas. Los textos citan siempre su fuente; las correcciones y aportaciones documentales son bienvenidas."),
    ),
    "en": dict(
        carpeta="en/", fragmentos="pages-en", locale="en_GB", nombre="Blessed Donato Jiménez Bibiano",
        og_imagen="og-portada-en.jpg",
        og_alt="Blessed Donato Jiménez Bibiano, Redemptorist priest and martyr (Alaejos, 1873 – Madrid, 1936).",
        saltar="Skip to content", marca_sub="Blessed martyr, 1873–1936", menu_aria="Site sections",
        menu="Menu", otro="es", otro_texto="Español", otro_titulo="Leer esta página en español",
        paso_aria="Next section", anterior="Previous", siguiente="Next",
        volver="Back to the beginning", portada="Home",
        pie_quien="Blessed Donato Jiménez Bibiano<small>Alaejos, 21 March 1873 · Fuencarral, Madrid, 18 September 1936</small>",
        aviso=("A non-profit memorial site. It is not an official publication of the Redemptorist Missionaries or of any Church institution.",
               "The photographs and documents come from the archive of the cause and are reproduced with the permission of the Redemptorist Missionaries. Quotations are translated from the Spanish originals, and every one gives its source; corrections and further documents are welcome."),
    ),
}

CABEZA = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{titulo}</title>
<meta name="description" content="{descripcion}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{url_es}">
<link rel="alternate" hreflang="en" href="{url_en}">
<link rel="alternate" hreflang="x-default" href="{url_es}">
<meta name="theme-color" content="#85621a">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:locale" content="{locale}">
<meta property="og:locale:alternate" content="{locale_otro}">
<meta property="og:site_name" content="{nombre}">
<meta property="og:title" content="{titulo_og}">
<meta property="og:description" content="{descripcion}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{base}assets/img/{og_imagen}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{og_alt}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{r}assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="preload" href="{r}assets/fonts/ibarra-real-nova-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{r}assets/css/estilo.css">
<script>document.documentElement.classList.add('js');</script>
</head>
<body class="{clase}">
<a class="saltar" href="#contenido">{saltar}</a>
<header class="cabecera">
  <div class="envoltorio">
    <a class="marca" href="index.html"><span>Donato Jiménez Bibiano</span><small>{marca_sub}</small></a>
    <div class="herramientas">
      <nav class="menu" id="menu" aria-label="{menu_aria}">
        <button class="menu-boton" type="button" aria-expanded="false" aria-controls="menu-lista">{menu_texto}</button>
        <ul id="menu-lista">
{menu}
        </ul>
      </nav>
      <a class="idioma" href="{href_otro}" hreflang="{otro}" lang="{otro}" title="{otro_titulo}">{otro_texto}</a>
    </div>
  </div>
</header>
<main id="contenido">
"""

PASO = """<nav class="paso envoltorio" aria-label="{aria}">
{ant}
{sig}
</nav>
"""

PIE = """</main>
<footer class="pie">
  <div class="envoltorio">
    <p class="quien-pie">{quien}</p>
    <ul>
{menu_pie}
    </ul>
    <div class="aviso">
      <p>{aviso1}</p>
      <p>{aviso2}</p>
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


def url_de(lengua, archivo):
    return URL_BASE + IDIOMAS[lengua]["carpeta"] + ("" if archivo == "index.html" else archivo)


def menu(lengua, actual, sangria):
    filas = []
    for clase, _, datos in PAGINAS:
        archivo, etiqueta = datos[lengua][:2]
        cur = ' aria-current="page"' if archivo == actual else ""
        filas.append(f'{sangria}<li class="{clase.replace("cap-", "c-")}"><a href="{archivo}"{cur}>{etiqueta}</a></li>')
    return "\n".join(filas)


def construir():
    for lengua, I in IDIOMAS.items():
        otro = I["otro"]
        destino = RAIZ / I["carpeta"]
        destino.mkdir(exist_ok=True)
        r = "../" if I["carpeta"] else ""
        sufijo = " · " + I["nombre"]
        for i, (clase, num, datos) in enumerate(PAGINAS):
            archivo, etiqueta, titulo, desc = datos[lengua]
            portada = archivo == "index.html"
            titulo_completo = titulo if portada else titulo + sufijo
            cuerpo = (RAIZ / "_fuente" / I["fragmentos"] / archivo).read_text(encoding="utf-8")
            archivo_otro = datos[otro][0]
            href_otro = ("../" if I["carpeta"] else "en/") + archivo_otro
            html = CABEZA.format(
                lang=lengua, titulo=esc(titulo_completo), descripcion=esc(desc),
                url=url_de(lengua, archivo), url_es=url_de("es", datos["es"][0]), url_en=url_de("en", datos["en"][0]),
                locale=I["locale"], locale_otro=IDIOMAS[otro]["locale"], nombre=I["nombre"],
                titulo_og=esc(I["nombre"] + " (1873–1936)" if portada else titulo),
                base=URL_BASE, og_imagen=I["og_imagen"], og_alt=esc(I["og_alt"]), r=r, clase=clase,
                saltar=I["saltar"], marca_sub=I["marca_sub"], menu_aria=I["menu_aria"], menu_texto=I["menu"],
                menu=menu(lengua, archivo, " " * 10), href_otro=href_otro, otro=otro,
                otro_titulo=I["otro_titulo"], otro_texto=I["otro_texto"],
            )
            html += cuerpo
            if num:
                ant = PAGINAS[i - 1][2][lengua]
                sig = PAGINAS[i + 1][2][lengua] if i + 1 < len(PAGINAS) else None
                a = f'  <a class="ant" href="{ant[0]}"><span>{I["anterior"]}</span><strong>{ant[1]}</strong></a>'
                s = (f'  <a class="sig" href="{sig[0]}"><span>{I["siguiente"]}</span><strong>{sig[1]}</strong></a>'
                     if sig else f'  <a class="sig" href="index.html"><span>{I["volver"]}</span><strong>{I["portada"]}</strong></a>')
                html += PASO.format(aria=I["paso_aria"], ant=a, sig=s)
            html += PIE.format(quien=I["pie_quien"], menu_pie=menu(lengua, archivo, " " * 6),
                               aviso1=I["aviso"][0], aviso2=I["aviso"][1])
            (destino / archivo).write_text(html, encoding="utf-8")

    hoy = date.today().isoformat()
    mapa = ['<?xml version="1.0" encoding="UTF-8"?>',
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for _, _, datos in PAGINAS:
        alternos = "".join(f'<xhtml:link rel="alternate" hreflang="{l}" href="{url_de(l, datos[l][0])}"/>' for l in IDIOMAS)
        for lengua in IDIOMAS:
            mapa.append(f"  <url><loc>{url_de(lengua, datos[lengua][0])}</loc><lastmod>{hoy}</lastmod>{alternos}</url>")
    mapa.append("</urlset>")
    (RAIZ / "sitemap.xml").write_text("\n".join(mapa) + "\n", encoding="utf-8")
    (RAIZ / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {URL_BASE}sitemap.xml\n", encoding="utf-8")

    (RAIZ / "404.html").write_text(f"""<!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Página no encontrada · Page not found</title><meta name="robots" content="noindex">
<link rel="stylesheet" href="{URL_BASE}assets/css/estilo.css"></head>
<body><main class="envoltorio" style="padding-block: 5rem;">
<p class="acta">Esta dirección no corresponde a ninguna página del sitio.</p>
<h1 style="font-size: var(--t-h1); margin-top: .5rem;">Página no encontrada</h1>
<p style="margin-top: 1.5rem;"><a href="{URL_BASE}">Ir a la portada</a></p>
<p lang="en" style="margin-top: 2.5rem; color: var(--texto-2);">This page does not exist. <a href="{URL_BASE}en/">Go to the English home page</a>.</p>
</main></body></html>
""", encoding="utf-8")
    print("Sitio generado:", ", ".join(I["carpeta"] + d[l][0] for l, I in IDIOMAS.items() for _, _, d in PAGINAS))


if __name__ == "__main__":
    construir()
