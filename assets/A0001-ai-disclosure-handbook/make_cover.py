#!/usr/bin/env python3
"""
Cover generator for A0001 - The AI Disclosure Handbook.

Original typographic design. Deliberately contains no photorealistic people
(which would trigger Amazon's `contains-synthetic-performer` IPTC requirement),
no brand marks, and no purchased or templated design assets.

Design rationale: the book's differentiator is that every claim is graded and
dated. The cover states that visually - an evidence key and a prominent edition
date - rather than asserting authority it has not earned. The date must stay
legible at thumbnail size, because recency is the product.

Output: cover.png at 1600x2560 (1:1.6, Kindle's recommended ratio).
"""
from PIL import Image, ImageDraw, ImageFont

W, H = 1600, 2560
INK = (11, 18, 32)          # near-black navy field
PAPER = (247, 245, 240)     # warm off-white
ACCENT = (212, 160, 74)     # muted gold - the edition date
MUTED = (138, 152, 176)     # cool grey for secondary text
RULE = (58, 72, 98)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def f(path, size):
    return ImageFont.truetype(path, size)


def center(d, y, text, font, fill):
    w = d.textbbox((0, 0), text, font=font)[2]
    d.text(((W - w) // 2, y), text, font=font, fill=fill)
    return w


img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

# Thin border inset - gives the cover a "document" feel at thumbnail size
d.rectangle([54, 54, W - 54, H - 54], outline=RULE, width=3)

# --- Eyebrow -------------------------------------------------------------
center(d, 250, "A DATED, SOURCED REFERENCE", f(MONO, 44), MUTED)

# --- Title ---------------------------------------------------------------
center(d, 430, "THE AI", f(SERIF_B, 168), PAPER)
center(d, 620, "DISCLOSURE", f(SERIF_B, 168), PAPER)
center(d, 810, "HANDBOOK", f(SERIF_B, 168), PAPER)

# --- Rule ----------------------------------------------------------------
d.line([(340, 1040), (W - 340, 1040)], fill=ACCENT, width=5)

# --- Subtitle ------------------------------------------------------------
center(d, 1110, "What Creators and Sellers", f(SERIF, 74), PAPER)
center(d, 1210, "Must Declare in 2026", f(SERIF, 74), PAPER)

# --- Platform list -------------------------------------------------------
center(d, 1400, "AMAZON KDP  ·  ETSY  ·  YOUTUBE", f(MONO, 42), MUTED)
center(d, 1470, "MEDIUM  ·  ROYAL ROAD  ·  EU AI ACT", f(MONO, 42), MUTED)

# --- Evidence key: the actual differentiator -----------------------------
# Every claim in the book carries one of these grades. Showing them on the
# cover is a promise the reader can verify in the free sample.
tags = [("[Official]", ACCENT), ("[Reported]", MUTED), ("[Unknown]", MUTED)]
tag_font = f(MONO_B, 40)
pad_x, gap = 26, 26
widths = [d.textbbox((0, 0), t, font=tag_font)[2] + pad_x * 2 for t, _ in tags]
x = (W - (sum(widths) + gap * (len(tags) - 1))) // 2
y = 1650
for (label, colour), bw in zip(tags, widths):
    d.rectangle([x, y, x + bw, y + 82], outline=colour, width=3)
    d.text((x + pad_x, y + 20), label, font=tag_font, fill=colour)
    x += bw + gap

center(d, 1780, "Every claim carries its source and its date.", f(SERIF, 46), MUTED)

# --- Edition date: must survive thumbnail scaling ------------------------
d.rectangle([300, 1990, W - 300, 2160], fill=ACCENT)
bbox = d.textbbox((0, 0), "AUGUST 2026 EDITION", font=f(MONO_B, 62))
d.text(((W - bbox[2]) // 2, 2035), "AUGUST 2026 EDITION", font=f(MONO_B, 62), fill=INK)

# --- Author --------------------------------------------------------------
# AUTHOR_NAME is an Owner decision (see METADATA.md) - placeholder until set.
center(d, 2320, "AUTHOR NAME", f(SERIF_B, 62), PAPER)

img.save("cover.png", "PNG", optimize=True)

# Thumbnail legibility check - Amazon search results show covers very small.
img.resize((160, 256), Image.LANCZOS).save("cover_thumbnail_check.png", "PNG")
print(f"cover.png written ({W}x{H})")
print("cover_thumbnail_check.png written (160x256) - verify the edition date is readable")
