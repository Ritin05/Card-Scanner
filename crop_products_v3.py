"""
Final refined cropping - skip header text completely, crop only product cells
"""
from PIL import Image
import os

OUT = "D:/Nidhi/n8n/Card Scan/product_images"
SRC = "D:/Nidhi/n8n/Card Scan/extracted_images"
os.makedirs(OUT, exist_ok=True)

def crop_save(page_file, crops, prefix):
    img = Image.open(os.path.join(SRC, page_file))
    w, h = img.size
    for name, l, t, r, b in crops:
        l, t, r, b = max(0,l), max(0,t), min(w,r), min(h,b)
        cropped = img.crop((l, t, r, b))
        fname = f"{prefix}_{name}.png"
        cropped.save(os.path.join(OUT, fname))
        print(f"  {fname} ({cropped.size})")

# PAGE 3: Industrial Automation (1156 x 1566)
# Red header bar + "INDUSTRIAL AUTOMATION PRODUCTS" title = ~80px
# Grey background grid starts at ~85
# Each cell: image area ~top 65%, then brand logo + text at bottom
# Cells are separated by thin grey lines
# 2 cols: Left ~28-558, Right ~578-1130
# Row heights: each cell is about ~310-320px tall
# Row 1 starts at ~85, Row 2 at ~430, Row 3 at ~710, Row 4 at ~1005
# Let me crop just the product image portion of each cell (skip bottom brand text area)
print("Page 3 - Industrial Automation (tight crops):")
crop_save("page3_X0_1156x1566.png", [
    # Crop from INSIDE the cells, skipping header. Each cell product image is ~200px from cell top
    ("ac_servo_motor",     40, 110, 545, 370),   # skip red header
    ("panasonic_servo",   595, 110,1120, 370),
    ("ac_dc_gear_motor",   40, 440, 545, 650),
    ("stepper_motor",     595, 440,1120, 650),
    ("stepper_driver",     40, 720, 545, 940),
    ("closeloop_motor",   595, 720,1120, 940),
    ("planetary_gearbox",  40,1010, 545,1250),
    ("encoder",           595,1010,1120,1250),
], "p3")

# PAGE 4: Mechanical Products (1156 x 1556)
# Red header + title ~70px
print("\nPage 4 - Mechanical Products (tight crops):")
crop_save("page4_X0_1156x1556.png", [
    ("block_guideway",     40,  95, 550, 310),
    ("rack_gear",         595,  95,1120, 310),
    ("drag_chain",         40, 355, 375, 575),
    ("ball_screw",        395, 355, 745, 575),
    ("cross_roller",      775, 355,1120, 575),
    ("aluminum_sliding",   40, 625, 550, 840),
    ("linear_actuator",   595, 625,1120, 840),
    ("diamond_moly_wire",  35, 975, 300,1215),
    ("mimy_moly_wire",    320, 975, 570,1215),
    ("jr1a_composite",    590, 975, 850,1215),
    ("jr3a_ointment",     870, 975,1125,1215),
], "p4")

# PAGE 5: Pneumatic + CNC (1156 x 1576)
print("\nPage 5 - Pneumatic & CNC (tight crops):")
crop_save("page5_X0_1156x1576.png", [
    ("cylinder",           40,  95, 550, 350),
    ("valve",             595,  95,1120, 350),
    ("spindle_motor",      40, 460, 380, 665),
    ("dust_collector",    405, 460, 750, 665),
    ("cnc_gearbox",       775, 460,1120, 665),
    ("richauto_ctrl",      40, 700, 380, 920),
    ("cnc_controllers",   405, 700, 750, 920),
    ("servo_spindle",     775, 700,1120, 920),
    ("saw_blade_motor",    40, 960, 550,1210),
    ("stone_bridge_motor",595, 960,1120,1210),
], "p5")

# PAGE 6: Laser Machinery (1156 x 1576)
print("\nPage 6 - Laser Machinery (tight crops):")
crop_save("page6_X0_1156x1576.png", [
    ("qswitch_fiber",      40, 100, 370, 310),
    ("laser_source",      400, 100, 745, 310),
    ("uv_source",         775, 100,1120, 310),
    ("rf_co2_laser",       40, 360, 370, 575),
    ("galvo_scanner",     400, 360, 745, 575),
    ("jcz_control",       775, 360,1120, 575),
    ("fly_mark_ctrl",      40, 625, 370, 855),
    ("ftheta_lens",       400, 625, 745, 855),
    ("all_optics",        775, 625,1120, 855),
    ("column_beampath",    40, 905, 370,1175),
    ("rotary_chunk",      400, 905, 745,1175),
    ("co2_tube_power",    775, 905,1120,1175),
], "p6")

# PAGE 7: Welding & Cutting (1156 x 1590)
print("\nPage 7 - Welding & Cutting (tight crops):")
crop_save("page7_X0_1156x1590.png", [
    ("power_supply",       40,  90, 370, 360),
    ("optical_path",      400,  90, 745, 360),
    ("all_optics_w",      775,  90,1120, 360),
    ("xenon_lamp",         40, 395, 550, 635),
    ("yag_crystal",       595, 395,1120, 635),
    ("nd31",               40, 735, 370, 970),
    ("nc36",              400, 735, 745, 970),
    ("hd31",              775, 735,1120, 970),
    ("blt310",             40,1010, 550,1275),
    ("blt421s",           595,1010,1120,1275),
], "p7")

# PAGE 8: Back page (1156 x 1596)
print("\nPage 8 - Additional:")
crop_save("page8_X0_1156x1596.png", [
    ("max_photonics_1",    40,  70, 550, 340),
    ("max_photonics_2",   595,  70,1120, 340),
    ("sa_chiller",         40, 380, 550, 630),
    ("rk_chunk",          595, 380,1120, 630),
], "p8")

print(f"\nTotal: {len(os.listdir(OUT))} images")
