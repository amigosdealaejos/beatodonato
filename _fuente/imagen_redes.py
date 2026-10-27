#!/usr/bin/env python3
"""Genera assets/img/og-portada.jpg y og-portada-en.jpg (1200×630), la imagen que muestran WhatsApp, Facebook, etc.

Uso:  python3 _fuente/imagen_redes.py   (necesita Pillow, fonttools y brotli)
"""
import io
from pathlib import Path
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
IMG, FUENTES = RAIZ / "assets" / "img", RAIZ / "assets" / "fonts"
ORO, ORO_CLARO, TEXTO2 = "#85621a", "#d2ad5b", "#645b4f"
FRANJA = ("#b48a35", "#e9cd84")  # franja dorada: de los bordes al centro


def fuente(nombre, tam):
    f = TTFont(FUENTES / nombre); f.flavor = None
    b = io.BytesIO(); f.save(b); b.seek(0)
    return ImageFont.truetype(b, tam)


TEXTOS = {
    "og-portada.jpg": ("BEATO MÁRTIR REDENTORISTA", "Alaejos, 1873 · Madrid, 1936", "Beatificado el 22 de octubre de 2022",
                       "Su vida, su martirio y su memoria, desde las fuentes"),
    "og-portada-en.jpg": ("BLESSED REDEMPTORIST MARTYR", "Alaejos, 1873 · Madrid, 1936", "Beatified on 22 October 2022",
                          "His life, martyrdom and memory, told from the sources"),
}


def generar(archivo, rotulo, linea1, linea2, lema):
    lienzo = Image.new("RGB", (1200, 630), "white")
    d = ImageDraw.Draw(lienzo)
    a, b = (tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) for c in FRANJA)
    for x in range(1200):
        t = 1 - abs(x - 600) / 600
        d.line([x, 0, x, 11], fill=tuple(round(a[k] + (b[k] - a[k]) * t) for k in range(3)))
    foto = ImageOps.exif_transpose(Image.open(IMG / "1915-restaurada.jpg")).convert("RGB")
    foto = ImageOps.fit(foto, (400, 540), Image.LANCZOS, centering=(0.5, 0.3))
    d.rectangle([738, 48, 1142, 592], outline=ORO_CLARO, width=2)
    lienzo.paste(foto, (740, 50))
    d.text((70, 120), rotulo, font=fuente("ibarra-real-nova-latin-600-normal.woff2", 26), fill=ORO)
    grande = fuente("ibarra-real-nova-latin-600-normal.woff2", 76)
    d.text((66, 170), "Donato Jiménez", font=grande, fill=ORO)
    d.text((66, 255), "Bibiano", font=grande, fill=ORO)
    media = fuente("ibarra-real-nova-latin-400-italic.woff2", 34)
    d.text((70, 370), linea1, font=media, fill=TEXTO2)
    d.text((70, 418), linea2, font=media, fill=TEXTO2)
    d.line([70, 500, 260, 500], fill=ORO_CLARO, width=3)
    d.text((70, 520), lema, font=fuente("ibarra-real-nova-latin-400-normal.woff2", 26), fill=TEXTO2)
    lienzo.save(IMG / archivo, "JPEG", quality=88, optimize=True)
    print(archivo, "generada")


for archivo, textos in TEXTOS.items():
    generar(archivo, *textos)
