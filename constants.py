import os
import textwrap
from math import floor

VERSION = "v8.3.4"
APP_TITLE = "ЯECOLLECTOR " + VERSION
COMMANDS = ("search", "t-and-c", "help", "whats-new", "thanks")
BLOCK_CHARACTER = "█"
ASSETS_PATH = "assets"
FONT_PATH = os.path.join(ASSETS_PATH, "bedstead-20.bdf")
LINE_Y_DISTANCE = 20
TOP_LINE_Y = 40
RED_COL = 8

APP_WIDTH = 1024
HALF_APP_WIDTH = APP_WIDTH // 2
APP_HEIGHT = 768

with open(os.path.join(ASSETS_PATH, "logo"), "r") as f:
    LOGO = f.readlines()
LOGO = LOGO + ["", VERSION]

TERMS_AND_CONDITIONS_TITLE = "TERMS AND CONDITIONS"
TERMS_AND_CONDITIONS_BORDER = 80
ACCEPT_OR_DECLINE = "(A)ccept" + " " * 10 + "(D)ecline"

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
    return int(show_vline) * RED_COL


def wrap_text_for_border(text: str, border: int) -> str:
    max_pixel_width = APP_WIDTH - border * 2
    max_chars = floor(max_pixel_width / 12 + (1 / 6))
    return textwrap.wrap(text, max_chars, replace_whitespace=False)


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
