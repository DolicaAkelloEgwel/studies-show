import os
import textwrap
from math import floor

VERSION = "v8.3.4"
APP_TITLE = "ЯECOLLECTOR " + VERSION
BLOCK_CHARACTER = "█"
SELECTED_CHARACTER = "▷ "
MENU_LOGO_Y = 100

ASSETS_PATH = "assets"
BEDSTEAD_PATH = os.path.join(ASSETS_PATH, "bedstead-20.bdf")
BOLD_BEDSTEAD_PATH = os.path.join(ASSETS_PATH, "bedstead-bold-20.bdf")

# height of the font in pixels
TEXT_PIXEL_HEIGHT = 20
# the colour red in pyxel
RED = 8
# amount of x-border in pixels for the terms and conditions text
BORDER_TERMS_AND_CONDITIONS = 100

APP_WIDTH = 1024
HALF_APP_WIDTH = APP_WIDTH // 2
APP_HEIGHT = 768

# load the logo text into a list + blank line + version text
with open(os.path.join(ASSETS_PATH, "logo"), "r") as f:
    LOGO = f.readlines()
LOGO = LOGO + ["", VERSION]


def _width_of_string_in_pixels(num_chars: int) -> int:
    """Finds the width of the text in pixels given the number of characters.

    Args:
        num_chars (int): Number of characters in a string.

    Returns:
        int: Width of the string in pixels.
    """
    return num_chars * 10 + (num_chars - 1) * 2


def text_centre_x(text: str) -> int:
    """Finds the x value that will centre text on the screen.

    Args:
        text (str): The text to be displayed.

    Raises:
        ValueError: When the string is empty.

    Returns:
        int: x-value to give to pyxel in order to centre the string.
    """
    num_chars = len(text)
    if num_chars == 0:
        raise ValueError("String has length 0")
    string_width_in_pixels = _width_of_string_in_pixels(num_chars)
    return HALF_APP_WIDTH - string_width_in_pixels // 2 - 2


def get_vline_colour(show_vline: bool) -> int:
    """Determines what colour the vertical line should be.

    Args:
        show_vline (bool): Bool that tells us whether or not the vertical line
                           should be visible.

    Returns:
        int: Returns the pyxel red colour value when show_vline is True,
             otherwise black is returned.
    """
    return int(show_vline) * RED


def wrap_text_for_border(text: str, border: int) -> str:
    max_pixel_width = APP_WIDTH - border * 2
    max_chars = floor(max_pixel_width / 12 + (1 / 6))
    return textwrap.wrap(text, max_chars)


# load the terms and conditions text
with open(os.path.join(ASSETS_PATH, "terms-and-conditions"), "r") as f:
    terms_and_conditions_text = f.readlines()

TEXT_TERMS_AND_CONDITIONS = []

# create wrapped terms and conditions text
for line in terms_and_conditions_text:
    split_text = wrap_text_for_border(line, BORDER_TERMS_AND_CONDITIONS)
    if len(split_text) == 0:
        split_text += [""]
    TEXT_TERMS_AND_CONDITIONS += split_text


class CenteredText:
    def __init__(self, text: str, y: int):
        """Simple object for storing info about centered text.

        Args:
            text (str): The text to be displayed.
            y (int): The y-value for the string's position.
        """
        self.text = text
        self.x = text_centre_x(text)
        self.y = y


class MenuCenteredText(CenteredText):
    def __init__(self, text: str, y: int, selected: bool = False):
        super().__init__(text, y)
        self._selected = selected

    @property
    def color(self) -> int:
        if self._selected:
            return 0
        else:
            return 11


def _centre_block_of_text(text: list[str], line_height: int) -> int:
    return int((APP_HEIGHT - (line_height * len(text))) * 0.5)


# prepare text that will be centered in the different states
TERMS_TEXT_Y = _centre_block_of_text(
    TEXT_TERMS_AND_CONDITIONS, TEXT_PIXEL_HEIGHT
)

START_TEXT = CenteredText("[PRESS RETURN TO START]", APP_HEIGHT - 120)
COPYRIGHT_TEXT = CenteredText("(C) 2025 GRAVE MATTER", APP_HEIGHT - 60)
ACCEPT_OR_DECLINE = CenteredText(
    "(A)CCEPT" + " " * 20 + "(D)ECLINE",
    APP_HEIGHT - TERMS_TEXT_Y // 2 - 10,
)

# creating some padding to make it look more title-ish
padding = max([len(line) for line in TEXT_TERMS_AND_CONDITIONS])
padding = (padding - len("TERMS AND CONDITIONS")) // 2 - 1
padding = "*" * padding
TERMS_AND_CONDITIONS_TITLE = CenteredText(
    padding + " TERMS AND CONDITIONS " + padding, TERMS_TEXT_Y // 2 - 10
)

MENU_LOGO_PIXEL_HEIGHT = (2 * MENU_LOGO_Y) + (TEXT_PIXEL_HEIGHT * len(LOGO))
REMAINING_MENU_Y = APP_HEIGHT - MENU_LOGO_PIXEL_HEIGHT


MENU_OPTIONS = ["SEARCH", "HELP", "WHAT'S NEW", "THANKS", "QUIT"]
N_MENU_OPTIONS = len(MENU_OPTIONS)

MENU_ITEM_GAP = 50
MENU_OPTIONS_PIXEL_HEIGHT = (TEXT_PIXEL_HEIGHT * N_MENU_OPTIONS) + (
    (N_MENU_OPTIONS - 1) * (MENU_ITEM_GAP - TEXT_PIXEL_HEIGHT)
)

OFFSET = (
    floor((REMAINING_MENU_Y - MENU_LOGO_PIXEL_HEIGHT) // 2)
    + MENU_LOGO_PIXEL_HEIGHT
    + 30
)


MENU_OPTIONS = [
    MenuCenteredText(text, OFFSET + (i * MENU_ITEM_GAP))
    for i, text in enumerate(MENU_OPTIONS)
]
MENU_OPTIONS[2]._selected = True
