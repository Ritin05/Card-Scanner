"""
Kids Books Creator - Creates 4 sample books for Amazon KDP
1. Coloring Book
2. Story Book
3. Activity Book
4. Handwriting Practice Book
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import (
    black, white, gray, lightgrey, HexColor,
    red, blue, green, orange, purple, pink, yellow, brown
)
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import math
import random
import os

OUTPUT_DIR = "D:/Nidhi/n8n/Card Scan/Sample_Books"
os.makedirs(OUTPUT_DIR, exist_ok=True)

PAGE_W, PAGE_H = A4  # 595.27 x 841.89

# ─────────────────────────────────────────────
# HELPER FUNCTIONS
# ─────────────────────────────────────────────

def draw_cover(c, title, subtitle, color):
    """Draw a colorful cover page"""
    # Background
    c.setFillColor(color)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1)

    # White center box
    margin = 60
    c.setFillColor(white)
    c.roundRect(margin, margin, PAGE_W - 2*margin, PAGE_H - 2*margin, 20, fill=1)

    # Decorative border
    c.setStrokeColor(color)
    c.setLineWidth(3)
    c.roundRect(margin+10, margin+10, PAGE_W - 2*margin - 20, PAGE_H - 2*margin - 20, 15, fill=0)

    # Stars decoration
    c.setFillColor(color)
    for i in range(8):
        x = random.randint(100, int(PAGE_W - 100))
        y = random.randint(500, 750)
        draw_star(c, x, y, 15, color)

    # Title
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 36)
    c.drawCentredString(PAGE_W/2, PAGE_H/2 + 120, title)

    # Subtitle
    c.setFillColor(gray)
    c.setFont("Helvetica", 18)
    c.drawCentredString(PAGE_W/2, PAGE_H/2 + 80, subtitle)

    # Age group
    c.setFillColor(color)
    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(PAGE_W/2, PAGE_H/2 - 20, "Ages 3-8 Years")

    # Bottom text
    c.setFillColor(gray)
    c.setFont("Helvetica", 12)
    c.drawCentredString(PAGE_W/2, margin + 40, "Sample Book - Created for Amazon KDP")

    c.showPage()


def draw_star(c, cx, cy, size, color):
    """Draw a simple star shape"""
    c.setFillColor(color)
    p = c.beginPath()
    for i in range(5):
        angle = math.radians(90 + i * 72)
        x = cx + size * math.cos(angle)
        y = cy + size * math.sin(angle)
        if i == 0:
            p.moveTo(x, y)
        else:
            p.lineTo(x, y)
        angle2 = math.radians(90 + i * 72 + 36)
        x2 = cx + size * 0.4 * math.cos(angle2)
        y2 = cy + size * 0.4 * math.sin(angle2)
        p.lineTo(x2, y2)
    p.close()
    c.drawPath(p, fill=1)


def draw_page_number(c, page_num):
    c.setFont("Helvetica", 10)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W/2, 30, f"- {page_num} -")


# ─────────────────────────────────────────────
# BOOK 1: COLORING BOOK
# ─────────────────────────────────────────────

def create_coloring_book():
    filepath = os.path.join(OUTPUT_DIR, "01_Kids_Coloring_Book.pdf")
    c = canvas.Canvas(filepath, pagesize=A4)
    c.setTitle("My Fun Coloring Book - For Kids")
    c.setAuthor("Kids Book Publisher")

    draw_cover(c, "My Fun", "Coloring Book", HexColor("#FF6B6B"))

    pages = [
        ("Smiling Sun", "sun"),
        ("Cute Star", "star_big"),
        ("Beautiful Flower", "flower"),
        ("Friendly Fish", "fish"),
        ("Happy House", "house"),
        ("Lovely Heart", "heart"),
        ("Butterfly", "butterfly"),
        ("Rainbow", "rainbow"),
        ("Cute Cat Face", "cat"),
        ("Christmas Tree", "tree"),
    ]

    for i, (title, shape) in enumerate(pages):
        # Title
        c.setFont("Helvetica-Bold", 24)
        c.setFillColor(black)
        c.drawCentredString(PAGE_W/2, PAGE_H - 60, f"Color the {title}!")

        c.setStrokeColor(black)
        c.setLineWidth(2.5)
        c.setFillColor(white)

        cx, cy = PAGE_W/2, PAGE_H/2 - 20

        if shape == "sun":
            # Sun with rays
            c.circle(cx, cy, 80, fill=0)
            # Rays
            for angle_deg in range(0, 360, 30):
                angle = math.radians(angle_deg)
                x1 = cx + 90 * math.cos(angle)
                y1 = cy + 90 * math.sin(angle)
                x2 = cx + 130 * math.cos(angle)
                y2 = cy + 130 * math.sin(angle)
                c.line(x1, y1, x2, y2)
            # Smile
            c.setLineWidth(2)
            c.arc(cx-30, cy-30, cx+30, cy+10, 200, 140)
            # Eyes
            c.circle(cx-25, cy+20, 6, fill=1)
            c.circle(cx+25, cy+20, 6, fill=1)

        elif shape == "star_big":
            size = 120
            p = c.beginPath()
            for j in range(5):
                angle = math.radians(90 + j * 72)
                x = cx + size * math.cos(angle)
                y = cy + size * math.sin(angle)
                if j == 0:
                    p.moveTo(x, y)
                else:
                    p.lineTo(x, y)
                angle2 = math.radians(90 + j * 72 + 36)
                x2 = cx + size * 0.45 * math.cos(angle2)
                y2 = cy + size * 0.45 * math.sin(angle2)
                p.lineTo(x2, y2)
            p.close()
            c.drawPath(p, fill=0, stroke=1)
            # Happy face on star
            c.circle(cx-20, cy+15, 5, fill=1)
            c.circle(cx+20, cy+15, 5, fill=1)
            c.arc(cx-20, cy-15, cx+20, cy+5, 200, 140)

        elif shape == "flower":
            # Petals
            for angle_deg in range(0, 360, 60):
                angle = math.radians(angle_deg)
                px = cx + 70 * math.cos(angle)
                py = cy + 70 * math.sin(angle)
                c.circle(px, py, 45, fill=0)
            # Center
            c.circle(cx, cy, 35, fill=0)
            # Stem
            c.line(cx, cy - 80, cx, cy - 250)
            # Leaves
            p = c.beginPath()
            p.moveTo(cx, cy - 150)
            p.curveTo(cx + 60, cy - 130, cx + 60, cy - 180, cx, cy - 170)
            c.drawPath(p, fill=0, stroke=1)
            p = c.beginPath()
            p.moveTo(cx, cy - 190)
            p.curveTo(cx - 60, cy - 170, cx - 60, cy - 220, cx, cy - 210)
            c.drawPath(p, fill=0, stroke=1)

        elif shape == "fish":
            # Body (ellipse)
            c.saveState()
            c.translate(cx, cy)
            c.scale(1.5, 1)
            c.circle(0, 0, 80, fill=0)
            c.restoreState()
            # Tail
            p = c.beginPath()
            p.moveTo(cx + 115, cy)
            p.lineTo(cx + 170, cy + 50)
            p.lineTo(cx + 170, cy - 50)
            p.close()
            c.drawPath(p, fill=0, stroke=1)
            # Eye
            c.circle(cx - 50, cy + 15, 10, fill=0)
            c.circle(cx - 50, cy + 15, 4, fill=1)
            # Mouth
            c.arc(cx - 90, cy - 15, cx - 60, cy + 5, 200, 140)
            # Scales pattern
            for row in range(3):
                for col in range(4):
                    sx = cx - 30 + col * 25
                    sy = cy - 20 + row * 20
                    c.arc(sx - 10, sy - 8, sx + 10, sy + 8, 0, 180)

        elif shape == "house":
            # Main body
            c.rect(cx - 90, cy - 100, 180, 150, fill=0)
            # Roof
            p = c.beginPath()
            p.moveTo(cx - 110, cy + 50)
            p.lineTo(cx, cy + 150)
            p.lineTo(cx + 110, cy + 50)
            p.close()
            c.drawPath(p, fill=0, stroke=1)
            # Door
            c.rect(cx - 25, cy - 100, 50, 80, fill=0)
            c.circle(cx + 15, cy - 60, 4, fill=0)
            # Windows
            c.rect(cx - 70, cy - 10, 40, 40, fill=0)
            c.line(cx - 70, cy + 10, cx - 30, cy + 10)
            c.line(cx - 50, cy - 10, cx - 50, cy + 30)
            c.rect(cx + 30, cy - 10, 40, 40, fill=0)
            c.line(cx + 30, cy + 10, cx + 70, cy + 10)
            c.line(cx + 50, cy - 10, cx + 50, cy + 30)
            # Chimney
            c.rect(cx + 40, cy + 100, 25, 50, fill=0)

        elif shape == "heart":
            size = 120
            p = c.beginPath()
            p.moveTo(cx, cy - size + 30)
            p.curveTo(cx - size, cy - size + 30, cx - size, cy + 30, cx, cy + size - 20)
            p.curveTo(cx + size, cy + 30, cx + size, cy - size + 30, cx, cy - size + 30)
            c.drawPath(p, fill=0, stroke=1)

        elif shape == "butterfly":
            # Body
            c.setLineWidth(3)
            c.line(cx, cy + 80, cx, cy - 80)
            # Antennae
            p = c.beginPath()
            p.moveTo(cx, cy + 80)
            p.curveTo(cx - 30, cy + 120, cx - 40, cy + 110, cx - 35, cy + 100)
            c.drawPath(p, fill=0, stroke=1)
            p = c.beginPath()
            p.moveTo(cx, cy + 80)
            p.curveTo(cx + 30, cy + 120, cx + 40, cy + 110, cx + 35, cy + 100)
            c.drawPath(p, fill=0, stroke=1)
            # Wings
            c.setLineWidth(2.5)
            # Upper wings
            c.saveState()
            c.translate(cx - 60, cy + 30)
            c.scale(1.2, 1)
            c.circle(0, 0, 55, fill=0)
            c.restoreState()
            c.saveState()
            c.translate(cx + 60, cy + 30)
            c.scale(1.2, 1)
            c.circle(0, 0, 55, fill=0)
            c.restoreState()
            # Lower wings
            c.saveState()
            c.translate(cx - 45, cy - 30)
            c.scale(1, 1)
            c.circle(0, 0, 40, fill=0)
            c.restoreState()
            c.saveState()
            c.translate(cx + 45, cy - 30)
            c.scale(1, 1)
            c.circle(0, 0, 40, fill=0)
            c.restoreState()
            # Wing patterns
            c.circle(cx - 60, cy + 30, 20, fill=0)
            c.circle(cx + 60, cy + 30, 20, fill=0)
            c.circle(cx - 45, cy - 30, 15, fill=0)
            c.circle(cx + 45, cy - 30, 15, fill=0)

        elif shape == "rainbow":
            for j, radius in enumerate([180, 155, 130, 105, 80]):
                c.arc(cx - radius, cy - radius, cx + radius, cy + radius, 0, 180)
            # Clouds
            for cloud_cx in [cx - 170, cx + 170]:
                c.circle(cloud_cx, cy, 30, fill=0)
                c.circle(cloud_cx - 20, cy - 10, 25, fill=0)
                c.circle(cloud_cx + 20, cy - 10, 25, fill=0)

        elif shape == "cat":
            # Face
            c.circle(cx, cy, 90, fill=0)
            # Ears
            p = c.beginPath()
            p.moveTo(cx - 70, cy + 65)
            p.lineTo(cx - 50, cy + 140)
            p.lineTo(cx - 20, cy + 75)
            p.close()
            c.drawPath(p, fill=0, stroke=1)
            p = c.beginPath()
            p.moveTo(cx + 70, cy + 65)
            p.lineTo(cx + 50, cy + 140)
            p.lineTo(cx + 20, cy + 75)
            p.close()
            c.drawPath(p, fill=0, stroke=1)
            # Inner ears
            p = c.beginPath()
            p.moveTo(cx - 60, cy + 75)
            p.lineTo(cx - 48, cy + 120)
            p.lineTo(cx - 30, cy + 80)
            p.close()
            c.drawPath(p, fill=0, stroke=1)
            p = c.beginPath()
            p.moveTo(cx + 60, cy + 75)
            p.lineTo(cx + 48, cy + 120)
            p.lineTo(cx + 30, cy + 80)
            p.close()
            c.drawPath(p, fill=0, stroke=1)
            # Eyes
            c.circle(cx - 30, cy + 15, 15, fill=0)
            c.circle(cx + 30, cy + 15, 15, fill=0)
            c.circle(cx - 30, cy + 15, 6, fill=1)
            c.circle(cx + 30, cy + 15, 6, fill=1)
            # Nose
            p = c.beginPath()
            p.moveTo(cx, cy - 5)
            p.lineTo(cx - 8, cy - 15)
            p.lineTo(cx + 8, cy - 15)
            p.close()
            c.drawPath(p, fill=1, stroke=1)
            # Mouth
            c.line(cx, cy - 15, cx, cy - 25)
            c.arc(cx - 20, cy - 35, cx, cy - 15, 0, -180)
            c.arc(cx, cy - 35, cx + 20, cy - 15, 0, -180)
            # Whiskers
            for dy in [0, -12, 12]:
                c.line(cx - 40, cy - 20 + dy, cx - 100, cy - 15 + dy)
                c.line(cx + 40, cy - 20 + dy, cx + 100, cy - 15 + dy)

        elif shape == "tree":
            # Trunk
            c.rect(cx - 20, cy - 150, 40, 120, fill=0)
            # Tree layers
            for j, (w, y_off) in enumerate([(140, -30), (120, 50), (100, 120), (80, 180)]):
                p = c.beginPath()
                p.moveTo(cx, cy + y_off + 60)
                p.lineTo(cx - w/2, cy + y_off)
                p.lineTo(cx + w/2, cy + y_off)
                p.close()
                c.drawPath(p, fill=0, stroke=1)
            # Star on top
            draw_star_outline(c, cx, cy + 250, 20)
            # Ornaments
            ornaments = [(cx-30, cy+20), (cx+35, cy+40), (cx-15, cy+90),
                         (cx+20, cy+130), (cx-25, cy+160), (cx+10, cy+70)]
            for ox, oy in ornaments:
                c.circle(ox, oy, 8, fill=0)

        # Instruction text
        c.setFont("Helvetica", 14)
        c.setFillColor(gray)
        c.drawCentredString(PAGE_W/2, 60, "Use your favorite colors to make it beautiful!")

        draw_page_number(c, i + 1)
        c.showPage()

    c.save()
    print(f"Coloring Book saved: {filepath}")


def draw_star_outline(c, cx, cy, size):
    p = c.beginPath()
    for j in range(5):
        angle = math.radians(90 + j * 72)
        x = cx + size * math.cos(angle)
        y = cy + size * math.sin(angle)
        if j == 0:
            p.moveTo(x, y)
        else:
            p.lineTo(x, y)
        angle2 = math.radians(90 + j * 72 + 36)
        x2 = cx + size * 0.45 * math.cos(angle2)
        y2 = cy + size * 0.45 * math.sin(angle2)
        p.lineTo(x2, y2)
    p.close()
    c.drawPath(p, fill=0, stroke=1)


# ─────────────────────────────────────────────
# BOOK 2: STORY BOOK
# ─────────────────────────────────────────────

def create_story_book():
    filepath = os.path.join(OUTPUT_DIR, "02_Kids_Story_Book.pdf")
    c = canvas.Canvas(filepath, pagesize=A4)
    c.setTitle("Magical Stories for Kids")
    c.setAuthor("Kids Book Publisher")

    draw_cover(c, "Magical Stories", "For Little Readers", HexColor("#4ECDC4"))

    stories = [
        {
            "title": "The Brave Little Rabbit",
            "pages": [
                {
                    "text": "Once upon a time, in a green forest, there lived a little rabbit named Bunny.\nBunny was small but very brave. He loved to explore new places\nand make new friends every day.",
                    "illustration": "rabbit_forest"
                },
                {
                    "text": "One day, Bunny heard a tiny cry near the river.\nA baby bird had fallen from its nest!\n'Don't worry, little bird!' said Bunny. 'I will help you!'",
                    "illustration": "rabbit_bird"
                },
                {
                    "text": "Bunny carefully picked up the baby bird.\nHe climbed the tree slowly and gently placed\nthe bird back in its nest. The mama bird was so happy!",
                    "illustration": "rabbit_tree"
                },
                {
                    "text": "From that day, the bird family and Bunny\nbecame the best of friends.\nMoral: Always be kind and help others in need!",
                    "illustration": "rabbit_friends"
                }
            ]
        },
        {
            "title": "The Magic Rainbow",
            "pages": [
                {
                    "text": "Little Mia loved colors more than anything.\nShe painted rainbows on everything -\nher walls, her books, even her shoes!",
                    "illustration": "girl_painting"
                },
                {
                    "text": "One rainy day, Mia saw a real rainbow in the sky.\n'I wish I could touch it!' she said.\nSuddenly, a magical bridge appeared!",
                    "illustration": "rainbow_bridge"
                },
                {
                    "text": "Mia walked on the rainbow bridge.\nEach color gave her a special gift -\nRed gave courage, Blue gave wisdom, Yellow gave joy!",
                    "illustration": "rainbow_walk"
                },
                {
                    "text": "When Mia came back, she shared her gifts\nwith everyone. The whole town became\nhappier and more colorful!\nMoral: Share your gifts with others!",
                    "illustration": "town_happy"
                }
            ]
        },
        {
            "title": "The Friendly Dragon",
            "pages": [
                {
                    "text": "Everyone in the village was scared of\nthe dragon on the mountain.\nBut little Rohan was curious, not scared.",
                    "illustration": "village_mountain"
                },
                {
                    "text": "Rohan climbed the mountain and found\nthe dragon. But the dragon was crying!\n'Why are you sad?' asked Rohan.",
                    "illustration": "dragon_crying"
                },
                {
                    "text": "'Nobody wants to be my friend,' said the dragon.\n'They all run away from me.'\n'I'll be your friend!' said Rohan with a big smile.",
                    "illustration": "dragon_rohan"
                },
                {
                    "text": "Rohan and the dragon became best friends.\nThe dragon helped the village by keeping\nthem warm in winter with his gentle fire.\nMoral: Don't judge others by how they look!",
                    "illustration": "dragon_village"
                }
            ]
        }
    ]

    for story in stories:
        # Story title page
        c.setFillColor(HexColor("#4ECDC4"))
        c.rect(0, 0, PAGE_W, PAGE_H, fill=1)
        c.setFillColor(white)
        c.setFont("Helvetica-Bold", 32)
        # Wrap title
        c.drawCentredString(PAGE_W/2, PAGE_H/2 + 30, story["title"])
        c.setFont("Helvetica", 16)
        c.drawCentredString(PAGE_W/2, PAGE_H/2 - 20, "~ A Story for You ~")
        c.showPage()

        for j, page in enumerate(story["pages"]):
            # Illustration placeholder (top half)
            c.setStrokeColor(lightgrey)
            c.setLineWidth(2)
            c.setFillColor(HexColor("#F7F7F7"))
            c.roundRect(50, PAGE_H/2 + 20, PAGE_W - 100, PAGE_H/2 - 80, 10, fill=1)

            # Placeholder icon
            c.setFillColor(lightgrey)
            c.setFont("Helvetica", 14)
            c.drawCentredString(PAGE_W/2, PAGE_H * 0.72, f"[ Illustration: {page['illustration']} ]")
            c.setFont("Helvetica", 11)
            c.drawCentredString(PAGE_W/2, PAGE_H * 0.68, "Add your beautiful illustration here!")

            # Decorative frame for illustration
            c.setStrokeColor(HexColor("#4ECDC4"))
            c.setLineWidth(1)
            c.setDash(3, 3)
            c.roundRect(60, PAGE_H/2 + 30, PAGE_W - 120, PAGE_H/2 - 100, 8, fill=0)
            c.setDash()

            # Text (bottom half)
            c.setFillColor(black)
            c.setFont("Helvetica", 16)
            lines = page["text"].split("\n")
            y = PAGE_H/2 - 30
            for line in lines:
                c.drawCentredString(PAGE_W/2, y, line.strip())
                y -= 28

            draw_page_number(c, j + 1)
            c.showPage()

    c.save()
    print(f"Story Book saved: {filepath}")


# ─────────────────────────────────────────────
# BOOK 3: ACTIVITY BOOK
# ─────────────────────────────────────────────

def create_activity_book():
    filepath = os.path.join(OUTPUT_DIR, "03_Kids_Activity_Book.pdf")
    c = canvas.Canvas(filepath, pagesize=A4)
    c.setTitle("Super Fun Activity Book")
    c.setAuthor("Kids Book Publisher")

    draw_cover(c, "Super Fun", "Activity Book", HexColor("#FFB347"))

    page_num = 1

    # ── MAZE PAGES ──
    def draw_maze_page(title, rows, cols):
        nonlocal page_num
        c.setFont("Helvetica-Bold", 22)
        c.setFillColor(HexColor("#FFB347"))
        c.drawCentredString(PAGE_W/2, PAGE_H - 50, title)

        c.setFont("Helvetica", 12)
        c.setFillColor(gray)
        c.drawCentredString(PAGE_W/2, PAGE_H - 75, "Find your way from START to FINISH!")

        # Generate a simple maze using randomized walls
        random.seed(42 + page_num)
        cell_w = (PAGE_W - 120) / cols
        cell_h = (PAGE_H - 220) / rows
        start_x = 60
        start_y = PAGE_H - 120

        c.setStrokeColor(black)
        c.setLineWidth(2)

        # Outer border
        c.rect(start_x, start_y - rows * cell_h, cols * cell_w, rows * cell_h)

        # Random internal walls
        for r in range(rows):
            for col_idx in range(cols):
                x = start_x + col_idx * cell_w
                y = start_y - r * cell_h

                # Random right wall
                if col_idx < cols - 1 and random.random() > 0.45:
                    c.line(x + cell_w, y, x + cell_w, y - cell_h)
                # Random bottom wall
                if r < rows - 1 and random.random() > 0.45:
                    c.line(x, y - cell_h, x + cell_w, y - cell_h)

        # START and FINISH labels
        c.setFillColor(HexColor("#4CAF50"))
        c.setFont("Helvetica-Bold", 14)
        c.drawString(start_x + 5, start_y + 10, "START >>>")

        c.setFillColor(HexColor("#F44336"))
        c.drawRightString(start_x + cols * cell_w - 5, start_y - rows * cell_h - 20, "<<< FINISH")

        draw_page_number(c, page_num)
        page_num += 1
        c.showPage()

    draw_maze_page("Easy Maze", 6, 6)
    draw_maze_page("Medium Maze", 8, 8)
    draw_maze_page("Hard Maze", 10, 10)

    # ── DOT-TO-DOT PAGES ──
    def draw_dot_to_dot(title, points):
        nonlocal page_num
        c.setFont("Helvetica-Bold", 22)
        c.setFillColor(HexColor("#FFB347"))
        c.drawCentredString(PAGE_W/2, PAGE_H - 50, title)

        c.setFont("Helvetica", 12)
        c.setFillColor(gray)
        c.drawCentredString(PAGE_W/2, PAGE_H - 75, "Connect the dots from 1 to finish the picture!")

        c.setFillColor(black)
        c.setStrokeColor(lightgrey)
        c.setLineWidth(0.5)
        c.setDash(2, 2)

        for i, (x, y) in enumerate(points):
            # Dot
            c.setFillColor(black)
            c.circle(x, y, 4, fill=1)
            # Number
            c.setFont("Helvetica-Bold", 11)
            c.drawString(x + 8, y + 3, str(i + 1))
            # Dashed line to next
            if i < len(points) - 1:
                c.setStrokeColor(lightgrey)
                c.line(x, y, points[i+1][0], points[i+1][1])

        c.setDash()
        draw_page_number(c, page_num)
        page_num += 1
        c.showPage()

    # Star shape dots
    star_points = []
    cx, cy = PAGE_W/2, PAGE_H/2
    for i in range(10):
        angle = math.radians(90 + i * 36)
        r = 150 if i % 2 == 0 else 70
        star_points.append((cx + r * math.cos(angle), cy + r * math.sin(angle)))
    star_points.append(star_points[0])  # close
    draw_dot_to_dot("Dot-to-Dot: Star", star_points)

    # House shape dots
    house_points = [
        (200, 250), (400, 250),  # bottom
        (400, 450),  # right wall up
        (PAGE_W/2, 580),  # roof peak
        (200, 450),  # left wall
        (200, 250),  # close
        (270, 250), (270, 350), (330, 350), (330, 250),  # door
    ]
    draw_dot_to_dot("Dot-to-Dot: House", house_points)

    # Heart shape dots
    heart_points = []
    for i in range(20):
        t = math.radians(i * 18)
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        heart_points.append((cx + x * 10, cy + y * 10))
    draw_dot_to_dot("Dot-to-Dot: Heart", heart_points)

    # ── SPOT THE DIFFERENCE ──
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(HexColor("#FFB347"))
    c.drawCentredString(PAGE_W/2, PAGE_H - 50, "Spot 5 Differences!")
    c.setFont("Helvetica", 12)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W/2, PAGE_H - 75, "Look carefully at both pictures and find 5 differences!")

    # Picture A
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(black)
    c.drawCentredString(PAGE_W/2, PAGE_H - 110, "Picture A")
    c.setStrokeColor(black)
    c.setLineWidth(2)
    box_y_a = PAGE_H - 120
    c.rect(80, box_y_a - 250, PAGE_W - 160, 240)

    # Draw scene A
    ya = box_y_a - 250
    # Ground
    c.setStrokeColor(black)
    c.line(80, ya + 50, PAGE_W - 80, ya + 50)
    # House
    c.rect(150, ya + 50, 100, 80)
    p = c.beginPath()
    p.moveTo(140, ya + 130)
    p.lineTo(200, ya + 180)
    p.lineTo(260, ya + 130)
    p.close()
    c.drawPath(p, fill=0, stroke=1)
    # Tree
    c.rect(350, ya + 50, 15, 60)
    c.circle(357, ya + 130, 35, fill=0)
    # Sun
    c.circle(450, ya + 200, 25, fill=0)
    # Bird
    c.arc(300, ya + 180, 320, ya + 195, 0, 180)
    c.arc(320, ya + 180, 340, ya + 195, 0, 180)
    # Flowers
    c.circle(120, ya + 60, 6, fill=0)
    c.circle(420, ya + 60, 6, fill=0)
    c.circle(440, ya + 55, 6, fill=0)

    # Picture B (with differences)
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(PAGE_W/2, box_y_a - 280, "Picture B")
    box_y_b = box_y_a - 290
    c.rect(80, box_y_b - 250, PAGE_W - 160, 240)

    yb = box_y_b - 250
    c.line(80, yb + 50, PAGE_W - 80, yb + 50)
    # House (same)
    c.rect(150, yb + 50, 100, 80)
    p = c.beginPath()
    p.moveTo(140, yb + 130)
    p.lineTo(200, yb + 180)
    p.lineTo(260, yb + 130)
    p.close()
    c.drawPath(p, fill=0, stroke=1)
    # Tree (DIFFERENT - bigger)
    c.rect(350, yb + 50, 15, 60)
    c.circle(357, yb + 130, 45, fill=0)  # Diff 1: bigger tree
    # Sun (DIFFERENT - no sun) -- Diff 2
    # Bird missing -- Diff 3
    # Flowers (DIFFERENT)
    c.circle(120, yb + 60, 6, fill=0)
    c.circle(420, yb + 60, 10, fill=0)  # Diff 4: bigger flower
    # Extra cloud -- Diff 5
    c.circle(430, yb + 200, 20, fill=0)
    c.circle(450, yb + 195, 18, fill=0)
    c.circle(410, yb + 195, 18, fill=0)

    # Answer box
    c.setFont("Helvetica", 10)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W/2, 50, "Differences: 1. Tree size  2. Sun missing  3. Bird missing  4. Flower size  5. Cloud added")

    draw_page_number(c, page_num)
    page_num += 1
    c.showPage()

    # ── COUNTING PAGE ──
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(HexColor("#FFB347"))
    c.drawCentredString(PAGE_W/2, PAGE_H - 50, "Count and Write!")

    c.setFont("Helvetica", 12)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W/2, PAGE_H - 75, "Count the shapes and write the number in the box!")

    items = [
        ("Stars", 7, "star"),
        ("Circles", 5, "circle"),
        ("Hearts", 4, "heart"),
        ("Triangles", 6, "triangle"),
    ]

    y_pos = PAGE_H - 130
    for name, count, shape_type in items:
        c.setFont("Helvetica-Bold", 16)
        c.setFillColor(black)
        c.drawString(60, y_pos, f"{name}:")

        # Draw shapes
        random.seed(hash(name))
        for k in range(count):
            sx = 180 + k * 45
            sy = y_pos + 5
            c.setStrokeColor(black)
            c.setLineWidth(1.5)
            c.setFillColor(white)

            if shape_type == "star":
                draw_star_outline(c, sx, sy, 12)
            elif shape_type == "circle":
                c.circle(sx, sy, 12, fill=0)
            elif shape_type == "heart":
                s = 12
                p = c.beginPath()
                p.moveTo(sx, sy - s + 5)
                p.curveTo(sx - s, sy - s + 5, sx - s, sy + 5, sx, sy + s - 3)
                p.curveTo(sx + s, sy + 5, sx + s, sy - s + 5, sx, sy - s + 5)
                c.drawPath(p, fill=0, stroke=1)
            elif shape_type == "triangle":
                p = c.beginPath()
                p.moveTo(sx, sy + 14)
                p.lineTo(sx - 12, sy - 8)
                p.lineTo(sx + 12, sy - 8)
                p.close()
                c.drawPath(p, fill=0, stroke=1)

        # Answer box
        c.setStrokeColor(black)
        c.setLineWidth(2)
        c.rect(PAGE_W - 100, y_pos - 10, 40, 35, fill=0)
        c.setFont("Helvetica", 10)
        c.setFillColor(gray)
        c.drawCentredString(PAGE_W - 80, y_pos - 25, "Answer")

        y_pos -= 80

    # ── MATCHING ACTIVITY ──
    y_pos -= 20
    c.setFont("Helvetica-Bold", 18)
    c.setFillColor(HexColor("#FFB347"))
    c.drawCentredString(PAGE_W/2, y_pos, "Match the Animals to Their Homes!")

    y_pos -= 40
    animals = ["Dog", "Fish", "Bird", "Rabbit"]
    homes = ["Nest", "Burrow", "Kennel", "Water"]

    c.setFont("Helvetica", 14)
    c.setFillColor(black)
    for i, animal in enumerate(animals):
        c.drawString(80, y_pos - i * 35, f"{i+1}. {animal}")
        c.circle(160, y_pos - i * 35 + 5, 5, fill=1)

    random.shuffle(homes)
    for i, home in enumerate(homes):
        c.drawRightString(PAGE_W - 80, y_pos - i * 35, f"{home}")
        c.circle(PAGE_W - 165, y_pos - i * 35 + 5, 5, fill=1)

    draw_page_number(c, page_num)
    page_num += 1
    c.showPage()

    # ── WORD SEARCH ──
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(HexColor("#FFB347"))
    c.drawCentredString(PAGE_W/2, PAGE_H - 50, "Word Search!")

    c.setFont("Helvetica", 12)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W/2, PAGE_H - 75, "Find these words in the grid: CAT, DOG, FISH, BIRD, FROG")

    # Create grid
    grid_size = 8
    cell_size = 40
    grid_start_x = (PAGE_W - grid_size * cell_size) / 2
    grid_start_y = PAGE_H - 130

    # Pre-made grid with hidden words
    grid_data = [
        ['C', 'A', 'T', 'P', 'R', 'M', 'K', 'L'],
        ['X', 'B', 'I', 'R', 'D', 'N', 'O', 'E'],
        ['F', 'G', 'H', 'J', 'K', 'L', 'M', 'N'],
        ['R', 'D', 'O', 'G', 'P', 'Q', 'R', 'S'],
        ['O', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        ['G', 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
        ['H', 'F', 'I', 'S', 'H', 'I', 'J', 'K'],
        ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S'],
    ]

    c.setFont("Helvetica-Bold", 18)
    c.setStrokeColor(black)
    c.setLineWidth(1)

    for r in range(grid_size):
        for col_idx in range(grid_size):
            x = grid_start_x + col_idx * cell_size
            y = grid_start_y - r * cell_size
            c.rect(x, y - cell_size, cell_size, cell_size)
            c.setFillColor(black)
            c.drawCentredString(x + cell_size/2, y - cell_size/2 - 6, grid_data[r][col_idx])

    # Word list
    y_list = grid_start_y - grid_size * cell_size - 40
    c.setFont("Helvetica-Bold", 16)
    c.setFillColor(black)
    c.drawCentredString(PAGE_W/2, y_list, "Words to find:")

    words = ["CAT", "DOG", "FISH", "BIRD", "FROG"]
    c.setFont("Helvetica", 14)
    word_x = 100
    for word in words:
        c.drawString(word_x, y_list - 30, f"[ ] {word}")
        word_x += 90

    draw_page_number(c, page_num)
    page_num += 1
    c.showPage()

    c.save()
    print(f"Activity Book saved: {filepath}")


# ─────────────────────────────────────────────
# BOOK 4: HANDWRITING PRACTICE BOOK
# ─────────────────────────────────────────────

def create_handwriting_book():
    filepath = os.path.join(OUTPUT_DIR, "04_Kids_Handwriting_Practice.pdf")
    c = canvas.Canvas(filepath, pagesize=A4)
    c.setTitle("My First Handwriting Practice")
    c.setAuthor("Kids Book Publisher")

    draw_cover(c, "My First", "Handwriting Practice", HexColor("#9B59B6"))

    page_num = 1

    def draw_lined_area(c, start_y, num_lines, line_height=35):
        """Draw writing lines"""
        for i in range(num_lines):
            y = start_y - i * line_height
            # Main line (solid)
            c.setStrokeColor(black)
            c.setLineWidth(1)
            c.line(60, y, PAGE_W - 60, y)
            # Midline (dashed)
            c.setStrokeColor(lightgrey)
            c.setLineWidth(0.5)
            c.setDash(3, 3)
            c.line(60, y + line_height/2, PAGE_W - 60, y + line_height/2)
            c.setDash()
        return start_y - num_lines * line_height

    # ── UPPERCASE LETTERS ──
    uppercase_pages = [
        "A B C D E F",
        "G H I J K L",
        "M N O P Q R",
        "S T U V W X Y Z"
    ]

    for letters in uppercase_pages:
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(HexColor("#9B59B6"))
        c.drawCentredString(PAGE_W/2, PAGE_H - 45, "Uppercase Letters Practice")

        # Show letters to trace
        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(black)
        c.drawString(60, PAGE_H - 80, f"Trace and write: {letters}")

        # Guide letters (large, light)
        c.setFont("Helvetica-Bold", 40)
        c.setFillColor(HexColor("#E8D5F5"))
        letter_list = letters.replace(" ", "")
        x_pos = 80
        for letter in letter_list:
            c.drawString(x_pos, PAGE_H - 140, letter)
            x_pos += 70

        # Practice lines
        draw_lined_area(c, PAGE_H - 170, 16)

        draw_page_number(c, page_num)
        page_num += 1
        c.showPage()

    # ── LOWERCASE LETTERS ──
    lowercase_pages = [
        "a b c d e f",
        "g h i j k l",
        "m n o p q r",
        "s t u v w x y z"
    ]

    for letters in lowercase_pages:
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(HexColor("#9B59B6"))
        c.drawCentredString(PAGE_W/2, PAGE_H - 45, "Lowercase Letters Practice")

        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(black)
        c.drawString(60, PAGE_H - 80, f"Trace and write: {letters}")

        # Guide letters
        c.setFont("Helvetica-Bold", 40)
        c.setFillColor(HexColor("#E8D5F5"))
        letter_list = letters.replace(" ", "")
        x_pos = 80
        for letter in letter_list:
            c.drawString(x_pos, PAGE_H - 140, letter)
            x_pos += 70

        draw_lined_area(c, PAGE_H - 170, 16)

        draw_page_number(c, page_num)
        page_num += 1
        c.showPage()

    # ── NUMBERS 1-10 ──
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#9B59B6"))
    c.drawCentredString(PAGE_W/2, PAGE_H - 45, "Number Practice (1-10)")

    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(black)
    c.drawString(60, PAGE_H - 80, "Trace and write each number:")

    y_pos = PAGE_H - 110
    for num in range(1, 11):
        # Number
        c.setFont("Helvetica-Bold", 28)
        c.setFillColor(HexColor("#9B59B6"))
        c.drawString(65, y_pos, str(num))

        # Light guide repeated
        c.setFont("Helvetica-Bold", 28)
        c.setFillColor(HexColor("#E8D5F5"))
        for k in range(8):
            c.drawString(110 + k * 50, y_pos, str(num))

        # Line
        c.setStrokeColor(lightgrey)
        c.setLineWidth(0.5)
        c.line(60, y_pos - 5, PAGE_W - 60, y_pos - 5)

        y_pos -= 55

    # Number word at bottom
    c.setFont("Helvetica", 10)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W/2, 50, "Practice writing each number neatly on the line!")

    draw_page_number(c, page_num)
    page_num += 1
    c.showPage()

    # ── NUMBERS 1-10 PAGE 2 ──
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#9B59B6"))
    c.drawCentredString(PAGE_W/2, PAGE_H - 45, "Number Words Practice")

    c.setFont("Helvetica", 12)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W/2, PAGE_H - 70, "Write the number word next to each number!")

    number_words = [
        ("1", "One"), ("2", "Two"), ("3", "Three"), ("4", "Four"),
        ("5", "Five"), ("6", "Six"), ("7", "Seven"), ("8", "Eight"),
        ("9", "Nine"), ("10", "Ten")
    ]

    y_pos = PAGE_H - 110
    for num, word in number_words:
        # Number
        c.setFont("Helvetica-Bold", 22)
        c.setFillColor(HexColor("#9B59B6"))
        c.drawString(65, y_pos, num)

        # Word guide (light)
        c.setFont("Helvetica-Bold", 22)
        c.setFillColor(HexColor("#E8D5F5"))
        c.drawString(120, y_pos, word)

        # Practice space
        c.setStrokeColor(lightgrey)
        c.setLineWidth(0.5)
        c.line(250, y_pos - 5, PAGE_W - 60, y_pos - 5)

        y_pos -= 55

    draw_page_number(c, page_num)
    page_num += 1
    c.showPage()

    # ── SIMPLE WORDS ──
    simple_words = [
        ["Cat", "Dog", "Bat", "Rat"],
        ["Sun", "Run", "Fun", "Bun"],
        ["Red", "Bed", "Led", "Fed"],
        ["Big", "Dig", "Fig", "Pig"],
    ]

    for word_group in simple_words:
        c.setFont("Helvetica-Bold", 20)
        c.setFillColor(HexColor("#9B59B6"))
        c.drawCentredString(PAGE_W/2, PAGE_H - 45, "Simple Words Practice")

        y_pos = PAGE_H - 90
        for word in word_group:
            # Word to copy
            c.setFont("Helvetica-Bold", 24)
            c.setFillColor(HexColor("#9B59B6"))
            c.drawString(65, y_pos, word)

            # Light guide
            c.setFont("Helvetica-Bold", 24)
            c.setFillColor(HexColor("#E8D5F5"))
            c.drawString(180, y_pos, word)

            # Two practice lines
            for line_idx in range(3):
                ly = y_pos - 5 - (line_idx) * 40
                c.setStrokeColor(black)
                c.setLineWidth(0.8)
                c.line(60, ly - 35, PAGE_W - 60, ly - 35)
                c.setStrokeColor(lightgrey)
                c.setLineWidth(0.3)
                c.setDash(2, 2)
                c.line(60, ly - 15, PAGE_W - 60, ly - 15)
                c.setDash()

            y_pos -= 170

        draw_page_number(c, page_num)
        page_num += 1
        c.showPage()

    # ── HINDI ALPHABETS (BONUS) ──
    c.setFont("Helvetica-Bold", 20)
    c.setFillColor(HexColor("#9B59B6"))
    c.drawCentredString(PAGE_W/2, PAGE_H - 45, "Hindi Alphabet Practice")

    c.setFont("Helvetica", 12)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W/2, PAGE_H - 70, "Trace the Hindi letters on the lines below")

    # Since we can't render Hindi in default fonts, we'll create placeholder boxes
    y_pos = PAGE_H - 110
    hindi_letters = [
        "Ka", "Kha", "Ga", "Gha", "Nga",
        "Cha", "Chha", "Ja", "Jha", "Nya",
        "Ta", "Tha", "Da", "Dha", "Na",
    ]

    for i, letter in enumerate(hindi_letters):
        row = i // 5
        col = i % 5
        x = 60 + col * 100
        y = y_pos - row * 120

        # Box with letter name
        c.setStrokeColor(HexColor("#9B59B6"))
        c.setLineWidth(1.5)
        c.rect(x, y, 80, 50, fill=0)

        c.setFont("Helvetica-Bold", 14)
        c.setFillColor(HexColor("#9B59B6"))
        c.drawCentredString(x + 40, y + 18, letter)

        # Practice line below
        c.setStrokeColor(lightgrey)
        c.setLineWidth(0.5)
        c.line(x, y - 5, x + 80, y - 5)
        c.line(x, y - 30, x + 80, y - 30)

    c.setFont("Helvetica", 10)
    c.setFillColor(gray)
    c.drawCentredString(PAGE_W/2, 50, "Note: Write the actual Hindi characters in these practice spaces!")

    draw_page_number(c, page_num)
    page_num += 1
    c.showPage()

    c.save()
    print(f"Handwriting Practice Book saved: {filepath}")


# ─────────────────────────────────────────────
# CREATE ALL BOOKS
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("Creating all 4 sample books...\n")

    print("1/4 - Creating Coloring Book...")
    create_coloring_book()

    print("\n2/4 - Creating Story Book...")
    create_story_book()

    print("\n3/4 - Creating Activity Book...")
    create_activity_book()

    print("\n4/4 - Creating Handwriting Practice Book...")
    create_handwriting_book()

    print(f"\n{'='*50}")
    print(f"All 4 books created successfully!")
    print(f"Location: {OUTPUT_DIR}")
    print(f"{'='*50}")
    print("\nFiles created:")
    for f in sorted(os.listdir(OUTPUT_DIR)):
        size = os.path.getsize(os.path.join(OUTPUT_DIR, f))
        print(f"  - {f} ({size/1024:.1f} KB)")
