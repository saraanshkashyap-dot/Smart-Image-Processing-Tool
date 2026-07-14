"""
=========================================================
Smart Image Processing Tool
Utility Functions
=========================================================
"""

import os
from pathlib import Path

import cv2
import numpy as np
from PIL import Image


# =========================================================
# Supported Image Extensions
# =========================================================

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff",
    ".gif",
    ".webp"
}


# =========================================================
# Folder Functions
# =========================================================

def create_folder(folder_name):

    Path(folder_name).mkdir(parents=True, exist_ok=True)


def create_project_folders():

    create_folder("output")
    create_folder("temp")
    create_folder("assets")
    create_folder("assets/icons")


# =========================================================
# File Validation
# =========================================================

def is_image_file(file_path):

    if not file_path:
        return False

    extension = Path(file_path).suffix.lower()

    return extension in SUPPORTED_EXTENSIONS


# =========================================================
# Image Information
# =========================================================

def get_image_info(image):

    if image is None:
        return None

    return {
        "width": image.width,
        "height": image.height,
        "mode": image.mode,
        "size": image.size
    }


# =========================================================
# PIL ↔ NumPy
# =========================================================

def pil_to_numpy(image):

    return np.array(image)


def numpy_to_pil(image):

    return Image.fromarray(image)


# =========================================================
# PIL ↔ OpenCV
# =========================================================

def pil_to_cv(image):

    rgb = np.array(image)

    return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)


def cv_to_pil(image):

    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    return Image.fromarray(rgb)


# =========================================================
# RGB ↔ BGR
# =========================================================

def rgb_to_bgr(image):

    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


def bgr_to_rgb(image):

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# =========================================================
# Copy Image
# =========================================================

def copy_image(image):

    if image is None:
        return None

    return image.copy()
# =========================================================
# Resize Helper
# =========================================================

def resize_image(image, width, height):

    if image is None:
        return None

    return image.resize((width, height), Image.LANCZOS)


# =========================================================
# Rotate Helper
# =========================================================

def rotate_image(image, angle):

    if image is None:
        return None

    return image.rotate(angle, expand=True)


# =========================================================
# Flip Helpers
# =========================================================

def flip_horizontal(image):

    if image is None:
        return None

    return image.transpose(Image.FLIP_LEFT_RIGHT)


def flip_vertical(image):

    if image is None:
        return None

    return image.transpose(Image.FLIP_TOP_BOTTOM)


# =========================================================
# Image Mode
# =========================================================

def convert_to_rgb(image):

    if image is None:
        return None

    if image.mode != "RGB":
        return image.convert("RGB")

    return image


# =========================================================
# Path Helpers
# =========================================================

def get_filename(path):

    return Path(path).name


def get_extension(path):

    return Path(path).suffix.lower()


def get_parent_folder(path):

    return Path(path).parent


# =========================================================
# Output Path
# =========================================================

def generate_output_path(file_name):

    output_folder = Path("output")

    output_folder.mkdir(exist_ok=True)

    return output_folder / file_name


# =========================================================
# Image Size
# =========================================================

def get_image_size(image):

    if image is None:
        return (0, 0)

    return image.size


# =========================================================
# Image Dimension String
# =========================================================

def image_dimension_text(image):

    if image is None:
        return "-"

    return f"{image.width} x {image.height}"


# =========================================================
# Reset Zoom
# =========================================================

def default_zoom():

    return 1.0


# =========================================================
# Error Helper
# =========================================================

def safe_execute(function, *args, **kwargs):

    try:

        return function(*args, **kwargs)

    except Exception as error:

        print("ERROR :", error)

        return None


# =========================================================
# Save Copy
# =========================================================

def save_copy(image, path):

    if image is None:
        return False

    try:

        image.save(path)

        return True

    except Exception:

        return False