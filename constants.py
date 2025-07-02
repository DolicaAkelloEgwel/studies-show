import os
import textwrap
from math import floor

VERSION = "v8.3.4"
APP_TITLE = "ЯECOLLECTOR " + VERSION
COMMANDS = ("Search", "Help", "What's New", "Thanks", "Quit")
BLOCK_CHARACTER = "█"
ASSETS_PATH = "assets"
FONT_PATH = os.path.join(ASSETS_PATH, "bedstead-20.bdf")

# height of the font in pixels
TEXT_PIXEL_HEIGHT = 20
# the colour red in pyxel
RED = 8
# amount of x-border in pixels for the terms and conditions text
TERMS_AND_CONDITIONS_BORDER = 80

APP_WIDTH = 1024
HALF_APP_WIDTH = APP_WIDTH // 2
APP_HEIGHT = 768

# load the logo text into a list + blank line + version text
with open(os.path.join(ASSETS_PATH, "logo"), "r") as f:
    LOGO = f.readlines()
LOGO = LOGO + ["", VERSION]

# load the terms and conditions text
with open(os.path.join(ASSETS_PATH, "terms-and-conditions"), "r") as f:
    terms_and_conditions_text = f.readlines()


def _width_of_string_in_pixels(num_chars: int) -> int:
    return num_chars * 10 + (num_chars - 1) * 2


def text_centre_x(text: str) -> int:
    num_chars = len(text)
    if num_chars == 0:
        raise ValueError("String has length 0")
    string_width_in_pixels = _width_of_string_in_pixels(num_chars)
    return HALF_APP_WIDTH - string_width_in_pixels // 2 - 2


def get_vline_colour(show_vline: bool) -> int:
    return int(show_vline) * RED


def wrap_text_for_border(text: str, border: int) -> str:
    max_pixel_width = APP_WIDTH - border * 2
    max_chars = floor(max_pixel_width / 12 + (1 / 6))
    return textwrap.wrap(text, max_chars)


TERMS_AND_CONDITIONS_TEXT = []

for line in terms_and_conditions_text:
    split_text = wrap_text_for_border(line, TERMS_AND_CONDITIONS_BORDER)
    if len(split_text) == 0:
        split_text += [""]
    TERMS_AND_CONDITIONS_TEXT += split_text


class CenteredText:
    def __init__(self, text: str, y: int):
        self.text = text
        self.x = text_centre_x(text)
        self.y = y


START_TEXT = CenteredText("[PRESS RETURN TO START]", APP_HEIGHT - 120)
COPYRIGHT_TEXT = CenteredText("(C) 2025 GRAVE MATTER", APP_HEIGHT - 60)
TERMS_AND_CONDITIONS_TITLE = CenteredText("TERMS AND CONDITIONS", 20)
ACCEPT_OR_DECLINE = CenteredText(
    "(A)CCEPT" + " " * 20 + "(D)ECLINE", APP_HEIGHT - 80
)
