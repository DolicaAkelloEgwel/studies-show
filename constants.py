import os
import textwrap
from enum import Enum
from math import floor


class State(Enum):
    TITLE = 1
    TERMS_AND_CONDITIONS = 2
    MAIN_MENU = 3
    SEARCH = 4
    HELP = 5
    WHATS_NEW = 6
    THANKS = 7


VERSION = "v8.3.4"
APP_TITLE = "ЯECOLLECTOR " + VERSION

SELECTED_CHARACTER = "▷ "

# how far down the menu screen the first line of the logo appears
MENU_LOGO_Y = 100
# offset for the menu description text that appears on the bottom
MENU_DESCRIPTION_OFFSET = 40

ASSETS_PATH = "assets"
BEDSTEAD_PATH = os.path.join(ASSETS_PATH, "bedstead-20.bdf")
BOLD_BEDSTEAD_PATH = os.path.join(ASSETS_PATH, "bedstead-bold-20.bdf")

# height of the font in pixels
TEXT_PIXEL_HEIGHT = 20
# the colour red in pyxel
RED = 8
# the colour grey in pyxel
GREY = 13
# the colour green in pyxel
GREEN = 11
# amount of x-border in pixels for blocks of text
BORDER_TEXT_BLOCK = 100

APP_WIDTH = 1024
HALF_APP_WIDTH = APP_WIDTH // 2
APP_HEIGHT = 768

IDLE_LIMIT = 30
PRINTER_NAME = "M834"


