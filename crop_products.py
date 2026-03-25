"""
Crop individual product images from the original PDF page images.
Each page image is ~1156px wide, and products are laid out in grids.
"""
from PIL import Image
import os

OUT = "D:/Nidhi/n8n/Card Scan/product_images"
SRC = "D:/Nidhi/n8n/Card Scan/extracted_images"
os.makedirs(OUT, exist_ok=True)

def crop_and_save(page_file, crops, prefix):
    """
    crops: list of (name, left, top, right, bottom) tuples
    """
    img = Image.open(os.path.join(SRC, page_file))
    w, h = img.size
    for name, l, t, r, b in crops:
        # Clamp coordinates
        l = max(0, l)
        t = max(0, t)
        r = min(w, r)
        b = min(h, b)
        cropped = img.crop((l, t, r, b))
        fname = f"{prefix}_{name}.png"
        cropped.save(os.path.join(OUT, fname))
        print(f"  Saved: {fname} ({cropped.size})")

# ================================================================
# PAGE 3: Industrial Automation Products (1156 x 1566)
# Header bar ~0-75px
# Grid: 2 columns, 4 rows
# Left col: ~20-560, Right col: ~580-1136
# Row heights approx: 75-440, 440-700, 700-1000, 1000-1300, 1300-1540
# Each cell has product image in upper portion, brand logo + text at bottom
# ================================================================
print("Page 3 - Industrial Automation Products:")
p3_crops = [
    ("ac_servo_motor",      20,  85,  560,  430),
    ("panasonic_servo",    580,  85, 1136,  430),
    ("ac_dc_gear_motor",    20, 440,  560,  700),
    ("stepper_motor",      580, 440, 1136,  700),
    ("stepper_driver",      20, 710,  560,  990),
    ("closeloop_motor",    580, 710, 1136,  990),
    ("planetary_gearbox",   20, 1000, 560, 1280),
    ("encoder",            580, 1000,1136, 1280),
]
crop_and_save("page3_X0_1156x1566.png", p3_crops, "p3")

# ================================================================
# PAGE 4: Mechanical Products (1156 x 1556)
# Header ~0-65
# Mechanical Products grid: 2 columns, 4 rows approx
# Row 1: ~70-360 (Block Guideway, Rack and Gear)
# Row 2: ~360-620 (Drag Chain, Ball Screw, Cross Roller - 3 cols!)
# Row 3: ~620-880 (Aluminum Sliding, Single Axis Linear)
# EDM section starts ~880
# ================================================================
print("\nPage 4 - Mechanical Products:")
p4_crops = [
    ("block_guideway",       20,  70,  560,  350),
    ("rack_gear",           580,  70, 1136,  350),
    ("drag_chain",           20, 355,  380,  610),
    ("ball_screw",          385, 355,  760,  610),
    ("cross_roller",        765, 355, 1136,  610),
    ("aluminum_sliding",     20, 620,  560,  870),
    ("linear_actuator",     580, 620, 1136,  870),
    # EDM Section
    ("diamond_moly_wire",    20, 950,  310, 1240),
    ("mimy_moly_wire",      310, 950,  580, 1240),
    ("jr1a_composite",      580, 950,  860, 1240),
    ("jr3a_ointment",       860, 950, 1136, 1240),
]
crop_and_save("page4_X0_1156x1556.png", p4_crops, "p4")

# ================================================================
# PAGE 5: Pneumatic Parts + CNC Machine (1156 x 1576)
# Pneumatic: ~60-380, 2 items
# CNC header: ~390
# CNC grid: 3 cols, 3 rows
# ================================================================
print("\nPage 5 - Pneumatic & CNC:")
p5_crops = [
    ("cylinder",             20,  70,  560,  370),
    ("valve",               580,  70, 1136,  370),
    # CNC Products
    ("spindle_motor",        20, 420,  390,  680),
    ("dust_collector",      395, 420,  760,  680),
    ("cnc_gearbox",         765, 420, 1136,  680),
    ("richauto_ctrl",        20, 690,  390,  940),
    ("cnc_controllers",     395, 690,  760,  940),
    ("servo_spindle",       765, 690, 1136,  940),
    ("saw_blade_motor",      20, 950,  560, 1230),
    ("stone_bridge_motor",  580, 950, 1136, 1230),
]
crop_and_save("page5_X0_1156x1576.png", p5_crops, "p5")

# ================================================================
# PAGE 6: Laser Machinery Products (1156 x 1576)
# 3 columns, 4 rows
# ================================================================
print("\nPage 6 - Laser Machinery:")
p6_crops = [
    ("qswitch_fiber",        20,  75,  385,  350),
    ("laser_source",        390,  75,  760,  350),
    ("uv_source",           765,  75, 1136,  350),
    ("rf_co2_laser",         20, 360,  385,  620),
    ("galvo_scanner",       390, 360,  760,  620),
    ("jcz_control",         765, 360, 1136,  620),
    ("fly_mark_ctrl",        20, 630,  385,  900),
    ("ftheta_lens",         390, 630,  760,  900),
    ("all_optics",          765, 630, 1136,  900),
    ("column_beampath",      20, 910,  385, 1200),
    ("rotary_chunk",        390, 910,  760, 1200),
    ("co2_tube_power",      765, 910, 1136, 1200),
]
crop_and_save("page6_X0_1156x1576.png", p6_crops, "p6")

# ================================================================
# PAGE 7: Spot Welding + Laser Cutting (1156 x 1590)
# Spot welding: 3 cols, 2 rows (~70-680)
# Laser cutting: 3 cols, 2 rows (~720-1300)
# ================================================================
print("\nPage 7 - Welding & Cutting:")
p7_crops = [
    ("power_supply",         20,  70,  385,  380),
    ("optical_path",        390,  70,  760,  380),
    ("all_optics_w",        765,  70, 1136,  380),
    ("xenon_lamp",           20, 390,  560,  660),
    ("yag_crystal",         580, 390, 1136,  660),
    # Laser cutting
    ("nd31",                 20, 720,  385,  990),
    ("nc36",                390, 720,  760,  990),
    ("hd31",                765, 720, 1136,  990),
    ("blt310",               20, 1000, 560, 1280),
    ("blt421s",             580, 1000,1136, 1280),
]
crop_and_save("page7_X0_1156x1590.png", p7_crops, "p7")

# ================================================================
# PAGE 8: Back page (1156 x 1596)
# 4 products in 2x2 grid at top
# Logo/QR at bottom
# ================================================================
print("\nPage 8 - Additional Equipment:")
p8_crops = [
    ("max_photonics_1",      20,  55,  560,  360),
    ("max_photonics_2",     580,  55, 1136,  360),
    ("sa_chiller",           20, 370,  560,  650),
    ("rk_chunk",            580, 370, 1136,  650),
    ("logo_qr",              20, 800, 1136, 1250),
]
crop_and_save("page8_X0_1156x1596.png", p8_crops, "p8")

print(f"\nDone! Total images in {OUT}:")
print(len(os.listdir(OUT)))
