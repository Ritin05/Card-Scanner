"""
Super Sonic Industrial Machinery Products - Professional Catalogue Generator
Creates a high-tech, premium catalogue PDF with modern design
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm, inch
from reportlab.lib.colors import HexColor, white, black, Color
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from PIL import Image
import os
import math

# ============ DESIGN CONSTANTS ============
W, H = A4  # 595.27 x 841.89 points

# Premium Color Palette - High-tech industrial theme
DARK_BG = HexColor('#0B1426')        # Deep navy background
DARK_BG2 = HexColor('#0F1D35')       # Slightly lighter navy
ACCENT_BLUE = HexColor('#00A8FF')    # Electric blue accent
ACCENT_CYAN = HexColor('#00D4FF')    # Cyan highlight
ACCENT_RED = HexColor('#FF3B3B')     # Red accent
GOLD = HexColor('#C5A55A')           # Gold/premium accent
LIGHT_GREY = HexColor('#E8ECF1')     # Light background
CARD_BG = HexColor('#FFFFFF')        # White card
CARD_BORDER = HexColor('#E0E5EC')    # Card border
TEXT_DARK = HexColor('#1A1A2E')      # Dark text
TEXT_GREY = HexColor('#6B7280')      # Grey text
TEXT_LIGHT = HexColor('#9CA3AF')     # Light grey text
HEADER_BG = HexColor('#0D2137')      # Header background
GRADIENT_START = HexColor('#0a1628')  # Gradient dark
GRADIENT_END = HexColor('#1a3a5c')    # Gradient lighter
SECTION_BLUE = HexColor('#003366')   # Section header blue
WHITE_TRANS = Color(1, 1, 1, 0.1)    # Transparent white

# Margins
MARGIN = 25 * mm
INNER_MARGIN = 15 * mm

OUTPUT_FILE = "D:/Nidhi/n8n/Card Scan/SuperSonic_Professional_Catalogue.pdf"
IMG_DIR = "D:/Nidhi/n8n/Card Scan/extracted_images"


def draw_gradient_rect(c, x, y, w, h, color1, color2, steps=50, direction='vertical'):
    """Draw a gradient rectangle"""
    r1, g1, b1 = color1.red, color1.green, color1.blue
    r2, g2, b2 = color2.red, color2.green, color2.blue

    if direction == 'vertical':
        step_h = h / steps
        for i in range(steps):
            t = i / steps
            r = r1 + (r2 - r1) * t
            g = g1 + (g2 - g1) * t
            b = b1 + (b2 - b1) * t
            c.setFillColor(Color(r, g, b))
            c.rect(x, y + h - (i + 1) * step_h, w, step_h + 0.5, fill=1, stroke=0)
    else:
        step_w = w / steps
        for i in range(steps):
            t = i / steps
            r = r1 + (r2 - r1) * t
            g = g1 + (g2 - g1) * t
            b = b1 + (b2 - b1) * t
            c.setFillColor(Color(r, g, b))
            c.rect(x + i * step_w, y, step_w + 0.5, h, fill=1, stroke=0)


def draw_hex_pattern(c, x, y, w, h, size=20, color=None):
    """Draw subtle hexagonal pattern as background decoration"""
    if color is None:
        color = Color(1, 1, 1, 0.03)
    c.setStrokeColor(color)
    c.setLineWidth(0.3)

    hex_w = size * 1.732
    hex_h = size * 2

    cols = int(w / hex_w) + 2
    rows = int(h / hex_h) + 2

    for row in range(rows):
        for col in range(cols):
            cx = x + col * hex_w + (row % 2) * hex_w / 2
            cy = y + row * hex_h * 0.75
            if cx < x + w + size and cy < y + h + size:
                draw_hexagon(c, cx, cy, size * 0.8)


def draw_hexagon(c, cx, cy, size):
    """Draw a single hexagon"""
    path = c.beginPath()
    for i in range(6):
        angle = math.pi / 3 * i - math.pi / 6
        px = cx + size * math.cos(angle)
        py = cy + size * math.sin(angle)
        if i == 0:
            path.moveTo(px, py)
        else:
            path.lineTo(px, py)
    path.close()
    c.drawPath(path, stroke=1, fill=0)


def draw_decorative_line(c, x, y, w, color=None):
    """Draw a decorative accent line with dots"""
    if color is None:
        color = ACCENT_BLUE
    c.setStrokeColor(color)
    c.setLineWidth(2)
    c.line(x, y, x + w * 0.3, y)
    c.setLineWidth(0.5)
    c.line(x + w * 0.32, y, x + w, y)


def draw_modern_header(c, y, title, subtitle=None):
    """Draw a modern section header with accent bar"""
    # Accent bar
    c.setFillColor(ACCENT_BLUE)
    c.rect(MARGIN, y - 2, 4, 24, fill=1, stroke=0)

    # Title
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN + 12, y + 4, title)

    # Thin line
    c.setStrokeColor(ACCENT_BLUE)
    c.setLineWidth(0.5)
    title_width = c.stringWidth(title, "Helvetica-Bold", 16)
    c.line(MARGIN + 18 + title_width, y + 10, W - MARGIN, y + 10)

    if subtitle:
        c.setFillColor(TEXT_GREY)
        c.setFont("Helvetica", 8)
        c.drawString(MARGIN + 12, y - 8, subtitle)


def draw_product_card(c, x, y, w, h, product_name, brand="MiMY", has_image=False, img_path=None):
    """Draw a modern product card"""
    # Card shadow
    c.setFillColor(Color(0, 0, 0, 0.05))
    c.roundRect(x + 2, y - 2, w, h, 6, fill=1, stroke=0)

    # Card background
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, 6, fill=1, stroke=1)

    # Image area (top 65% of card)
    img_h = h * 0.62
    img_area_y = y + h - img_h - 8

    # Light grey image placeholder with icon
    c.setFillColor(HexColor('#F8FAFC'))
    c.roundRect(x + 8, img_area_y, w - 16, img_h, 4, fill=1, stroke=0)

    if img_path and os.path.exists(img_path):
        try:
            c.drawImage(img_path, x + 12, img_area_y + 4, w - 24, img_h - 8,
                       preserveAspectRatio=True, anchor='c', mask='auto')
        except:
            # Fallback: draw a tech icon
            draw_tech_icon(c, x + w/2, img_area_y + img_h/2, min(w, img_h) * 0.2)
    else:
        draw_tech_icon(c, x + w/2, img_area_y + img_h/2, min(w, img_h) * 0.2)

    # Bottom section - brand and product name
    bottom_y = y + 6

    # Brand tag
    c.setFillColor(ACCENT_BLUE)
    brand_w = c.stringWidth(brand, "Helvetica-Bold", 7) + 12
    c.roundRect(x + 8, bottom_y + 22, brand_w, 14, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawString(x + 14, bottom_y + 26, brand)

    # Product name
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 8)

    # Handle long names - word wrap
    words = product_name.split()
    lines = []
    current_line = ""
    max_w = w - 20
    for word in words:
        test = current_line + " " + word if current_line else word
        if c.stringWidth(test, "Helvetica-Bold", 8) < max_w:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)

    for i, line in enumerate(lines[:2]):
        c.drawString(x + 10, bottom_y + 12 - i * 10, line)


def draw_tech_icon(c, cx, cy, size):
    """Draw a simple tech/gear icon placeholder"""
    c.setStrokeColor(HexColor('#CBD5E1'))
    c.setLineWidth(1.5)
    c.setFillColor(Color(0, 0, 0, 0))

    # Outer circle
    c.circle(cx, cy, size, fill=0, stroke=1)
    # Inner circle
    c.circle(cx, cy, size * 0.4, fill=0, stroke=1)

    # Gear teeth
    for i in range(8):
        angle = math.pi / 4 * i
        x1 = cx + size * 0.7 * math.cos(angle)
        y1 = cy + size * 0.7 * math.sin(angle)
        x2 = cx + size * 1.1 * math.cos(angle)
        y2 = cy + size * 1.1 * math.sin(angle)
        c.line(x1, y1, x2, y2)


def draw_footer(c, page_num, total_pages):
    """Draw professional footer"""
    y = 20

    # Footer line
    c.setStrokeColor(ACCENT_BLUE)
    c.setLineWidth(1)
    c.line(MARGIN, y + 18, W - MARGIN, y + 18)

    # Company name
    c.setFillColor(TEXT_GREY)
    c.setFont("Helvetica", 7)
    c.drawString(MARGIN, y + 6, "SUPER SONIC  |  www.supersonicgroup.in  |  info@supersonicgroup.in")

    # Page number
    c.setFillColor(ACCENT_BLUE)
    c.setFont("Helvetica-Bold", 9)
    page_text = f"{page_num:02d}"
    c.drawRightString(W - MARGIN, y + 4, page_text)

    # Total pages indicator
    c.setFillColor(TEXT_LIGHT)
    c.setFont("Helvetica", 7)
    c.drawRightString(W - MARGIN, y - 4, f"of {total_pages:02d}")


def draw_white_footer(c, page_num, total_pages):
    """Draw footer for dark pages"""
    y = 20
    c.setStrokeColor(Color(1, 1, 1, 0.3))
    c.setLineWidth(0.5)
    c.line(MARGIN, y + 18, W - MARGIN, y + 18)

    c.setFillColor(Color(1, 1, 1, 0.6))
    c.setFont("Helvetica", 7)
    c.drawString(MARGIN, y + 6, "SUPER SONIC  |  www.supersonicgroup.in  |  info@supersonicgroup.in")

    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(W - MARGIN, y + 4, f"{page_num:02d}")
    c.setFillColor(Color(1, 1, 1, 0.4))
    c.setFont("Helvetica", 7)
    c.drawRightString(W - MARGIN, y - 4, f"of {total_pages:02d}")


# ============ PAGE BUILDERS ============

def page_cover(c):
    """Page 1 - Premium Cover Page"""
    # Full dark gradient background
    draw_gradient_rect(c, 0, 0, W, H, HexColor('#060d1a'), HexColor('#0f2847'), steps=80)

    # Hex pattern overlay
    draw_hex_pattern(c, 0, 0, W, H, size=30, color=Color(0, 0.66, 1, 0.04))

    # Top accent line
    c.setFillColor(ACCENT_BLUE)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    # Geometric accent shapes
    # Top-right corner decoration
    c.setStrokeColor(Color(0, 0.66, 1, 0.15))
    c.setLineWidth(1)
    for i in range(5):
        offset = i * 15
        c.line(W - 150 + offset, H - 80, W - 50 + offset, H - 180)

    # Left accent bar
    c.setFillColor(ACCENT_BLUE)
    c.rect(40, H - 420, 4, 120, fill=1, stroke=0)

    # Company name - top area
    c.setFillColor(Color(1, 1, 1, 0.9))
    c.setFont("Helvetica-Bold", 14)
    c.drawString(55, H - 100, "SUPER SONIC")

    c.setFillColor(ACCENT_BLUE)
    c.setFont("Helvetica", 9)
    c.drawString(55, H - 116, "IMPORT & EXPORT TRADING COMPANY")

    # Decorative line under company name
    c.setStrokeColor(Color(1, 1, 1, 0.2))
    c.setLineWidth(0.5)
    c.line(55, H - 128, 300, H - 128)

    # Main Title
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(55, H - 310, "INDUSTRIAL")
    c.drawString(55, H - 352, "MACHINERY")

    # "PRODUCTS" with accent color
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(55, H - 394, "PRODUCTS")

    # Accent line under title
    c.setFillColor(ACCENT_BLUE)
    c.rect(55, H - 410, 80, 3, fill=1, stroke=0)
    c.setFillColor(Color(1, 1, 1, 0.3))
    c.rect(140, H - 410, 200, 1, fill=1, stroke=0)

    # Subtitle
    c.setFillColor(Color(1, 1, 1, 0.7))
    c.setFont("Helvetica", 11)
    c.drawString(55, H - 435, "Premium Quality  |  Global Standards  |  Trusted Since 2003")

    # Product Categories - modern card style
    categories = [
        ("INDUSTRIAL\nAUTOMATION", "Servo Motors, Drivers\n& Controllers"),
        ("LASER\nMACHINERY", "Fiber Laser, CO2\n& Optics"),
        ("CNC MACHINE\nPRODUCTS", "Spindle Motors\n& Controllers"),
        ("MECHANICAL\nPRODUCTS", "Guideways, Screws\n& Actuators"),
        ("CUTTING &\nWELDING", "Laser Heads\n& Parts"),
    ]

    start_y = H - 530
    card_w = 95
    card_h = 85
    gap = 8
    start_x = 55

    for i, (title, desc) in enumerate(categories):
        x = start_x + i * (card_w + gap)
        y = start_y

        # Card with semi-transparent background
        c.setFillColor(Color(1, 1, 1, 0.06))
        c.setStrokeColor(Color(0, 0.66, 1, 0.2))
        c.setLineWidth(0.5)
        c.roundRect(x, y, card_w, card_h, 4, fill=1, stroke=1)

        # Blue top line on card
        c.setFillColor(ACCENT_BLUE)
        c.rect(x + 10, y + card_h - 3, card_w - 20, 2, fill=1, stroke=0)

        # Category title
        lines = title.split('\n')
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 8)
        for j, line in enumerate(lines):
            c.drawString(x + 8, y + card_h - 18 - j * 10, line)

        # Description
        desc_lines = desc.split('\n')
        c.setFillColor(Color(1, 1, 1, 0.5))
        c.setFont("Helvetica", 6.5)
        for j, line in enumerate(desc_lines):
            c.drawString(x + 8, y + 22 - j * 8, line)

    # Bottom section - Contact info
    # Dark panel at bottom
    c.setFillColor(Color(0, 0, 0, 0.4))
    c.rect(0, 0, W, 130, fill=1, stroke=0)

    # Blue accent line
    c.setFillColor(ACCENT_BLUE)
    c.rect(0, 130, W, 2, fill=1, stroke=0)

    # Logo area
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(55, 75, "SUPER SONIC")

    c.setFillColor(ACCENT_BLUE)
    c.setFont("Helvetica", 8)
    c.drawString(55, 60, "Excellence  |  Ethics  |  Growth for All")

    # Contact details - right side
    c.setFillColor(Color(1, 1, 1, 0.8))
    c.setFont("Helvetica", 7.5)
    contact_x = W - 55
    c.drawRightString(contact_x, 95, "Plot No. C-10/5-6, Soma Kanji Estate-2, (SK-2)")
    c.drawRightString(contact_x, 83, "Near Sosyo Circle, Opp. Sanidev Temple, Udhna Magdalla Road")
    c.drawRightString(contact_x, 71, "Surat (Gujarat) India - 395007")

    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(contact_x, 52, "+91 63537 67128  /  92745 51510")
    c.drawRightString(contact_x, 40, "www.supersonicgroup.in  |  info@supersonicgroup.in")

    # Catalogue year badge
    c.setFillColor(Color(1, 1, 1, 0.08))
    c.setStrokeColor(Color(1, 1, 1, 0.15))
    c.setLineWidth(0.5)
    c.roundRect(W - 120, H - 80, 70, 35, 4, fill=1, stroke=1)
    c.setFillColor(Color(1, 1, 1, 0.6))
    c.setFont("Helvetica", 7)
    c.drawCentredString(W - 85, H - 56, "CATALOGUE")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(W - 85, H - 72, "2025")

    draw_white_footer(c, 1, 8)


def page_company_profile(c):
    """Page 2 - Company Profile"""
    # White background with subtle pattern
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Top accent bar
    draw_gradient_rect(c, 0, H - 8, W, 8, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Side accent
    c.setFillColor(DARK_BG)
    c.rect(0, H - 200, 8, 200, fill=1, stroke=0)

    # Header section with dark background
    draw_gradient_rect(c, 0, H - 200, W, 192, DARK_BG, HexColor('#0f2847'))

    # Hex pattern in header
    draw_hex_pattern(c, 0, H - 200, W, 192, size=25, color=Color(1, 1, 1, 0.03))

    # "COMPANY" in large faded text
    c.setFillColor(Color(1, 1, 1, 0.05))
    c.setFont("Helvetica-Bold", 72)
    c.drawString(30, H - 170, "COMPANY")

    # Actual title
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(MARGIN + 10, H - 90, "COMPANY")
    c.setFillColor(ACCENT_CYAN)
    c.drawString(MARGIN + 10, H - 122, "PROFILE")

    # Blue accent line
    c.setFillColor(ACCENT_BLUE)
    c.rect(MARGIN + 10, H - 135, 60, 3, fill=1, stroke=0)

    # "Since 2003" badge
    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W - MARGIN - 100, H - 130, 90, 30, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(W - MARGIN - 55, H - 118, "Since 2003")

    # Decorative right side element
    c.setStrokeColor(Color(1, 1, 1, 0.1))
    c.setLineWidth(0.5)
    for i in range(3):
        c.line(W - 30 - i*12, H - 40, W - 30 - i*12, H - 180)

    # Main content area
    content_y = H - 240

    # Company description
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN, content_y, "Super Sonic")

    c.setFont("Helvetica", 9.5)
    c.setFillColor(TEXT_GREY)

    desc_lines = [
        "has been founded in 2003. It's one of the largest Import & Export Trading",
        "Company situated in Surat, Gujarat, India. Super Sonic has been spread in",
        "42,000 sq. ft areas. Super Sonic is dedicated to serve High Quality and",
        "Cost-effective Products to Customers worldwide.",
    ]

    for i, line in enumerate(desc_lines):
        c.drawString(MARGIN, content_y - 18 - i * 14, line)

    # Product range highlight box
    box_y = content_y - 100
    c.setFillColor(HexColor('#F0F7FF'))
    c.roundRect(MARGIN, box_y, W - 2*MARGIN, 55, 6, fill=1, stroke=0)

    # Blue left border
    c.setFillColor(ACCENT_BLUE)
    c.rect(MARGIN, box_y, 4, 55, fill=1, stroke=0)

    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(MARGIN + 15, box_y + 38, "Our Product Range:")
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_GREY)
    c.drawString(MARGIN + 15, box_y + 24, "Industrial Automation Products  |  Industrial Mechanical Products  |  Industrial Laser Products")
    c.drawString(MARGIN + 15, box_y + 12, "Textile Machinery & Parts  |  Textile Value Added Materials  |  Health Care Massage Products")

    # Core values section - modern cards
    values_y = box_y - 50

    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 13)
    # Decorative line
    draw_decorative_line(c, MARGIN, values_y - 5, W - 2*MARGIN)

    # Value cards in a row
    card_data = [
        ("CORE IDEOLOGY", "We will always search and work for\nthe betterment and development of\nindustries. Delivering excellent\nservices & solutions globally.", ACCENT_BLUE),
        ("OUR DNA", "Excellence | Ethics\nGrowth for All\n\nAccountability & Passion\nfor Growth", HexColor('#10B981')),
        ("BUSINESS MANTRA", '"Growing Together"\n\nLong-term business\nrelationship with customers\nand suppliers', GOLD),
        ("MANAGEMENT\nMANTRA", "Easy | Fast | Accurate\n\nInnovative value for\nmoney products &\nexcellent services", HexColor('#8B5CF6')),
    ]

    card_w = (W - 2*MARGIN - 3*10) / 4
    card_h = 160
    card_start_y = values_y - 25

    for i, (title, desc, color) in enumerate(card_data):
        x = MARGIN + i * (card_w + 10)
        y = card_start_y - card_h

        # Card
        c.setFillColor(white)
        c.setStrokeColor(CARD_BORDER)
        c.setLineWidth(0.5)
        c.roundRect(x, y, card_w, card_h, 6, fill=1, stroke=1)

        # Top color accent
        c.setFillColor(color)
        # Clip rounded rect top - just draw a small rect
        c.rect(x + 1, y + card_h - 4, card_w - 2, 4, fill=1, stroke=0)

        # Icon circle
        c.setFillColor(Color(color.red, color.green, color.blue, 0.1))
        c.circle(x + 20, y + card_h - 25, 12, fill=1, stroke=0)
        c.setFillColor(color)
        c.circle(x + 20, y + card_h - 25, 5, fill=1, stroke=0)

        # Title
        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica-Bold", 8)
        title_lines = title.split('\n')
        for j, tl in enumerate(title_lines):
            c.drawString(x + 10, y + card_h - 48 - j*10, tl)

        # Description
        c.setFillColor(TEXT_GREY)
        c.setFont("Helvetica", 7)
        desc_lines = desc.split('\n')
        desc_start = y + card_h - 68 - (len(title_lines) - 1) * 10
        for j, dl in enumerate(desc_lines):
            c.drawString(x + 10, desc_start - j * 10, dl)

    # Stats section at bottom
    stats_y = card_start_y - card_h - 50

    # Stats background
    c.setFillColor(DARK_BG)
    c.roundRect(MARGIN, stats_y, W - 2*MARGIN, 60, 6, fill=1, stroke=0)

    stats = [
        ("20+", "Years of\nExperience"),
        ("42,000", "Sq. Ft.\nFacility"),
        ("500+", "Satisfied\nCustomers"),
        ("1000+", "Products\nRange"),
    ]

    stat_w = (W - 2*MARGIN) / 4
    for i, (num, label) in enumerate(stats):
        x = MARGIN + i * stat_w + stat_w / 2

        # Divider
        if i > 0:
            c.setStrokeColor(Color(1, 1, 1, 0.15))
            c.setLineWidth(0.5)
            c.line(MARGIN + i * stat_w, stats_y + 10, MARGIN + i * stat_w, stats_y + 50)

        c.setFillColor(ACCENT_CYAN)
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(x, stats_y + 32, num)

        c.setFillColor(Color(1, 1, 1, 0.6))
        c.setFont("Helvetica", 7)
        label_lines = label.split('\n')
        for j, ll in enumerate(label_lines):
            c.drawCentredString(x, stats_y + 18 - j * 9, ll)

    draw_footer(c, 2, 8)


def draw_product_page(c, page_num, title, subtitle, products, cols=2):
    """Generic product page builder"""
    # White background
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Top accent
    draw_gradient_rect(c, 0, H - 6, W, 6, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Section header area
    header_h = 65
    draw_gradient_rect(c, 0, H - header_h - 6, W, header_h, DARK_BG, HexColor('#0f2847'))

    # Subtle hex pattern in header
    draw_hex_pattern(c, 0, H - header_h - 6, W, header_h, size=20, color=Color(1, 1, 1, 0.03))

    # Title
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(MARGIN, H - 45, title)

    if subtitle:
        c.setFillColor(ACCENT_CYAN)
        c.setFont("Helvetica", 8)
        c.drawString(MARGIN, H - 60, subtitle)

    # Category indicator on right
    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W - MARGIN - 50, H - 55, 45, 20, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W - MARGIN - 27.5, H - 48, f"PAGE {page_num:02d}")

    # Product grid
    content_y = H - header_h - 20
    available_h = content_y - 55  # Leave space for footer

    rows = math.ceil(len(products) / cols)

    card_gap = 10
    card_w = (W - 2*MARGIN - (cols-1)*card_gap) / cols
    card_h = min(available_h / rows - card_gap, 155)

    for i, (name, brand) in enumerate(products):
        row = i // cols
        col = i % cols

        x = MARGIN + col * (card_w + card_gap)
        y = content_y - (row + 1) * (card_h + card_gap)

        draw_product_card(c, x, y, card_w, card_h, name, brand)

    draw_footer(c, page_num, 8)


def page_industrial_automation(c):
    """Page 3 - Industrial Automation Products"""
    products = [
        ("AC Servo Motor & Driver", "YAKO"),
        ("Panasonic Servo Products", "Panasonic"),
        ("AC & DC Gear Motor", "MiMY"),
        ("Stepper Motor", "MiMY"),
        ("Stepper Driver", "YAKO"),
        ("Close-Loop Motor & Driver", "YAKO"),
        ("Planetary Gear Box & Harmonic Gear Box", "MiMY"),
        ("Encoder", "MiMY"),
    ]
    draw_product_page(c, 3, "INDUSTRIAL AUTOMATION PRODUCTS",
                      "Precision Motion Control & Drive Solutions", products, cols=2)


def page_mechanical_products(c):
    """Page 4 - Mechanical Products"""
    # White background
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Top accent
    draw_gradient_rect(c, 0, H - 6, W, 6, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Section 1: Mechanical Products
    header_h = 65
    draw_gradient_rect(c, 0, H - header_h - 6, W, header_h, DARK_BG, HexColor('#0f2847'))
    draw_hex_pattern(c, 0, H - header_h - 6, W, header_h, size=20, color=Color(1, 1, 1, 0.03))

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(MARGIN, H - 45, "MECHANICAL PRODUCTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN, H - 60, "Precision Mechanical Components & Linear Motion Systems")

    # Page badge
    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W - MARGIN - 50, H - 55, 45, 20, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W - MARGIN - 27.5, H - 48, "PAGE 04")

    mech_products = [
        ("Block Guideway", "MiMY"),
        ("Rack and Gear", "MiMY"),
        ("Drag Chain", "MiMY"),
        ("Ball Screw", "MiMY"),
        ("Cross Roller Guideway", "MiMY"),
        ("Aluminum Sliding Unit", "MiMY"),
        ("Single Axis Linear Actuator", "MiMY"),
    ]

    content_y = H - header_h - 15
    cols = 3
    card_gap = 8
    card_w = (W - 2*MARGIN - (cols-1)*card_gap) / cols
    card_h = 120

    for i, (name, brand) in enumerate(mech_products):
        row = i // cols
        col = i % cols
        x = MARGIN + col * (card_w + card_gap)
        y = content_y - (row + 1) * (card_h + card_gap)
        draw_product_card(c, x, y, card_w, card_h, name, brand)

    # Section 2: EDM Wire Cut Machines Consumables
    edm_y = content_y - 3 * (card_h + card_gap) - 15

    # Sub-header
    c.setFillColor(DARK_BG)
    c.roundRect(MARGIN, edm_y, W - 2*MARGIN, 30, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 12)
    c.drawString(MARGIN + 12, edm_y + 8, "EDM WIRE CUT MACHINES CONSUMABLES")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 7)
    c.drawRightString(W - MARGIN - 10, edm_y + 10, "Wires, Liquids & Coolants")

    edm_products = [
        ("DIAMOND Moly Wire", "Diamond"),
        ("MIMY Moly Wire", "MiMY"),
        ("JR1A Composite Liquid", "Jiarun"),
        ("JR3A Super Ointment (Coolant Gel)", "Jiarun"),
    ]

    edm_card_y = edm_y - 10
    cols = 4
    card_w2 = (W - 2*MARGIN - 3*8) / 4
    card_h2 = 110

    for i, (name, brand) in enumerate(edm_products):
        x = MARGIN + i * (card_w2 + 8)
        y = edm_card_y - card_h2
        draw_product_card(c, x, y, card_w2, card_h2, name, brand)

    draw_footer(c, 4, 8)


def page_pneumatic_cnc(c):
    """Page 5 - Pneumatic Parts & CNC Machine Products"""
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Top accent
    draw_gradient_rect(c, 0, H - 6, W, 6, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Section 1: Pneumatic Parts
    header_h = 50
    draw_gradient_rect(c, 0, H - header_h - 6, W, header_h, DARK_BG, HexColor('#0f2847'))
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, H - 40, "PNEUMATIC PARTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN, H - 52, "Cylinders, Valves & Pneumatic Components")

    pneu_products = [
        ("Cylinder", "MiMY"),
        ("Valve", "MiMY"),
    ]

    content_y = H - header_h - 15
    card_w = (W - 2*MARGIN - 10) / 2
    card_h = 120

    for i, (name, brand) in enumerate(pneu_products):
        x = MARGIN + i * (card_w + 10)
        y = content_y - card_h
        draw_product_card(c, x, y, card_w, card_h, name, brand)

    # Section 2: CNC Machine Products
    cnc_y = content_y - card_h - 20

    # Sub-header
    draw_gradient_rect(c, 0, cnc_y, W, 45, DARK_BG, HexColor('#0f2847'))
    draw_hex_pattern(c, 0, cnc_y, W, 45, size=15, color=Color(1, 1, 1, 0.03))

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, cnc_y + 15, "CNC MACHINE PRODUCTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN, cnc_y + 3, "High-Performance CNC Components & Controllers")

    # Page badge
    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W - MARGIN - 50, cnc_y + 12, 45, 20, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W - MARGIN - 27.5, cnc_y + 19, "PAGE 05")

    cnc_products = [
        ("Spindle Motor", "MiMY / HQD"),
        ("Dust Collector", "MiMY"),
        ("CNC Gear Box", "MiMY"),
        ("Rich Auto Controllers", "RichAuto"),
        ("CNC Controllers", "WEIHONG"),
        ("Servo Spindle Motor", "MiMY"),
        ("SAW Blade Spindle Motors", "MiMY"),
        ("Stone Bridge Cutting Motors", "MiMY"),
    ]

    cnc_content_y = cnc_y - 8
    cols = 3
    card_gap = 8
    card_w = (W - 2*MARGIN - 2*card_gap) / 3
    card_h = 115

    for i, (name, brand) in enumerate(cnc_products):
        row = i // cols
        col = i % cols
        x = MARGIN + col * (card_w + card_gap)
        y = cnc_content_y - (row + 1) * (card_h + card_gap)
        draw_product_card(c, x, y, card_w, card_h, name, brand)

    draw_footer(c, 5, 8)


def page_laser_machinery(c):
    """Page 6 - Laser Machinery Products"""
    products = [
        ("Q-switch Pulsed Fiber Laser", "Lianpin"),
        ("Laser Source", "MAX Photonics"),
        ("UV Source", "Gainlaser"),
        ("RF Co2 Laser Source", "DAVI"),
        ("Galvo Scanner Head", "MiMY"),
        ("JCZ/EZ Card Control Board", "JCZ"),
        ("Fly Mark Controller", "JCZ"),
        ("F-Theta Scan Lens", "MiMY"),
        ("All Optics", "MiMY"),
        ("Column & Beampath", "MiMY"),
        ("Rotary with Chunk", "MiMY"),
        ("CO2 Laser Glass Tube & Power Supply", "EFR Laser"),
    ]
    draw_product_page(c, 6, "LASER MACHINERY PRODUCTS",
                      "Advanced Laser Sources, Optics & Control Systems", products, cols=3)


def page_welding_parts(c):
    """Page 7 - Spot Welding & Laser Cutting Parts"""
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Top accent
    draw_gradient_rect(c, 0, H - 6, W, 6, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Section 1: Spot Welding
    header_h = 50
    draw_gradient_rect(c, 0, H - header_h - 6, W, header_h, DARK_BG, HexColor('#0f2847'))
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, H - 40, "SPOT WELDING MACHINE & PARTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN, H - 52, "Power Supplies, Optical Components & Consumables")

    weld_products = [
        ("Power Supply", "Generic"),
        ("Optical Path", "Generic"),
        ("All Optics", "Generic"),
        ("Pulsed Xenon Lamp", "Generic"),
        ("YAG Crystal Rod", "Generic"),
    ]

    content_y = H - header_h - 15
    cols = 3
    card_gap = 8
    card_w = (W - 2*MARGIN - 2*card_gap) / 3
    card_h = 115

    for i, (name, brand) in enumerate(weld_products):
        row = i // cols
        col = i % cols
        x = MARGIN + col * (card_w + card_gap)
        y = content_y - (row + 1) * (card_h + card_gap)
        draw_product_card(c, x, y, card_w, card_h, name, brand)

    # Section 2: Laser Cutting & Welding Parts
    cut_y = content_y - 2 * (card_h + card_gap) - 15

    draw_gradient_rect(c, 0, cut_y, W, 40, DARK_BG, HexColor('#0f2847'))
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN, cut_y + 12, "LASER CUTTING & WELDING PARTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN, cut_y + 2, "Industrial Laser Heads & Welding Systems")

    # Page badge
    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W - MARGIN - 50, cut_y + 10, 45, 20, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W - MARGIN - 27.5, cut_y + 17, "PAGE 07")

    cut_products = [
        ("ND 31 Laser Head", "WSX"),
        ("NC36 Laser Head", "WSX"),
        ("HD 31 Welding Head", "WSX"),
        ("BLT310 Controller", "BOCHU"),
        ("FS 2000E System", "BOCHU"),
        ("BLT421S Controller", "BOCHU"),
    ]

    cut_content_y = cut_y - 8
    for i, (name, brand) in enumerate(cut_products):
        row = i // cols
        col = i % cols
        x = MARGIN + col * (card_w + card_gap)
        y = cut_content_y - (row + 1) * (card_h + card_gap)
        draw_product_card(c, x, y, card_w, card_h, name, brand)

    draw_footer(c, 7, 8)


def page_back_cover(c):
    """Page 8 - Back Cover"""
    # Full dark background
    draw_gradient_rect(c, 0, 0, W, H, HexColor('#060d1a'), HexColor('#0f2847'), steps=80)
    draw_hex_pattern(c, 0, 0, W, H, size=30, color=Color(0, 0.66, 1, 0.03))

    # Top accent
    c.setFillColor(ACCENT_BLUE)
    c.rect(0, H - 6, W, 6, fill=1, stroke=0)

    # Additional products section
    c.setFillColor(Color(1, 1, 1, 0.08))
    c.roundRect(MARGIN, H - 350, W - 2*MARGIN, 300, 8, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN + 20, H - 65, "ADDITIONAL EQUIPMENT")

    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN + 20, H - 80, "High-Power Laser Sources & Cooling Systems")

    # Accent line
    c.setFillColor(ACCENT_BLUE)
    c.rect(MARGIN + 20, H - 90, 50, 2, fill=1, stroke=0)

    add_products = [
        ("MAX Photonics Laser Source", "MAX Photonics"),
        ("MAX Photonics High Power", "MAX Photonics"),
        ("S & A Industrial Chiller", "S&A"),
        ("RK Chunk Rotary", "RK"),
    ]

    cols = 2
    card_gap = 12
    card_w = (W - 2*MARGIN - card_gap - 40) / 2
    card_h = 115

    for i, (name, brand) in enumerate(add_products):
        row = i // cols
        col = i % cols
        x = MARGIN + 20 + col * (card_w + card_gap)
        y = H - 110 - (row + 1) * (card_h + card_gap)

        # Dark themed card
        c.setFillColor(Color(1, 1, 1, 0.06))
        c.setStrokeColor(Color(1, 1, 1, 0.1))
        c.setLineWidth(0.5)
        c.roundRect(x, y, card_w, card_h, 6, fill=1, stroke=1)

        # Product image area
        img_h = card_h * 0.55
        c.setFillColor(Color(1, 1, 1, 0.04))
        c.roundRect(x + 8, y + card_h - img_h - 8, card_w - 16, img_h, 4, fill=1, stroke=0)

        # Tech icon
        draw_tech_icon(c, x + card_w/2, y + card_h - img_h/2 - 4, 18)

        # Brand tag
        c.setFillColor(ACCENT_BLUE)
        brand_w = c.stringWidth(brand, "Helvetica-Bold", 7) + 12
        c.roundRect(x + 8, y + 22, brand_w, 14, 3, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 7)
        c.drawString(x + 14, y + 26, brand)

        # Product name
        c.setFillColor(Color(1, 1, 1, 0.9))
        c.setFont("Helvetica-Bold", 8)
        c.drawString(x + 10, y + 8, name)

    # Main branding section
    brand_y = 250

    # Accent line
    c.setFillColor(ACCENT_BLUE)
    c.rect(W/2 - 40, brand_y + 80, 80, 2, fill=1, stroke=0)

    # Company name
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(W/2, brand_y + 40, "SUPER SONIC")

    # Tagline
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 10)
    c.drawCentredString(W/2, brand_y + 18, "IMPORT & EXPORT TRADING COMPANY")

    # Business mantra
    c.setFillColor(Color(1, 1, 1, 0.5))
    c.setFont("Helvetica", 9)
    c.drawCentredString(W/2, brand_y - 5, '"Growing Together"')

    # Divider
    c.setStrokeColor(Color(1, 1, 1, 0.15))
    c.setLineWidth(0.5)
    c.line(W/2 - 100, brand_y - 20, W/2 + 100, brand_y - 20)

    # Contact information - clean layout
    contact_y = brand_y - 50

    c.setFillColor(Color(1, 1, 1, 0.7))
    c.setFont("Helvetica", 8.5)

    # Address
    c.setFillColor(ACCENT_BLUE)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(W/2, contact_y, "SUPER SONIC HOUSE")

    c.setFillColor(Color(1, 1, 1, 0.7))
    c.setFont("Helvetica", 8)
    c.drawCentredString(W/2, contact_y - 14, "Plot No. C-10/5-6, Soma Kanji Estate-2, (SK-2)")
    c.drawCentredString(W/2, contact_y - 26, "Near Sosyo Circle, Opp. Sanidev Temple, Udhna Magdalla Road")
    c.drawCentredString(W/2, contact_y - 38, "Surat (Gujarat) India - 395007")

    # Contact details with icons
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(W/2, contact_y - 60, "+91 63537 67128  /  92745 51510")

    c.setFillColor(Color(1, 1, 1, 0.8))
    c.setFont("Helvetica", 8.5)
    c.drawCentredString(W/2, contact_y - 76, "www.supersonicgroup.in  |  info@supersonicgroup.in")

    # DNA values at very bottom
    c.setFillColor(Color(1, 1, 1, 0.3))
    c.setFont("Helvetica", 7)
    c.drawCentredString(W/2, 55, "Excellence  |  Ethics  |  Growth for All  |  Easy  |  Fast  |  Accurate")

    draw_white_footer(c, 8, 8)


# ============ MAIN ============

def main():
    print("Creating professional catalogue...")

    c = canvas.Canvas(OUTPUT_FILE, pagesize=A4)
    c.setTitle("Super Sonic - Industrial Machinery Products Catalogue 2025")
    c.setAuthor("Super Sonic Import & Export Trading Company")
    c.setSubject("Industrial Machinery Products Catalogue")

    # Page 1 - Cover
    print("  Page 1: Cover...")
    page_cover(c)
    c.showPage()

    # Page 2 - Company Profile
    print("  Page 2: Company Profile...")
    page_company_profile(c)
    c.showPage()

    # Page 3 - Industrial Automation
    print("  Page 3: Industrial Automation Products...")
    page_industrial_automation(c)
    c.showPage()

    # Page 4 - Mechanical Products
    print("  Page 4: Mechanical Products & EDM Consumables...")
    page_mechanical_products(c)
    c.showPage()

    # Page 5 - Pneumatic & CNC
    print("  Page 5: Pneumatic Parts & CNC Machine Products...")
    page_pneumatic_cnc(c)
    c.showPage()

    # Page 6 - Laser Machinery
    print("  Page 6: Laser Machinery Products...")
    page_laser_machinery(c)
    c.showPage()

    # Page 7 - Welding Parts
    print("  Page 7: Spot Welding & Laser Cutting Parts...")
    page_welding_parts(c)
    c.showPage()

    # Page 8 - Back Cover
    print("  Page 8: Back Cover...")
    page_back_cover(c)
    c.showPage()

    c.save()
    print(f"\nCatalogue created successfully!")
    print(f"Output: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
