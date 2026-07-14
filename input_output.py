"""
=========================================================
Smart Image Processing Tool
Input Output Module
=========================================================
"""

from tkinter import filedialog
from PIL import Image


# ==========================================
# Open File
# ==========================================

def open_file():

    path = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp")
        ]
    )

    return path



# ==========================================
# Load Image
# ==========================================

def load_image(path):

    if path:

        img = Image.open(path)

        return img.convert("RGB")

    return None



# ==========================================
# Save File
# ==========================================

def save_file(image):

    if image:

        path = filedialog.asksaveasfilename(
            title="Save Image",
            defaultextension=".png",
            filetypes=[
                ("PNG Image","*.png"),
                ("JPEG Image","*.jpg")
            ]
        )

        if path:

            image.save(path)