"""
=========================================================
Smart Image Processing Tool
Image Processing Module
=========================================================
"""

from PIL import Image
from PIL import ImageEnhance
from tkinter import simpledialog
from utils import (
    copy_image,
    resize_image,
    rotate_image,
    flip_horizontal,
    flip_vertical,
    convert_to_rgb
)


# =========================================================
# Resize
# =========================================================

def resize(image, width, height):

    if image is None:
        return None

    return resize_image(image, width, height)


# =========================================================
# Rotate
# =========================================================

def rotate(image, angle):

    if image is None:
        return None

    return rotate_image(image, angle)


# =========================================================
# Flip Horizontal
# =========================================================

def flip_h(image):

    if image is None:
        return None

    return flip_horizontal(image)


# =========================================================
# Flip Vertical
# =========================================================

def flip_v(image):

    if image is None:
        return None

    return flip_vertical(image)


# =========================================================
# Crop
# =========================================================

def crop_image(self):

    if self.current_image:

        w, h = self.current_image.size

        left = simpledialog.askinteger(
            "Crop",
            "Left crop pixels:",
            initialvalue=50
        )

        top = simpledialog.askinteger(
            "Crop",
            "Top crop pixels:",
            initialvalue=50
        )

        right = simpledialog.askinteger(
            "Crop",
            "Right crop pixels:",
            initialvalue=50
        )

        bottom = simpledialog.askinteger(
            "Crop",
            "Bottom crop pixels:",
            initialvalue=50
        )


        if None not in (left, top, right, bottom):

            self.current_image = self.current_image.crop(
                (
                    left,
                    top,
                    w-right,
                    h-bottom
                )
            )

            self.display_image()

            self.status.configure(
                text="Custom Crop Applied"
            )

# =========================================================
# Brightness
# =========================================================

def brightness(image, value):

    if image is None:
        return None

    enhancer = ImageEnhance.Brightness(image)

    return enhancer.enhance(value)


# =========================================================
# Contrast
# =========================================================

def contrast(image, value):

    if image is None:
        return None

    enhancer = ImageEnhance.Contrast(image)

    return enhancer.enhance(value)
# =========================================================
# Sharpness
# =========================================================

def sharpness(image, value):

    if image is None:
        return None

    enhancer = ImageEnhance.Sharpness(image)

    return enhancer.enhance(value)


# =========================================================
# Color Enhancement
# =========================================================

def color(image, value):

    if image is None:
        return None

    enhancer = ImageEnhance.Color(image)

    return enhancer.enhance(value)


# =========================================================
# Zoom In
# =========================================================

def zoom_in(image, factor=1.25):

    if image is None:
        return None

    width, height = image.size

    width = int(width * factor)

    height = int(height * factor)

    return resize_image(image, width, height)


# =========================================================
# Zoom Out
# =========================================================

def zoom_out(image, factor=0.80):

    if image is None:
        return None

    width, height = image.size

    width = max(1, int(width * factor))

    height = max(1, int(height * factor))

    return resize_image(image, width, height)


# =========================================================
# Reset Image
# =========================================================

def reset_image(original_image):

    if original_image is None:
        return None

    return copy_image(original_image)


# =========================================================
# Get Image Size
# =========================================================

def get_size(image):

    if image is None:
        return (0, 0)

    return image.size


# =========================================================
# Convert RGB
# =========================================================

def to_rgb(image):

    if image is None:
        return None

    return convert_to_rgb(image)


# =========================================================
# Duplicate Image
# =========================================================

def duplicate(image):

    if image is None:
        return None

    return copy_image(image)
# =========================================================
# Thumbnail
# =========================================================

def create_thumbnail(image, size=(250, 250)):

    if image is None:
        return None

    thumbnail = image.copy()
    thumbnail.thumbnail(size)

    return thumbnail


# =========================================================
# Auto Resize
# =========================================================

def auto_resize(image, max_width=1200, max_height=800):

    if image is None:
        return None

    width, height = image.size

    scale = min(max_width / width, max_height / height)

    if scale >= 1:
        return image.copy()

    new_width = int(width * scale)
    new_height = int(height * scale)

    return resize_image(image, new_width, new_height)


# =========================================================
# Image Mode
# =========================================================

def get_mode(image):

    if image is None:
        return ""

    return image.mode


# =========================================================
# Image Width
# =========================================================

def get_width(image):

    if image is None:
        return 0

    return image.width


# =========================================================
# Image Height
# =========================================================

def get_height(image):

    if image is None:
        return 0

    return image.height


# =========================================================
# Image Information
# =========================================================

def image_info(image):

    if image is None:
        return {}

    return {

        "Width": image.width,

        "Height": image.height,

        "Mode": image.mode,

        "Size": image.size

    }


# =========================================================
# Histogram Array
# =========================================================

def histogram(image):

    if image is None:
        return None

    return image.histogram()


# =========================================================
# Clone Image
# =========================================================

def clone(image):

    if image is None:
        return None

    return image.copy()


# =========================================================
# Validate Image
# =========================================================

def is_valid(image):

    return image is not None



    

    
    


