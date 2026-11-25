import sys
from PIL import Image, ImageDraw, ImageFont
def credit(im, text="Foto: SPA"):
    im = im.convert("RGBA")
    try: f = ImageFont.truetype("DejaVuSans.ttf", 15)
    except Exception: f = ImageFont.load_default(size=15)
    ov = Image.new("RGBA", im.size, (0,0,0,0)); d = ImageDraw.Draw(ov)
    l,t,r,b = d.textbbox((0,0), text, font=f); tw, th = r-l, b-t; pad = 6
    x1 = im.width-20; y1 = im.height-10; x0 = x1-tw-2*pad; y0 = y1-th-2*pad
    d.rounded_rectangle((x0,y0,x1,y1), radius=6, fill=(0,0,0,90))
    d.text((x0+pad-l, y0+pad-t), text, font=f, fill=(255,255,255,220))
    return Image.alpha_composite(im, ov).convert("RGB")
