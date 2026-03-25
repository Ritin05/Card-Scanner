"""
Shree Krishna Birth Story - Bilingual Kids Story Book (Hindi + English)
Professional layout with image placeholders + AI prompt guide
"""

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, Color, black, white, gray, lightgrey
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math
import os

OUTPUT_DIR = "D:/Nidhi/n8n/Card Scan/Sample_Books"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PAGE_W, PAGE_H = A4

# ─── COLORS ───
KRISHNA_BLUE = HexColor("#2E75B6")
GOLDEN = HexColor("#FFD700")
GOLDEN_DARK = HexColor("#DAA520")
SAFFRON = HexColor("#FF9933")
CREAM = HexColor("#FFF8DC")
WARM_BG = HexColor("#FFF5E6")
SOFT_BLUE = HexColor("#E8F4FD")
SOFT_YELLOW = HexColor("#FFFDE7")
SOFT_PINK = HexColor("#FFF0F5")
SOFT_GREEN = HexColor("#F0FFF0")
DEEP_RED = HexColor("#C0392B")
DARK_TEXT = HexColor("#2C2C2C")
BORDER_GOLD = HexColor("#D4A017")

# Try to register Hindi font
HINDI_FONT_AVAILABLE = False
hindi_font_paths = [
    "C:/Windows/Fonts/NirmalaUI-Regular.ttf",   # Nirmala UI (Win10/11)
    "C:/Windows/Fonts/Nirmala.ttf",
    "C:/Windows/Fonts/mangal.ttf",               # Mangal
    "C:/Windows/Fonts/aparaj.ttf",               # Aparajita
    "C:/Windows/Fonts/KOKILA.TTF",               # Kokila
    "C:/Windows/Fonts/Raavi.ttf",
]

hindi_bold_paths = [
    "C:/Windows/Fonts/NirmalaUI-Bold.ttf",
    "C:/Windows/Fonts/NirmalaB.ttf",
    "C:/Windows/Fonts/mangalb.ttf",
    "C:/Windows/Fonts/aparajb.ttf",
    "C:/Windows/Fonts/KOKILAB.TTF",
]

for fp in hindi_font_paths:
    if os.path.exists(fp):
        try:
            pdfmetrics.registerFont(TTFont('Hindi', fp))
            HINDI_FONT_AVAILABLE = True
            print(f"Hindi font loaded: {fp}")
            break
        except:
            continue

HINDI_BOLD_AVAILABLE = False
for fp in hindi_bold_paths:
    if os.path.exists(fp):
        try:
            pdfmetrics.registerFont(TTFont('HindiBold', fp))
            HINDI_BOLD_AVAILABLE = True
            print(f"Hindi Bold font loaded: {fp}")
            break
        except:
            continue

if not HINDI_BOLD_AVAILABLE and HINDI_FONT_AVAILABLE:
    pdfmetrics.registerFont(TTFont('HindiBold', hindi_font_paths[0] if os.path.exists(hindi_font_paths[0]) else fp))


def draw_hindi(c, x, y, text, size=14, bold=False, color=DARK_TEXT, align="center"):
    """Draw Hindi text with proper font"""
    c.setFillColor(color)
    if bold and HINDI_BOLD_AVAILABLE:
        c.setFont("HindiBold", size)
    elif HINDI_FONT_AVAILABLE:
        c.setFont("Hindi", size)
    else:
        c.setFont("Helvetica", size)

    if align == "center":
        c.drawCentredString(x, y, text)
    elif align == "left":
        c.drawString(x, y, text)
    elif align == "right":
        c.drawRightString(x, y, text)


def draw_english(c, x, y, text, size=12, bold=False, italic=False, color=DARK_TEXT, align="center"):
    """Draw English text"""
    c.setFillColor(color)
    if bold and italic:
        c.setFont("Helvetica-BoldOblique", size)
    elif bold:
        c.setFont("Helvetica-Bold", size)
    elif italic:
        c.setFont("Helvetica-Oblique", size)
    else:
        c.setFont("Helvetica", size)

    if align == "center":
        c.drawCentredString(x, y, text)
    elif align == "left":
        c.drawString(x, y, text)
    elif align == "right":
        c.drawRightString(x, y, text)


def draw_decorative_border(c, x, y, w, h, color=BORDER_GOLD):
    """Draw a decorative double border"""
    c.setStrokeColor(color)
    c.setLineWidth(2.5)
    c.roundRect(x, y, w, h, 12, fill=0)
    c.setLineWidth(1)
    c.roundRect(x + 5, y + 5, w - 10, h - 10, 8, fill=0)


