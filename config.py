"""
=========================================================
Smart Image Processing Tool
Configuration File
=========================================================
"""

# ==========================
# Window Settings
# ==========================
APP_TITLE = "Smart Image Processing Tool"

WINDOW_WIDTH = 1300
WINDOW_HEIGHT = 820

MIN_WIDTH = 1050
MIN_HEIGHT = 650


# ==========================
# Theme Colors
# ==========================

PRIMARY = "#2F6FED"
SECONDARY = "#EEF3FA"

BACKGROUND = "#EEF3FA"
PANEL = "#F5F8FC"

WHITE = "#FFFFFF"
BLACK = "#000000"

STATUS = "#E4ECF9"

BORDER = "#C9D6EA"

BUTTON_HOVER = "#DCE7FB"


# ==========================
# Fonts
# ==========================

TITLE_FONT = ("Segoe UI", 12, "bold")

HEADER_FONT = ("Segoe UI", 10, "bold")

NORMAL_FONT = ("Segoe UI", 9)


# ==========================
# Image Formats
# ==========================

SUPPORTED_FORMATS = (
    "*.jpg",
    "*.jpeg",
    "*.png"
)


# ==========================
# Zoom
# ==========================

DEFAULT_ZOOM = 1.0

MIN_ZOOM = 0.20

MAX_ZOOM = 5.00


# ==========================
# History
# ==========================

MAX_HISTORY = 25


# ==========================
# Histogram
# ==========================

HISTOGRAM_BINS = 64


# ==========================
# Blur
# ==========================

MIN_BLUR = 0

MAX_BLUR = 25


# ==========================
# Brightness
# ==========================

MIN_BRIGHTNESS = 0

MAX_BRIGHTNESS = 3


# ==========================
# Contrast
# ==========================

MIN_CONTRAST = 0

MAX_CONTRAST = 3


# ==========================
# Sharpness
# ==========================

MIN_SHARPNESS = 0

MAX_SHARPNESS = 3


# ==========================
# Color
# ==========================

MIN_COLOR = 0

MAX_COLOR = 3