"""
Shree Krishna Birth Story - Kids Story Book with Cute Illustrations
Beautiful illustrated book for children about Lord Krishna's birth
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import (
    black, white, gray, lightgrey, HexColor, Color,
    red, blue, green, orange, purple, pink, yellow, brown
)
from reportlab.lib import colors
import math
import os

OUTPUT_DIR = "D:/Nidhi/n8n/Card Scan/Sample_Books"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PAGE_W, PAGE_H = A4

# ─── COLOR PALETTE ───
KRISHNA_BLUE = HexColor("#5B9BD5")
KRISHNA_DARK_BLUE = HexColor("#2E75B6")
KRISHNA_SKIN = HexColor("#7EC8E3")
GOLDEN = HexColor("#FFD700")
GOLDEN_DARK = HexColor("#DAA520")
SAFFRON = HexColor("#FF9933")
DEEP_RED = HexColor("#C0392B")
CREAM = HexColor("#FFF8DC")
SKY_BLUE = HexColor("#87CEEB")
DARK_SKY = HexColor("#1A1A3E")
NIGHT_BLUE = HexColor("#0D1B2A")
FOREST_GREEN = HexColor("#228B22")
LIGHT_GREEN = HexColor("#90EE90")
RIVER_BLUE = HexColor("#4A90D9")
WARM_YELLOW = HexColor("#FFF3CD")
SOFT_PINK = HexColor("#FFB6C1")
PEACOCK_GREEN = HexColor("#00A86B")
PEACOCK_BLUE = HexColor("#007BA7")
SKIN_TONE = HexColor("#F5CBA7")
DARK_BROWN = HexColor("#5D4037")
LIGHT_BROWN = HexColor("#8D6E63")
PRISON_GRAY = HexColor("#4A4A4A")
CHAIN_COLOR = HexColor("#808080")
LOTUS_PINK = HexColor("#FF69B4")
GLOW_YELLOW = HexColor("#FFFACD")


def draw_page_number(c, page_num):
    c.setFont("Helvetica", 9)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W / 2, 20, f"- {page_num} -")


def draw_stars(c, count=15, y_min=500, y_max=780):
    """Draw twinkling stars"""
    import random
    random.seed(42)
    c.setFillColor(GOLDEN)
    for _ in range(count):
        x = random.randint(30, int(PAGE_W - 30))
        y = random.randint(y_min, y_max)
        size = random.choice([1.5, 2, 2.5, 3])
        c.circle(x, y, size, fill=1, stroke=0)
        # Twinkle lines
        if size > 2:
            c.setStrokeColor(HexColor("#FFE066"))
            c.setLineWidth(0.5)
            c.line(x - 5, y, x + 5, y)
            c.line(x, y - 5, x, y + 5)


def draw_cute_face(c, cx, cy, radius, skin_color, is_baby=False, is_krishna=False):
    """Draw a cute cartoon face"""
    # Face circle
    c.setFillColor(skin_color)
    c.setStrokeColor(HexColor("#8B6914") if is_krishna else DARK_BROWN)
    c.setLineWidth(1.5)
    c.circle(cx, cy, radius, fill=1)

    eye_r = radius * 0.15
    eye_dist = radius * 0.3
    eye_y = cy + radius * 0.1

    # Eyes - big cute eyes
    # White
    c.setFillColor(white)
    c.circle(cx - eye_dist, eye_y, eye_r * 1.4, fill=1, stroke=0)
    c.circle(cx + eye_dist, eye_y, eye_r * 1.4, fill=1, stroke=0)
    # Iris
    c.setFillColor(HexColor("#2C1810"))
    c.circle(cx - eye_dist, eye_y, eye_r, fill=1, stroke=0)
    c.circle(cx + eye_dist, eye_y, eye_r, fill=1, stroke=0)
    # Sparkle
    c.setFillColor(white)
    c.circle(cx - eye_dist + eye_r * 0.3, eye_y + eye_r * 0.3, eye_r * 0.35, fill=1, stroke=0)
    c.circle(cx + eye_dist + eye_r * 0.3, eye_y + eye_r * 0.3, eye_r * 0.35, fill=1, stroke=0)

    # Cute smile
    smile_w = radius * 0.35
    smile_y = cy - radius * 0.2
    c.setStrokeColor(HexColor("#8B4513"))
    c.setLineWidth(1.2)
    p = c.beginPath()
    p.moveTo(cx - smile_w, smile_y)
    p.curveTo(cx - smile_w * 0.5, smile_y - radius * 0.2,
              cx + smile_w * 0.5, smile_y - radius * 0.2,
              cx + smile_w, smile_y)
    c.drawPath(p, fill=0, stroke=1)

    # Blush cheeks
    c.setFillColor(Color(1, 0.6, 0.6, alpha=0.4))
    c.circle(cx - radius * 0.5, cy - radius * 0.1, radius * 0.15, fill=1, stroke=0)
    c.circle(cx + radius * 0.5, cy - radius * 0.1, radius * 0.15, fill=1, stroke=0)

    if is_baby:
        # Tiny nose
        c.setFillColor(Color(0.8, 0.5, 0.3, alpha=0.5))
        c.circle(cx, cy - radius * 0.05, radius * 0.06, fill=1, stroke=0)


def draw_crown(c, cx, cy, width, height):
    """Draw a royal crown"""
    c.setFillColor(GOLDEN)
    c.setStrokeColor(GOLDEN_DARK)
    c.setLineWidth(1.5)
    # Base
    p = c.beginPath()
    p.moveTo(cx - width / 2, cy)
    p.lineTo(cx - width / 2, cy + height * 0.4)
    p.lineTo(cx - width * 0.3, cy + height * 0.7)
    p.lineTo(cx - width * 0.15, cy + height * 0.5)
    p.lineTo(cx, cy + height)
    p.lineTo(cx + width * 0.15, cy + height * 0.5)
    p.lineTo(cx + width * 0.3, cy + height * 0.7)
    p.lineTo(cx + width / 2, cy + height * 0.4)
    p.lineTo(cx + width / 2, cy)
    p.close()
    c.drawPath(p, fill=1, stroke=1)
    # Gems
    c.setFillColor(DEEP_RED)
    c.circle(cx, cy + height * 0.4, 3, fill=1, stroke=0)
    c.setFillColor(HexColor("#00CED1"))
    c.circle(cx - width * 0.25, cy + height * 0.35, 2.5, fill=1, stroke=0)
    c.circle(cx + width * 0.25, cy + height * 0.35, 2.5, fill=1, stroke=0)


def draw_peacock_feather(c, cx, cy, scale=1.0):
    """Draw a cute peacock feather"""
    s = scale
    c.saveState()
    # Stem
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1.5 * s)
    p = c.beginPath()
    p.moveTo(cx, cy)
    p.curveTo(cx + 5 * s, cy + 40 * s, cx - 5 * s, cy + 80 * s, cx + 2 * s, cy + 120 * s)
    c.drawPath(p, fill=0, stroke=1)

    # Feather eye
    ey = cy + 95 * s
    # Outer
    c.setFillColor(PEACOCK_BLUE)
    c.saveState()
    c.translate(cx, ey)
    c.scale(0.7 * s, 1.0 * s)
    c.circle(0, 0, 18, fill=1, stroke=0)
    c.restoreState()
    # Middle
    c.setFillColor(PEACOCK_GREEN)
    c.saveState()
    c.translate(cx, ey)
    c.scale(0.6 * s, 0.85 * s)
    c.circle(0, 0, 13, fill=1, stroke=0)
    c.restoreState()
    # Inner
    c.setFillColor(GOLDEN)
    c.saveState()
    c.translate(cx, ey)
    c.scale(0.5 * s, 0.7 * s)
    c.circle(0, 0, 8, fill=1, stroke=0)
    c.restoreState()
    # Center dot
    c.setFillColor(NIGHT_BLUE)
    c.circle(cx, ey, 3 * s, fill=1, stroke=0)

    # Side feather wisps
    c.setStrokeColor(PEACOCK_GREEN)
    c.setLineWidth(0.8 * s)
    for angle in range(-40, 41, 10):
        rad = math.radians(angle)
        length = 25 * s
        ex = cx + length * math.sin(rad)
        ey2 = ey + length * math.cos(rad) * 0.5
        c.line(cx, ey - 5 * s, ex, ey2)

    c.restoreState()


def draw_flute(c, cx, cy, length=80, angle=15):
    """Draw Krishna's flute"""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(angle)

    # Flute body
    c.setFillColor(HexColor("#DEB887"))
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1)
    c.roundRect(-length / 2, -6, length, 12, 5, fill=1)

    # Holes
    c.setFillColor(DARK_BROWN)
    for i in range(5):
        hx = -length / 2 + 20 + i * 12
        c.circle(hx, 0, 2.5, fill=1, stroke=0)

    # Ribbon
    c.setFillColor(SAFFRON)
    c.setStrokeColor(HexColor("#E67E22"))
    c.setLineWidth(0.8)
    p = c.beginPath()
    p.moveTo(length / 2 - 5, 0)
    p.curveTo(length / 2 + 10, 10, length / 2 + 15, -5, length / 2 + 25, 5)
    c.drawPath(p, fill=0, stroke=1)
    p = c.beginPath()
    p.moveTo(length / 2 - 5, 0)
    p.curveTo(length / 2 + 8, -12, length / 2 + 18, 3, length / 2 + 22, -8)
    c.drawPath(p, fill=0, stroke=1)

    c.restoreState()


