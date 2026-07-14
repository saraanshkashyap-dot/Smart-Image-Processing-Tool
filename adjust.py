import tkinter as tk
from PIL import Image

def resize_image(self):

    if self.current_image is None:
        return

    window = tk.Toplevel(self)
    window.title("Resize Image")
    window.geometry("300x180")

    tk.Label(window, text="Width").pack(pady=5)
    width_entry = tk.Entry(window)
    width_entry.pack()

    tk.Label(window, text="Height").pack(pady=5)
    height_entry = tk.Entry(window)
    height_entry.pack()

    def apply():

        try:
            width = int(width_entry.get())
            height = int(height_entry.get())

            self.add_history()

            self.current_image = self.current_image.resize(
                (width, height),
                Image.Resampling.LANCZOS
            )

            self.display_image()

            self.status.configure(
                text="Image Resized"
            )

            window.destroy()

        except Exception:
            self.status.configure(
                text="Invalid Size"
            )

    tk.Button(
        window,
        text="Resize",
        command=apply
    ).pack(pady=15)
# ==========================================
# Rotate Image
# ==========================================

def rotate_image(self):

    if self.current_image is None:
        return

    self.add_history()

    self.current_image = self.current_image.rotate(
        90,
        expand=True
    )

    self.display_image()

    self.status.configure(text="Image Rotated")


# ==========================================
# Flip Horizontal
# ==========================================

def flip_horizontal(self):

    if self.current_image is None:
        return

    self.add_history()

    self.current_image = self.current_image.transpose(
        Image.Transpose.FLIP_LEFT_RIGHT
    )

    self.display_image()

    self.status.configure(text="Horizontal Flip Applied")


# ==========================================
# Flip Vertical
# ==========================================

def flip_vertical(self):

    if self.current_image is None:
        return

    self.add_history()

    self.current_image = self.current_image.transpose(
        Image.Transpose.FLIP_TOP_BOTTOM
    )

    self.display_image()

    self.status.configure(text="Vertical Flip Applied")


# ==========================================
# Crop Tool
# ==========================================

def crop_image(self):

    if self.current_image is None:
        return

    # create variables if not already created
    if not hasattr(self, "crop_rect"):
        self.crop_rect = None

    self.crop_mode = True

    self.status.configure(
        text="Drag mouse to select crop area"
    )

    self.canvas.bind("<Button-1>", lambda e: crop_start(self, e))
    self.canvas.bind("<B1-Motion>", lambda e: crop_drag(self, e))
    self.canvas.bind("<ButtonRelease-1>", lambda e: crop_finish(self, e))


# ==========================================
# Mouse Press
# ==========================================

def crop_start(self, event):

    self.start_x = event.x
    self.start_y = event.y

    if hasattr(self, "crop_rect") and self.crop_rect:

        self.canvas.delete(self.crop_rect)

    self.crop_rect = self.canvas.create_rectangle(

        self.start_x,
        self.start_y,

        self.start_x,
        self.start_y,

        outline="#3B82F6",
        width=2,
        dash=(5, 3)

    )


# ==========================================
# Mouse Drag
# ==========================================

def crop_drag(self, event):

    if not hasattr(self, "crop_rect"):
        return

    self.end_x = event.x
    self.end_y = event.y

    self.canvas.coords(

        self.crop_rect,

        self.start_x,
        self.start_y,

        self.end_x,
        self.end_y

    )


# ==========================================
# Mouse Release
# ==========================================

def crop_finish(self, event):

    self.canvas.unbind("<Button-1>")
    self.canvas.unbind("<B1-Motion>")
    self.canvas.unbind("<ButtonRelease-1>")

    self.end_x = event.x
    self.end_y = event.y

    x1 = min(self.start_x, self.end_x)
    y1 = min(self.start_y, self.end_y)

    x2 = max(self.start_x, self.end_x)
    y2 = max(self.start_y, self.end_y)

    img_w, img_h = self.current_image.size

    canvas_w = self.canvas.winfo_width()
    canvas_h = self.canvas.winfo_height()

    scale_x = img_w / canvas_w
    scale_y = img_h / canvas_h

    left = int(x1 * scale_x)
    top = int(y1 * scale_y)

    right = int(x2 * scale_x)
    bottom = int(y2 * scale_y)

    if right <= left or bottom <= top:

        self.status.configure(text="Invalid Crop Area")

        if self.crop_rect:
            self.canvas.delete(self.crop_rect)
            self.crop_rect = None

        return

    self.add_history()

    self.current_image = self.current_image.crop(

        (
            left,
            top,
            right,
            bottom
        )

    )

    self.display_image()

    if self.crop_rect:

        self.canvas.delete(self.crop_rect)
        self.crop_rect = None

    self.status.configure(text="Crop Applied")
import tkinter as tk
from PIL import ImageEnhance

# ==========================================
# Brightness
# ==========================================

def adjust_brightness(self):

    if self.current_image is None:
        return

    window = tk.Toplevel(self)
    window.title("Brightness")
    window.geometry("320x120")
    window.resizable(False, False)

    original = self.current_image.copy()

    def change(value):

        enhancer = ImageEnhance.Brightness(original)

        self.current_image = enhancer.enhance(float(value))

        self.display_image()

    def apply():

        self.add_history()
        window.destroy()
        self.status.configure(text="Brightness Applied")

    slider = tk.Scale(
        window,
        from_=0.1,
        to=3.0,
        resolution=0.1,
        orient="horizontal",
        length=250,
        label="Brightness",
        command=change
    )

    slider.set(1.0)
    slider.pack(pady=10)

    tk.Button(
        window,
        text="Apply",
        command=apply
    ).pack(pady=5)


# ==========================================
# Contrast
# ==========================================

def adjust_contrast(self):

    if self.current_image is None:
        return

    window = tk.Toplevel(self)
    window.title("Contrast")
    window.geometry("320x120")
    window.resizable(False, False)

    original = self.current_image.copy()

    def change(value):

        enhancer = ImageEnhance.Contrast(original)

        self.current_image = enhancer.enhance(float(value))

        self.display_image()

    def apply():

        self.add_history()
        window.destroy()
        self.status.configure(text="Contrast Applied")

    slider = tk.Scale(
        window,
        from_=0.1,
        to=3.0,
        resolution=0.1,
        orient="horizontal",
        length=250,
        label="Contrast",
        command=change
    )

    slider.set(1.0)
    slider.pack(pady=10)

    tk.Button(
        window,
        text="Apply",
        command=apply
    ).pack(pady=5)


# ==========================================
# Sharpness
# ==========================================

def adjust_sharpness(self):

    if self.current_image is None:
        return

    window = tk.Toplevel(self)
    window.title("Sharpness")
    window.geometry("320x120")
    window.resizable(False, False)

    original = self.current_image.copy()

    def change(value):

        enhancer = ImageEnhance.Sharpness(original)

        self.current_image = enhancer.enhance(float(value))

        self.display_image()

    def apply():

        self.add_history()
        window.destroy()
        self.status.configure(text="Sharpness Applied")

    slider = tk.Scale(
        window,
        from_=0.1,
        to=5.0,
        resolution=0.1,
        orient="horizontal",
        length=250,
        label="Sharpness",
        command=change
    )

    slider.set(1.0)
    slider.pack(pady=10)

    tk.Button(
        window,
        text="Apply",
        command=apply
    ).pack(pady=5)