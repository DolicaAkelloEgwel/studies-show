import os

VERSION = "v8.3.4"
APP_TITLE = "ЯECOLLECTOR " + VERSION
COMMANDS = ("search", "t-and-c", "help", "whats-new", "thanks")
BLOCK_CHARACTER = "█"
ASSETS_PATH = "assets"
FONT_PATH = os.path.join(ASSETS_PATH, "bedstead-20.bdf")
LOGO_PATH = os.path.join(ASSETS_PATH, "logo")
LINE_Y_DISTANCE = 20
TOP_LINE_Y = 40
RED_COL = 8

APP_WIDTH = 1024
APP_HEIGHT = 768

START_TEXT = "[PRESS ANY KEY TO START]"
COPYRIGHT_TEXT = "(C) 2025 GRAVE MATTER"

with open(LOGO_PATH, "r") as f:
    LOGO = f.readlines()
LOGO = LOGO + ["", VERSION]


def _width_of_string_in_pixels(text: str) -> int:
    n = len(text)
    if n == 0:
        return 0
    return n * 10 + (n - 1) * 2


def text_centre_x(text: str) -> int:
    string_length = _width_of_string_in_pixels(text)
    return APP_WIDTH // 2 - string_length // 2 - 2


def get_vline_colour(show_vline: bool) -> int:
    return int(show_vline) * RED_COL