def draw_lotus(c, cx, cy, size=20):
    """Draw a lotus flower"""
    # Petals
    num_petals = 8
    for i in range(num_petals):
        angle = math.radians(i * 360 / num_petals)
        px = cx + size * 0.5 * math.cos(angle)
        py = cy + size * 0.5 * math.sin(angle)

        c.saveState()
        c.setFillColor(LOTUS_PINK)
        c.setStrokeColor(HexColor("#FF1493"))
        c.setLineWidth(0.5)
        c.translate(px, py)
        c.rotate(math.degrees(angle) - 90)
        c.scale(0.4, 1)
        c.circle(0, 0, size * 0.5, fill=1)
        c.restoreState()

    # Center
    c.setFillColor(GOLDEN)
    c.circle(cx, cy, size * 0.25, fill=1, stroke=0)


def draw_baby_krishna(c, cx, cy, size=1.0):
    """Draw cute baby Krishna"""
    s = size

    # Body (round cute baby body)
    c.setFillColor(KRISHNA_SKIN)
    c.setStrokeColor(KRISHNA_DARK_BLUE)
    c.setLineWidth(1)
    # Torso
    c.saveState()
    c.translate(cx, cy - 10 * s)
    c.scale(1, 0.8)
    c.circle(0, 0, 25 * s, fill=1)
    c.restoreState()

    # Yellow dhoti
    c.setFillColor(GOLDEN)
    c.setStrokeColor(GOLDEN_DARK)
    c.setLineWidth(1)
    p = c.beginPath()
    p.moveTo(cx - 22 * s, cy - 10 * s)
    p.curveTo(cx - 25 * s, cy - 35 * s, cx + 25 * s, cy - 35 * s, cx + 22 * s, cy - 10 * s)
    p.close()
    c.drawPath(p, fill=1, stroke=1)

    # Cute little hands
    c.setFillColor(KRISHNA_SKIN)
    c.circle(cx - 28 * s, cy - 5 * s, 7 * s, fill=1, stroke=0)
    c.circle(cx + 28 * s, cy - 5 * s, 7 * s, fill=1, stroke=0)

    # Cute little feet
    c.circle(cx - 12 * s, cy - 38 * s, 6 * s, fill=1, stroke=0)
    c.circle(cx + 12 * s, cy - 38 * s, 6 * s, fill=1, stroke=0)

    # Head
    draw_cute_face(c, cx, cy + 25 * s, 20 * s, KRISHNA_SKIN, is_baby=True, is_krishna=True)

    # Cute curly hair
    c.setFillColor(HexColor("#1A1A2E"))
    for angle_deg in range(-60, 70, 20):
        angle = math.radians(angle_deg)
        hx = cx + 20 * s * math.cos(angle)
        hy = cy + 25 * s + 20 * s * math.sin(angle)
        c.circle(hx, hy, 5 * s, fill=1, stroke=0)
    # Top hair puff
    c.circle(cx, cy + 47 * s, 8 * s, fill=1, stroke=0)
    c.circle(cx - 7 * s, cy + 45 * s, 6 * s, fill=1, stroke=0)
    c.circle(cx + 7 * s, cy + 45 * s, 6 * s, fill=1, stroke=0)

    # Peacock feather on head
    draw_peacock_feather(c, cx + 3 * s, cy + 45 * s, scale=0.4 * s)

    # Golden necklace
    c.setStrokeColor(GOLDEN)
    c.setLineWidth(1.5)
    c.arc(cx - 15 * s, cy, cx + 15 * s, cy + 20 * s, 200, 140)

    # Butter ball (makhan) - optional cute element
    c.setFillColor(HexColor("#FFF8DC"))
    c.setStrokeColor(HexColor("#DAA520"))
    c.setLineWidth(0.8)
    # Pot
    c.circle(cx + 32 * s, cy - 5 * s, 10 * s, fill=1)
    # Butter on top
    c.setFillColor(GOLDEN)
    c.circle(cx + 32 * s, cy + 4 * s, 6 * s, fill=1, stroke=0)


def draw_glow(c, cx, cy, radius, color=GOLDEN, alpha_start=0.3):
    """Draw a divine glow effect"""
    for i in range(5):
        factor = 1 + i * 0.3
        a = alpha_start * (1 - i * 0.18)
        r, g, b = color.red, color.green, color.blue
        c.setFillColor(Color(r, g, b, alpha=max(a, 0.05)))
        c.circle(cx, cy, radius * factor, fill=1, stroke=0)


# ═══════════════════════════════════════════════════
# MAIN BOOK CREATION
# ═══════════════════════════════════════════════════

