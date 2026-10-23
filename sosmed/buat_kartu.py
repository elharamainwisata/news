"""Buat kartu Instagram gaya @elharamainnews dari foto + judul artikel.

Pemakaian:
  python3 buat_kartu.py --foto foto.jpg --judul "Judul artikel" --out kartu.jpg [--format feed|story] [--logo logo.png]
"""
import argparse
import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

DIR = os.path.dirname(os.path.abspath(__file__))
FONT = os.path.join(DIR, "fonts")

BIRU_TUA = (0, 83, 181)
BIRU_MUDA = (0, 144, 231)
BIRU_JUDUL = (16, 82, 168)
BIRU_LOGO = (30, 128, 226)
PUTIH = (255, 255, 255)

UKURAN = {"feed": (1080, 1350), "story": (1080, 1920)}


def font(nama, size):
    return ImageFont.truetype(os.path.join(FONT, nama), size)


def isi_foto(foto, w, h):
    """Crop foto agar memenuhi area w x h (cover)."""
    im = Image.open(foto).convert("RGB")
    skala = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * skala), round(im.height * skala)), Image.LANCZOS)
    x = (im.width - w) // 2
    y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def gradasi_biru(w, h):
    bg = Image.new("RGB", (w, h))
    px = bg.load()
    for x in range(w):
        t = x / (w - 1)
        r = round(BIRU_TUA[0] + (BIRU_MUDA[0] - BIRU_TUA[0]) * t)
        g = round(BIRU_TUA[1] + (BIRU_MUDA[1] - BIRU_TUA[1]) * t)
        b = round(BIRU_TUA[2] + (BIRU_MUDA[2] - BIRU_TUA[2]) * t)
        for y in range(h):
            px[x, y] = (r, g, b)
    return bg


def bungkus(draw, teks, fnt, lebar_maks):
    baris, kini = [], ""
    for kata in teks.split():
        coba = (kini + " " + kata).strip()
        if draw.textlength(coba, font=fnt) <= lebar_maks:
            kini = coba
        else:
            baris.append(kini)
            kini = kata
    if kini:
        baris.append(kini)
    return baris


def logo_teks(lebar):
    """Logo pengganti sementara bila file logo asli belum ada."""
    h = round(lebar * 0.5)
    lg = Image.new("RGBA", (lebar, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(lg)
    d.polygon([(round(lebar * 0.18), round(h * 0.12)), (lebar, 0), (lebar, round(h * 0.5)),
               (round(lebar * 0.12), round(h * 0.55))], fill=PUTIH)
    f1 = font("Poppins-ExtraBoldItalic.ttf", round(h * 0.2))
    f2 = font("Poppins-ExtraBoldItalic.ttf", round(h * 0.46))
    d.text((round(lebar * 0.22), round(h * 0.12)), "ELHARAMAIN", font=f1, fill=BIRU_LOGO,
           stroke_width=3, stroke_fill=PUTIH)
    d.text((round(lebar * 0.24), round(h * 0.32)), "NEWS", font=f2, fill=BIRU_LOGO,
           stroke_width=5, stroke_fill=PUTIH)
    return lg


def buat_kartu(foto, judul, out, fmt="feed", logo=None):
    W, H = UKURAN[fmt]
    s = W / 1080
    tinggi_foto = round(H * (0.60 if fmt == "feed" else 0.55))

    kanvas = gradasi_biru(W, H)
    ft = isi_foto(foto, W, tinggi_foto)
    # pudarkan bagian bawah foto ke biru
    mask = Image.new("L", (W, tinggi_foto), 255)
    md = ImageDraw.Draw(mask)
    awal = round(tinggi_foto * 0.72)
    for y in range(awal, tinggi_foto):
        md.line([(0, y), (W, y)], fill=round(255 * (1 - (y - awal) / (tinggi_foto - awal))))
    kanvas.paste(ft, (0, 0), mask)

    d = ImageDraw.Draw(kanvas)
    # kotak judul
    kx0, kx1 = round(70 * s), W - round(110 * s)
    ky0 = tinggi_foto - round(25 * s)
    f_judul = font("Poppins-Bold.ttf", round(56 * s))
    baris = bungkus(d, judul, f_judul, (kx1 - kx0) - round(90 * s))
    while len(baris) > 4 and f_judul.size > 36:
        f_judul = font("Poppins-Bold.ttf", f_judul.size - 4)
        baris = bungkus(d, judul, f_judul, (kx1 - kx0) - round(90 * s))
    tinggi_baris = round(f_judul.size * 1.12)
    ky1 = ky0 + round(130 * s) + tinggi_baris * len(baris)
    d.rectangle([kx1 - round(10 * s), ky0 - round(18 * s), kx1 + round(22 * s), ky1 - round(40 * s)],
                fill=BIRU_MUDA)
    bayang = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(bayang).rectangle([kx0 + 6, ky0 + 10, kx1 + 6, ky1 + 10], fill=(0, 30, 80, 90))
    kanvas.paste(bayang.filter(ImageFilter.GaussianBlur(12)), (0, 0), bayang.filter(ImageFilter.GaussianBlur(12)))
    d = ImageDraw.Draw(kanvas)
    d.rectangle([kx0, ky0, kx1, ky1], fill=PUTIH)
    y = ky0 + round(70 * s)
    for b in baris:
        lw = d.textlength(b, font=f_judul)
        d.text(((kx0 + kx1 - lw) / 2, y), b, font=f_judul, fill=BIRU_JUDUL)
        y += tinggi_baris

    # logo di pojok kanan atas kotak
    lebar_logo = round(330 * s)
    lg = Image.open(logo).convert("RGBA") if logo else logo_teks(lebar_logo)
    lg = lg.resize((lebar_logo, round(lebar_logo * lg.height / lg.width)), Image.LANCZOS)
    kanvas.paste(lg, (W - lebar_logo - round(85 * s), ky0 - round(lg.height * 0.7)), lg)

    # footer
    fy = ky1 + round(55 * s) if fmt == "feed" else H - round(260 * s)
    gx, gr = round(182 * s), round(31 * s)
    d.ellipse([gx - gr, fy - gr + round(30 * s), gx + gr, fy + gr + round(30 * s)], outline=PUTIH, width=3)
    cy = fy + round(30 * s)
    d.ellipse([gx - gr // 2, cy - gr, gx + gr // 2, cy + gr], outline=PUTIH, width=3)
    d.line([gx - gr, cy, gx + gr, cy], fill=PUTIH, width=3)
    d.line([gx, cy - gr, gx, cy + gr], fill=PUTIH, width=3)
    d.text((round(238 * s), fy), "Selengkapnya di.", font=font("Poppins-SemiBold.ttf", round(28 * s)), fill=PUTIH)
    d.text((round(240 * s), fy + round(36 * s)), "www.news.elharamainwisata.com",
           font=font("Poppins-Regular.ttf", round(24 * s)), fill=PUTIH)

    kanvas.save(out, quality=90)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--foto", required=True)
    ap.add_argument("--judul", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--format", default="feed", choices=list(UKURAN))
    ap.add_argument("--logo")
    a = ap.parse_args()
    print(buat_kartu(a.foto, a.judul, a.out, a.format, a.logo))
