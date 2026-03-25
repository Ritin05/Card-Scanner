"""
Super Sonic Industrial Machinery Products - Professional Catalogue Generator
FINAL VERSION with actual product images from original PDF
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white, Color
from reportlab.pdfgen import canvas
import os
import math

# ============ DESIGN CONSTANTS ============
W, H = A4  # 595.27 x 841.89 points

# Premium Color Palette
DARK_BG = HexColor('#0B1426')
ACCENT_BLUE = HexColor('#00A8FF')
ACCENT_CYAN = HexColor('#00D4FF')
GOLD = HexColor('#C5A55A')
CARD_BG = HexColor('#FFFFFF')
CARD_BORDER = HexColor('#E0E5EC')
TEXT_DARK = HexColor('#1A1A2E')
TEXT_GREY = HexColor('#6B7280')
TEXT_LIGHT = HexColor('#9CA3AF')

MARGIN = 25 * mm
IMG_DIR = "D:/Nidhi/n8n/Card Scan/product_images"
OUTPUT_FILE = "D:/Nidhi/n8n/Card Scan/SuperSonic_Professional_Catalogue.pdf"


def draw_gradient_rect(c, x, y, w, h, color1, color2, steps=50, direction='vertical'):
    r1, g1, b1 = color1.red, color1.green, color1.blue
    r2, g2, b2 = color2.red, color2.green, color2.blue
    if direction == 'vertical':
        step_h = h / steps
        for i in range(steps):
            t = i / steps
            c.setFillColor(Color(r1+(r2-r1)*t, g1+(g2-g1)*t, b1+(b2-b1)*t))
            c.rect(x, y + h - (i+1)*step_h, w, step_h+0.5, fill=1, stroke=0)
    else:
        step_w = w / steps
        for i in range(steps):
            t = i / steps
            c.setFillColor(Color(r1+(r2-r1)*t, g1+(g2-g1)*t, b1+(b2-b1)*t))
            c.rect(x + i*step_w, y, step_w+0.5, h, fill=1, stroke=0)


def draw_hex_pattern(c, x, y, w, h, size=20, color=None):
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
            cx_ = x + col * hex_w + (row % 2) * hex_w / 2
            cy_ = y + row * hex_h * 0.75
            if cx_ < x + w + size and cy_ < y + h + size:
                path = c.beginPath()
                for i in range(6):
                    angle = math.pi / 3 * i - math.pi / 6
                    px = cx_ + size * 0.8 * math.cos(angle)
                    py = cy_ + size * 0.8 * math.sin(angle)
                    if i == 0:
                        path.moveTo(px, py)
                    else:
                        path.lineTo(px, py)
                path.close()
                c.drawPath(path, stroke=1, fill=0)


def draw_product_card(c, x, y, w, h, product_name, brand="MiMY", img_file=None):
    """Draw a modern product card with actual image"""
    # Card shadow
    c.setFillColor(Color(0, 0, 0, 0.06))
    c.roundRect(x+2, y-2, w, h, 6, fill=1, stroke=0)

    # Card background
    c.setFillColor(CARD_BG)
    c.setStrokeColor(CARD_BORDER)
    c.setLineWidth(0.5)
    c.roundRect(x, y, w, h, 6, fill=1, stroke=1)

    # Top accent line on card
    c.setFillColor(ACCENT_BLUE)
    c.rect(x+15, y+h-2, w-30, 2, fill=1, stroke=0)

    # Image area
    img_h = h * 0.58
    img_area_y = y + h - img_h - 6
    img_pad = 6

    # Light background for image
    c.setFillColor(HexColor('#F8FAFC'))
    c.roundRect(x+img_pad, img_area_y, w-2*img_pad, img_h, 4, fill=1, stroke=0)

    # Draw actual product image
    img_path = os.path.join(IMG_DIR, img_file) if img_file else None
    if img_path and os.path.exists(img_path):
        try:
            c.drawImage(img_path, x+img_pad+2, img_area_y+2, w-2*img_pad-4, img_h-4,
                       preserveAspectRatio=True, anchor='c', mask='auto')
        except Exception as e:
            print(f"  Warning: could not draw {img_file}: {e}")

    # Bottom section
    bottom_y = y + 4

    # Brand tag
    c.setFillColor(ACCENT_BLUE)
    brand_w = max(c.stringWidth(brand, "Helvetica-Bold", 6.5) + 10, 30)
    c.roundRect(x+8, bottom_y + 20, brand_w, 13, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 6.5)
    c.drawString(x+13, bottom_y + 23.5, brand)

    # Product name
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 7.5)
    # Word wrap
    words = product_name.split()
    lines = []
    current = ""
    for word in words:
        test = current + " " + word if current else word
        if c.stringWidth(test, "Helvetica-Bold", 7.5) < w - 20:
            current = test
        else:
            if current: lines.append(current)
            current = word
    if current: lines.append(current)
    for i, line in enumerate(lines[:2]):
        c.drawString(x+8, bottom_y + 10 - i*9, line)


def draw_footer(c, page_num, total_pages, dark=False):
    y = 18
    if dark:
        c.setStrokeColor(Color(1,1,1,0.2))
        c.setLineWidth(0.5)
        c.line(MARGIN, y+16, W-MARGIN, y+16)
        c.setFillColor(Color(1,1,1,0.5))
        c.setFont("Helvetica", 6.5)
        c.drawString(MARGIN, y+5, "SUPER SONIC  |  www.supersonicgroup.in  |  info@supersonicgroup.in")
        c.setFillColor(ACCENT_CYAN)
        c.setFont("Helvetica-Bold", 8)
        c.drawRightString(W-MARGIN, y+4, f"{page_num:02d} / {total_pages:02d}")
    else:
        c.setStrokeColor(ACCENT_BLUE)
        c.setLineWidth(0.8)
        c.line(MARGIN, y+16, W-MARGIN, y+16)
        c.setFillColor(TEXT_GREY)
        c.setFont("Helvetica", 6.5)
        c.drawString(MARGIN, y+5, "SUPER SONIC  |  www.supersonicgroup.in  |  info@supersonicgroup.in")
        c.setFillColor(ACCENT_BLUE)
        c.setFont("Helvetica-Bold", 8)
        c.drawRightString(W-MARGIN, y+4, f"{page_num:02d} / {total_pages:02d}")


# ======================== PAGE 1: COVER ========================
def page_cover(c):
    draw_gradient_rect(c, 0, 0, W, H, HexColor('#060d1a'), HexColor('#0f2847'), steps=80)
    draw_hex_pattern(c, 0, 0, W, H, size=30, color=Color(0, 0.66, 1, 0.04))

    # Top accent
    c.setFillColor(ACCENT_BLUE)
    c.rect(0, H-6, W, 6, fill=1, stroke=0)

    # Geometric lines top-right
    c.setStrokeColor(Color(0, 0.66, 1, 0.12))
    c.setLineWidth(0.8)
    for i in range(6):
        c.line(W-180+i*18, H-70, W-60+i*18, H-200)

    # Left accent bar
    c.setFillColor(ACCENT_BLUE)
    c.rect(40, H-420, 4, 120, fill=1, stroke=0)

    # Company name
    c.setFillColor(Color(1,1,1,0.9))
    c.setFont("Helvetica-Bold", 14)
    c.drawString(55, H-100, "SUPER SONIC")
    c.setFillColor(ACCENT_BLUE)
    c.setFont("Helvetica", 9)
    c.drawString(55, H-116, "IMPORT & EXPORT TRADING COMPANY")
    c.setStrokeColor(Color(1,1,1,0.2))
    c.setLineWidth(0.5)
    c.line(55, H-128, 300, H-128)

    # Main Title
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(55, H-310, "INDUSTRIAL")
    c.drawString(55, H-354, "MACHINERY")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica-Bold", 38)
    c.drawString(55, H-398, "PRODUCTS")

    # Accent line
    c.setFillColor(ACCENT_BLUE)
    c.rect(55, H-414, 80, 3, fill=1, stroke=0)
    c.setFillColor(Color(1,1,1,0.3))
    c.rect(140, H-413, 200, 1, fill=1, stroke=0)

    # Subtitle
    c.setFillColor(Color(1,1,1,0.7))
    c.setFont("Helvetica", 11)
    c.drawString(55, H-440, "Premium Quality  |  Global Standards  |  Trusted Since 2003")

    # Category cards
    categories = [
        ("INDUSTRIAL\nAUTOMATION", "Servo Motors, Drivers\n& Controllers"),
        ("LASER\nMACHINERY", "Fiber Laser, CO2\n& Optics"),
        ("CNC MACHINE\nPRODUCTS", "Spindle Motors\n& Controllers"),
        ("MECHANICAL\nPRODUCTS", "Guideways, Screws\n& Actuators"),
        ("CUTTING &\nWELDING", "Laser Heads\n& Parts"),
    ]

    card_w = 95
    card_h = 85
    gap = 8
    start_x = 55
    start_y = H - 540

    for i, (title, desc) in enumerate(categories):
        x = start_x + i*(card_w+gap)
        y = start_y
        c.setFillColor(Color(1,1,1,0.06))
        c.setStrokeColor(Color(0,0.66,1,0.2))
        c.setLineWidth(0.5)
        c.roundRect(x, y, card_w, card_h, 4, fill=1, stroke=1)
        c.setFillColor(ACCENT_BLUE)
        c.rect(x+10, y+card_h-3, card_w-20, 2, fill=1, stroke=0)
        lines = title.split('\n')
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 8)
        for j, ln in enumerate(lines):
            c.drawString(x+8, y+card_h-18-j*10, ln)
        c.setFillColor(Color(1,1,1,0.5))
        c.setFont("Helvetica", 6.5)
        for j, ln in enumerate(desc.split('\n')):
            c.drawString(x+8, y+22-j*8, ln)

    # Bottom contact panel
    c.setFillColor(Color(0,0,0,0.4))
    c.rect(0, 0, W, 130, fill=1, stroke=0)
    c.setFillColor(ACCENT_BLUE)
    c.rect(0, 130, W, 2, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 22)
    c.drawString(55, 78, "SUPER SONIC")
    c.setFillColor(ACCENT_BLUE)
    c.setFont("Helvetica", 8)
    c.drawString(55, 62, "Excellence  |  Ethics  |  Growth for All")

    cx = W - 55
    c.setFillColor(Color(1,1,1,0.8))
    c.setFont("Helvetica", 7.5)
    c.drawRightString(cx, 98, "Plot No. C-10/5-6, Soma Kanji Estate-2, (SK-2)")
    c.drawRightString(cx, 86, "Near Sosyo Circle, Opp. Sanidev Temple, Udhna Magdalla Road")
    c.drawRightString(cx, 74, "Surat (Gujarat) India - 395007")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica-Bold", 8)
    c.drawRightString(cx, 55, "+91 63537 67128  /  92745 51510")
    c.drawRightString(cx, 43, "www.supersonicgroup.in  |  info@supersonicgroup.in")

    # Year badge
    c.setFillColor(Color(1,1,1,0.08))
    c.setStrokeColor(Color(1,1,1,0.15))
    c.roundRect(W-120, H-80, 70, 35, 4, fill=1, stroke=1)
    c.setFillColor(Color(1,1,1,0.6))
    c.setFont("Helvetica", 7)
    c.drawCentredString(W-85, H-56, "CATALOGUE")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica-Bold", 13)
    c.drawCentredString(W-85, H-72, "2025")

    draw_footer(c, 1, 8, dark=True)


# ======================== PAGE 2: COMPANY PROFILE ========================
def page_company_profile(c):
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Top accent
    draw_gradient_rect(c, 0, H-8, W, 8, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Header
    draw_gradient_rect(c, 0, H-200, W, 192, DARK_BG, HexColor('#0f2847'))
    draw_hex_pattern(c, 0, H-200, W, 192, size=25, color=Color(1,1,1,0.03))

    # Watermark text
    c.setFillColor(Color(1,1,1,0.04))
    c.setFont("Helvetica-Bold", 72)
    c.drawString(30, H-170, "COMPANY")

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 28)
    c.drawString(MARGIN+10, H-90, "COMPANY")
    c.setFillColor(ACCENT_CYAN)
    c.drawString(MARGIN+10, H-122, "PROFILE")

    c.setFillColor(ACCENT_BLUE)
    c.rect(MARGIN+10, H-135, 60, 3, fill=1, stroke=0)

    # Since badge
    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W-MARGIN-100, H-130, 90, 30, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 11)
    c.drawCentredString(W-MARGIN-55, H-118, "Since 2003")

    # Description
    cy = H - 240
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN, cy, "Super Sonic")
    c.setFont("Helvetica", 9.5)
    c.setFillColor(TEXT_GREY)
    lines = [
        "has been founded in 2003. It's one of the largest Import & Export Trading Company",
        "situated in Surat, Gujarat, India. Super Sonic has been spread in 42,000 sq. ft areas.",
        "Super Sonic is dedicated to serve High Quality and Cost-effective Products to Customers.",
        "Our company believes in long-term business relationships with customers and suppliers.",
        "We have hundreds of satisfied customers around the Indian and world.",
    ]
    for i, ln in enumerate(lines):
        c.drawString(MARGIN, cy-18-i*14, ln)

    # Product range box
    by = cy - 110
    c.setFillColor(HexColor('#F0F7FF'))
    c.roundRect(MARGIN, by, W-2*MARGIN, 55, 6, fill=1, stroke=0)
    c.setFillColor(ACCENT_BLUE)
    c.rect(MARGIN, by, 4, 55, fill=1, stroke=0)
    c.setFillColor(TEXT_DARK)
    c.setFont("Helvetica-Bold", 8.5)
    c.drawString(MARGIN+15, by+38, "Our Product Range:")
    c.setFont("Helvetica", 8)
    c.setFillColor(TEXT_GREY)
    c.drawString(MARGIN+15, by+24, "Industrial Automation Products  |  Industrial Mechanical Products  |  Industrial Laser Products")
    c.drawString(MARGIN+15, by+12, "Textile Machinery & Parts  |  Textile Value Added Materials  |  Health Care Massage Products")

    # Value cards
    vy = by - 30
    c.setFillColor(ACCENT_BLUE)
    c.rect(MARGIN, vy-2, 50, 2, fill=1, stroke=0)

    card_data = [
        ("CORE IDEOLOGY", "We will always search and work\nfor the betterment of industries.\nDelivering excellent services\n& solutions globally.", ACCENT_BLUE),
        ("OUR DNA", "Excellence | Ethics\nGrowth for All\n\nAccountability & Passion\nfor Growth", HexColor('#10B981')),
        ("BUSINESS MANTRA", '"Growing Together"\n\nLong-term business\nrelationship with customers\nand suppliers', GOLD),
        ("MANAGEMENT\nMANTRA", "Easy | Fast | Accurate\n\nInnovative value for\nmoney products &\nexcellent services", HexColor('#8B5CF6')),
    ]

    card_w = (W - 2*MARGIN - 3*10) / 4
    card_h = 155

    for i, (title, desc, color) in enumerate(card_data):
        x = MARGIN + i*(card_w+10)
        y = vy - card_h - 10

        c.setFillColor(white)
        c.setStrokeColor(CARD_BORDER)
        c.setLineWidth(0.5)
        c.roundRect(x, y, card_w, card_h, 6, fill=1, stroke=1)
        c.setFillColor(color)
        c.rect(x+1, y+card_h-4, card_w-2, 4, fill=1, stroke=0)

        # Color dot
        c.setFillColor(Color(color.red, color.green, color.blue, 0.1))
        c.circle(x+20, y+card_h-25, 12, fill=1, stroke=0)
        c.setFillColor(color)
        c.circle(x+20, y+card_h-25, 5, fill=1, stroke=0)

        c.setFillColor(TEXT_DARK)
        c.setFont("Helvetica-Bold", 7.5)
        for j, tl in enumerate(title.split('\n')):
            c.drawString(x+10, y+card_h-48-j*10, tl)

        c.setFillColor(TEXT_GREY)
        c.setFont("Helvetica", 6.5)
        title_lines = len(title.split('\n'))
        for j, dl in enumerate(desc.split('\n')):
            c.drawString(x+10, y+card_h-65-title_lines*5-j*9, dl)

    # Stats bar
    stats_y = vy - card_h - 70
    c.setFillColor(DARK_BG)
    c.roundRect(MARGIN, stats_y, W-2*MARGIN, 55, 6, fill=1, stroke=0)

    stats = [("20+", "Years of\nExperience"), ("42,000", "Sq. Ft.\nFacility"),
             ("500+", "Satisfied\nCustomers"), ("1000+", "Products\nRange")]
    stat_w = (W-2*MARGIN)/4
    for i, (num, label) in enumerate(stats):
        x = MARGIN + i*stat_w + stat_w/2
        if i > 0:
            c.setStrokeColor(Color(1,1,1,0.15))
            c.setLineWidth(0.5)
            c.line(MARGIN+i*stat_w, stats_y+8, MARGIN+i*stat_w, stats_y+47)
        c.setFillColor(ACCENT_CYAN)
        c.setFont("Helvetica-Bold", 16)
        c.drawCentredString(x, stats_y+30, num)
        c.setFillColor(Color(1,1,1,0.6))
        c.setFont("Helvetica", 6.5)
        for j, ll in enumerate(label.split('\n')):
            c.drawCentredString(x, stats_y+16-j*9, ll)

    draw_footer(c, 2, 8)


# ======================== GENERIC PRODUCT PAGE ========================
def draw_product_page(c, page_num, title, subtitle, products, cols=2):
    """products: list of (name, brand, img_file)"""
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    # Top accent
    draw_gradient_rect(c, 0, H-6, W, 6, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Header
    header_h = 60
    draw_gradient_rect(c, 0, H-header_h-6, W, header_h, DARK_BG, HexColor('#0f2847'))
    draw_hex_pattern(c, 0, H-header_h-6, W, header_h, size=18, color=Color(1,1,1,0.03))

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, H-42, title)
    if subtitle:
        c.setFillColor(ACCENT_CYAN)
        c.setFont("Helvetica", 7.5)
        c.drawString(MARGIN, H-55, subtitle)

    # Page badge
    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W-MARGIN-48, H-50, 42, 18, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W-MARGIN-27, H-44, f"PAGE {page_num:02d}")

    # Product grid
    content_y = H - header_h - 16
    available_h = content_y - 50
    rows = math.ceil(len(products) / cols)
    card_gap = 9
    card_w = (W - 2*MARGIN - (cols-1)*card_gap) / cols
    card_h = min(available_h / rows - card_gap, 155)

    for i, (name, brand, img) in enumerate(products):
        row = i // cols
        col = i % cols
        x = MARGIN + col*(card_w+card_gap)
        y = content_y - (row+1)*(card_h+card_gap)
        draw_product_card(c, x, y, card_w, card_h, name, brand, img)

    draw_footer(c, page_num, 8)


# ======================== PAGE 3: INDUSTRIAL AUTOMATION ========================
def page_industrial_automation(c):
    products = [
        ("AC Servo Motor & Driver", "YAKO", "p3_ac_servo_motor.png"),
        ("Panasonic Servo Products", "Panasonic", "p3_panasonic_servo.png"),
        ("AC & DC Gear Motor", "MiMY", "p3_ac_dc_gear_motor.png"),
        ("Stepper Motor", "MiMY", "p3_stepper_motor.png"),
        ("Stepper Driver", "YAKO", "p3_stepper_driver.png"),
        ("Close-Loop Motor & Driver", "YAKO", "p3_closeloop_motor.png"),
        ("Planetary Gear Box & Harmonic Gear Box", "MiMY", "p3_planetary_gearbox.png"),
        ("Encoder", "MiMY", "p3_encoder.png"),
    ]
    draw_product_page(c, 3, "INDUSTRIAL AUTOMATION PRODUCTS",
                      "Precision Motion Control & Drive Solutions", products, cols=2)


# ======================== PAGE 4: MECHANICAL + EDM ========================
def page_mechanical(c):
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)

    draw_gradient_rect(c, 0, H-6, W, 6, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Header
    header_h = 55
    draw_gradient_rect(c, 0, H-header_h-6, W, header_h, DARK_BG, HexColor('#0f2847'))
    draw_hex_pattern(c, 0, H-header_h-6, W, header_h, size=18, color=Color(1,1,1,0.03))

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(MARGIN, H-40, "MECHANICAL PRODUCTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 7.5)
    c.drawString(MARGIN, H-53, "Precision Mechanical Components & Linear Motion Systems")

    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W-MARGIN-48, H-48, 42, 18, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W-MARGIN-27, H-42, "PAGE 04")

    # Mechanical products - 3 cols
    mech = [
        ("Block Guideway", "MiMY", "p4_block_guideway.png"),
        ("Rack and Gear", "MiMY", "p4_rack_gear.png"),
        ("Drag Chain", "MiMY", "p4_drag_chain.png"),
        ("Ball Screw", "MiMY", "p4_ball_screw.png"),
        ("Cross Roller Guideway", "MiMY", "p4_cross_roller.png"),
        ("Aluminum Sliding Unit", "MiMY", "p4_aluminum_sliding.png"),
        ("Single Axis Linear Actuator", "MiMY", "p4_linear_actuator.png"),
    ]

    cy = H - header_h - 12
    cols = 3
    gap = 8
    cw = (W - 2*MARGIN - 2*gap) / 3
    ch = 115

    for i, (name, brand, img) in enumerate(mech):
        row = i // cols
        col = i % cols
        x = MARGIN + col*(cw+gap)
        y = cy - (row+1)*(ch+gap)
        draw_product_card(c, x, y, cw, ch, name, brand, img)

    # EDM Section header
    edm_y = cy - 3*(ch+gap) - 12
    c.setFillColor(DARK_BG)
    c.roundRect(MARGIN, edm_y, W-2*MARGIN, 28, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 11)
    c.drawString(MARGIN+12, edm_y+8, "EDM WIRE CUT MACHINES CONSUMABLES")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 7)
    c.drawRightString(W-MARGIN-10, edm_y+10, "Wires, Liquids & Coolants")

    edm = [
        ("DIAMOND Moly Wire", "Diamond", "p4_diamond_moly_wire.png"),
        ("MIMY Moly Wire", "MiMY", "p4_mimy_moly_wire.png"),
        ("JR1A Composite Liquid", "Jiarun", "p4_jr1a_composite.png"),
        ("JR3A Super Ointment", "Jiarun", "p4_jr3a_ointment.png"),
    ]

    cw2 = (W - 2*MARGIN - 3*8) / 4
    ch2 = 108

    for i, (name, brand, img) in enumerate(edm):
        x = MARGIN + i*(cw2+8)
        y = edm_y - ch2 - 8
        draw_product_card(c, x, y, cw2, ch2, name, brand, img)

    draw_footer(c, 4, 8)


# ======================== PAGE 5: PNEUMATIC + CNC ========================
def page_pneumatic_cnc(c):
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    draw_gradient_rect(c, 0, H-6, W, 6, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Pneumatic header
    hh = 48
    draw_gradient_rect(c, 0, H-hh-6, W, hh, DARK_BG, HexColor('#0f2847'))
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN, H-38, "PNEUMATIC PARTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 7.5)
    c.drawString(MARGIN, H-50, "Cylinders, Valves & Pneumatic Components")

    # Pneumatic products
    cy = H - hh - 12
    cw = (W - 2*MARGIN - 10) / 2
    ch = 115

    pneu = [
        ("Cylinder", "MiMY", "p5_cylinder.png"),
        ("Valve", "MiMY", "p5_valve.png"),
    ]
    for i, (name, brand, img) in enumerate(pneu):
        x = MARGIN + i*(cw+10)
        draw_product_card(c, x, cy-ch, cw, ch, name, brand, img)

    # CNC header
    cnc_y = cy - ch - 18
    draw_gradient_rect(c, 0, cnc_y, W, 42, DARK_BG, HexColor('#0f2847'))
    draw_hex_pattern(c, 0, cnc_y, W, 42, size=15, color=Color(1,1,1,0.03))
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN, cnc_y+15, "CNC MACHINE PRODUCTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 7.5)
    c.drawString(MARGIN, cnc_y+3, "High-Performance CNC Components & Controllers")

    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W-MARGIN-48, cnc_y+12, 42, 18, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W-MARGIN-27, cnc_y+18, "PAGE 05")

    cnc = [
        ("Spindle Motor", "MiMY / HQD", "p5_spindle_motor.png"),
        ("Dust Collector", "MiMY", "p5_dust_collector.png"),
        ("CNC Gear Box", "MiMY", "p5_cnc_gearbox.png"),
        ("Rich Auto Controllers", "RichAuto", "p5_richauto_ctrl.png"),
        ("CNC Controllers", "WEIHONG", "p5_cnc_controllers.png"),
        ("Servo Spindle Motor", "MiMY", "p5_servo_spindle.png"),
        ("SAW Blade Spindle Motors", "MiMY", "p5_saw_blade_motor.png"),
        ("Stone Bridge Cutting Motors", "MiMY", "p5_stone_bridge_motor.png"),
    ]

    ccy = cnc_y - 8
    cols = 3
    gap = 8
    ccw = (W - 2*MARGIN - 2*gap) / 3
    cch = 112

    for i, (name, brand, img) in enumerate(cnc):
        row = i // cols
        col = i % cols
        x = MARGIN + col*(ccw+gap)
        y = ccy - (row+1)*(cch+gap)
        draw_product_card(c, x, y, ccw, cch, name, brand, img)

    draw_footer(c, 5, 8)


# ======================== PAGE 6: LASER MACHINERY ========================
def page_laser(c):
    products = [
        ("Q-switch Pulsed Fiber Laser", "Lianpin", "p6_qswitch_fiber.png"),
        ("Laser Source", "MAX Photonics", "p6_laser_source.png"),
        ("UV Source", "Gainlaser", "p6_uv_source.png"),
        ("RF Co2 Laser Source", "DAVI", "p6_rf_co2_laser.png"),
        ("Galvo Scanner Head", "MiMY", "p6_galvo_scanner.png"),
        ("JCZ/EZ Card Control Board", "JCZ", "p6_jcz_control.png"),
        ("Fly Mark Controller", "JCZ", "p6_fly_mark_ctrl.png"),
        ("F-Theta Scan Lens", "MiMY", "p6_ftheta_lens.png"),
        ("All Optics", "MiMY", "p6_all_optics.png"),
        ("Column & Beampath", "MiMY", "p6_column_beampath.png"),
        ("Rotary with Chunk", "MiMY", "p6_rotary_chunk.png"),
        ("CO2 Laser Glass Tube & Power Supply", "EFR Laser", "p6_co2_tube_power.png"),
    ]
    draw_product_page(c, 6, "LASER MACHINERY PRODUCTS",
                      "Advanced Laser Sources, Optics & Control Systems", products, cols=3)


# ======================== PAGE 7: WELDING & CUTTING ========================
def page_welding(c):
    c.setFillColor(white)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    draw_gradient_rect(c, 0, H-6, W, 6, ACCENT_BLUE, HexColor('#0066CC'), direction='horizontal')

    # Spot welding header
    hh = 48
    draw_gradient_rect(c, 0, H-hh-6, W, hh, DARK_BG, HexColor('#0f2847'))
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN, H-38, "SPOT WELDING MACHINE & PARTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 7.5)
    c.drawString(MARGIN, H-50, "Power Supplies, Optical Components & Consumables")

    weld = [
        ("Power Supply", "Generic", "p7_power_supply.png"),
        ("Optical Path", "Generic", "p7_optical_path.png"),
        ("All Optics", "Generic", "p7_all_optics_w.png"),
        ("Pulsed Xenon Lamp", "Generic", "p7_xenon_lamp.png"),
        ("YAG Crystal Rod", "Generic", "p7_yag_crystal.png"),
    ]

    cy = H - hh - 10
    cols = 3
    gap = 8
    cw = (W - 2*MARGIN - 2*gap) / 3
    ch = 112

    for i, (name, brand, img) in enumerate(weld):
        row = i // cols
        col = i % cols
        x = MARGIN + col*(cw+gap)
        y = cy - (row+1)*(ch+gap)
        draw_product_card(c, x, y, cw, ch, name, brand, img)

    # Laser cutting header
    lc_y = cy - 2*(ch+gap) - 15
    draw_gradient_rect(c, 0, lc_y, W, 38, DARK_BG, HexColor('#0f2847'))
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 14)
    c.drawString(MARGIN, lc_y+12, "LASER CUTTING & WELDING PARTS")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 7.5)
    c.drawString(MARGIN, lc_y+2, "Industrial Laser Heads & Welding Systems")

    c.setFillColor(ACCENT_BLUE)
    c.roundRect(W-MARGIN-48, lc_y+10, 42, 18, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 7)
    c.drawCentredString(W-MARGIN-27, lc_y+16, "PAGE 07")

    cut = [
        ("ND 31 Laser Head", "WSX", "p7_nd31.png"),
        ("NC36 Laser Head", "WSX", "p7_nc36.png"),
        ("HD 31 Welding Head", "WSX", "p7_hd31.png"),
        ("BLT310 Controller", "BOCHU", "p7_blt310.png"),
        ("FS 2000E System", "BOCHU", None),
        ("BLT421S Controller", "BOCHU", "p7_blt421s.png"),
    ]

    lcy = lc_y - 8
    for i, (name, brand, img) in enumerate(cut):
        row = i // cols
        col = i % cols
        x = MARGIN + col*(cw+gap)
        y = lcy - (row+1)*(ch+gap)
        draw_product_card(c, x, y, cw, ch, name, brand, img)

    draw_footer(c, 7, 8)


# ======================== PAGE 8: BACK COVER ========================
def page_back(c):
    draw_gradient_rect(c, 0, 0, W, H, HexColor('#060d1a'), HexColor('#0f2847'), steps=80)
    draw_hex_pattern(c, 0, 0, W, H, size=30, color=Color(0, 0.66, 1, 0.03))

    c.setFillColor(ACCENT_BLUE)
    c.rect(0, H-6, W, 6, fill=1, stroke=0)

    # Additional equipment section
    c.setFillColor(Color(1,1,1,0.06))
    c.setStrokeColor(Color(0,0.66,1,0.08))
    c.setLineWidth(0.5)
    c.roundRect(MARGIN, H-360, W-2*MARGIN, 310, 8, fill=1, stroke=1)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(MARGIN+18, H-68, "ADDITIONAL EQUIPMENT")
    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 8)
    c.drawString(MARGIN+18, H-82, "High-Power Laser Sources & Cooling Systems")
    c.setFillColor(ACCENT_BLUE)
    c.rect(MARGIN+18, H-90, 50, 2, fill=1, stroke=0)

    add_prods = [
        ("MAX Photonics Laser Source", "MAX Photonics", "p8_max_photonics_1.png"),
        ("MAX Photonics High Power", "MAX Photonics", "p8_max_photonics_2.png"),
        ("S & A Industrial Chiller", "S&A", "p8_sa_chiller.png"),
        ("RK Chunk Rotary", "RK", "p8_rk_chunk.png"),
    ]

    cols = 2
    gap = 12
    cw = (W - 2*MARGIN - gap - 36) / 2
    ch = 115

    for i, (name, brand, img) in enumerate(add_prods):
        row = i // cols
        col = i % cols
        x = MARGIN + 18 + col*(cw+gap)
        y = H - 100 - (row+1)*(ch+gap)

        # Dark card
        c.setFillColor(Color(1,1,1,0.05))
        c.setStrokeColor(Color(1,1,1,0.1))
        c.roundRect(x, y, cw, ch, 6, fill=1, stroke=1)

        # Image
        c.setFillColor(Color(1,1,1,0.03))
        ih = ch * 0.55
        c.roundRect(x+6, y+ch-ih-6, cw-12, ih, 4, fill=1, stroke=0)

        img_path = os.path.join(IMG_DIR, img) if img else None
        if img_path and os.path.exists(img_path):
            try:
                c.drawImage(img_path, x+8, y+ch-ih-4, cw-16, ih-4,
                           preserveAspectRatio=True, anchor='c', mask='auto')
            except:
                pass

        # Brand
        c.setFillColor(ACCENT_BLUE)
        bw = max(c.stringWidth(brand, "Helvetica-Bold", 6.5)+10, 30)
        c.roundRect(x+8, y+20, bw, 12, 3, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 6.5)
        c.drawString(x+13, y+23, brand)

        c.setFillColor(Color(1,1,1,0.9))
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(x+8, y+7, name)

    # Branding section
    by = 260

    c.setFillColor(ACCENT_BLUE)
    c.rect(W/2-40, by+85, 80, 2, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(W/2, by+45, "SUPER SONIC")

    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica", 10)
    c.drawCentredString(W/2, by+22, "IMPORT & EXPORT TRADING COMPANY")

    c.setFillColor(Color(1,1,1,0.5))
    c.setFont("Helvetica", 9)
    c.drawCentredString(W/2, by, '"Growing Together"')

    c.setStrokeColor(Color(1,1,1,0.15))
    c.setLineWidth(0.5)
    c.line(W/2-100, by-15, W/2+100, by-15)

    # Contact
    cy = by - 45
    c.setFillColor(ACCENT_BLUE)
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(W/2, cy, "SUPER SONIC HOUSE")

    c.setFillColor(Color(1,1,1,0.7))
    c.setFont("Helvetica", 8)
    c.drawCentredString(W/2, cy-14, "Plot No. C-10/5-6, Soma Kanji Estate-2, (SK-2)")
    c.drawCentredString(W/2, cy-26, "Near Sosyo Circle, Opp. Sanidev Temple, Udhna Magdalla Road")
    c.drawCentredString(W/2, cy-38, "Surat (Gujarat) India - 395007")

    c.setFillColor(ACCENT_CYAN)
    c.setFont("Helvetica-Bold", 9)
    c.drawCentredString(W/2, cy-58, "+91 63537 67128  /  92745 51510")
    c.setFillColor(Color(1,1,1,0.8))
    c.setFont("Helvetica", 8.5)
    c.drawCentredString(W/2, cy-73, "www.supersonicgroup.in  |  info@supersonicgroup.in")

    c.setFillColor(Color(1,1,1,0.3))
    c.setFont("Helvetica", 7)
    c.drawCentredString(W/2, 55, "Excellence  |  Ethics  |  Growth for All  |  Easy  |  Fast  |  Accurate")

    draw_footer(c, 8, 8, dark=True)


# ======================== MAIN ========================
def main():
    print("Creating FINAL professional catalogue with product images...")
    c = canvas.Canvas(OUTPUT_FILE, pagesize=A4)
    c.setTitle("Super Sonic - Industrial Machinery Products Catalogue 2025")
    c.setAuthor("Super Sonic Import & Export Trading Company")
    c.setSubject("Industrial Machinery Products Catalogue")

    pages = [
        ("Cover", page_cover),
        ("Company Profile", page_company_profile),
        ("Industrial Automation", page_industrial_automation),
        ("Mechanical Products", page_mechanical),
        ("Pneumatic & CNC", page_pneumatic_cnc),
        ("Laser Machinery", page_laser),
        ("Welding & Cutting", page_welding),
        ("Back Cover", page_back),
    ]

    for i, (name, func) in enumerate(pages):
        print(f"  Page {i+1}: {name}...")
        func(c)
        c.showPage()

    c.save()
    print(f"\nCatalogue created: {OUTPUT_FILE}")
    sz = os.path.getsize(OUTPUT_FILE)
    print(f"File size: {sz/1024/1024:.1f} MB")


if __name__ == "__main__":
    main()
