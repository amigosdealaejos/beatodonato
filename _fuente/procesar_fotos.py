#!/usr/bin/env python3
"""Convierte las fotos originales (carpeta _originales/) en las versiones web de assets/img/.

Uso:  python3 _fuente/procesar_fotos.py
Necesita Pillow (pip install pillow).
"""
from pathlib import Path
from PIL import Image, ImageOps

RAIZ = Path(__file__).resolve().parent.parent
ORIG = RAIZ / "_originales"
DEST = RAIZ / "assets" / "img"

# nombre del archivo original (tal como está en Drive) -> nombre en la web
MAPA = {
    "P. Jiménez 1934.jpg": "retrato-1934.jpg",
    "P. jiménez 1934 2.jpg": "1934-b.jpg",
    "P. jiménez 1934 3_edited.jpg": "1934-detalle.jpg",
    "P. Jimenez, Astorga 1896.jpg": "astorga-1896.jpg",
    "P. Jiménez 1915.jpg": "1915.jpg",
    "P. Jiménez 1915.1.jpg": "1915-detalle.jpg",
    "P. Jiménez 1918.jpg": "1918.jpg",
    "P. Jiménez 1927.jpg": "1927.jpg",
    "P. Jiménez 01.jpg": "1918-detalle.jpg",
    "P. Jiménez 02.jpg": "1915-restaurada.jpg",
    "P. Jiménez 03.jpg": "1918-restaurada.jpg",
    "P. Jiménez 04.jpg": "lamina-impresa.jpg",
    "Dibujo del P. Jiménez.jpg": "dibujo.jpg",
    "Virgen de la Casita.jpg": "virgen-de-la-casita.jpg",
}
LADO_MAX = 1600


def normaliza(n):
    import unicodedata
    return unicodedata.normalize("NFC", n).lower()


def procesar():
    disponibles = {normaliza(p.name): p for p in ORIG.glob("*") if p.is_file()}
    for original, destino in MAPA.items():
        p = disponibles.get(normaliza(original))
        if not p:
            print("FALTA:", original)
            continue
        im = ImageOps.exif_transpose(Image.open(p)).convert("RGB")
        im.thumbnail((LADO_MAX, LADO_MAX), Image.LANCZOS)
        im.save(DEST / destino, "JPEG", quality=84, optimize=True, progressive=True)
        print(f"{original} -> {destino} {im.size}")


if __name__ == "__main__":
    procesar()
