#!/usr/bin/env python3
"""Genera assets/img/og-portada.jpg (1200×630), la imagen que muestran WhatsApp, Facebook, etc.

Uso:  python3 _fuente/imagen_redes.py   (necesita Pillow, fonttools y brotli)
"""
import io
from pathlib import Path
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
IMG, FUENTES = RAIZ / "assets" / "img", RAIZ / "assets" / "fonts"
AZUL, TEXTO2, ROJO = "#1f4e8c", "#5d5852", "#b2382a"
FRANJA = ["#2d6a4b", "#b2382a", "#8f6611", "#1f4e8c", "#16707a", "#673f89"]


def fuente(nombre, tam):
    f = TTFont(FUENTES / nombre); f.flavor = None
    b = io.BytesIO(); f.save(b); b.seek(0)
    return ImageFont.truetype(b, tam)


lienzo = Image.new("RGB", (1200, 630), "white")
d = ImageDraw.Draw(lienzo)
for i, c in enumerate(FRANJA):
    d.rectangle([i * 200, 0, (i + 1) * 200, 11], fill=c)

foto = ImageOps.exif_transpose(Image.open(IMG / "1915-restaurada.jpg")).convert("RGB")
foto = ImageOps.fit(foto, (400, 540), Image.LANCZOS, centering=(0.5, 0.3))
d.rectangle([739, 49, 1141, 591], outline="#e5e1da", width=1)
lienzo.paste(foto, (740, 50))

d.text((70, 120), "BEATO MÁRTIR REDENTORISTA", font=fuente("ibarra-real-nova-latin-600-normal.woff2", 26), fill=ROJO)
grande = fuente("ibarra-real-nova-latin-600-normal.woff2", 76)
d.text((66, 170), "Donato Jiménez", font=grande, fill=AZUL)
d.text((66, 255), "Bibiano", font=grande, fill=AZUL)
media = fuente("ibarra-real-nova-latin-400-italic.woff2", 34)
d.text((70, 370), "Alaejos, 1873 · Madrid, 1936", font=media, fill=TEXTO2)
d.text((70, 418), "Beatificado el 22 de octubre de 2022", font=media, fill=TEXTO2)
d.line([70, 500, 260, 500], fill="#e3b548", width=3)
d.text((70, 520), "Su vida, su martirio y su memoria, desde las fuentes", font=fuente("ibarra-real-nova-latin-400-normal.woff2", 26), fill=TEXTO2)

lienzo.save(IMG / "og-portada.jpg", "JPEG", quality=88, optimize=True)
print("og-portada.jpg generada")