def draw_corner_flourish(c, x, y, size=20, flip_x=False, flip_y=False):
    """Draw corner decorative element"""
    c.setStrokeColor(BORDER_GOLD)
    c.setFillColor(SAFFRON)
    c.setLineWidth(1.5)
    sx = -1 if flip_x else 1
    sy = -1 if flip_y else 1
    # Simple floral corner
    c.circle(x, y, 4, fill=1, stroke=0)
    p = c.beginPath()
    p.moveTo(x, y)
    p.curveTo(x + sx * size * 0.5, y + sy * size * 0.3,
              x + sx * size * 0.3, y + sy * size * 0.5,
              x + sx * size, y)
    c.drawPath(p, fill=0, stroke=1)
    p = c.beginPath()
    p.moveTo(x, y)
    p.curveTo(x + sx * size * 0.3, y + sy * size * 0.5,
              x + sx * size * 0.5, y + sy * size * 0.3,
              x, y + sy * size)
    c.drawPath(p, fill=0, stroke=1)


def draw_image_placeholder(c, x, y, w, h, label, prompt_num):
    """Draw a beautiful image placeholder with instructions"""
    # Soft background
    c.setFillColor(Color(0.95, 0.95, 0.98))
    c.roundRect(x, y, w, h, 10, fill=1, stroke=0)

    # Dashed border
    c.setStrokeColor(HexColor("#B0B0B0"))
    c.setLineWidth(1.5)
    c.setDash(6, 4)
    c.roundRect(x + 3, y + 3, w - 6, h - 6, 8, fill=0)
    c.setDash()

    # Image icon (camera/picture icon)
    cx = x + w / 2
    cy = y + h / 2 + 15

    # Mountain/picture icon
    c.setStrokeColor(HexColor("#888888"))
    c.setLineWidth(1.5)
    c.setFillColor(Color(0.85, 0.85, 0.9))
    c.roundRect(cx - 30, cy - 20, 60, 45, 5, fill=1)

    # Mountain shape inside
    c.setFillColor(HexColor("#A0C4A0"))
    p = c.beginPath()
    p.moveTo(cx - 25, cy - 15)
    p.lineTo(cx - 10, cy + 10)
    p.lineTo(cx + 5, cy - 5)
    p.lineTo(cx + 20, cy + 10)
    p.lineTo(cx + 25, cy - 15)
    p.close()
    c.drawPath(p, fill=1, stroke=0)

    # Sun
    c.setFillColor(HexColor("#FFD700"))
    c.circle(cx + 15, cy + 12, 6, fill=1, stroke=0)

    # Label
    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(HexColor("#666666"))
    c.drawCentredString(cx, cy - 30, f"IMAGE {prompt_num}")

    c.setFont("Helvetica", 9)
    c.setFillColor(HexColor("#888888"))
    # Wrap label text
    words = label.split()
    lines = []
    current = ""
    for word in words:
        test = current + " " + word if current else word
        if len(test) > 40:
            lines.append(current)
            current = word
        else:
            current = test
    if current:
        lines.append(current)

    label_y = cy - 45
    for line in lines[:3]:
        c.drawCentredString(cx, label_y, line)
        label_y -= 12

    c.setFont("Helvetica", 8)
    c.setFillColor(HexColor("#AAAAAA"))
    c.drawCentredString(cx, y + 12, f"(See AI Prompt Guide - Prompt #{prompt_num})")


def draw_page_number(c, num):
    c.setFont("Helvetica", 9)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W / 2, 18, f"- {num} -")


def draw_om_divider(c, y):
    """Simple decorative divider"""
    c.setStrokeColor(SAFFRON)
    c.setLineWidth(1)
    c.line(PAGE_W / 2 - 80, y, PAGE_W / 2 - 20, y)
    c.line(PAGE_W / 2 + 20, y, PAGE_W / 2 + 80, y)
    c.setFillColor(SAFFRON)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(PAGE_W / 2, y - 5, "\u2736")


# ═══════════════════════════════════════════════
# STORY DATA
# ═══════════════════════════════════════════════

