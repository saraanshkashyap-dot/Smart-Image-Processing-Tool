# ======================================================
# TOOLBAR MODULE START
# ======================================================
import tkinter as tk
from tkinter import ttk
import theme
import input_output

import customtkinter as ctk


def create_toolbar(self):

    self.toolbar = ctk.CTkFrame(
        self,
        height=70,
        fg_color="#111827",
        corner_radius=0
    )

    self.toolbar.pack(
        side="top",
        fill="x"
    )

    self.toolbar.pack_propagate(False)

    # ---------------- Logo ----------------

    self.logo = ctk.CTkLabel(
        self.toolbar,
        text="🖼 Smart Image Studio",
        font=("Segoe UI",24,"bold")
    )

    self.logo.pack(
        side="left",
        padx=20
    )

    # ---------------- Buttons ----------------

    button_style = {
    "width": 95,
    "height": 42,
    "corner_radius": 12,
    "font": ("Segoe UI Semibold", 13),
    "fg_color": "#2563EB",
    "hover_color": "#3B82F6",
    "border_width": 1,
    "border_color": "#4F8EF7",
    "text_color": "white"
}

    self.open_btn = ctk.CTkButton(
        self.toolbar,
        text="📂 Open",
        command=self.open_image,
        **button_style
    )

    self.open_btn.pack(side="left", padx=5)

    self.save_btn = ctk.CTkButton(
        self.toolbar,
        text="💾 Save",
        command=self.save_image,
        **button_style
    )

    self.save_btn.pack(side="left", padx=5)

    self.undo_btn = ctk.CTkButton(
        self.toolbar,
        text="↩ Undo",
        command=self.undo,
        **button_style
    )

    self.undo_btn.pack(side="left", padx=5)

    self.redo_btn = ctk.CTkButton(
        self.toolbar,
        text="↪ Redo",
        command=self.redo,
        **button_style
    )

    self.redo_btn.pack(side="left", padx=5)

    self.zoom_in_btn = ctk.CTkButton(
        self.toolbar,
        text="➕ Zoom",
        command=self.zoom_in,
        **button_style
    )

    self.zoom_in_btn.pack(side="left", padx=5)

    self.zoom_out_btn = ctk.CTkButton(
        self.toolbar,
        text="➖ Zoom",
        command=self.zoom_out,
        **button_style
    )

    self.zoom_out_btn.pack(side="left", padx=5)

    # ---------------- Theme ----------------

    self.theme_box = ctk.CTkOptionMenu(
    self.toolbar,
    values=["Dark","Light"],
    width=130,
    height=40,
    corner_radius=12,
    fg_color="#2563EB",
    button_color="#1D4ED8",
    button_hover_color="#2563EB",
    command=self.change_theme
)

    self.theme_box.set("Dark")

    self.theme_box.pack(
        side="right",
        padx=20
    )
def open_image(self):

    path = input_output.open_file()

    if path:

        self.file_path = path
        self.original_image = input_output.load_image(path)
        self.current_image = self.original_image.copy()

        self.zoom_factor = 1.0

        self.history.add(self.current_image)

        self.after(100, self.display_image)

        self.status.configure(text="Image Opened")