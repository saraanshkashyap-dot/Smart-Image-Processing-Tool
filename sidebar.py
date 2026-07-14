# ==========================================
    # Left Sidebar
    # =========================================
import customtkinter as ctk
import filters


def create_sidebar(self):

    self.sidebar = ctk.CTkFrame(
        self,
        width=250,
        fg_color="#172554",
        corner_radius=0
    )

    self.sidebar.pack(
        side="left",
        fill="y"
    )

   

    # =========================
    # Title
    # =========================

    title = ctk.CTkLabel(
        self.sidebar,
        text="🛠 TOOLS",
        font=("Segoe UI",22,"bold")
    )

    title.pack(pady=(20,25))

    button_style = {
        "width":200,
        "height":40,
        "corner_radius":12,
        "font":("Segoe UI",14),
        "fg_color":"#2563EB",
        "hover_color":"#1D4ED8"
    }

    # =========================
    # Editing
    # =========================

    ctk.CTkLabel(
        self.sidebar,
        text="Editing",
        font=("Segoe UI",16,"bold")
    ).pack(pady=(10,5))

    ctk.CTkButton(
        self.sidebar,
        text="✂ Crop",
        command=self.crop_image,
        **button_style
    ).pack(pady=4)

    ctk.CTkButton(
        self.sidebar,
        text="📐 Resize",
        command=self.resize_image,
        **button_style
    ).pack(pady=4)

    ctk.CTkButton(
        self.sidebar,
        text="🔄 Rotate",
        command=self.rotate_image,
        **button_style
    ).pack(pady=4)

    ctk.CTkButton(
        self.sidebar,
        text="↔ Flip Horizontal",
        command=self.flip_horizontal,
        **button_style
    ).pack(pady=4)

    ctk.CTkButton(
        self.sidebar,
        text="↕ Flip Vertical",
        command=self.flip_vertical,
        **button_style
    ).pack(pady=4)

    # =========================
    # Enhancement
    # =========================

    ctk.CTkLabel(
        self.sidebar,
        text="Enhancement",
        font=("Segoe UI",16,"bold")
    ).pack(pady=(20,5))

    ctk.CTkButton(
        self.sidebar,
        text="☀ Brightness",
        command=self.adjust_brightness,
        **button_style
    ).pack(pady=4)

    ctk.CTkButton(
        self.sidebar,
        text="◐ Contrast",
        command=self.adjust_contrast,
        **button_style
    ).pack(pady=4)

    ctk.CTkButton(
        self.sidebar,
        text="✨ Sharpness",
        command=self.adjust_sharpness,
        **button_style
    ).pack(pady=4)
