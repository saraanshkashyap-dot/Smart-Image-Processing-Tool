"""
=========================================================
Smart Image Processing Tool
GUI Module
=========================================================
"""
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import simpledialog
import config
import theme

import image_processing
import filters
import history
import icons
import toolbar
import sidebar
import zoom
import adjust
import display
import layout

class SmartImageEditor(ctk.CTk):

    def __init__(self):

        super().__init__()

        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        self.title("Smart Image Studio")
        self.geometry("1500x900")
        self.minsize(1300,750)
        self.crop_mode = False

        self.crop_rect = None

        self.start_x = 0
        self.start_y = 0

        self.end_x = 0
        self.end_y = 0
    
        self.current_image = None

        self.original_image = None

        self.file_path = None

        self.photo = None

        self.zoom_factor=1.0

        self.history = history.History()

        self.current_theme = theme.get_theme("Light")

        self.configure(fg_color="#111827")
        self.create_widgets()

    # ==========================================
    # Create All Widgets
    # ==========================================

    def create_widgets(self):

        toolbar.create_toolbar(self)

        sidebar.create_sidebar(self)

        layout.create_canvas(self)
        layout.create_histogram(self)
        layout.create_statusbar(self)

# ==========================================
    # Image Preview Area
    # ==========================================
    # ==========================================
# Layout Wrappers
# ==========================================

    def create_canvas(self):
        layout.create_canvas(self)


    def create_histogram(self):
        layout.create_histogram(self)


    def create_statusbar(self):
        layout.create_statusbar(self)
    
# ==========================================
    # Open Image Function
    # ==========================================

    def open_image(self):
        toolbar.open_image(self)

    def save_image(self):
        toolbar.save_image(self)

    def undo(self):
        toolbar.undo(self)

    def redo(self):
        toolbar.redo(self)

    def change_theme(self, event=None):
        toolbar.change_theme(self, event)

    # ==========================================
    # Display Image
    # ==========================================
    def display_image(self):
        display.display_image(self)


    def update_histogram(self):
        display.update_histogram(self)
    # ==========================================
    # Undo
    # ==========================================

    def undo(self):

        img = self.history.undo()

        if img:

            self.current_image = img

            self.display_image()


    # ==========================================
    # Redo
    # ==========================================

    def redo(self):

        img = self.history.redo()

        if img:

            self.current_image = img

            self.display_image()


    # ==========================================
    # Theme Change
    # ==========================================

   

    # ==========================================
    # Apply Filter
    # ==========================================

    def apply_filter(self):

        if self.current_image:

            selected = self.filter_box.get()
            self.add_history()

            self.current_image = filters.apply(
                self.current_image,
                selected
            )

            self.history.add(
                self.current_image
            )

            self.display_image()

            self.status.configure(
                text=f"{selected} Applied"
            )
# ==========================================
# Zoom In
# ==========================================

    def zoom_in(self):
        zoom.zoom_in(self)

    def zoom_out(self):
        zoom.zoom_out(self)
# adj
    def crop_image(self):
        adjust.crop_image(self)

    def resize_image(self):
        adjust.resize_image(self)

    def rotate_image(self):
        adjust.rotate_image(self)

    def flip_horizontal(self):
        adjust.flip_horizontal(self)

    def flip_vertical(self):
        adjust.flip_vertical(self)

    def adjust_brightness(self):
        adjust.adjust_brightness(self)

    def adjust_contrast(self):
        adjust.adjust_contrast(self)

    def adjust_sharpness(self):
        adjust.adjust_sharpness(self)
    
# ==========================================
    # Advanced Filters
    # ==========================================

    def grayscale_image(self):

        if self.current_image:

            self.current_image = self.current_image.convert(
                "L"
            )

            self.display_image()

            self.status.configure(
                text="Grayscale Applied"
            )


    # ==========================================
    # Blur Filter
    # ==========================================

    def blur_image(self):

        if self.current_image:

            from PIL import ImageFilter

            self.current_image = self.current_image.filter(
                ImageFilter.BLUR
            )

            self.display_image()

            self.status.configure(
                text="Blur Applied"
            )


    # ==========================================
    # Edge Detection
    # ==========================================

    def edge_detection(self):

        if self.current_image:

            from PIL import ImageFilter

            self.current_image = self.current_image.filter(
                ImageFilter.FIND_EDGES
            )

            self.display_image()

            self.status.configure(
                text="Edge Detection Applied"
            )


    # ==========================================
    # Sharpen Filter
    # ==========================================

    def sharpen_image(self):

        if self.current_image:

            from PIL import ImageFilter

            self.current_image = self.current_image.filter(
                ImageFilter.SHARPEN
            )

            self.display_image()

            self.status.configure(
                text="Sharpen Applied"
            )


    # ==========================================
    # Sepia Filter
    # ==========================================

    def sepia_image(self):

        if self.current_image:

            img = self.current_image.convert(
                "RGB"
            )

            pixels = img.load()


            for x in range(img.width):

                for y in range(img.height):

                    r,g,b = pixels[x,y]


                    tr = int(
                        0.393*r + 0.769*g + 0.189*b
                    )

                    tg = int(
                        0.349*r + 0.686*g + 0.168*b
                    )

                    tb = int(
                        0.272*r + 0.534*g + 0.131*b
                    )


                    pixels[x,y] = (
                        min(tr,255),
                        min(tg,255),
                        min(tb,255)
                    )


            self.current_image = img

            self.display_image()

            self.status.configure(
                text="Sepia Applied"
            )
# ==========================================
    # Add History
    # ==========================================

    def add_history(self):

        if self.current_image:

            self.history.add(
                self.current_image.copy()
            )
