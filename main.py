import tkinter as tk
from PIL import Image, ImageTk
import customtkinter as ctk

# Preserving your custom tracking modules
from record import record
from find_motion import find_motion
from identify import maincall

# Initialize UI Configuration
ctk.set_appearance_mode("dark")
window = ctk.CTk()
window.title("Smart CCTV - Advanced Tactical HUD")
window.geometry('1024x640')  # Scaled cleanly to fit standard dashboard aspect ratios
window.resizable(False, False)

# -------------------------------------------------------------
# 🖼️ HUD INTERFACE CANVAS BACKGROUND
# -------------------------------------------------------------
# FIX: Points straight to your .jpg asset inside the icons folder
try:
    bg_image_raw = Image.open("icons/dashboard_bg.jpg").resize((1024, 640), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_image_raw)
except FileNotFoundError:
    # Backup check in case it's named .png on your disk
    bg_image_raw = Image.open("icons/dashboard_bg.png").resize((1024, 640), Image.Resampling.LANCZOS)
    bg_image = ImageTk.PhotoImage(bg_image_raw)

# Render background on flat canvas frame
canvas = tk.Canvas(window, width=1024, height=640, bg="#0d1117", bd=0, highlightthickness=0)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_image, anchor="nw")

# -------------------------------------------------------------
# 🎛️ TRANSPARENT-STYLE CLICK ENGINE (Hex Configurations)
# -------------------------------------------------------------
# We use flat dark grey bases that let the neon background lines show, 
# and use vibrant matching colors when hovered over.

# 1. Object Detection Module Button (Left Card Position)
btn_detection = ctk.CTkButton(
    window, text="ENGAGE DETECTION", command=find_motion,
    font=("Segoe UI", 11, "bold"),
    fg_color="#1a233a",        # Sleek deep blue-tinted card slate
    hover_color="#29b6f6",     # Glows electric blue on hover
    text_color="#29b6f6",
    border_width=1, border_color="#29b6f6",
    corner_radius=6, height=36, width=180
)
canvas.create_window(175, 410, window=btn_detection, anchor="center")

# 2. Identification Module Button (Middle Card Position)
btn_identify = ctk.CTkButton(
    window, text="SCAN IDENTITY", command=maincall,
    font=("Segoe UI", 11, "bold"),
    fg_color="#231a3a",        # Deep dark purple slate
    hover_color="#ab47bc",     # Glows bright purple on hover
    text_color="#ab47bc",
    border_width=1, border_color="#ab47bc",
    corner_radius=6, height=36, width=180
)
canvas.create_window(520, 410, window=btn_identify, anchor="center")

# 3. Recording Module Button (Right Card Position)
btn_record = ctk.CTkButton(
    window, text="START ARCHIVE", command=record,
    font=("Segoe UI", 11, "bold"),
    fg_color="#3a1a1a",        # Muted dark crimson slate
    hover_color="#ef5350",     # Glows bright red on hover
    text_color="#ef5350",
    border_width=1, border_color="#ef5350",
    corner_radius=6, height=36, width=180
)
canvas.create_window(860, 410, window=btn_record, anchor="center")

# -------------------------------------------------------------
# 🚪 INVISIBLE EXIT CLICK-ZONE (FIXED)
# -------------------------------------------------------------
def on_exit_clicked(event):
    window.quit()

# 1. Create the transparent box directly over the background image's exit graphic area
exit_zone = canvas.create_rectangle(400, 480, 640, 560, fill="", outline="", width=0)

# 2. Bind the left-mouse button click event (<Button-1>) to your exit function
canvas.tag_bind(exit_zone, "<Button-1>", on_exit_clicked)

# 3. FIXED: Change cursor to a hand selection link when hovering over the zone
canvas.tag_bind(exit_zone, "<Enter>", lambda e: canvas.config(cursor="hand2"))
canvas.tag_bind(exit_zone, "<Leave>", lambda e: canvas.config(cursor=""))

window.mainloop()