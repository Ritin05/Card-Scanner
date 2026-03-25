"""
Refined cropping - isolate just product images from original page images.
Each page is ~1156px wide. Need to crop tighter to avoid header text.
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
        l, t = max(0, l), max(0, t)
        r, b = min(w, r), min(h, b)
        cropped = img.crop((l, t, r, b))
        # Clean up white borders by checking for mostly-white edges
        fname = f"{prefix}_{name}.png"
        cropped.save(os.path.join(OUT, fname))
        print(f"  {fname} ({cropped.size})")

# PAGE 3: Industrial Automation (1156 x 1566)
# Header red bar ends at ~70px. Products in 2 columns.
# Each product cell: product image takes top portion, brand+text at bottom
# Need to crop from inside the grey cell areas
# Row 1: y ~85-425 (top header included), actual product area ~95-420
# Row 2: y ~435-695
# Row 3: y ~700-985
# Row 4: y ~1000-1285
# Left: 28-558, Right: 582-1130
print("Page 3 - Industrial Automation:")
crop_save("page3_X0_1156x1566.png", [
    ("ac_servo_motor",     35, 100, 550, 410),
    ("panasonic_servo",   590, 100,1125, 410),
    ("ac_dc_gear_motor",   35, 430, 550, 690),
    ("stepper_motor",     590, 430,1125, 690),
    ("stepper_driver",     35, 705, 550, 980),
    ("closeloop_motor",   590, 705,1125, 980),
    ("planetary_gearbox",  35,1000, 550,1280),
    ("encoder",           590,1000,1125,1280),
], "p3")

# PAGE 4: Mechanical Products (1156 x 1556)
# Header ends ~65. First section grid starts ~75
# Row 1: ~75-340, 2 items (Block Guideway, Rack and Gear)
# Row 2: ~345-600, 3 items (Drag Chain, Ball Screw, Cross Roller)
# Row 3: ~610-865, 2 items (Aluminum Sliding, Single Axis)
# EDM header ~885, EDM products ~920-1240
print("\nPage 4 - Mechanical Products:")
crop_save("page4_X0_1156x1556.png", [
    ("block_guideway",     35,  80, 555, 330),
    ("rack_gear",         590,  80,1125, 330),
    ("drag_chain",         35, 345, 380, 600),
    ("ball_screw",        390, 345, 755, 600),
    ("cross_roller",      770, 345,1125, 600),
    ("aluminum_sliding",   35, 615, 555, 860),
    ("linear_actuator",   590, 615,1125, 860),
    ("diamond_moly_wire",  30, 960, 305,1235),
    ("mimy_moly_wire",    315, 960, 575,1235),
    ("jr1a_composite",    585, 960, 855,1235),
    ("jr3a_ointment",     865, 960,1130,1235),
], "p4")

# PAGE 5: Pneumatic + CNC (1156 x 1576)
# Pneumatic header ends ~65. Products ~75-370 (2 items)
# CNC header ~395-430
# CNC grid: 3 cols, starts ~440
# Row 1: ~440-685
# Row 2: ~690-930
# Row 3: ~940-1235
print("\nPage 5 - Pneumatic & CNC:")
crop_save("page5_X0_1156x1576.png", [
    ("cylinder",           35,  80, 555, 365),
    ("valve",             590,  80,1125, 365),
    ("spindle_motor",      35, 445, 385, 680),
    ("dust_collector",    400, 445, 755, 680),
    ("cnc_gearbox",       770, 445,1125, 680),
    ("richauto_ctrl",      35, 695, 385, 935),
    ("cnc_controllers",   400, 695, 755, 935),
    ("servo_spindle",     770, 695,1125, 935),
    ("saw_blade_motor",    35, 950, 555,1230),
    ("stone_bridge_motor",590, 950,1125,1230),
], "p5")

# PAGE 6: Laser Machinery (1156 x 1576)
# Header ends ~70. Grid: 3 columns, 4 rows
# Col: 28-380, 385-755, 760-1130
# Row 1: ~80-335
# Row 2: ~345-600
# Row 3: ~610-880
# Row 4: ~890-1195
print("\nPage 6 - Laser Machinery:")
crop_save("page6_X0_1156x1576.png", [
    ("qswitch_fiber",      35,  85, 375, 330),
    ("laser_source",      395,  85, 750, 330),
    ("uv_source",         770,  85,1125, 330),
    ("rf_co2_laser",       35, 345, 375, 595),
    ("galvo_scanner",     395, 345, 750, 595),
    ("jcz_control",       770, 345,1125, 595),
    ("fly_mark_ctrl",      35, 610, 375, 875),
    ("ftheta_lens",       395, 610, 750, 875),
    ("all_optics",        770, 610,1125, 875),
    ("column_beampath",    35, 890, 375,1195),
    ("rotary_chunk",      395, 890, 750,1195),
    ("co2_tube_power",    770, 890,1125,1195),
], "p6")

# PAGE 7: Welding & Cutting (1156 x 1590)
# Spot welding header ~0-65
# Row 1: ~70-370, 3 items
# Row 2: ~380-650, 2 items
# Laser cutting header ~660-700
# Row 3: ~710-980, 3 items
# Row 4: ~990-1290, 2-3 items
print("\nPage 7 - Welding & Cutting:")
crop_save("page7_X0_1156x1590.png", [
    ("power_supply",       35,  75, 375, 370),
    ("optical_path",      395,  75, 750, 370),
    ("all_optics_w",      770,  75,1125, 370),
    ("xenon_lamp",         35, 385, 555, 650),
    ("yag_crystal",       590, 385,1125, 650),
    ("nd31",               35, 720, 375, 985),
    ("nc36",              395, 720, 750, 985),
    ("hd31",              770, 720,1125, 985),
    ("blt310",             35, 995, 555,1290),
    ("blt421s",           590, 995,1125,1290),
], "p7")

# PAGE 8: Back page (1156 x 1596)
# Products at top in 2x2 grid
# Row 1: ~55-355
# Row 2: ~365-650
print("\nPage 8 - Additional:")
crop_save("page8_X0_1156x1596.png", [
    ("max_photonics_1",    35,  60, 555, 350),
    ("max_photonics_2",   590,  60,1125, 350),
    ("sa_chiller",         35, 370, 555, 645),
    ("rk_chunk",          590, 370,1125, 645),
], "p8")

print(f"\nDone! {len(os.listdir(OUT))} images")