def create_krishna_book():
    filepath = os.path.join(OUTPUT_DIR, "05_Shree_Krishna_Birth_Story.pdf")
    c = canvas.Canvas(filepath, pagesize=A4)
    c.setTitle("Shree Krishna Birth Story - For Kids")
    c.setAuthor("Kids Book Publisher")

    page_num = 0

    # ════════════════════════════════════════
    # COVER PAGE
    # ════════════════════════════════════════
    # Night sky gradient
    for i in range(50):
        y = PAGE_H - i * (PAGE_H / 50)
        ratio = i / 50
        r = 0.05 + ratio * 0.02
        g = 0.1 + ratio * 0.05
        b = 0.25 - ratio * 0.1
        c.setFillColor(Color(r, g, b))
        c.rect(0, y, PAGE_W, PAGE_H / 50 + 1, fill=1, stroke=0)

    # Stars
    draw_stars(c, count=40, y_min=200, y_max=int(PAGE_H - 50))

    # Moon
    c.setFillColor(GLOW_YELLOW)
    c.circle(PAGE_W - 100, PAGE_H - 120, 50, fill=1, stroke=0)
    c.setFillColor(DARK_SKY)
    c.circle(PAGE_W - 80, PAGE_H - 105, 45, fill=1, stroke=0)

    # Divine glow in center
    draw_glow(c, PAGE_W / 2, PAGE_H / 2 + 50, 80, GOLDEN, 0.15)

    # Baby Krishna
    draw_baby_krishna(c, PAGE_W / 2, PAGE_H / 2 + 40, size=2.2)

    # Lotus base
    for i in range(3):
        draw_lotus(c, PAGE_W / 2 - 40 + i * 40, PAGE_H / 2 - 60, size=25)

    # Title
    c.setFillColor(GOLDEN)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 70, "Shree Krishna")

    c.setFont("Helvetica-Bold", 28)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 110, "Birth Story")

    # Subtitle
    c.setFillColor(white)
    c.setFont("Helvetica", 16)
    c.drawCentredString(PAGE_W / 2, 120, "A Beautiful Story for Little Ones")

    c.setFillColor(GOLDEN)
    c.setFont("Helvetica", 13)
    c.drawCentredString(PAGE_W / 2, 90, "~ Janmashtami Special ~")

    # Decorative line
    c.setStrokeColor(GOLDEN)
    c.setLineWidth(1)
    c.line(PAGE_W / 2 - 80, 80, PAGE_W / 2 + 80, 80)

    c.setFillColor(Color(1, 1, 1, alpha=0.5))
    c.setFont("Helvetica", 10)
    c.drawCentredString(PAGE_W / 2, 50, "For Kids Ages 3-10")

    c.showPage()
    page_num += 1

    # ════════════════════════════════════════
    # PAGE 1: MATHURA KINGDOM
    # ════════════════════════════════════════
    # Sky
    c.setFillColor(SKY_BLUE)
    c.rect(0, PAGE_H / 2, PAGE_W, PAGE_H / 2, fill=1, stroke=0)

    # Sun
    c.setFillColor(GOLDEN)
    c.circle(100, PAGE_H - 80, 35, fill=1, stroke=0)
    # Sun rays
    c.setStrokeColor(GOLDEN)
    c.setLineWidth(2)
    for a in range(0, 360, 30):
        rad = math.radians(a)
        c.line(100 + 40 * math.cos(rad), PAGE_H - 80 + 40 * math.sin(rad),
               100 + 55 * math.cos(rad), PAGE_H - 80 + 55 * math.sin(rad))

    # Clouds
    for cx_c, cy_c in [(200, PAGE_H - 60), (400, PAGE_H - 90), (500, PAGE_H - 55)]:
        c.setFillColor(white)
        c.circle(cx_c, cy_c, 25, fill=1, stroke=0)
        c.circle(cx_c - 20, cy_c - 5, 20, fill=1, stroke=0)
        c.circle(cx_c + 20, cy_c - 5, 20, fill=1, stroke=0)
        c.circle(cx_c + 10, cy_c + 10, 18, fill=1, stroke=0)

    # Ground
    c.setFillColor(LIGHT_GREEN)
    c.rect(0, PAGE_H / 2 - 20, PAGE_W, 30, fill=1, stroke=0)

    # Palace
    c.setFillColor(HexColor("#F5DEB3"))
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1.5)
    # Main building
    c.rect(150, PAGE_H / 2, 300, 150, fill=1)
    # Dome
    c.setFillColor(SAFFRON)
    c.arc(250, PAGE_H / 2 + 130, 350, PAGE_H / 2 + 200, 0, 180)
    # Towers
    c.setFillColor(HexColor("#F5DEB3"))
    c.rect(150, PAGE_H / 2, 50, 180, fill=1)
    c.rect(400, PAGE_H / 2, 50, 180, fill=1)
    # Tower tops
    c.setFillColor(SAFFRON)
    for tx in [175, 425]:
        p = c.beginPath()
        p.moveTo(tx - 20, PAGE_H / 2 + 180)
        p.lineTo(tx, PAGE_H / 2 + 220)
        p.lineTo(tx + 20, PAGE_H / 2 + 180)
        p.close()
        c.drawPath(p, fill=1, stroke=1)
    # Flag
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1)
    c.line(300, PAGE_H / 2 + 200, 300, PAGE_H / 2 + 240)
    c.setFillColor(SAFFRON)
    p = c.beginPath()
    p.moveTo(300, PAGE_H / 2 + 240)
    p.lineTo(330, PAGE_H / 2 + 230)
    p.lineTo(300, PAGE_H / 2 + 220)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # Windows
    c.setFillColor(SKY_BLUE)
    for wx in [200, 270, 340]:
        c.rect(wx, PAGE_H / 2 + 80, 30, 40, fill=1)
        c.setFillColor(HexColor("#DEB887"))
        c.rect(wx + 13, PAGE_H / 2 + 80, 4, 40, fill=1)
        c.setFillColor(SKY_BLUE)
    # Gate
    c.setFillColor(DARK_BROWN)
    c.rect(275, PAGE_H / 2, 50, 60, fill=1)
    c.setFillColor(GOLDEN)
    c.arc(275, PAGE_H / 2 + 30, 325, PAGE_H / 2 + 75, 0, 180)

    # Trees
    for tx in [80, 500]:
        c.setFillColor(DARK_BROWN)
        c.rect(tx - 8, PAGE_H / 2 - 10, 16, 60, fill=1, stroke=0)
        c.setFillColor(FOREST_GREEN)
        c.circle(tx, PAGE_H / 2 + 60, 35, fill=1, stroke=0)
        c.setFillColor(LIGHT_GREEN)
        c.circle(tx + 10, PAGE_H / 2 + 70, 20, fill=1, stroke=0)

    # Text area
    c.setFillColor(CREAM)
    c.roundRect(30, 40, PAGE_W - 60, PAGE_H / 2 - 80, 15, fill=1, stroke=0)

    # Decorative border
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(2)
    c.roundRect(35, 45, PAGE_W - 70, PAGE_H / 2 - 90, 12, fill=0)

    # Om symbol decoration
    c.setFillColor(SAFFRON)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 55, "~ * ~")

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 80, "The Kingdom of Mathura")

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#333333"))
    story_lines = [
        "Long, long ago, there was a beautiful kingdom",
        "called Mathura. It had grand palaces, lovely",
        "gardens, and happy people everywhere.",
        "",
        "But one day, a cruel king named Kansa",
        "took over the kingdom. He was very mean",
        "and made everyone sad and scared.",
    ]
    y = PAGE_H / 2 - 110
    for line in story_lines:
        c.drawCentredString(PAGE_W / 2, y, line)
        y -= 22

    draw_page_number(c, page_num)
    c.showPage()
    page_num += 1

    # ════════════════════════════════════════
    # PAGE 2: KANSA AND DEVAKI
    # ════════════════════════════════════════
    # Palace interior
    c.setFillColor(HexColor("#FFF0DB"))
    c.rect(0, PAGE_H / 2, PAGE_W, PAGE_H / 2, fill=1, stroke=0)

    # Pillars
    for px in [60, PAGE_W - 60]:
        c.setFillColor(HexColor("#DEB887"))
        c.setStrokeColor(DARK_BROWN)
        c.setLineWidth(1)
        c.rect(px - 15, PAGE_H / 2, 30, PAGE_H / 2, fill=1)
        c.setFillColor(GOLDEN_DARK)
        c.rect(px - 18, PAGE_H / 2, 36, 15, fill=1)
        c.rect(px - 18, PAGE_H - 20, 36, 15, fill=1)

    # Curtains
    for side in [-1, 1]:
        cx_cur = PAGE_W / 2 + side * 220
        c.setFillColor(Color(0.8, 0.1, 0.1, alpha=0.7))
        p = c.beginPath()
        p.moveTo(cx_cur, PAGE_H)
        p.curveTo(cx_cur + side * 40, PAGE_H - 100,
                  cx_cur - side * 20, PAGE_H - 200,
                  cx_cur + side * 10, PAGE_H / 2)
        p.lineTo(cx_cur, PAGE_H / 2)
        p.close()
        c.drawPath(p, fill=1, stroke=0)

    # Kansa (angry face, crown, dark clothes)
    kx = PAGE_W / 2 - 100
    ky = PAGE_H / 2 + 150

    # Kansa body
    c.setFillColor(HexColor("#2C2C2C"))
    c.setStrokeColor(black)
    c.setLineWidth(1)
    p = c.beginPath()
    p.moveTo(kx - 35, ky - 40)
    p.lineTo(kx + 35, ky - 40)
    p.lineTo(kx + 30, ky + 30)
    p.lineTo(kx - 30, ky + 30)
    p.close()
    c.drawPath(p, fill=1, stroke=1)

    # Kansa face (angry)
    c.setFillColor(HexColor("#CD853F"))
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1.2)
    c.circle(kx, ky + 55, 28, fill=1)
    # Angry eyes
    c.setFillColor(white)
    c.circle(kx - 10, ky + 60, 6, fill=1, stroke=0)
    c.circle(kx + 10, ky + 60, 6, fill=1, stroke=0)
    c.setFillColor(HexColor("#8B0000"))
    c.circle(kx - 10, ky + 59, 3.5, fill=1, stroke=0)
    c.circle(kx + 10, ky + 59, 3.5, fill=1, stroke=0)
    # Angry eyebrows
    c.setStrokeColor(black)
    c.setLineWidth(2)
    c.line(kx - 17, ky + 68, kx - 5, ky + 70)
    c.line(kx + 17, ky + 68, kx + 5, ky + 70)
    # Frown
    c.setLineWidth(1.5)
    p = c.beginPath()
    p.moveTo(kx - 10, ky + 45)
    p.curveTo(kx - 5, ky + 50, kx + 5, ky + 50, kx + 10, ky + 45)
    c.drawPath(p, fill=0, stroke=1)
    # Crown
    draw_crown(c, kx, ky + 78, 40, 25)
    # Mustache
    c.setFillColor(black)
    c.setLineWidth(1)
    p = c.beginPath()
    p.moveTo(kx - 3, ky + 50)
    p.curveTo(kx - 15, ky + 52, kx - 20, ky + 45, kx - 22, ky + 48)
    c.drawPath(p, fill=0, stroke=1)
    p = c.beginPath()
    p.moveTo(kx + 3, ky + 50)
    p.curveTo(kx + 15, ky + 52, kx + 20, ky + 45, kx + 22, ky + 48)
    c.drawPath(p, fill=0, stroke=1)

    # Devaki and Vasudev (sweet couple, sad)
    dx = PAGE_W / 2 + 100
    dy = PAGE_H / 2 + 140

    # Vasudev
    c.setFillColor(HexColor("#F0E68C"))
    p = c.beginPath()
    p.moveTo(dx + 25, dy - 30)
    p.lineTo(dx + 55, dy - 30)
    p.lineTo(dx + 50, dy + 30)
    p.lineTo(dx + 30, dy + 30)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # Face
    c.setFillColor(SKIN_TONE)
    c.circle(dx + 40, dy + 50, 18, fill=1, stroke=0)
    # Eyes (sad)
    c.setFillColor(HexColor("#2C1810"))
    c.circle(dx + 35, dy + 52, 2.5, fill=1, stroke=0)
    c.circle(dx + 45, dy + 52, 2.5, fill=1, stroke=0)
    # Sad mouth
    c.setStrokeColor(HexColor("#8B4513"))
    c.setLineWidth(1)
    p = c.beginPath()
    p.moveTo(dx + 35, dy + 42)
    p.curveTo(dx + 38, dy + 45, dx + 42, dy + 45, dx + 45, dy + 42)
    c.drawPath(p, fill=0, stroke=1)
    # Hair
    c.setFillColor(HexColor("#1A1A2E"))
    c.circle(dx + 40, dy + 67, 16, fill=1, stroke=0)

    # Devaki
    c.setFillColor(DEEP_RED)
    p = c.beginPath()
    p.moveTo(dx - 15, dy - 30)
    p.lineTo(dx + 15, dy - 30)
    p.lineTo(dx + 10, dy + 30)
    p.lineTo(dx - 10, dy + 30)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # Dupatta
    c.setFillColor(Color(1, 0.2, 0.2, alpha=0.6))
    p = c.beginPath()
    p.moveTo(dx - 5, dy + 65)
    p.curveTo(dx - 25, dy + 50, dx - 30, dy + 20, dx - 20, dy - 10)
    p.lineTo(dx - 10, dy - 10)
    p.curveTo(dx - 20, dy + 20, dx - 15, dy + 45, dx + 5, dy + 60)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # Face
    c.setFillColor(SKIN_TONE)
    c.circle(dx, dy + 50, 18, fill=1, stroke=0)
    # Big sad eyes
    c.setFillColor(white)
    c.circle(dx - 6, dy + 53, 5, fill=1, stroke=0)
    c.circle(dx + 6, dy + 53, 5, fill=1, stroke=0)
    c.setFillColor(HexColor("#2C1810"))
    c.circle(dx - 6, dy + 52, 3, fill=1, stroke=0)
    c.circle(dx + 6, dy + 52, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.circle(dx - 5, dy + 53, 1.2, fill=1, stroke=0)
    c.circle(dx + 7, dy + 53, 1.2, fill=1, stroke=0)
    # Sad eyebrows
    c.setStrokeColor(HexColor("#5D4037"))
    c.setLineWidth(1)
    c.line(dx - 10, dy + 60, dx - 3, dy + 62)
    c.line(dx + 10, dy + 60, dx + 3, dy + 62)
    # Tear drop
    c.setFillColor(Color(0.5, 0.8, 1, alpha=0.7))
    c.circle(dx - 12, dy + 47, 2, fill=1, stroke=0)
    # Bindi
    c.setFillColor(DEEP_RED)
    c.circle(dx, dy + 62, 2, fill=1, stroke=0)
    # Hair
    c.setFillColor(HexColor("#1A1A2E"))
    c.circle(dx, dy + 67, 16, fill=1, stroke=0)

    # Text area
    c.setFillColor(CREAM)
    c.roundRect(30, 40, PAGE_W - 60, PAGE_H / 2 - 80, 15, fill=1, stroke=0)
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(2)
    c.roundRect(35, 45, PAGE_W - 70, PAGE_H / 2 - 90, 12, fill=0)

    c.setFillColor(SAFFRON)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 55, "~ * ~")

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 80, "The Cruel King Kansa")

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#333333"))
    lines = [
        "Kansa had a sweet sister named Devaki.",
        "She married a kind prince named Vasudev.",
        "",
        "But one day, a voice from the sky said:",
        "'Devaki's 8th child will defeat you, Kansa!'",
        "",
        "Kansa got very angry and scared!",
        "He locked Devaki and Vasudev in a dark prison.",
    ]
    y = PAGE_H / 2 - 110
    for line in lines:
        if line.startswith("'"):
            c.setFont("Helvetica-BoldOblique", 14)
            c.setFillColor(DEEP_RED)
        else:
            c.setFont("Helvetica", 14)
            c.setFillColor(HexColor("#333333"))
        c.drawCentredString(PAGE_W / 2, y, line)
        y -= 22

    draw_page_number(c, page_num)
    c.showPage()
    page_num += 1

    # ════════════════════════════════════════
    # PAGE 3: PRISON AND DIVINE PROPHECY
    # ════════════════════════════════════════
    # Dark prison background
    c.setFillColor(HexColor("#1A1A1A"))
    c.rect(0, PAGE_H / 2, PAGE_W, PAGE_H / 2, fill=1, stroke=0)

    # Stone wall texture
    c.setStrokeColor(HexColor("#333333"))
    c.setLineWidth(0.5)
    for row in range(12):
        y_brick = PAGE_H / 2 + row * 35
        offset = 30 if row % 2 else 0
        for col in range(10):
            x_brick = -30 + offset + col * 65
            c.rect(x_brick, y_brick, 60, 30, fill=0)

    # Window with bars
    wx, wy = PAGE_W / 2, PAGE_H - 80
    c.setFillColor(DARK_SKY)
    c.rect(wx - 30, wy - 25, 60, 50, fill=1)
    c.setStrokeColor(CHAIN_COLOR)
    c.setLineWidth(3)
    for i in range(4):
        bx = wx - 20 + i * 14
        c.line(bx, wy - 25, bx, wy + 25)

    # Moon through window
    c.setFillColor(GLOW_YELLOW)
    c.circle(wx, wy, 12, fill=1, stroke=0)

    # Stars through window
    c.setFillColor(white)
    for sx, sy in [(wx - 15, wy + 15), (wx + 18, wy + 10), (wx - 8, wy - 15)]:
        c.circle(sx, sy, 1.5, fill=1, stroke=0)

    # Chains on wall
    c.setStrokeColor(CHAIN_COLOR)
    c.setLineWidth(2)
    for chain_x in [120, PAGE_W - 120]:
        for i in range(5):
            cy_chain = PAGE_H - 200 + i * 20
            c.circle(chain_x, cy_chain, 6, fill=0)

    # Devaki and Vasudev in prison (sad, sitting)
    # Devaki sitting
    c.setFillColor(DEEP_RED)
    c.roundRect(PAGE_W / 2 - 80, PAGE_H / 2 + 40, 40, 50, 5, fill=1, stroke=0)
    c.setFillColor(SKIN_TONE)
    c.circle(PAGE_W / 2 - 60, PAGE_H / 2 + 110, 18, fill=1, stroke=0)
    # Sad eyes with tears
    c.setFillColor(HexColor("#2C1810"))
    c.circle(PAGE_W / 2 - 66, PAGE_H / 2 + 112, 2.5, fill=1, stroke=0)
    c.circle(PAGE_W / 2 - 54, PAGE_H / 2 + 112, 2.5, fill=1, stroke=0)
    c.setFillColor(Color(0.5, 0.8, 1, alpha=0.8))
    c.circle(PAGE_W / 2 - 68, PAGE_H / 2 + 105, 2, fill=1, stroke=0)
    c.circle(PAGE_W / 2 - 52, PAGE_H / 2 + 105, 2, fill=1, stroke=0)
    # Hair & dupatta
    c.setFillColor(HexColor("#1A1A2E"))
    c.circle(PAGE_W / 2 - 60, PAGE_H / 2 + 126, 16, fill=1, stroke=0)
    c.setFillColor(Color(0.8, 0.1, 0.1, alpha=0.5))
    p = c.beginPath()
    p.moveTo(PAGE_W / 2 - 75, PAGE_H / 2 + 126)
    p.curveTo(PAGE_W / 2 - 85, PAGE_H / 2 + 100, PAGE_W / 2 - 80, PAGE_H / 2 + 70, PAGE_W / 2 - 85, PAGE_H / 2 + 50)
    p.lineTo(PAGE_W / 2 - 75, PAGE_H / 2 + 50)
    p.curveTo(PAGE_W / 2 - 70, PAGE_H / 2 + 70, PAGE_W / 2 - 75, PAGE_H / 2 + 100, PAGE_W / 2 - 65, PAGE_H / 2 + 120)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    # Vasudev sitting
    c.setFillColor(HexColor("#F0E68C"))
    c.roundRect(PAGE_W / 2 + 40, PAGE_H / 2 + 40, 40, 50, 5, fill=1, stroke=0)
    c.setFillColor(SKIN_TONE)
    c.circle(PAGE_W / 2 + 60, PAGE_H / 2 + 110, 18, fill=1, stroke=0)
    c.setFillColor(HexColor("#2C1810"))
    c.circle(PAGE_W / 2 + 54, PAGE_H / 2 + 112, 2.5, fill=1, stroke=0)
    c.circle(PAGE_W / 2 + 66, PAGE_H / 2 + 112, 2.5, fill=1, stroke=0)
    c.setFillColor(HexColor("#1A1A2E"))
    c.circle(PAGE_W / 2 + 60, PAGE_H / 2 + 126, 16, fill=1, stroke=0)

    # Prayer gesture (folded hands between them)
    c.setFillColor(SKIN_TONE)
    for hx in [PAGE_W / 2 - 40, PAGE_W / 2 + 38]:
        c.circle(hx, PAGE_H / 2 + 80, 5, fill=1, stroke=0)

    # Lamp / Diya
    c.setFillColor(GOLDEN)
    c.circle(PAGE_W / 2, PAGE_H / 2 + 45, 8, fill=1, stroke=0)
    # Flame
    c.setFillColor(Color(1, 0.8, 0, alpha=0.9))
    p = c.beginPath()
    p.moveTo(PAGE_W / 2, PAGE_H / 2 + 55)
    p.curveTo(PAGE_W / 2 - 4, PAGE_H / 2 + 65, PAGE_W / 2 + 4, PAGE_H / 2 + 70, PAGE_W / 2, PAGE_H / 2 + 75)
    p.curveTo(PAGE_W / 2 + 3, PAGE_H / 2 + 68, PAGE_W / 2 - 3, PAGE_H / 2 + 63, PAGE_W / 2, PAGE_H / 2 + 55)
    c.drawPath(p, fill=1, stroke=0)
    # Glow from lamp
    draw_glow(c, PAGE_W / 2, PAGE_H / 2 + 60, 20, GOLDEN, 0.1)

    # Text area
    c.setFillColor(CREAM)
    c.roundRect(30, 40, PAGE_W - 60, PAGE_H / 2 - 80, 15, fill=1, stroke=0)
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(2)
    c.roundRect(35, 45, PAGE_W - 70, PAGE_H / 2 - 90, 12, fill=0)

    c.setFillColor(SAFFRON)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 55, "~ * ~")

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 80, "The Dark Prison")

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#333333"))
    lines = [
        "Devaki and Vasudev were very sad in prison.",
        "The prison was dark, cold, and scary.",
        "",
        "But they never lost hope. They prayed",
        "to Lord Vishnu every day and every night.",
        "",
        "They believed that God would help them",
        "and save everyone from mean King Kansa.",
    ]
    y = PAGE_H / 2 - 110
    for line in lines:
        c.drawCentredString(PAGE_W / 2, y, line)
        y -= 22

    draw_page_number(c, page_num)
    c.showPage()
    page_num += 1

    # ════════════════════════════════════════
    # PAGE 4: KRISHNA'S BIRTH - THE MIRACLE NIGHT
    # ════════════════════════════════════════
    # Dark night sky
    for i in range(50):
        y_grad = PAGE_H - i * (PAGE_H / 50)
        ratio = i / 50
        c.setFillColor(Color(0.02 + ratio * 0.05, 0.05 + ratio * 0.03, 0.2 - ratio * 0.1))
        c.rect(0, y_grad, PAGE_W, PAGE_H / 50 + 1, fill=1, stroke=0)

    # Lots of stars
    draw_stars(c, count=50, y_min=int(PAGE_H / 2 + 30), y_max=int(PAGE_H - 30))

    # Divine glow - big golden radiance
    draw_glow(c, PAGE_W / 2, PAGE_H / 2 + 180, 120, GOLDEN, 0.12)
    draw_glow(c, PAGE_W / 2, PAGE_H / 2 + 180, 80, Color(1, 1, 0.8), 0.15)

    # Vishnu form (4-armed divine figure - simplified cute version)
    vx = PAGE_W / 2
    vy = PAGE_H / 2 + 200

    # Divine aura
    c.setFillColor(Color(1, 0.95, 0.7, alpha=0.15))
    c.circle(vx, vy, 90, fill=1, stroke=0)
    c.setFillColor(Color(1, 0.95, 0.7, alpha=0.1))
    c.circle(vx, vy, 110, fill=1, stroke=0)

    # Body
    c.setFillColor(KRISHNA_BLUE)
    c.setStrokeColor(KRISHNA_DARK_BLUE)
    c.setLineWidth(1)
    p = c.beginPath()
    p.moveTo(vx - 25, vy - 20)
    p.lineTo(vx + 25, vy - 20)
    p.lineTo(vx + 20, vy + 20)
    p.lineTo(vx - 20, vy + 20)
    p.close()
    c.drawPath(p, fill=1, stroke=1)

    # 4 arms
    c.setFillColor(KRISHNA_SKIN)
    # Left arms
    c.setLineWidth(5)
    c.setStrokeColor(KRISHNA_SKIN)
    for arm_y_off, arm_x in [(-5, -45), (5, -40)]:
        c.line(vx - 25, vy + arm_y_off, vx + arm_x, vy + arm_y_off + 15)
        c.circle(vx + arm_x, vy + arm_y_off + 15, 5, fill=1, stroke=0)
    # Right arms
    for arm_y_off, arm_x in [(-5, 45), (5, 40)]:
        c.line(vx + 25, vy + arm_y_off, vx + arm_x, vy + arm_y_off + 15)
        c.circle(vx + arm_x, vy + arm_y_off + 15, 5, fill=1, stroke=0)

    # Items in hands - Sudarshan Chakra (golden disc)
    c.setFillColor(GOLDEN)
    c.setStrokeColor(GOLDEN_DARK)
    c.setLineWidth(1)
    c.circle(vx + 48, vy + 15, 10, fill=1)
    # Conch shell
    c.setFillColor(white)
    c.circle(vx - 48, vy + 15, 8, fill=1)
    # Lotus
    draw_lotus(c, vx - 42, vy + 25, size=8)
    # Mace
    c.setFillColor(GOLDEN)
    c.rect(vx + 37, vy + 15, 4, 18, fill=1, stroke=0)
    c.circle(vx + 39, vy + 35, 5, fill=1, stroke=0)

    # Face
    draw_cute_face(c, vx, vy + 40, 18, KRISHNA_SKIN, is_krishna=True)

    # Crown (Mukut)
    draw_crown(c, vx, vy + 55, 30, 22)

    # Yellow dhoti
    c.setFillColor(GOLDEN)
    p = c.beginPath()
    p.moveTo(vx - 22, vy - 20)
    p.curveTo(vx - 25, vy - 45, vx + 25, vy - 45, vx + 22, vy - 20)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    # Sleeping parents below
    # Devaki sleeping
    c.setFillColor(DEEP_RED)
    c.roundRect(PAGE_W / 2 - 120, PAGE_H / 2 + 50, 60, 25, 5, fill=1, stroke=0)
    c.setFillColor(SKIN_TONE)
    c.circle(PAGE_W / 2 - 130, PAGE_H / 2 + 68, 12, fill=1, stroke=0)
    # Closed eyes (sleeping)
    c.setStrokeColor(HexColor("#5D4037"))
    c.setLineWidth(1)
    c.line(PAGE_W / 2 - 135, PAGE_H / 2 + 69, PAGE_W / 2 - 128, PAGE_H / 2 + 69)

    # Vasudev sleeping
    c.setFillColor(HexColor("#F0E68C"))
    c.roundRect(PAGE_W / 2 + 60, PAGE_H / 2 + 50, 60, 25, 5, fill=1, stroke=0)
    c.setFillColor(SKIN_TONE)
    c.circle(PAGE_W / 2 + 128, PAGE_H / 2 + 68, 12, fill=1, stroke=0)
    c.setStrokeColor(HexColor("#5D4037"))
    c.line(PAGE_W / 2 + 123, PAGE_H / 2 + 69, PAGE_W / 2 + 133, PAGE_H / 2 + 69)

    # Baby Krishna appeared! (small, glowing)
    draw_glow(c, PAGE_W / 2, PAGE_H / 2 + 90, 25, GOLDEN, 0.2)
    draw_baby_krishna(c, PAGE_W / 2, PAGE_H / 2 + 85, size=0.8)

    # Text area
    c.setFillColor(CREAM)
    c.roundRect(30, 40, PAGE_W - 60, PAGE_H / 2 - 80, 15, fill=1, stroke=0)
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(2)
    c.roundRect(35, 45, PAGE_W - 70, PAGE_H / 2 - 90, 12, fill=0)

    c.setFillColor(SAFFRON)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 55, "~ * ~")

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 80, "The Miracle Night!")

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#333333"))
    lines = [
        "Then came the magical night of Ashtami!",
        "At midnight, Lord Vishnu appeared with",
        "a bright golden light filling the whole prison!",
        "",
        "He said: 'I will be born as your baby boy.",
        "Take me across the river to Gokul.",
        "A kind family will keep me safe.'",
        "And then... Baby Krishna was born!",
    ]
    y = PAGE_H / 2 - 110
    for line in lines:
        if line.startswith("He said") or line.startswith("'"):
            c.setFont("Helvetica-BoldOblique", 14)
            c.setFillColor(KRISHNA_DARK_BLUE)
        elif "Baby Krishna" in line:
            c.setFont("Helvetica-Bold", 14)
            c.setFillColor(KRISHNA_DARK_BLUE)
        else:
            c.setFont("Helvetica", 14)
            c.setFillColor(HexColor("#333333"))
        c.drawCentredString(PAGE_W / 2, y, line)
        y -= 22

    draw_page_number(c, page_num)
    c.showPage()
    page_num += 1

    # ════════════════════════════════════════
    # PAGE 5: VASUDEV CROSSES THE YAMUNA RIVER
    # ════════════════════════════════════════
    # Stormy night sky
    for i in range(25):
        y_grad = PAGE_H - i * 16
        ratio = i / 25
        c.setFillColor(Color(0.03, 0.05 + ratio * 0.02, 0.15 + ratio * 0.05))
        c.rect(0, y_grad, PAGE_W, 17, fill=1, stroke=0)

    draw_stars(c, count=20, y_min=int(PAGE_H * 0.7), y_max=int(PAGE_H - 20))

    # Rain
    c.setStrokeColor(Color(0.6, 0.8, 1, alpha=0.4))
    c.setLineWidth(0.8)
    import random
    random.seed(55)
    for _ in range(60):
        rx = random.randint(0, int(PAGE_W))
        ry = random.randint(int(PAGE_H / 2 + 50), int(PAGE_H - 20))
        c.line(rx, ry, rx - 3, ry - 15)

    # Yamuna River
    c.setFillColor(Color(0.1, 0.2, 0.5, alpha=0.8))
    c.rect(0, PAGE_H / 2, PAGE_W, 100, fill=1, stroke=0)
    # Waves
    c.setStrokeColor(Color(0.3, 0.5, 0.8, alpha=0.6))
    c.setLineWidth(2)
    for wave_y in [PAGE_H / 2 + 20, PAGE_H / 2 + 50, PAGE_H / 2 + 80]:
        p = c.beginPath()
        p.moveTo(0, wave_y)
        for wx_pos in range(0, int(PAGE_W), 40):
            p.curveTo(wx_pos + 10, wave_y + 10, wx_pos + 20, wave_y + 10, wx_pos + 30, wave_y)
            p.curveTo(wx_pos + 35, wave_y - 5, wx_pos + 38, wave_y - 5, wx_pos + 40, wave_y)
        c.drawPath(p, fill=0, stroke=1)

    # Sheshnag (serpent) hood protecting baby - simplified cute version
    snx = PAGE_W / 2
    sny = PAGE_H / 2 + 200

    # Serpent hood (multi-headed, simplified)
    c.setFillColor(Color(0.2, 0.4, 0.2, alpha=0.9))
    for hood_off in [-25, -12, 0, 12, 25]:
        c.saveState()
        c.translate(snx + hood_off, sny + 70)
        c.scale(0.6, 1)
        c.circle(0, 0, 15, fill=1, stroke=0)
        c.restoreState()
    # Hood body
    c.setFillColor(Color(0.15, 0.35, 0.15))
    p = c.beginPath()
    p.moveTo(snx - 35, sny + 55)
    p.curveTo(snx - 40, sny + 30, snx + 40, sny + 30, snx + 35, sny + 55)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # Eyes on center hood
    c.setFillColor(GOLDEN)
    c.circle(snx - 4, sny + 72, 2.5, fill=1, stroke=0)
    c.circle(snx + 4, sny + 72, 2.5, fill=1, stroke=0)

    # Snake body going down (coiled)
    c.setStrokeColor(Color(0.15, 0.35, 0.15))
    c.setLineWidth(8)
    p = c.beginPath()
    p.moveTo(snx, sny + 30)
    p.curveTo(snx + 30, sny, snx - 30, sny - 30, snx, sny - 40)
    c.drawPath(p, fill=0, stroke=1)

    # Vasudev walking in river with baby
    vx_walk = PAGE_W / 2
    vy_walk = PAGE_H / 2 + 120

    # Body
    c.setFillColor(HexColor("#F0E68C"))
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1)
    p = c.beginPath()
    p.moveTo(vx_walk - 20, vy_walk - 30)
    p.lineTo(vx_walk + 20, vy_walk - 30)
    p.lineTo(vx_walk + 15, vy_walk + 25)
    p.lineTo(vx_walk - 15, vy_walk + 25)
    p.close()
    c.drawPath(p, fill=1, stroke=1)

    # Face
    c.setFillColor(SKIN_TONE)
    c.circle(vx_walk, vy_walk + 42, 16, fill=1, stroke=0)
    # Eyes (determined)
    c.setFillColor(HexColor("#2C1810"))
    c.circle(vx_walk - 5, vy_walk + 44, 2, fill=1, stroke=0)
    c.circle(vx_walk + 5, vy_walk + 44, 2, fill=1, stroke=0)
    # Hair
    c.setFillColor(HexColor("#1A1A2E"))
    c.circle(vx_walk, vy_walk + 56, 14, fill=1, stroke=0)

    # Basket on head with baby
    c.setFillColor(HexColor("#DEB887"))
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1)
    c.rect(vx_walk - 18, vy_walk + 60, 36, 20, fill=1)
    # Baby Krishna in basket (tiny and cute)
    draw_glow(c, vx_walk, vy_walk + 78, 12, GOLDEN, 0.2)
    c.setFillColor(KRISHNA_SKIN)
    c.circle(vx_walk, vy_walk + 78, 7, fill=1, stroke=0)
    # Baby eyes (closed, sleeping)
    c.setStrokeColor(HexColor("#2C1810"))
    c.setLineWidth(0.8)
    c.line(vx_walk - 3, vy_walk + 79, vx_walk - 1, vy_walk + 79)
    c.line(vx_walk + 1, vy_walk + 79, vx_walk + 3, vy_walk + 79)
    # Tiny smile
    c.arc(vx_walk - 2, vy_walk + 74, vx_walk + 2, vy_walk + 77, 200, 140)
    # Yellow cloth
    c.setFillColor(GOLDEN)
    c.rect(vx_walk - 10, vy_walk + 65, 20, 8, fill=1, stroke=0)

    # Arms holding basket
    c.setStrokeColor(SKIN_TONE)
    c.setLineWidth(4)
    c.line(vx_walk - 15, vy_walk + 25, vx_walk - 15, vy_walk + 60)
    c.line(vx_walk + 15, vy_walk + 25, vx_walk + 15, vy_walk + 60)

    # Water splashes around feet
    c.setFillColor(Color(0.6, 0.8, 1, alpha=0.5))
    for splash_x in [vx_walk - 25, vx_walk + 25]:
        c.circle(splash_x, vy_walk - 25, 5, fill=1, stroke=0)
        c.circle(splash_x - 5, vy_walk - 20, 3, fill=1, stroke=0)
        c.circle(splash_x + 5, vy_walk - 20, 3, fill=1, stroke=0)

    # Text area
    c.setFillColor(CREAM)
    c.roundRect(30, 40, PAGE_W - 60, PAGE_H / 2 - 80, 15, fill=1, stroke=0)
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(2)
    c.roundRect(35, 45, PAGE_W - 70, PAGE_H / 2 - 90, 12, fill=0)

    c.setFillColor(SAFFRON)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 55, "~ * ~")

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 80, "Crossing the Yamuna River")

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#333333"))
    lines = [
        "When Baby Krishna was born, all the prison",
        "doors opened by themselves! Magic!",
        "",
        "Vasudev put baby Krishna in a basket",
        "and walked through the stormy night.",
        "",
        "The great serpent Sheshnag came to protect",
        "the baby from rain with his big hood!",
        "The river Yamuna made way for them!",
    ]
    y = PAGE_H / 2 - 105
    for line in lines:
        if "Magic!" in line or "Sheshnag" in line:
            c.setFont("Helvetica-Bold", 14)
            c.setFillColor(KRISHNA_DARK_BLUE)
        else:
            c.setFont("Helvetica", 14)
            c.setFillColor(HexColor("#333333"))
        c.drawCentredString(PAGE_W / 2, y, line)
        y -= 21

    draw_page_number(c, page_num)
    c.showPage()
    page_num += 1

    # ════════════════════════════════════════
    # PAGE 6: GOKUL - NAND & YASHODA
    # ════════════════════════════════════════
    # Beautiful morning sky - dawn
    for i in range(25):
        y_grad = PAGE_H - i * 16
        ratio = i / 25
        r = 0.9 - ratio * 0.3
        g = 0.7 - ratio * 0.2
        b = 0.4 + ratio * 0.2
        c.setFillColor(Color(r, g, b))
        c.rect(0, y_grad, PAGE_W, 17, fill=1, stroke=0)

    # Soft clouds
    c.setFillColor(Color(1, 0.95, 0.85, alpha=0.7))
    for cc_x, cc_y in [(100, PAGE_H - 50), (350, PAGE_H - 70), (480, PAGE_H - 45)]:
        c.circle(cc_x, cc_y, 20, fill=1, stroke=0)
        c.circle(cc_x - 15, cc_y - 5, 16, fill=1, stroke=0)
        c.circle(cc_x + 15, cc_y - 5, 16, fill=1, stroke=0)

    # Green ground
    c.setFillColor(FOREST_GREEN)
    c.rect(0, PAGE_H / 2, PAGE_W, 20, fill=1, stroke=0)
    c.setFillColor(LIGHT_GREEN)
    c.rect(0, PAGE_H / 2 - 10, PAGE_W, 15, fill=1, stroke=0)

    # Cute village hut
    hut_x = PAGE_W / 2
    hut_y = PAGE_H / 2 + 20

    # Hut walls
    c.setFillColor(HexColor("#F5DEB3"))
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1.5)
    c.rect(hut_x - 70, hut_y, 140, 100, fill=1)

    # Thatched roof
    c.setFillColor(HexColor("#8B7355"))
    p = c.beginPath()
    p.moveTo(hut_x - 90, hut_y + 100)
    p.lineTo(hut_x, hut_y + 170)
    p.lineTo(hut_x + 90, hut_y + 100)
    p.close()
    c.drawPath(p, fill=1, stroke=1)

    # Roof texture
    c.setStrokeColor(HexColor("#6B5B3A"))
    c.setLineWidth(0.5)
    for ry_off in range(0, 60, 10):
        c.line(hut_x - 80 + ry_off, hut_y + 105 + ry_off * 0.8,
               hut_x + 80 - ry_off, hut_y + 105 + ry_off * 0.8)

    # Door
    c.setFillColor(DARK_BROWN)
    c.rect(hut_x - 18, hut_y, 36, 55, fill=1)
    c.setFillColor(GOLDEN)
    c.circle(hut_x + 10, hut_y + 28, 3, fill=1, stroke=0)

    # Window
    c.setFillColor(HexColor("#87CEEB"))
    c.rect(hut_x + 35, hut_y + 45, 25, 25, fill=1)
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1)
    c.rect(hut_x + 35, hut_y + 45, 25, 25, fill=0)
    c.line(hut_x + 47, hut_y + 45, hut_x + 47, hut_y + 70)

    # Flowers around hut
    flower_colors = [LOTUS_PINK, GOLDEN, DEEP_RED, SAFFRON]
    for fx, fy, fc in [(hut_x - 100, hut_y + 10, 0), (hut_x + 100, hut_y + 15, 1),
                       (hut_x - 80, hut_y + 5, 2), (hut_x + 110, hut_y + 8, 3)]:
        c.setFillColor(FOREST_GREEN)
        c.line(fx, hut_y - 5, fx, fy)
        draw_lotus(c, fx, fy, size=10)

    # Cow next to hut (cute!)
    cow_x = hut_x + 140
    cow_y = hut_y + 30
    # Body
    c.setFillColor(white)
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1)
    c.saveState()
    c.translate(cow_x, cow_y)
    c.scale(1.3, 0.8)
    c.circle(0, 0, 22, fill=1)
    c.restoreState()
    # Head
    c.setFillColor(white)
    c.circle(cow_x + 25, cow_y + 18, 14, fill=1)
    # Eyes
    c.setFillColor(black)
    c.circle(cow_x + 29, cow_y + 20, 2, fill=1, stroke=0)
    # Nose
    c.setFillColor(SOFT_PINK)
    c.circle(cow_x + 33, cow_y + 14, 4, fill=1, stroke=0)
    # Ears
    c.setFillColor(SOFT_PINK)
    c.circle(cow_x + 18, cow_y + 28, 5, fill=1, stroke=0)
    c.circle(cow_x + 32, cow_y + 28, 5, fill=1, stroke=0)
    # Horns
    c.setStrokeColor(GOLDEN_DARK)
    c.setLineWidth(2)
    c.line(cow_x + 20, cow_y + 30, cow_x + 15, cow_y + 40)
    c.line(cow_x + 30, cow_y + 30, cow_x + 35, cow_y + 40)
    # Legs
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(3)
    for lx in [-15, -5, 10, 18]:
        c.line(cow_x + lx, cow_y - 5, cow_x + lx, cow_y - 22)
    # Spots
    c.setFillColor(HexColor("#D2691E"))
    c.circle(cow_x - 10, cow_y + 5, 6, fill=1, stroke=0)
    c.circle(cow_x + 8, cow_y + 8, 5, fill=1, stroke=0)

    # Yashoda Ma (happy, receiving baby)
    yx = hut_x - 20
    yy = hut_y + 60
    # Sari
    c.setFillColor(HexColor("#FF6347"))
    p = c.beginPath()
    p.moveTo(yx - 18, yy - 20)
    p.lineTo(yx + 18, yy - 20)
    p.lineTo(yx + 15, yy + 25)
    p.lineTo(yx - 15, yy + 25)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    # Face
    c.setFillColor(SKIN_TONE)
    c.circle(yx, yy + 42, 15, fill=1, stroke=0)
    # Happy eyes
    c.setFillColor(HexColor("#2C1810"))
    c.circle(yx - 5, yy + 44, 2, fill=1, stroke=0)
    c.circle(yx + 5, yy + 44, 2, fill=1, stroke=0)
    # Big happy smile
    c.setStrokeColor(HexColor("#8B4513"))
    c.setLineWidth(1)
    p = c.beginPath()
    p.moveTo(yx - 6, yy + 36)
    p.curveTo(yx - 3, yy + 32, yx + 3, yy + 32, yx + 6, yy + 36)
    c.drawPath(p, fill=0, stroke=1)
    # Bindi
    c.setFillColor(DEEP_RED)
    c.circle(yx, yy + 50, 2, fill=1, stroke=0)
    # Hair
    c.setFillColor(HexColor("#1A1A2E"))
    c.circle(yx, yy + 55, 13, fill=1, stroke=0)
    # Pallu on head
    c.setFillColor(Color(1, 0.4, 0.3, alpha=0.6))
    c.circle(yx, yy + 58, 16, fill=1, stroke=0)
    # Hands holding baby
    c.setFillColor(SKIN_TONE)
    c.circle(yx - 15, yy + 5, 5, fill=1, stroke=0)
    c.circle(yx + 15, yy + 5, 5, fill=1, stroke=0)

    # Baby Krishna in arms
    draw_glow(c, yx, yy + 5, 15, GOLDEN, 0.15)
    c.setFillColor(KRISHNA_SKIN)
    c.circle(yx, yy + 10, 8, fill=1, stroke=0)
    c.setFillColor(GOLDEN)
    c.roundRect(yx - 8, yy - 5, 16, 10, 3, fill=1, stroke=0)
    # Baby smile
    c.setStrokeColor(HexColor("#5D4037"))
    c.setLineWidth(0.5)
    c.arc(yx - 2, yy + 8, yx + 2, yy + 11, 200, 140)

    # Nand Baba (happy father figure)
    nx = hut_x + 30
    ny = hut_y + 60
    c.setFillColor(white)
    p = c.beginPath()
    p.moveTo(nx - 18, ny - 20)
    p.lineTo(nx + 18, ny - 20)
    p.lineTo(nx + 15, ny + 25)
    p.lineTo(nx - 15, ny + 25)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(SKIN_TONE)
    c.circle(nx, ny + 42, 15, fill=1, stroke=0)
    c.setFillColor(HexColor("#2C1810"))
    c.circle(nx - 5, ny + 44, 2, fill=1, stroke=0)
    c.circle(nx + 5, ny + 44, 2, fill=1, stroke=0)
    # Happy smile
    c.setStrokeColor(HexColor("#8B4513"))
    c.setLineWidth(1)
    p = c.beginPath()
    p.moveTo(nx - 6, ny + 36)
    p.curveTo(nx - 3, ny + 32, nx + 3, ny + 32, nx + 6, ny + 36)
    c.drawPath(p, fill=0, stroke=1)
    # Turban
    c.setFillColor(SAFFRON)
    c.circle(nx, ny + 56, 14, fill=1, stroke=0)
    c.circle(nx + 5, ny + 60, 6, fill=1, stroke=0)

    # Text area
    c.setFillColor(CREAM)
    c.roundRect(30, 40, PAGE_W - 60, PAGE_H / 2 - 80, 15, fill=1, stroke=0)
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(2)
    c.roundRect(35, 45, PAGE_W - 70, PAGE_H / 2 - 90, 12, fill=0)

    c.setFillColor(SAFFRON)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 55, "~ * ~")

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 80, "Welcome to Gokul!")

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#333333"))
    lines = [
        "Vasudev reached the village of Gokul safely.",
        "There lived kind Nand Baba and Yashoda Ma.",
        "",
        "Vasudev gently placed Baby Krishna",
        "in Yashoda Ma's loving arms.",
        "",
        "Yashoda Ma was so happy to see the",
        "beautiful blue baby! She hugged him tight.",
        "Baby Krishna smiled and the whole world lit up!",
    ]
    y = PAGE_H / 2 - 105
    for line in lines:
        if "Krishna smiled" in line:
            c.setFont("Helvetica-Bold", 14)
            c.setFillColor(KRISHNA_DARK_BLUE)
        else:
            c.setFont("Helvetica", 14)
            c.setFillColor(HexColor("#333333"))
        c.drawCentredString(PAGE_W / 2, y, line)
        y -= 21

    draw_page_number(c, page_num)
    c.showPage()
    page_num += 1

    # ════════════════════════════════════════
    # PAGE 7: HAPPY GOKUL - KRISHNA GROWING UP
    # ════════════════════════════════════════
    # Bright happy sky
    c.setFillColor(SKY_BLUE)
    c.rect(0, PAGE_H / 2, PAGE_W, PAGE_H / 2, fill=1, stroke=0)

    # Rainbow!
    rainbow_colors = [
        HexColor("#FF0000"), HexColor("#FF7F00"), HexColor("#FFFF00"),
        HexColor("#00FF00"), HexColor("#0000FF"), HexColor("#4B0082"), HexColor("#9400D3")
    ]
    for i, rc in enumerate(rainbow_colors):
        c.setStrokeColor(rc)
        c.setLineWidth(5)
        r = 200 - i * 8
        c.arc(PAGE_W / 2 - r, PAGE_H - 200, PAGE_W / 2 + r, PAGE_H - 200 + r * 1.3, 20, 140)

    # Fluffy clouds
    for cc_x, cc_y in [(80, PAGE_H - 50), (450, PAGE_H - 60)]:
        c.setFillColor(white)
        c.circle(cc_x, cc_y, 22, fill=1, stroke=0)
        c.circle(cc_x - 18, cc_y - 5, 18, fill=1, stroke=0)
        c.circle(cc_x + 18, cc_y - 5, 18, fill=1, stroke=0)

    # Green ground with flowers
    c.setFillColor(LIGHT_GREEN)
    c.rect(0, PAGE_H / 2 - 10, PAGE_W, 25, fill=1, stroke=0)
    c.setFillColor(FOREST_GREEN)
    c.rect(0, PAGE_H / 2, PAGE_W, 5, fill=1, stroke=0)

    # Small flowers in grass
    random.seed(88)
    for _ in range(15):
        fx = random.randint(20, int(PAGE_W - 20))
        fy = PAGE_H / 2 + random.randint(-5, 15)
        c.setFillColor(random.choice([LOTUS_PINK, GOLDEN, DEEP_RED, white, yellow]))
        c.circle(fx, fy, 3, fill=1, stroke=0)

    # Cute baby Krishna in center (bigger, playing)
    draw_glow(c, PAGE_W / 2, PAGE_H / 2 + 110, 60, GOLDEN, 0.08)
    draw_baby_krishna(c, PAGE_W / 2, PAGE_H / 2 + 100, size=1.8)

    # Flute
    draw_flute(c, PAGE_W / 2 - 35, PAGE_H / 2 + 90, length=50, angle=20)

    # Butter pot
    c.setFillColor(HexColor("#CD853F"))
    c.setStrokeColor(DARK_BROWN)
    c.setLineWidth(1)
    # Pot shape
    p = c.beginPath()
    p.moveTo(PAGE_W / 2 + 80, PAGE_H / 2 + 50)
    p.curveTo(PAGE_W / 2 + 60, PAGE_H / 2 + 40, PAGE_W / 2 + 60, PAGE_H / 2 + 70, PAGE_W / 2 + 80, PAGE_H / 2 + 75)
    p.curveTo(PAGE_W / 2 + 100, PAGE_H / 2 + 70, PAGE_W / 2 + 100, PAGE_H / 2 + 40, PAGE_W / 2 + 80, PAGE_H / 2 + 50)
    c.drawPath(p, fill=1, stroke=1)
    # Butter on top
    c.setFillColor(GOLDEN)
    c.circle(PAGE_W / 2 + 80, PAGE_H / 2 + 72, 8, fill=1, stroke=0)

    # Butterflies
    for bx, by in [(150, PAGE_H / 2 + 180), (420, PAGE_H / 2 + 160)]:
        c.setFillColor(Color(1, 0.6, 0.8, alpha=0.7))
        c.saveState()
        c.translate(bx - 8, by)
        c.scale(0.6, 1)
        c.circle(0, 0, 8, fill=1, stroke=0)
        c.restoreState()
        c.saveState()
        c.translate(bx + 8, by)
        c.scale(0.6, 1)
        c.circle(0, 0, 8, fill=1, stroke=0)
        c.restoreState()
        c.setFillColor(Color(0.8, 0.4, 0.6))
        c.circle(bx, by, 2, fill=1, stroke=0)

    # Peacock
    pk_x = 100
    pk_y = PAGE_H / 2 + 40
    c.setFillColor(PEACOCK_BLUE)
    c.saveState()
    c.translate(pk_x, pk_y)
    c.scale(1, 0.7)
    c.circle(0, 0, 15, fill=1, stroke=0)
    c.restoreState()
    # Head
    c.setFillColor(PEACOCK_BLUE)
    c.circle(pk_x + 12, pk_y + 18, 8, fill=1, stroke=0)
    # Eye
    c.setFillColor(white)
    c.circle(pk_x + 14, pk_y + 19, 2, fill=1, stroke=0)
    c.setFillColor(black)
    c.circle(pk_x + 14, pk_y + 19, 1, fill=1, stroke=0)
    # Crest
    c.setStrokeColor(PEACOCK_BLUE)
    c.setLineWidth(1)
    c.line(pk_x + 12, pk_y + 25, pk_x + 10, pk_y + 35)
    c.line(pk_x + 12, pk_y + 25, pk_x + 14, pk_y + 35)
    c.setFillColor(PEACOCK_GREEN)
    c.circle(pk_x + 10, pk_y + 36, 2, fill=1, stroke=0)
    c.circle(pk_x + 14, pk_y + 36, 2, fill=1, stroke=0)
    # Tail feathers
    for angle in range(-30, 31, 15):
        rad = math.radians(angle + 180)
        tx = pk_x + 30 * math.cos(rad)
        ty = pk_y + 30 * math.sin(rad)
        c.setFillColor(PEACOCK_GREEN)
        c.circle(tx, ty, 5, fill=1, stroke=0)
        c.setFillColor(PEACOCK_BLUE)
        c.circle(tx, ty, 2.5, fill=1, stroke=0)
        c.setFillColor(GOLDEN)
        c.circle(tx, ty, 1.2, fill=1, stroke=0)

    # Friend gopas (small cute kids)
    for gx, gy_off in [(PAGE_W / 2 - 120, 0), (PAGE_W / 2 + 120, 10)]:
        gy = PAGE_H / 2 + 70 + gy_off
        c.setFillColor(SAFFRON)
        c.roundRect(gx - 10, gy, 20, 25, 5, fill=1, stroke=0)
        c.setFillColor(SKIN_TONE)
        c.circle(gx, gy + 35, 10, fill=1, stroke=0)
        c.setFillColor(HexColor("#2C1810"))
        c.circle(gx - 3, gy + 36, 1.5, fill=1, stroke=0)
        c.circle(gx + 3, gy + 36, 1.5, fill=1, stroke=0)
        # Happy smile
        c.setStrokeColor(HexColor("#8B4513"))
        c.setLineWidth(0.8)
        p = c.beginPath()
        p.moveTo(gx - 4, gy + 31)
        p.curveTo(gx - 2, gy + 28, gx + 2, gy + 28, gx + 4, gy + 31)
        c.drawPath(p, fill=0, stroke=1)
        c.setFillColor(HexColor("#1A1A2E"))
        c.circle(gx, gy + 43, 9, fill=1, stroke=0)

    # Text area
    c.setFillColor(CREAM)
    c.roundRect(30, 40, PAGE_W - 60, PAGE_H / 2 - 80, 15, fill=1, stroke=0)
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(2)
    c.roundRect(35, 45, PAGE_W - 70, PAGE_H / 2 - 90, 12, fill=0)

    c.setFillColor(SAFFRON)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 55, "~ * ~")

    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 80, "The Naughty Little Krishna!")

    c.setFont("Helvetica", 14)
    c.setFillColor(HexColor("#333333"))
    lines = [
        "Krishna grew up to be the most adorable",
        "and naughty child in all of Gokul!",
        "",
        "He loved stealing butter (Makhan Chor!),",
        "playing his magical flute, and dancing",
        "with his friends and the peacocks.",
        "",
        "Everyone in Gokul loved little Krishna.",
        "He brought joy and happiness everywhere!",
    ]
    y = PAGE_H / 2 - 105
    for line in lines:
        if "Makhan Chor" in line:
            c.setFont("Helvetica-Bold", 14)
            c.setFillColor(KRISHNA_DARK_BLUE)
        elif "joy and happiness" in line:
            c.setFont("Helvetica-Bold", 14)
            c.setFillColor(KRISHNA_DARK_BLUE)
        else:
            c.setFont("Helvetica", 14)
            c.setFillColor(HexColor("#333333"))
        c.drawCentredString(PAGE_W / 2, y, line)
        y -= 21

    draw_page_number(c, page_num)
    c.showPage()
    page_num += 1

    # ════════════════════════════════════════
    # PAGE 8: MORAL / ENDING PAGE
    # ════════════════════════════════════════
    # Beautiful gradient background
    for i in range(50):
        y_grad = PAGE_H - i * (PAGE_H / 50)
        ratio = i / 50
        r = 1.0 - ratio * 0.1
        g = 0.95 - ratio * 0.15
        b = 0.8 - ratio * 0.2
        c.setFillColor(Color(r, g, b))
        c.rect(0, y_grad, PAGE_W, PAGE_H / 50 + 1, fill=1, stroke=0)

    # Decorative border
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(3)
    c.roundRect(30, 30, PAGE_W - 60, PAGE_H - 60, 20, fill=0)
    c.setStrokeColor(GOLDEN)
    c.setLineWidth(1.5)
    c.roundRect(40, 40, PAGE_W - 80, PAGE_H - 80, 15, fill=0)

    # Lotus border decorations
    for lx in range(80, int(PAGE_W - 50), 70):
        draw_lotus(c, lx, PAGE_H - 55, size=12)
        draw_lotus(c, lx, 55, size=12)

    # Baby Krishna (center, big)
    draw_glow(c, PAGE_W / 2, PAGE_H / 2 + 120, 70, GOLDEN, 0.1)
    draw_baby_krishna(c, PAGE_W / 2, PAGE_H / 2 + 110, size=2.0)

    # Flute
    draw_flute(c, PAGE_W / 2 - 50, PAGE_H / 2 + 100, length=60, angle=15)

    # Lotus pedestal
    for i in range(5):
        draw_lotus(c, PAGE_W / 2 - 40 + i * 20, PAGE_H / 2 + 30, size=18)

    # Title
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.setFont("Helvetica-Bold", 26)
    c.drawCentredString(PAGE_W / 2, PAGE_H - 100, "What We Learn:")

    # Moral box
    c.setFillColor(Color(1, 1, 1, alpha=0.8))
    c.roundRect(60, PAGE_H - 260, PAGE_W - 120, 140, 15, fill=1, stroke=0)
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(2)
    c.roundRect(65, PAGE_H - 255, PAGE_W - 130, 130, 12, fill=0)

    c.setFont("Helvetica", 15)
    c.setFillColor(HexColor("#333333"))
    morals = [
        "Good always wins over evil.",
        "God protects those who are kind and truthful.",
        "Love and courage can overcome any challenge.",
        "Be like Krishna - spread joy everywhere!",
    ]
    y = PAGE_H - 150
    for i, moral in enumerate(morals):
        c.setFillColor(SAFFRON)
        c.circle(90, y + 4, 5, fill=1, stroke=0)
        c.setFillColor(HexColor("#333333"))
        if i == 3:
            c.setFont("Helvetica-Bold", 15)
            c.setFillColor(KRISHNA_DARK_BLUE)
        c.drawString(105, y, moral)
        y -= 30

    # Bottom text
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(PAGE_W / 2, 120, "Jai Shree Krishna!")

    c.setFont("Helvetica", 12)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W / 2, 90, "~ Happy Janmashtami ~")

    c.setFont("Helvetica", 10)
    c.setFillColor(lightgrey)
    c.drawCentredString(PAGE_W / 2, 65, "A Kids Book for Amazon KDP")

    c.showPage()

    # ════════════════════════════════════════
    # BACK COVER
    # ════════════════════════════════════════
    c.setFillColor(KRISHNA_DARK_BLUE)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    draw_stars(c, count=30, y_min=100, y_max=int(PAGE_H - 100))

    # Central lotus
    draw_lotus(c, PAGE_W / 2, PAGE_H / 2, size=40)

    # Om symbol area
    c.setFillColor(GOLDEN)
    c.setFont("Helvetica-Bold", 48)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 + 80, "Om")

    c.setFont("Helvetica", 14)
    c.setFillColor(white)
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 60, "Shree Krishna Birth Story")
    c.drawCentredString(PAGE_W / 2, PAGE_H / 2 - 85, "A Beautiful Story for Children")

    c.setFont("Helvetica", 11)
    c.setFillColor(GOLDEN)
    c.drawCentredString(PAGE_W / 2, 150, "This book tells the divine story of")
    c.drawCentredString(PAGE_W / 2, 135, "Lord Krishna's birth in simple words")
    c.drawCentredString(PAGE_W / 2, 120, "that every child can understand and enjoy.")

    c.setFont("Helvetica", 10)
    c.setFillColor(Color(1, 1, 1, alpha=0.5))
    c.drawCentredString(PAGE_W / 2, 70, "Sample Book - Created for Amazon KDP")
    c.drawCentredString(PAGE_W / 2, 55, "Ages 3-10 | Janmashtami Special Edition")

    c.showPage()

    c.save()
    print(f"Krishna Story Book saved: {filepath}")
    return filepath


if __name__ == "__main__":
    print("Creating Shree Krishna Birth Story Book...")
    print("=" * 50)
    filepath = create_krishna_book()
    size = os.path.getsize(filepath)
    print(f"\nBook created successfully!")
    print(f"File: {filepath}")
    print(f"Size: {size / 1024:.1f} KB")
    print("=" * 50)
