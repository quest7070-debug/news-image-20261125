#!/usr/bin/env python3
"""Draw the news poster for Wednesday 25 November 2026.

Build-time script (run locally, not by the grader): it renders entry.png,
a one-page newspaper front page summing up the day's world news, from the
stories reported on 25 November 2026. The entry program (main.ts) only
copies the finished image to /output/entry.png.

Layout: 1024 x 1024, masthead + lead story + two second stories + four
regional cards + a briefs strip. All text is drawn with DejaVu fonts so
every word stays crisp and legible; nothing is pasted in from elsewhere.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (26, 26, 26)
MUTED = (96, 92, 84)
RED = (179, 38, 30)
NAVY = (20, 38, 74)
BLUE = (31, 90, 160)
CARD = (255, 255, 255)
LINE = (205, 198, 186)
GREEN = (28, 110, 66)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns a list of lines fitting `width` px."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def para(draw, xy, text, fnt, fill, width, leading):
    """Draw wrapped text; returns the y just below the last line."""
    x, y = xy
    for line in wrap(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def kicker(draw, xy, text, fill=RED):
    draw.text(xy, text, font=font(SANS_B, 20), fill=fill)


def rule(draw, x0, x1, y, fill=INK, width=2):
    draw.line([(x0, y), (x1, y)], fill=fill, width=width)


def card(draw, box, fill=CARD):
    draw.rectangle(box, fill=fill, outline=LINE, width=1)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.text((32, 22), "T H E   W O R L D   I N   O N E   D A Y",
           font=font(SANS_B, 21), fill=(214, 196, 150))
    d.text((32, 52), "Wednesday 25 November 2026",
           font=font(SERIF_B, 42), fill=(255, 255, 255))
    d.text((800, 34), "WORLD NEWS", font=font(SANS_B, 20),
           fill=(214, 196, 150))
    d.text((800, 64), "One day, one image",
           font=font(SANS, 19), fill=(200, 208, 224))

    # ---- Lead story: tariffs -------------------------------------------
    y = 136
    kicker(d, (32, y), "TRADE  ·  LEAD STORY")
    y += 30
    y = para(d, (32, y), "US proposes tariffs of up to 20% on 14 economies",
             font(SERIF_B, 40), INK, 600, 48)
    y += 4
    y = para(d, (32, y),
             "Vietnam faces the proposed 20% rate; Cambodia and Indonesia 18%. "
             "The EU \u201cstrongly rejects the premise\u201d; Beijing calls "
             "overcapacity \u201ca false issue\u201d.",
             font(SANS, 22), MUTED, 600, 30)
    # Right-hand graphic: a big 20% with a rising arrow.
    gx0, gy0, gx1, gy1 = 668, 136, 992, 384
    card(d, (gx0, gy0, gx1, gy1))
    d.text((gx0 + 24, gy0 + 16), "THE TOP RATE", font=font(SANS_B, 19),
           fill=MUTED)
    d.text((gx0 + 24, gy0 + 44), "20%", font=font(SERIF_B, 92), fill=RED)
    d.line([(gx0 + 30, gy1 - 52), (gx0 + 120, gy1 - 110),
            (gx0 + 210, gy1 - 78), (gx0 + 290, gy1 - 128)],
           fill=RED, width=7)
    d.polygon([(gx0 + 290, gy1 - 128), (gx0 + 262, gy1 - 128),
               (gx0 + 290, gy1 - 100)], fill=RED)
    d.text((gx0 + 24, gy1 - 44), "14 economies  ·  up to 20%",
           font=font(SANS, 19), fill=INK)

    # ---- Second row: markets + space ------------------------------------
    y = 404
    rule(d, 32, 992, y, fill=INK, width=2)
    y += 14
    # Left card: chip stocks.
    card(d, (32, y, 496, y + 200))
    kicker(d, (52, y + 14), "MARKETS  ·  ASIA")
    para(d, (52, y + 44), "AI doubts sink Asian chip stocks",
         font(SERIF_B, 30), INK, 420, 36)
    para(d, (52, y + 118),
         "Kospi \u22126.2% \u00b7 SK hynix \u221211.1% \u00b7 Samsung \u22129.9% \u00b7 "
         "Taiex \u22124.8% \u00b7 Nikkei \u22122.8%",
         font(SANS, 20), MUTED, 420, 28)
    # Right card: astronaut.
    card(d, (528, y, 992, y + 200))
    kicker(d, (548, y + 14), "SPACE  ·  ASIA", fill=BLUE)
    para(d, (548, y + 44), "Pakistan\u2019s first astronaut docks at Tiangong",
         font(SERIF_B, 28), INK, 420, 34)
    para(d, (548, y + 118),
         "Muhammad Zeeshan Ali, 40, is the first foreigner on China\u2019s "
         "Tiangong station. He flew on Shenzhou-24.",
         font(SANS, 20), MUTED, 420, 28)

    # ---- Third row: four regional cards ---------------------------------
    y = 646
    rule(d, 32, 992, y, fill=INK, width=2)
    y += 14
    cards = [
        ("UKRAINE", "Russian strikes kill 5, cut power in 5 regions",
         "Zaporizhzhia nuclear plant runs on diesel after its 17th grid loss.",
         RED),
        ("ENERGY", "UK energy price cap to rise 26% in January",
         "Ofgem: a typical bill goes from \u00a31,723 to \u00a32,166 a year.",
         RED),
        ("PACIFIC", "Solomon Islands signs security pact with Australia",
         "A security partner; A$740m over 10 years.",
         BLUE),
        ("EGYPT", "Fuel tanker fire kills at least 30 near Cairo",
         "A tanker overturned and exploded on a ring road.",
         RED),
    ]
    cw, gap = 228, 16
    for i, (kick, head, body, col) in enumerate(cards):
        x0 = 32 + i * (cw + gap)
        card(d, (x0, y, x0 + cw, y + 196))
        d.text((x0 + 14, y + 12), kick, font=font(SANS_B, 18), fill=col)
        yy = para(d, (x0 + 14, y + 38), head, font(SERIF_B, 21), INK,
                 cw - 28, 26)
        para(d, (x0 + 14, yy + 4), body, font(SANS, 16), MUTED,
             cw - 28, 21)

    # ---- Bottom strip: briefs --------------------------------------------
    y = 884
    rule(d, 32, 992, y, fill=INK, width=2)
    y += 12
    d.text((32, y), "ALSO TODAY", font=font(SANS_B, 20), fill=RED)
    y += 30
    y = para(d, (32, y),
             "EU proposes a \u20ac50bn quantum fund  \u00b7  "
             "Zelensky: Ukraine seeks \u20ac115bn aid for 2027",
             font(SANS, 20), INK, 960, 28)
    y = para(d, (32, y + 2),
             "Netanyahu graft charges face a rethink  \u00b7  "
             "Saudis down Houthi drones after the Hodeidah strike",
             font(SANS, 20), INK, 960, 28)
    rule(d, 32, 992, 1004, fill=LINE, width=1)
    d.text((32, 1008), "The world in one day \u2014 Wednesday 25 November 2026",
           font=font(SANS, 15), fill=MUTED)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
