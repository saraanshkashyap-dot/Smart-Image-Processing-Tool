"""
=========================================================
Smart Image Processing Tool
Filters Module
=========================================================
"""

import cv2
import numpy as np

from PIL import Image
from PIL import ImageFilter
from PIL import ImageOps

from utils import (
    pil_to_cv,
    cv_to_pil,
    convert_to_rgb
)


# =========================================================
# Grayscale
# =========================================================

def grayscale(image):

    if image is None:
        return None

    return ImageOps.grayscale(image).convert("RGB")


# =========================================================
# Negative
# =========================================================

def negative(image):

    if image is None:
        return None

    image = convert_to_rgb(image)

    return ImageOps.invert(image)


# =========================================================
# Blur
# =========================================================

def blur(image, radius=3):

    if image is None:
        return None

    return image.filter(
        ImageFilter.GaussianBlur(radius)
    )


# =========================================================
# Sharpen Filter
# =========================================================

def sharpen(image):

    if image is None:
        return None

    return image.filter(
        ImageFilter.SHARPEN
    )


# =========================================================
# Edge Enhance
# =========================================================

def edge_enhance(image):

    if image is None:
        return None

    return image.filter(
        ImageFilter.EDGE_ENHANCE
    )


# =========================================================
# Find Edges
# =========================================================

def edge_detection(image):

    if image is None:
        return None

    return image.filter(
        ImageFilter.FIND_EDGES
    )
# =========================================================
# Sepia Filter
# =========================================================

def sepia(image):

    if image is None:
        return None

    image = convert_to_rgb(image)

    img = np.array(image).astype(np.float32)

    transform = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])

    img = img @ transform.T
    img = np.clip(img, 0, 255).astype(np.uint8)

    return Image.fromarray(img)


# =========================================================
# Emboss
# =========================================================

def emboss(image):

    if image is None:
        return None

    return image.filter(ImageFilter.EMBOSS)


# =========================================================
# Smooth
# =========================================================

def smooth(image):

    if image is None:
        return None

    return image.filter(ImageFilter.SMOOTH)


# =========================================================
# Detail
# =========================================================

def detail(image):

    if image is None:
        return None

    return image.filter(ImageFilter.DETAIL)


# =========================================================
# Contour
# =========================================================

def contour(image):

    if image is None:
        return None

    return image.filter(ImageFilter.CONTOUR)


# =========================================================
# Median Blur
# =========================================================

def median_blur(image):

    if image is None:
        return None

    cv_img = pil_to_cv(image)

    result = cv2.medianBlur(cv_img, 5)

    return cv_to_pil(result)


# =========================================================
# Box Blur
# =========================================================

def box_blur(image):

    if image is None:
        return None

    return image.filter(ImageFilter.BoxBlur(5))


# =========================================================
# Mode Filter
# =========================================================

def mode_filter(image):

    if image is None:
        return None

    return image.filter(ImageFilter.ModeFilter(size=5))
# =========================================================
# Pencil Sketch
# =========================================================

def pencil_sketch(image):

    if image is None:
        return None

    cv_img = pil_to_cv(image)

    gray, sketch = cv2.pencilSketch(
        cv_img,
        sigma_s=60,
        sigma_r=0.07,
        shade_factor=0.05
    )

    return cv_to_pil(sketch)


# =========================================================
# Cartoon Effect
# =========================================================

def cartoon(image):

    if image is None:
        return None

    img = pil_to_cv(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)

    edges = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        9,
        9
    )

    color = cv2.bilateralFilter(img, 9, 300, 300)

    cartoon = cv2.bitwise_and(color, color, mask=edges)

    return cv_to_pil(cartoon)


# =========================================================
# HDR Effect
# =========================================================

def hdr(image):

    if image is None:
        return None

    img = pil_to_cv(image)

    hdr_img = cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)

    return cv_to_pil(hdr_img)


# =========================================================
# Canny Edge
# =========================================================

def canny(image):

    if image is None:
        return None

    img = pil_to_cv(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edge = cv2.Canny(gray, 100, 200)

    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)

    return cv_to_pil(edge)


# =========================================================
# Noise Reduction
# =========================================================

def denoise(image):

    if image is None:
        return None

    img = pil_to_cv(image)

    img = cv2.fastNlMeansDenoisingColored(
        img,
        None,
        10,
        10,
        7,
        21
    )

    return cv_to_pil(img)


# =========================================================
# Binary Threshold
# =========================================================

def binary(image):

    if image is None:
        return None

    img = pil_to_cv(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, result = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

    return cv_to_pil(result)
# =========================================================
# Adaptive Threshold
# =========================================================

def adaptive_threshold(image):

    if image is None:
        return None

    img = pil_to_cv(image)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    result = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    result = cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)

    return cv_to_pil(result)


# =========================================================
# Erode
# =========================================================

def erode(image, iterations=1):

    if image is None:
        return None

    img = pil_to_cv(image)

    kernel = np.ones((3,3), np.uint8)

    result = cv2.erode(img, kernel, iterations=iterations)

    return cv_to_pil(result)


# =========================================================
# Dilate
# =========================================================

def dilate(image, iterations=1):

    if image is None:
        return None

    img = pil_to_cv(image)

    kernel = np.ones((3,3), np.uint8)

    result = cv2.dilate(img, kernel, iterations=iterations)

    return cv_to_pil(result)


# =========================================================
# Bilateral Filter
# =========================================================

def bilateral(image):

    if image is None:
        return None

    img = pil_to_cv(image)

    result = cv2.bilateralFilter(img,9,75,75)

    return cv_to_pil(result)


# =========================================================
# Gaussian Blur
# =========================================================

def gaussian(image):

    if image is None:
        return None

    img = pil_to_cv(image)

    result = cv2.GaussianBlur(img,(5,5),0)

    return cv_to_pil(result)


# =========================================================
# Available Filters
# =========================================================

FILTERS = {

    "Grayscale": grayscale,
    "Negative": negative,
    "Sepia": sepia,
    "Blur": blur,
    "Gaussian": gaussian,
    "Sharpen": sharpen,
    "Emboss": emboss,
    "Smooth": smooth,
    "Detail": detail,
    "Contour": contour,
    "Median Blur": median_blur,
    "Box Blur": box_blur,
    "Mode Filter": mode_filter,
    "Pencil Sketch": pencil_sketch,
    "Cartoon": cartoon,
    "HDR": hdr,
    "Canny": canny,
    "Binary": binary,
    "Adaptive Threshold": adaptive_threshold,
    "Denoise": denoise,
    "Bilateral": bilateral,
    "Erode": erode,
    "Dilate": dilate

}


# =========================================================
# Get Filter Names
# =========================================================

def get_filter_names():

    return list(FILTERS.keys())


# =========================================================
# Apply Filter by Name
# =========================================================

def apply_filter(image, name):

    if name not in FILTERS:
        return image

    return FILTERS[name](image)
# =========================================================
# GUI Compatibility Function
# =========================================================

# =========================================================
# GUI Compatibility Function
# =========================================================

def apply(image, name):

    return apply_filter(
        image,
        name
    )