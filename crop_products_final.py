"""
Final cropping with header text cleanup.
For first-row items, paint over leaked header text with white.
"""
from PIL import Image, ImageDraw
import os

OUT = "D:/Nidhi/n8n/Card Scan/product_images"
SRC = "D:/Nidhi/n8n/Card Scan/extracted_images"
os.makedirs(OUT, exist_ok=True)

def crop_save(page_file, crops, prefix):
    img = Image.open(os.path.join(SRC, page_file))
    w, h = img.size
    for item in crops:
        if len(item) == 6:
            name, l, t, r, b, clean_top = item
        else:
            name, l, t, r, b = item
            clean_top = 0
        l, t, r, b = max(0,l), max(0,t), min(w,r), min(h,b)
        cropped = img.crop((l, t, r, b))

        # If clean_top > 0, paint white over the top portion to remove header text
        if clean_top > 0:
            draw = ImageDraw.Draw(cropped)
            cw, ch = cropped.size
            # Sample the background color from below the text (should be white/light grey)
            # Just use white
            draw.rectangle([0, 0, cw, clean_top], fill=(255, 255, 255))

        fname = f"{prefix}_{name}.png"
        cropped.save(os.path.join(OUT, fname))
        print(f"  {fname} ({cropped.size})")

# PAGE 3: Industrial Automation (1156 x 1566)
# The red header bar + "INDUSTRIAL AUTOMATION PRODUCTS" title occupies 0-~78px
# First product row grey cells start at ~82px
# But the title text is LARGE and bold, so the bottom of text touches ~75px
# Let me crop from y=82 for first row and clean top 5px just in case
print("Page 3 - Industrial Automation:")
crop_save("page3_X0_1156x1566.png", [
    ("ac_servo_motor",     30, 85, 555, 405, 5),
    ("panasonic_servo",   575, 85,1130, 405, 5),
    ("ac_dc_gear_motor",   30, 435, 555, 685),
    ("stepper_motor",     575, 435,1130, 685),
    ("stepper_driver",     30, 710, 555, 975),
    ("closeloop_motor",   575, 710,1130, 975),
    ("planetary_gearbox",  30,1005, 555,1280),
    ("encoder",           575,1005,1130,1280),
], "p3")

# PAGE 4: Mechanical Products (1156 x 1556)
print("\nPage 4 - Mechanical Products:")
crop_save("page4_X0_1156x1556.png", [
    ("block_guideway",     30,  75, 555, 330, 5),
    ("rack_gear",         575,  75,1130, 330, 5),
    ("drag_chain",         30, 350, 378, 600),
    ("ball_screw",        388, 350, 752, 600),
    ("cross_roller",      762, 350,1130, 600),
    ("aluminum_sliding",   30, 618, 555, 860),
    ("linear_actuator",   575, 618,1130, 860),
    ("diamond_moly_wire",  30, 950, 300,1240),
    ("mimy_moly_wire",    310, 950, 572,1240),
    ("jr1a_composite",    582, 950, 856,1240),
    ("jr3a_ointment",     866, 950,1130,1240),
], "p4")

# PAGE 5: Pneumatic + CNC (1156 x 1576)
print("\nPage 5 - Pneumatic & CNC:")
crop_save("page5_X0_1576.png" if not os.path.exists(os.path.join(SRC, "page5_X0_1156x1576.png")) else "page5_X0_1156x1576.png", [
    ("cylinder",           30,  75, 555, 365, 5),
    ("valve",             575,  75,1130, 365, 5),
    ("spindle_motor",      30, 445, 385, 680),
    ("dust_collector",    395, 445, 755, 680),
    ("cnc_gearbox",       765, 445,1130, 680),
    ("richauto_ctrl",      30, 690, 385, 935),
    ("cnc_controllers",   395, 690, 755, 935),
    ("servo_spindle",     765, 690,1130, 935),
    ("saw_blade_motor",    30, 950, 555,1230),
    ("stone_bridge_motor",575, 950,1130,1230),
], "p5")

# PAGE 6: Laser Machinery (1156 x 1576)
print("\nPage 6 - Laser Machinery:")
crop_save("page6_X0_1156x1576.png", [
    ("qswitch_fiber",      30,  82, 378, 330, 5),
    ("laser_source",      388,  82, 752, 330, 5),
    ("uv_source",         762,  82,1130, 330, 5),
    ("rf_co2_laser",       30, 350, 378, 605),
    ("galvo_scanner",     388, 350, 752, 605),
    ("jcz_control",       762, 350,1130, 605),
    ("fly_mark_ctrl",      30, 620, 378, 890),
    ("ftheta_lens",       388, 620, 752, 890),
    ("all_optics",        762, 620,1130, 890),
    ("column_beampath",    30, 905, 378,1195),
    ("rotary_chunk",      388, 905, 752,1195),
    ("co2_tube_power",    762, 905,1130,1195),
], "p6")

# PAGE 7: Welding & Cutting (1156 x 1590)
print("\nPage 7 - Welding & Cutting:")
crop_save("page7_X0_1156x1590.png", [
    ("power_supply",       30,  78, 378, 370, 5),
    ("optical_path",      388,  78, 752, 370, 5),
    ("all_optics_w",      762,  78,1130, 370, 5),
    ("xenon_lamp",         30, 390, 555, 650),
    ("yag_crystal",       575, 390,1130, 650),
    ("nd31",               30, 725, 378, 990),
    ("nc36",              388, 725, 752, 990),
    ("hd31",              762, 725,1130, 990),
    ("blt310",             30,1000, 555,1280),
    ("blt421s",           575,1000,1130,1280),
], "p7")

# PAGE 8: Back page (1156 x 1596)
print("\nPage 8 - Additional:")
crop_save("page8_X0_1156x1596.png", [
    ("max_photonics_1",    30,  55, 555, 355, 5),
    ("max_photonics_2",   575,  55,1130, 355, 5),
    ("sa_chiller",         30, 375, 555, 645),
    ("rk_chunk",          575, 375,1130, 645),
], "p8")

print(f"\nTotal: {len(os.listdir(OUT))} images")