def _read_text_block_from_file(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.readlines()


def _create_title_padding(title: str) -> str:
    padding = (TEXT_EXTENT - len(title)) // 2 - 1
    padding = "*" * padding
    return padding


# load the logo text into a list + blank line + version text
LOGO = _read_text_block_from_file(os.path.join(ASSETS_PATH, "logo")) + [
    "",
    VERSION,
]


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
terms_and_conditions_text = _read_text_block_from_file(
    os.path.join(ASSETS_PATH, "terms-and-conditions")
)


def _create_wrapped_text_list(text: list[str]) -> list[str]:
    wrapped_lines = []
    for line in text:
        split_text = wrap_text_for_border(line, BORDER_TEXT_BLOCK)
        if len(split_text) == 0:
            split_text += [""]
        wrapped_lines += split_text
    return wrapped_lines


# create wrapped terms and conditions text
TEXT_TERMS_AND_CONDITIONS = _create_wrapped_text_list(
    terms_and_conditions_text
)


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


class PaddedCenteredText(CenteredText):
    def __init__(self, title: str, y: int):
        padding = _create_title_padding(title)
        super().__init__(f"{padding} {title} {padding}", y)


class MenuCenteredText(CenteredText):
    def __init__(
        self,
        text: str,
        description: str,
        y: int,
        new_state: int,
        selected: bool = False,
    ):
        """Object for storing menu item info.

        Args:
            text (str): The text that gets displayed for the menu item.
            description (str): A description of the menu item.
            y (int): The y-value for the text position.
            new_state (int): The new state value for when the menu option has
                             been selected.
            selected (bool, optional): Whether or not this item has been
                                       selected. Defaults to False.
        """
        super().__init__(text, y)
        self._selected = selected
        self._description_text = description
        self._description_x = text_centre_x(description)
        self._new_state = new_state

    @property
    def selected(self) -> bool:
        return self._selected

    @property
    def description_text(self) -> str:
        return self._description_text

    @property
    def description_x(self) -> int:
        return self._description_x

    @property
    def new_state(self) -> int:
        return self._new_state

    @selected.setter
    def selected(self, selected):
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
TEXT_EXTENT = max([len(line) for line in TEXT_TERMS_AND_CONDITIONS])
padding = _create_title_padding("TERMS AND CONDITIONS")
TERMS_AND_CONDITIONS_TITLE = CenteredText(
    padding + " TERMS AND CONDITIONS " + padding, TERMS_TEXT_Y // 2 - 10
)

MENU_LOGO_PIXEL_HEIGHT = (2 * MENU_LOGO_Y) + (TEXT_PIXEL_HEIGHT * len(LOGO))
REMAINING_MENU_Y = APP_HEIGHT - MENU_LOGO_PIXEL_HEIGHT

# menu items + descriptions + states
MENU_OPTIONS = [
    ("SEARCH", "Search the database for an article or paper.", State.SEARCH),
    ("HELP", "See the help info.", State.HELP),
    (
        "WHAT'S NEW",
        "See the new features in our latest version.",
        State.WHATS_NEW,
    ),
    ("THANKS", "A shout-out to those who have helped.", State.THANKS),
    ("QUIT", "Return to the dancing logo screen.", State.TITLE),
]
N_MENU_OPTIONS = len(MENU_OPTIONS)

MENU_ITEM_GAP = 50
MENU_OPTIONS_PIXEL_HEIGHT = (TEXT_PIXEL_HEIGHT * N_MENU_OPTIONS) + (
    (N_MENU_OPTIONS - 1) * (MENU_ITEM_GAP - TEXT_PIXEL_HEIGHT)
)

MENU_ITEM_Y_OFFSET = (
    floor((REMAINING_MENU_Y - MENU_LOGO_PIXEL_HEIGHT) // 2)
    + MENU_LOGO_PIXEL_HEIGHT
)


MENU_OPTIONS = [
    MenuCenteredText(
        option[0],
        option[1],
        MENU_ITEM_Y_OFFSET + (i * MENU_ITEM_GAP),
        option[2],
    )
    for i, option in enumerate(MENU_OPTIONS)
]

# start with the first menu item being selected
MENU_OPTIONS[0]._selected = True


def move_main_menu_selection_up():
    """Move the selection on the main menu up."""
    if MENU_OPTIONS[0].selected:
        # do nothing if the top item is selected
        return
    for i in range(1, len(MENU_OPTIONS)):
        if MENU_OPTIONS[i].selected:
            # swapping the values because it's *~pythonic~*
            MENU_OPTIONS[i].selected, MENU_OPTIONS[i - 1].selected = (
                MENU_OPTIONS[i - 1].selected,
                MENU_OPTIONS[i].selected,
            )
            return


def move_main_menu_selection_down():
    """Move the selection on the main menu down."""
    if MENU_OPTIONS[-1].selected:
        # do nothing if the bottom item is selected
        return
    for i in range(len(MENU_OPTIONS) - 1):
        if MENU_OPTIONS[i].selected:
            MENU_OPTIONS[i].selected, MENU_OPTIONS[i + 1].selected = (
                MENU_OPTIONS[i + 1].selected,
                MENU_OPTIONS[i].selected,
            )
            return


def reset_main_menu():
    """Reset the main menu by making all but the first item unselected."""
    MENU_OPTIONS[0].selected = True
    for i in range(1, len(MENU_OPTIONS)):
        MENU_OPTIONS[i].selected = False


# thanks

# load the thanks screen text
thanks_text = _read_text_block_from_file(os.path.join(ASSETS_PATH, "thanks"))

# create wrapped thanks text
TEXT_THANKS = _create_wrapped_text_list(thanks_text)

# thanks screen title - just gonna make it match terms and conditions
THANKS_TITLE = PaddedCenteredText("THANKS", TERMS_TEXT_Y // 2 - 10)

# text for go back message - same y as accept or decline text
BACK_TEXT = CenteredText("Esc - Back", ACCEPT_OR_DECLINE.y)

# what's new

# load the what's new text
whats_new_text = _read_text_block_from_file(
    os.path.join(ASSETS_PATH, "whats-new")
)

# create wrapped what's new text
TEXT_WHATS_NEW = _create_wrapped_text_list(whats_new_text)

# what's new title
WHATS_NEW_TITLE = PaddedCenteredText("WHAT'S NEW", TERMS_TEXT_Y // 2 - 10)

# help

# load help text
help_text = _read_text_block_from_file(os.path.join(ASSETS_PATH, "help"))

# create wrapped help text
TEXT_HELP = _create_wrapped_text_list(help_text)

# help title
HELP_TITLE = PaddedCenteredText("HELP", TERMS_TEXT_Y // 2 - 10)

# search

# input title
SEARCH_TITLE = PaddedCenteredText("SEARCH", TERMS_TEXT_Y // 2 - 10)

# back text
SEARCH_BACK_TEXT = CenteredText(
    "Tab - Move || Enter - Search || Esc - Back", ACCEPT_OR_DECLINE.y
)


class Box:
    def __init__(self, x: int, y: int, width: int, height: int):
        self._x = x
        self._y = y
        self._width = width
        self._height = height

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height


# element for search screen
class SearchElement:
    def __init__(self, name: str, y: int):
        self._name = name
        self._selected = False
        self._x = SEARCH_TITLE.x

        self.outer_box = Box(
            SEARCH_TITLE.x + 2,
            y + TEXT_PIXEL_HEIGHT + 2,
            _width_of_string_in_pixels(len(SEARCH_TITLE.text)),
            TEXT_PIXEL_HEIGHT + 8,
        )
        self.inner_box = Box(
            self.outer_box.x + 2,
            self.outer_box.y + 2,
            _width_of_string_in_pixels(len(SEARCH_TITLE.text)) - 4,
            TEXT_PIXEL_HEIGHT + 4,
        )

        self._y = y
        self._content = ""

    @property
    def name(self) -> str:
        return self._name

    @property
    def selected(self) -> bool:
        return self._selected

    @selected.setter
    def selected(self, val: bool):
        self._selected = val

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def content(self) -> str:
        return self._content

    @content.setter
    def content(self, val: str):
        self._content = val

    @property
    def colour(self) -> int:
        if self._selected:
            return GREEN
        return GREY


YEAR_INPUT = SearchElement("YEAR:", 100)
SUMMARY_INPUT = SearchElement("SUMMARY:", 100)
START_SEARCH_BUTTON = SearchElement("Start Search", 200)

SEARCH_ELEMENTS = [
    YEAR_INPUT,
    SUMMARY_INPUT,
    START_SEARCH_BUTTON,
]

YEAR_INPUT.selected = True


def move_search_selection():
    """Move the selection on the search screen."""
    length = len(SEARCH_ELEMENTS)
    for i in range(length):
        if SEARCH_ELEMENTS[i].selected:
            (
                SEARCH_ELEMENTS[i].selected,
                SEARCH_ELEMENTS[(i + 1) % length].selected,
            ) = (
                SEARCH_ELEMENTS[(i + 1) % length].selected,
                SEARCH_ELEMENTS[i].selected,
            )
            return