pages_data = [
    {
        "page_num": 1,
        "bg_color": SOFT_YELLOW,
        "title_hi": "\u092E\u0925\u0941\u0930\u093E \u0915\u093E \u0930\u093E\u091C\u094D\u092F",
        "title_en": "The Kingdom of Mathura",
        "story_hi": [
            "\u092C\u0939\u0941\u0924 \u0938\u092E\u092F \u092A\u0939\u0932\u0947 \u0915\u0940 \u092C\u093E\u0924 \u0939\u0948\u0964",
            "\u092E\u0925\u0941\u0930\u093E \u0928\u093E\u092E \u0915\u093E \u090F\u0915 \u0938\u0941\u0902\u0926\u0930 \u0930\u093E\u091C\u094D\u092F \u0925\u093E\u0964",
            "\u0935\u0939\u093E\u0901 \u0915\u0947 \u0932\u094B\u0917 \u092C\u0939\u0941\u0924 \u0916\u0941\u0936 \u0925\u0947\u0964",
            "\u0938\u0941\u0902\u0926\u0930 \u092E\u0939\u0932, \u092C\u0917\u0940\u091A\u0947 \u0914\u0930 \u0928\u0926\u093F\u092F\u093E\u0901 \u0925\u0940\u0902\u0964",
        ],
        "story_en": [
            "A long, long time ago,",
            "there was a beautiful kingdom called Mathura.",
            "The people there were very happy.",
            "It had lovely palaces, gardens and rivers.",
        ],
        "image_label": "Beautiful Mathura kingdom with grand palace, gardens, river, sunny day, cartoon style for kids",
        "prompt_num": 1,
    },
    {
        "page_num": 2,
        "bg_color": SOFT_PINK,
        "title_hi": "\u0915\u094D\u0930\u0942\u0930 \u0930\u093E\u091C\u093E \u0915\u0902\u0938",
        "title_en": "The Cruel King Kansa",
        "story_hi": [
            "\u0932\u0947\u0915\u093F\u0928 \u090F\u0915 \u0926\u093F\u0928 \u0915\u0902\u0938 \u0928\u093E\u092E \u0915\u0947 \u092C\u0941\u0930\u0947 \u0930\u093E\u091C\u093E \u0928\u0947",
            "\u092E\u0925\u0941\u0930\u093E \u092A\u0930 \u0915\u092C\u094D\u091C\u093E \u0915\u0930 \u0932\u093F\u092F\u093E\u0964",
            "\u0915\u0902\u0938 \u0915\u0940 \u090F\u0915 \u092A\u094D\u092F\u093E\u0930\u0940 \u092C\u0939\u0928 \u0926\u0947\u0935\u0915\u0940 \u0925\u0940\u0964",
            "\u0906\u0915\u093E\u0936\u0935\u093E\u0923\u0940 \u0928\u0947 \u0915\u0939\u093E: '\u0926\u0947\u0935\u0915\u0940 \u0915\u093E 8\u0935\u093E\u0901 \u092C\u091A\u094D\u091A\u093E",
            "\u0924\u0941\u092E\u094D\u0939\u0947\u0902 \u0939\u0930\u093E\u090F\u0917\u093E, \u0915\u0902\u0938!'",
            "\u0915\u0902\u0938 \u0928\u0947 \u0926\u0947\u0935\u0915\u0940 \u0914\u0930 \u0935\u093E\u0938\u0941\u0926\u0947\u0935 \u0915\u094B",
            "\u0905\u0902\u0927\u0947\u0930\u0947 \u0915\u093E\u0930\u093E\u0917\u0943\u0939 \u092E\u0947\u0902 \u092C\u0902\u0926 \u0915\u0930 \u0926\u093F\u092F\u093E\u0964",
        ],
        "story_en": [
            "But one day, a cruel king named Kansa",
            "took over the kingdom of Mathura.",
            "Kansa had a dear sister named Devaki.",
            "A voice from the sky said: 'Devaki's 8th child",
            "will defeat you, Kansa!'",
            "Kansa got very angry and locked Devaki",
            "and Vasudev in a dark prison.",
        ],
        "image_label": "Angry King Kansa with crown, sad Devaki and Vasudev in chains, palace background, cute cartoon",
        "prompt_num": 2,
    },
    {
        "page_num": 3,
        "bg_color": Color(0.92, 0.92, 0.95),
        "title_hi": "\u0905\u0902\u0927\u0947\u0930\u093E \u0915\u093E\u0930\u093E\u0917\u0943\u0939",
        "title_en": "The Dark Prison",
        "story_hi": [
            "\u0926\u0947\u0935\u0915\u0940 \u0914\u0930 \u0935\u093E\u0938\u0941\u0926\u0947\u0935 \u092C\u0939\u0941\u0924 \u0926\u0941\u0916\u0940 \u0925\u0947\u0964",
            "\u0915\u093E\u0930\u093E\u0917\u0943\u0939 \u0905\u0902\u0927\u0947\u0930\u093E \u0914\u0930 \u0920\u0902\u0921\u093E \u0925\u093E\u0964",
            "",
            "\u0932\u0947\u0915\u093F\u0928 \u0909\u0928\u094D\u0939\u094B\u0902\u0928\u0947 \u0939\u093F\u092E\u094D\u092E\u0924 \u0928\u0939\u0940\u0902 \u0939\u093E\u0930\u0940\u0964",
            "\u0935\u094B \u0939\u0930 \u0930\u094B\u091C\u093C \u092D\u0917\u0935\u093E\u0928 \u0935\u093F\u0937\u094D\u0923\u0941 \u0938\u0947",
            "\u092A\u094D\u0930\u093E\u0930\u094D\u0925\u0928\u093E \u0915\u0930\u0924\u0947 \u0925\u0947\u0964",
            "\u0909\u0928\u094D\u0939\u0947\u0902 \u0935\u093F\u0936\u094D\u0935\u093E\u0938 \u0925\u093E \u0915\u093F \u092D\u0917\u0935\u093E\u0928 \u091C\u093C\u0930\u0942\u0930 \u0906\u090F\u0902\u0917\u0947!",
        ],
        "story_en": [
            "Devaki and Vasudev were very sad.",
            "The prison was dark and cold.",
            "",
            "But they never lost hope!",
            "Every day they prayed to Lord Vishnu.",
            "They believed God would surely come",
            "to save everyone from evil Kansa!",
        ],
        "image_label": "Devaki and Vasudev praying in dark prison, small lamp/diya glowing, moonlight through window bars, cute cartoon",
        "prompt_num": 3,
    },
    {
        "page_num": 4,
        "bg_color": SOFT_BLUE,
        "title_hi": "\u091A\u092E\u0924\u094D\u0915\u093E\u0930\u0940 \u0930\u093E\u0924 - \u0915\u0943\u0937\u094D\u0923 \u091C\u0928\u094D\u092E!",
        "title_en": "The Miracle Night - Krishna is Born!",
        "story_hi": [
            "\u092B\u093F\u0930 \u0906\u0908 \u0935\u094B \u091C\u093E\u0926\u0941\u0908 \u0930\u093E\u0924!",
            "\u0905\u0937\u094D\u091F\u092E\u0940 \u0915\u0940 \u0906\u0927\u0940 \u0930\u093E\u0924 \u0915\u094B,",
            "\u092D\u0917\u0935\u093E\u0928 \u0935\u093F\u0937\u094D\u0923\u0941 \u092A\u094D\u0930\u0915\u091F \u0939\u0941\u090F!",
            "",
            "\u0938\u094B\u0928\u0947 \u0915\u0940 \u0930\u094B\u0936\u0928\u0940 \u091B\u093E \u0917\u0908 \u092A\u0942\u0930\u0947 \u0915\u093E\u0930\u093E\u0917\u0943\u0939 \u092E\u0947\u0902!",
            "\u0914\u0930 \u092B\u093F\u0930... \u092C\u0947\u092C\u0940 \u0915\u0943\u0937\u094D\u0923 \u0915\u093E \u091C\u0928\u094D\u092E \u0939\u0941\u0906!",
            "\u0928\u0940\u0932\u0947 \u0930\u0902\u0917 \u0915\u093E \u0938\u0941\u0902\u0926\u0930 \u0936\u093F\u0936\u0941,",
            "\u092E\u094B\u0930 \u092A\u0902\u0916 \u0915\u093E \u092E\u0941\u0915\u0941\u091F \u0914\u0930 \u092E\u0927\u0941\u0930 \u092E\u0941\u0938\u094D\u0915\u093E\u0928!",
        ],
        "story_en": [
            "Then came the magical night!",
            "At midnight on Ashtami,",
            "Lord Vishnu appeared with divine light!",
            "",
            "Golden light filled the entire prison!",
            "And then... Baby Krishna was born!",
            "A beautiful blue baby,",
            "with a peacock feather crown and sweet smile!",
        ],
        "image_label": "Baby Krishna born with golden divine light, Lord Vishnu 4-armed appearing above, dark prison lit up, magical, cute 3D cartoon",
        "prompt_num": 4,
    },
    {
        "page_num": 5,
        "bg_color": Color(0.88, 0.92, 0.98),
        "title_hi": "\u092F\u092E\u0941\u0928\u093E \u0928\u0926\u0940 \u092A\u093E\u0930 \u0915\u0930\u0928\u093E",
        "title_en": "Crossing the River Yamuna",
        "story_hi": [
            "\u091C\u0948\u0938\u0947 \u0939\u0940 \u0915\u0943\u0937\u094D\u0923 \u0915\u093E \u091C\u0928\u094D\u092E \u0939\u0941\u0906,",
            "\u0915\u093E\u0930\u093E\u0917\u0943\u0939 \u0915\u0947 \u0938\u092C \u0926\u0930\u0935\u093E\u091C\u093C\u0947 \u0916\u0941\u0926 \u0916\u0941\u0932 \u0917\u090F!",
            "\u092A\u0939\u0930\u0947\u0926\u093E\u0930 \u0938\u094B \u0917\u090F!",
            "",
            "\u0935\u093E\u0938\u0941\u0926\u0947\u0935 \u0928\u0947 \u092C\u0947\u092C\u0940 \u0915\u0943\u0937\u094D\u0923 \u0915\u094B",
            "\u091F\u094B\u0915\u0930\u0940 \u092E\u0947\u0902 \u0930\u0916\u093E \u0914\u0930 \u091A\u0932 \u092A\u0921\u093C\u0947\u0964",
            "\u092C\u093E\u0930\u093F\u0936 \u0939\u094B \u0930\u0939\u0940 \u0925\u0940, \u0932\u0947\u0915\u093F\u0928 \u0936\u0947\u0937\u0928\u093E\u0917",
            "\u0928\u0947 \u0905\u092A\u0928\u0947 \u092B\u0928 \u0938\u0947 \u092C\u091A\u094D\u091A\u0947 \u0915\u094B \u092C\u091A\u093E\u092F\u093E!",
            "\u092F\u092E\u0941\u0928\u093E \u0928\u0926\u0940 \u0928\u0947 \u0930\u093E\u0938\u094D\u0924\u093E \u0926\u0947 \u0926\u093F\u092F\u093E!",
        ],
        "story_en": [
            "As soon as Krishna was born,",
            "all prison doors opened by themselves!",
            "Guards fell asleep! It was magic!",
            "",
            "Vasudev put Baby Krishna in a basket",
            "on his head and started walking.",
            "It was raining, but the great serpent Sheshnag",
            "protected the baby with his big hood!",
            "River Yamuna made way for them!",
        ],
        "image_label": "Vasudev carrying baby Krishna in basket on head, crossing river Yamuna at night, Sheshnag serpent protecting from rain, stormy night, cute 3D cartoon",
        "prompt_num": 5,
    },
    {
        "page_num": 6,
        "bg_color": SOFT_GREEN,
        "title_hi": "\u0917\u094B\u0915\u0941\u0932 \u092E\u0947\u0902 \u0938\u094D\u0935\u093E\u0917\u0924!",
        "title_en": "Welcome to Gokul!",
        "story_hi": [
            "\u0935\u093E\u0938\u0941\u0926\u0947\u0935 \u0917\u094B\u0915\u0941\u0932 \u0917\u093E\u0901\u0935 \u092A\u0939\u0941\u0901\u091A\u0947\u0964",
            "\u0935\u0939\u093E\u0901 \u0928\u0902\u0926 \u092C\u093E\u092C\u093E \u0914\u0930 \u092F\u0936\u094B\u0926\u093E \u092E\u093E\u0901 \u0930\u0939\u0924\u0947 \u0925\u0947\u0964",
            "",
            "\u0935\u093E\u0938\u0941\u0926\u0947\u0935 \u0928\u0947 \u092C\u0947\u092C\u0940 \u0915\u0943\u0937\u094D\u0923 \u0915\u094B",
            "\u092F\u0936\u094B\u0926\u093E \u092E\u093E\u0901 \u0915\u0940 \u0917\u094B\u0926 \u092E\u0947\u0902 \u0930\u0916 \u0926\u093F\u092F\u093E\u0964",
            "",
            "\u092F\u0936\u094B\u0926\u093E \u092E\u093E\u0901 \u092C\u0939\u0941\u0924 \u0916\u0941\u0936 \u0939\u0941\u0908\u0902!",
            "\u0909\u0928\u094D\u0939\u094B\u0902\u0928\u0947 \u0915\u0943\u0937\u094D\u0923 \u0915\u094B \u092A\u094D\u092F\u093E\u0930 \u0938\u0947 \u0917\u0932\u0947 \u0932\u0917\u093E\u092F\u093E\u0964",
        ],
        "story_en": [
            "Vasudev reached the village of Gokul.",
            "Kind Nand Baba and Yashoda Ma lived there.",
            "",
            "Vasudev gently placed Baby Krishna",
            "in Yashoda Ma's loving arms.",
            "",
            "Yashoda Ma was so happy!",
            "She hugged little Krishna with all her love.",
        ],
        "image_label": "Yashoda Ma holding baby Krishna lovingly, Nand Baba smiling, cute village hut with cows and flowers, sunrise, warm colors, cute 3D cartoon",
        "prompt_num": 6,
    },
    {
        "page_num": 7,
        "bg_color": SOFT_YELLOW,
        "title_hi": "\u0928\u091F\u0916\u091F \u0915\u0928\u094D\u0939\u0948\u092F\u093E - \u092E\u093E\u0916\u0928 \u091A\u094B\u0930!",
        "title_en": "The Naughty One - Makhan Chor!",
        "story_hi": [
            "\u0915\u0943\u0937\u094D\u0923 \u0917\u094B\u0915\u0941\u0932 \u092E\u0947\u0902 \u092C\u0921\u093C\u0947 \u0939\u0941\u090F\u0964",
            "\u0935\u094B \u092C\u0939\u0941\u0924 \u0936\u0930\u093E\u0930\u0924\u0940 \u0914\u0930 \u092A\u094D\u092F\u093E\u0930\u0947 \u0925\u0947!",
            "",
            "\u0915\u0943\u0937\u094D\u0923 \u0915\u094B \u092E\u093E\u0916\u0928 (\u092E\u0915\u094D\u0916\u0928) \u091A\u0941\u0930\u093E\u0928\u093E \u092C\u0939\u0941\u0924 \u092A\u0938\u0902\u0926 \u0925\u093E!",
            "\u0935\u094B \u092C\u093E\u0902\u0938\u0941\u0930\u0940 \u092C\u091C\u093E\u0924\u0947 \u0925\u0947,",
            "\u0926\u094B\u0938\u094D\u0924\u094B\u0902 \u0915\u0947 \u0938\u093E\u0925 \u0916\u0947\u0932\u0924\u0947 \u0925\u0947,",
            "\u0914\u0930 \u092E\u094B\u0930 \u0915\u0947 \u0938\u093E\u0925 \u0928\u093E\u091A\u0924\u0947 \u0925\u0947!",
            "\u0938\u092C \u0915\u0943\u0937\u094D\u0923 \u0938\u0947 \u092C\u0939\u0941\u0924 \u092A\u094D\u092F\u093E\u0930 \u0915\u0930\u0924\u0947 \u0925\u0947!",
        ],
        "story_en": [
            "Krishna grew up in Gokul.",
            "He was very naughty and loveable!",
            "",
            "Krishna loved stealing butter (Makhan Chor)!",
            "He played his magical flute,",
            "played with his friends,",
            "and danced with the peacocks!",
            "Everyone in Gokul loved Krishna so much!",
        ],
        "image_label": "Little Krishna stealing butter from pot, friends watching and laughing, peacock dancing, flute, Gokul village, colorful flowers, cute 3D cartoon like gitaforkids style",
        "prompt_num": 7,
    },
    {
        "page_num": 8,
        "bg_color": CREAM,
        "title_hi": "\u0915\u0943\u0937\u094D\u0923 \u0928\u0947 \u0938\u092C\u0915\u094B \u092C\u091A\u093E\u092F\u093E!",
        "title_en": "Krishna Saved Everyone!",
        "story_hi": [
            "\u091C\u092C \u0915\u0943\u0937\u094D\u0923 \u092C\u0921\u093C\u0947 \u0939\u0941\u090F,",
            "\u0909\u0928\u094D\u0939\u094B\u0902\u0928\u0947 \u0915\u0902\u0938 \u0915\u094B \u0939\u0930\u093E\u092F\u093E",
            "\u0914\u0930 \u092E\u0925\u0941\u0930\u093E \u0915\u094B \u0906\u091C\u093C\u093E\u0926 \u0915\u0930\u093E\u092F\u093E!",
            "",
            "\u0938\u092C \u0932\u094B\u0917 \u092C\u0939\u0941\u0924 \u0916\u0941\u0936 \u0939\u0941\u090F!",
            "",
            "\u0938\u0940\u0916: \u0905\u091A\u094D\u091B\u093E\u0908 \u0915\u0940 \u0939\u092E\u0947\u0936\u093E \u091C\u0940\u0924 \u0939\u094B\u0924\u0940 \u0939\u0948!",
            "\u092D\u0917\u0935\u093E\u0928 \u0939\u092E\u0947\u0936\u093E \u0905\u091A\u094D\u091B\u0947 \u0932\u094B\u0917\u094B\u0902 \u0915\u0940 \u0930\u0915\u094D\u0937\u093E \u0915\u0930\u0924\u0947 \u0939\u0948\u0902!",
            "\u0938\u092C\u0938\u0947 \u092A\u094D\u092F\u093E\u0930 \u0915\u0930\u094B, \u0938\u092C\u0915\u094B \u0916\u0941\u0936\u0940 \u0926\u094B!",
        ],
        "story_en": [
            "When Krishna grew up,",
            "He defeated the evil Kansa",
            "and freed the people of Mathura!",
            "",
            "Everyone was so happy!",
            "",
            "Moral: Good always wins over evil!",
            "God always protects kind people!",
            "Spread love and joy everywhere!",
        ],
        "image_label": "Krishna as young boy with flute, happy people celebrating, flowers raining from sky, Mathura palace, peacock, lotus, golden light, cute 3D cartoon",
        "prompt_num": 8,
    },
]


# ═══════════════════════════════════════════════
# CREATE THE BOOK
# ═══════════════════════════════════════════════

def create_book():
    filepath = os.path.join(OUTPUT_DIR, "05_Shree_Krishna_Story_Hindi_English.pdf")
    c = canvas.Canvas(filepath, pagesize=A4)
    c.setTitle("Shree Krishna Birth Story - Hindi & English")
    c.setAuthor("Kids Book Publisher")

    # ──────── COVER PAGE ────────
    # Saffron-cream gradient
    for i in range(50):
        y = PAGE_H - i * (PAGE_H / 50)
        ratio = i / 50
        r = 1.0
        g = 0.95 - ratio * 0.2
        b = 0.8 - ratio * 0.4
        c.setFillColor(Color(r, g, b))
        c.rect(0, y, PAGE_W, PAGE_H / 50 + 1, fill=1, stroke=0)

    # Decorative border
    draw_decorative_border(c, 25, 25, PAGE_W - 50, PAGE_H - 50)

    # Corner flourishes
    draw_corner_flourish(c, 40, 40, 25, flip_x=False, flip_y=False)
    draw_corner_flourish(c, PAGE_W - 40, 40, 25, flip_x=True, flip_y=False)
    draw_corner_flourish(c, 40, PAGE_H - 40, 25, flip_x=False, flip_y=True)
    draw_corner_flourish(c, PAGE_W - 40, PAGE_H - 40, 25, flip_x=True, flip_y=True)

    # Image placeholder (BIG - main cover image)
    draw_image_placeholder(c, 80, PAGE_H / 2 - 50, PAGE_W - 160, 300,
                          "Cute baby Krishna sitting on lotus, playing flute, peacock feather on head, butter pot, flowers around, golden divine glow, 3D cartoon style", 0)

    # Title
    draw_hindi(c, PAGE_W / 2, PAGE_H - 80, "\u0936\u094D\u0930\u0940 \u0915\u0943\u0937\u094D\u0923 \u091C\u0928\u094D\u092E \u0915\u0925\u093E",
               size=32, bold=True, color=KRISHNA_BLUE)

    draw_english(c, PAGE_W / 2, PAGE_H - 120, "Shree Krishna Birth Story",
                size=24, bold=True, color=KRISHNA_BLUE)

    # Subtitle
    draw_hindi(c, PAGE_W / 2, PAGE_H - 155, "\u092C\u091A\u094D\u091A\u094B\u0902 \u0915\u0947 \u0932\u093F\u090F \u090F\u0915 \u0938\u0941\u0902\u0926\u0930 \u0915\u0939\u093E\u0928\u0940",
               size=16, color=SAFFRON)
    draw_english(c, PAGE_W / 2, PAGE_H - 175, "A Beautiful Story for Little Ones",
                size=14, italic=True, color=SAFFRON)

    # Bottom info
    draw_om_divider(c, 110)
    draw_hindi(c, PAGE_W / 2, 80, "\u0939\u093F\u0902\u0926\u0940 + English", size=14, color=GOLDEN_DARK)
    draw_english(c, PAGE_W / 2, 55, "Ages 3-10 | Janmashtami Special", size=11, color=gray)

    c.showPage()

    # ──────── STORY PAGES ────────
    for page in pages_data:
        # Background
        c.setFillColor(page["bg_color"])
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

        # Decorative border (subtle)
        c.setStrokeColor(Color(BORDER_GOLD.red, BORDER_GOLD.green, BORDER_GOLD.blue, alpha=0.5))
        c.setLineWidth(1.5)
        c.roundRect(20, 20, PAGE_W - 40, PAGE_H - 40, 10, fill=0)

        # ── TOP: Image placeholder (60% of page height) ──
        img_h = PAGE_H * 0.42
        img_y = PAGE_H - img_h - 45
        draw_image_placeholder(c, 40, img_y, PAGE_W - 80, img_h,
                              page["image_label"], page["prompt_num"])

        # ── Title area ──
        title_y = img_y - 15

        # Hindi title
        draw_hindi(c, PAGE_W / 2, title_y, page["title_hi"],
                  size=20, bold=True, color=KRISHNA_BLUE)

        # English title
        draw_english(c, PAGE_W / 2, title_y - 22, page["title_en"],
                    size=14, bold=True, color=KRISHNA_BLUE)

        # Divider
        draw_om_divider(c, title_y - 38)

        # ── Story text area ──
        text_y = title_y - 58

        # Background for text
        text_bg_h = text_y - 30
        c.setFillColor(Color(1, 1, 1, alpha=0.7))
        c.roundRect(35, 32, PAGE_W - 70, text_bg_h, 10, fill=1, stroke=0)

        # Hindi text (left side)
        hindi_x = PAGE_W / 4 + 10
        y = text_y
        for line in page["story_hi"]:
            if not line:
                y -= 8
                continue
            is_moral = "\u0938\u0940\u0916" in line  # "Seekh" (Moral)
            draw_hindi(c, hindi_x, y, line, size=12,
                      bold=is_moral, color=DEEP_RED if is_moral else DARK_TEXT)
            y -= 17

        # Vertical divider
        div_x = PAGE_W / 2 + 5
        c.setStrokeColor(Color(SAFFRON.red, SAFFRON.green, SAFFRON.blue, alpha=0.4))
        c.setLineWidth(1)
        c.setDash(3, 3)
        c.line(div_x, text_y + 10, div_x, 40)
        c.setDash()

        # English text (right side)
        eng_x = PAGE_W * 3 / 4
        y = text_y
        for line in page["story_en"]:
            if not line:
                y -= 8
                continue
            is_moral = "Moral:" in line or "Spread" in line
            draw_english(c, eng_x, y, line, size=10.5,
                        bold=is_moral, italic=is_moral,
                        color=DEEP_RED if is_moral else HexColor("#444444"))
            y -= 17

        # Page number
        draw_page_number(c, page["page_num"])

        c.showPage()

    # ──────── MORAL / ENDING PAGE ────────
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_decorative_border(c, 25, 25, PAGE_W - 50, PAGE_H - 50)

    # Image placeholder
    draw_image_placeholder(c, 80, PAGE_H / 2 + 20, PAGE_W - 160, 260,
                          "Krishna playing flute sitting on lotus, peacocks dancing, Radha, gopas, cows, Vrindavan, sunset, beautiful, cute 3D cartoon", 9)

    # Title
    draw_hindi(c, PAGE_W / 2, PAGE_H / 2 - 10, "\u0939\u092E\u0928\u0947 \u0915\u094D\u092F\u093E \u0938\u0940\u0916\u093E?",
              size=24, bold=True, color=KRISHNA_BLUE)
    draw_english(c, PAGE_W / 2, PAGE_H / 2 - 35, "What Did We Learn?",
                size=18, bold=True, color=KRISHNA_BLUE)

    draw_om_divider(c, PAGE_H / 2 - 52)

    # Morals in Hindi + English
    morals = [
        ("\u0905\u091A\u094D\u091B\u093E\u0908 \u0915\u0940 \u0939\u092E\u0947\u0936\u093E \u091C\u0940\u0924 \u0939\u094B\u0924\u0940 \u0939\u0948!", "Good always wins over evil!"),
        ("\u092D\u0917\u0935\u093E\u0928 \u0939\u092E\u0947\u0936\u093E \u0930\u0915\u094D\u0937\u093E \u0915\u0930\u0924\u0947 \u0939\u0948\u0902!", "God always protects the kind and truthful!"),
        ("\u092A\u094D\u092F\u093E\u0930 \u0914\u0930 \u0939\u093F\u092E\u094D\u092E\u0924 \u0938\u0947 \u0938\u092C \u0939\u094B\u0924\u093E \u0939\u0948!", "Love and courage can overcome anything!"),
        ("\u0915\u0943\u0937\u094D\u0923 \u091C\u0948\u0938\u0947 \u092C\u0928\u094B - \u0938\u092C\u0915\u094B \u0916\u0941\u0936\u0940 \u0926\u094B!", "Be like Krishna - spread joy everywhere!"),
    ]

    y = PAGE_H / 2 - 80
    for hi, en in morals:
        c.setFillColor(SAFFRON)
        c.circle(55, y + 4, 5, fill=1, stroke=0)

        draw_hindi(c, 70, y, hi, size=13, bold=True, color=DARK_TEXT, align="left")
        draw_english(c, 70, y - 18, en, size=11, italic=True, color=HexColor("#555555"), align="left")
        y -= 48

    # Jai Shree Krishna
    draw_hindi(c, PAGE_W / 2, 100, "\u091C\u092F \u0936\u094D\u0930\u0940 \u0915\u0943\u0937\u094D\u0923!",
              size=28, bold=True, color=KRISHNA_BLUE)
    draw_english(c, PAGE_W / 2, 75, "Jai Shree Krishna!",
                size=18, bold=True, color=KRISHNA_BLUE)

    draw_english(c, PAGE_W / 2, 45, "~ Happy Janmashtami ~", size=12, color=SAFFRON)

    c.showPage()

    # ──────── BACK COVER ────────
    c.setFillColor(KRISHNA_BLUE)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)

    draw_decorative_border(c, 25, 25, PAGE_W - 50, PAGE_H - 50, color=GOLDEN)

    draw_hindi(c, PAGE_W / 2, PAGE_H / 2 + 80, "\u0936\u094D\u0930\u0940 \u0915\u0943\u0937\u094D\u0923 \u091C\u0928\u094D\u092E \u0915\u0925\u093E",
              size=24, bold=True, color=GOLDEN)
    draw_english(c, PAGE_W / 2, PAGE_H / 2 + 50, "Shree Krishna Birth Story",
                size=16, bold=True, color=white)

    draw_hindi(c, PAGE_W / 2, PAGE_H / 2, "\u092F\u0939 \u0915\u093F\u0924\u093E\u092C \u092C\u091A\u094D\u091A\u094B\u0902 \u0915\u094B \u0936\u094D\u0930\u0940 \u0915\u0943\u0937\u094D\u0923 \u0915\u0947",
              size=13, color=Color(1, 1, 1, alpha=0.8))
    draw_hindi(c, PAGE_W / 2, PAGE_H / 2 - 20, "\u091C\u0928\u094D\u092E \u0915\u0940 \u0938\u0941\u0902\u0926\u0930 \u0915\u0939\u093E\u0928\u0940 \u0938\u0941\u0928\u093E\u0924\u0940 \u0939\u0948",
              size=13, color=Color(1, 1, 1, alpha=0.8))
    draw_hindi(c, PAGE_W / 2, PAGE_H / 2 - 40, "\u0938\u0930\u0932 \u0939\u093F\u0902\u0926\u0940 \u0914\u0930 \u0905\u0902\u0917\u094D\u0930\u0947\u091C\u093C\u0940 \u092E\u0947\u0902\u0964",
              size=13, color=Color(1, 1, 1, alpha=0.8))

    draw_english(c, PAGE_W / 2, PAGE_H / 2 - 80, "A bilingual (Hindi + English) story book",
                size=11, color=Color(1, 1, 1, alpha=0.7))
    draw_english(c, PAGE_W / 2, PAGE_H / 2 - 100, "for children ages 3-10",
                size=11, color=Color(1, 1, 1, alpha=0.7))

    draw_english(c, PAGE_W / 2, 80, "Sample Book - Amazon KDP Ready",
                size=10, color=Color(1, 1, 1, alpha=0.5))

    c.showPage()
    c.save()
    print(f"Book saved: {filepath}")
    return filepath


if __name__ == "__main__":
    print("Creating Shree Krishna Birth Story (Hindi + English)...")
    print("=" * 50)
    filepath = create_book()
    size = os.path.getsize(filepath)
    print(f"\nBook created successfully!")
    print(f"File: {filepath}")
    print(f"Size: {size / 1024:.1f} KB")
    print("=" * 50)
