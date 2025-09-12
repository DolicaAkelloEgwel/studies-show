import argparse
import math
import time

import pyxel

import constants
import helpers


def _check_number_press() -> str:
    if pyxel.btnp(pyxel.KEY_0):
        return "0"
    if pyxel.btnp(pyxel.KEY_1):
        return "1"
    if pyxel.btnp(pyxel.KEY_2):
        return "2"
    if pyxel.btnp(pyxel.KEY_3):
        return "3"
    if pyxel.btnp(pyxel.KEY_4):
        return "4"
    if pyxel.btnp(pyxel.KEY_5):
        return "5"
    if pyxel.btnp(pyxel.KEY_6):
        return "6"
    if pyxel.btnp(pyxel.KEY_7):
        return "7"
    if pyxel.btnp(pyxel.KEY_8):
        return "8"
    if pyxel.btnp(pyxel.KEY_9):
        return "9"

    return ""


def _check_letter_press() -> str:
    if pyxel.btnp(pyxel.KEY_A):
        return "A"
    if pyxel.btnp(pyxel.KEY_B):
        return "B"
    if pyxel.btnp(pyxel.KEY_C):
        return "C"
    if pyxel.btnp(pyxel.KEY_D):
        return "D"
    if pyxel.btnp(pyxel.KEY_E):
        return "E"
    if pyxel.btnp(pyxel.KEY_F):
        return "F"
    if pyxel.btnp(pyxel.KEY_G):
        return "G"
    if pyxel.btnp(pyxel.KEY_H):
        return "H"
    if pyxel.btnp(pyxel.KEY_I):
        return "I"
    if pyxel.btnp(pyxel.KEY_J):
        return "J"
    if pyxel.btnp(pyxel.KEY_K):
        return "K"
    if pyxel.btnp(pyxel.KEY_L):
        return "L"
    if pyxel.btnp(pyxel.KEY_M):
        return "M"
    if pyxel.btnp(pyxel.KEY_N):
        return "N"
    if pyxel.btnp(pyxel.KEY_O):
        return "O"
    if pyxel.btnp(pyxel.KEY_P):
        return "P"
    if pyxel.btnp(pyxel.KEY_Q):
        return "Q"
    if pyxel.btnp(pyxel.KEY_R):
        return "R"
    if pyxel.btnp(pyxel.KEY_S):
        return "S"
    if pyxel.btnp(pyxel.KEY_T):
        return "T"
    if pyxel.btnp(pyxel.KEY_U):
        return "U"
    if pyxel.btnp(pyxel.KEY_V):
        return "V"
    if pyxel.btnp(pyxel.KEY_W):
        return "W"
    if pyxel.btnp(pyxel.KEY_X):
        return "X"
    if pyxel.btnp(pyxel.KEY_Y):
        return "Y"
    if pyxel.btnp(pyxel.KEY_Z):
        return "Z"
    if pyxel.btnp(pyxel.KEY_SPACE):
        return " "

    if pyxel.btn(pyxel.KEY_RSHIFT) or pyxel.btn(pyxel.KEY_LSHIFT):
        if pyxel.btnp(pyxel.KEY_0):
            return ")"
        if pyxel.btnp(pyxel.KEY_1):
            return "!"
        if pyxel.btnp(pyxel.KEY_2):
            return '"'
        if pyxel.btnp(pyxel.KEY_3):
            return "£"
        if pyxel.btnp(pyxel.KEY_4):
            return "$"
        if pyxel.btnp(pyxel.KEY_5):
            return "%"
        if pyxel.btnp(pyxel.KEY_6):
            return "^"
        if pyxel.btnp(pyxel.KEY_7):
            return "&"
        if pyxel.btnp(pyxel.KEY_8):
            return "*"
        if pyxel.btnp(pyxel.KEY_9):
            return "("
        if pyxel.btnp(pyxel.KEY_MINUS):
            return "_"
        if pyxel.btnp(pyxel.KEY_EQUALS):
            return "+"
        if pyxel.btnp(pyxel.KEY_SEMICOLON):
            return ":"
        if pyxel.btnp(pyxel.KEY_QUOTE):
            return "@"
        if pyxel.btnp(pyxel.KEY_HASH):
            return "~"
        if pyxel.btnp(pyxel.KEY_COMMA):
            return "<"
        if pyxel.btnp(pyxel.KEY_PERIOD):
            return ">"
        if pyxel.btnp(pyxel.KEY_SLASH):
            return "?"
        if pyxel.btnp(pyxel.KEY_LEFTBRACKET):
            return "{"
        if pyxel.btnp(pyxel.KEY_RIGHTBRACKET):
            return "}"

    if pyxel.btnp(pyxel.KEY_MINUS):
        return "-"
    if pyxel.btnp(pyxel.KEY_EQUALS):
        return "="

    if pyxel.btnp(pyxel.KEY_LEFTBRACKET):
        return "["
    if pyxel.btnp(pyxel.KEY_RIGHTBRACKET):
        return "]"

    if pyxel.btnp(pyxel.KEY_SEMICOLON):
        return ";"
    if pyxel.btnp(pyxel.KEY_QUOTE):
        return "'"

    if pyxel.btnp(pyxel.KEY_COLON):
        return ":"
    if pyxel.btnp(pyxel.KEY_QUOTE):
        return "'"
    if pyxel.btnp(pyxel.KEY_HASH):
        return "#"

    if pyxel.btnp(pyxel.KEY_COMMA):
        return ","
    if pyxel.btnp(pyxel.KEY_PERIOD):
        return "."
    if pyxel.btnp(pyxel.KEY_SLASH):
        return "/"

    if pyxel.btnp(pyxel.KEY_BACKSLASH):
        return "\\"

    return ""


class App:

    def __init__(
        self,
        show_vline: bool,
    ):
        pyxel.init(
            constants.APP_WIDTH,
            constants.APP_HEIGHT,
            constants.APP_TITLE,
            quit_key=300,
        )
        # swap out the default green for a more "terminal" green
        pyxel.colors[pyxel.COLOR_LIME] = 0x00FF7F

        # load retro computer-y font
        self.bedstead = pyxel.Font(constants.BEDSTEAD_PATH)
        self.bold_bedstead = pyxel.Font(constants.BOLD_BEDSTEAD_PATH)

        # set colour for vertical centre line
        self.vline_col = constants.get_vline_colour(show_vline)

        # determine x-values for text
        self.logo_x = constants.text_centre_x(constants.LOGO[1])

        # set initial state
        self._state = constants.State.TITLE

        # start timer
        self.start_time = None

        pyxel.run(self.update, self.draw)

    def _idle_limit(self):
        return time.time() - self.start_time >= constants.IDLE_LIMIT

    def _restart_timer(self):
        self.start_time = time.time()

    def _update_title(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self._restart_timer()
            self._state = constants.State.TERMS_AND_CONDITIONS

    def _update_terms_and_conditions(self):
        if pyxel.btnp(pyxel.KEY_A):
            self._restart_timer()
            self._state = constants.State.MAIN_MENU
        elif pyxel.btnp(pyxel.KEY_D):
            self._state = constants.State.TITLE
        elif self._idle_limit():
            self._state = constants.State.TITLE

    def _update_main_menu(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            for item in constants.MENU_OPTIONS:
                if item.selected:
                    self._state = item.new_state
                    return
        elif pyxel.btnp(pyxel.KEY_UP):
            self._restart_timer()
            constants.move_main_menu_selection_up()
        elif pyxel.btnp(pyxel.KEY_DOWN):
            self._restart_timer()
            constants.move_main_menu_selection_down()
        elif self._idle_limit():
            constants.reset_main_menu()
            self._state = constants.State.TITLE

    def _update_info_screen(self):
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self._restart_timer()
            self._state = constants.State.MAIN_MENU
        elif self._idle_limit():
            self._restart_timer()
            constants.reset_main_menu()
            self._state = constants.State.TITLE

    def _update_search(self):

        if pyxel.btnp(pyxel.KEY_ESCAPE):
            self._restart_timer()
            self._state = constants.State.MAIN_MENU

        if pyxel.btnp(pyxel.KEY_TAB):
            self._restart_timer()
            constants.move_search_selection()

        if constants.YEAR_INPUT.selected:

            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                self._restart_timer()
                constants.YEAR_INPUT.backspace()

            num = _check_number_press()
            if num:
                self._restart_timer()
                constants.YEAR_INPUT.add_char(num)

        elif constants.SUMMARY_INPUT.selected:
            if pyxel.btnp(pyxel.KEY_BACKSPACE):
                self._restart_timer()
                constants.SUMMARY_INPUT.backspace()
                return

            char = _check_letter_press()
            num = _check_number_press()

            if char:
                self._restart_timer()
                constants.SUMMARY_INPUT.add_char(char)
            elif num:
                self._restart_timer()
                constants.SUMMARY_INPUT.add_char(num)

        elif constants.START_SEARCH_BUTTON.selected:
            pass

        if self._idle_limit():
            self._restart_timer()
            constants.clear_search_inputs()
            constants.reset_main_menu()
            self._state = constants.State.TITLE

    def update(self):
        if self._state == constants.State.TITLE:
            self._update_title()
        elif self._state == constants.State.TERMS_AND_CONDITIONS:
            self._update_terms_and_conditions()
        elif self._state == constants.State.MAIN_MENU:
            self._update_main_menu()
        elif self._state in [
            constants.State.THANKS,
            constants.State.WHATS_NEW,
            constants.State.HELP,
        ]:
            self._update_info_screen()
        elif self._state == constants.State.SEARCH:
            self._update_search()

    def _draw_text(self, text: constants.CenteredText):
        pyxel.text(
            text.x,
            text.y,
            text.text,
            pyxel.COLOR_LIME,
            self.bedstead,
        )

    def _draw_title_screen(self):
        # draw the logo text
        for i, line in enumerate(constants.LOGO):
            pyxel.text(
                self.logo_x,
                41
                + (
                    (i * constants.TEXT_PIXEL_HEIGHT)
                    + math.sin(pyxel.frame_count * 0.125 * 0.25) * 125
                    + 100
                ),
                line,
                pyxel.COLOR_LIME,
                self.bedstead,
            )

        # make the start text flash
        if helpers.flash_text(pyxel.frame_count):
            self._draw_text(constants.START_TEXT)

        # copyright text
        self._draw_text(constants.COPYRIGHT_TEXT)

    def _draw_terms_and_conditions(self):

        # terms and conditions title
        self._draw_text(constants.TERMS_AND_CONDITIONS_TITLE)

        # display the lines from the terms and conditions text
        for i, line in enumerate(constants.TEXT_TERMS_AND_CONDITIONS):
            pyxel.text(
                constants.BORDER_TEXT_BLOCK,
                constants.TERMS_TEXT_Y + i * constants.TEXT_PIXEL_HEIGHT,
                line,
                pyxel.COLOR_LIME,
                self.bedstead,
            )

        # display the accept or decline text at the bottom
        self._draw_text(constants.ACCEPT_OR_DECLINE)

    def _draw_info_screen(
        self, title: constants.PaddedCenteredText, text_block: list[str]
    ):
        # title
        self._draw_text(title)

        # display the lines from the text block
        for i, line in enumerate(text_block):
            pyxel.text(
                constants.BORDER_TEXT_BLOCK,
                constants.TERMS_TEXT_Y + i * constants.TEXT_PIXEL_HEIGHT,
                line,
                pyxel.COLOR_LIME,
                self.bedstead,
            )

        # show the go back text
        self._draw_text(constants.BACK_TEXT)

    def _draw_main_menu(self):

        for i, line in enumerate(constants.LOGO):
            # draw the logo at the top of the menu screen
            pyxel.text(
                self.logo_x,
                constants.MENU_LOGO_Y + (i * constants.TEXT_PIXEL_HEIGHT),
                line,
                pyxel.COLOR_LIME,
                self.bedstead,
            )

        for item in constants.MENU_OPTIONS:
            if item.selected:
                # if an item is selected then draw a rectangle behind it
                pyxel.rect(
                    0, item.y - 16, constants.APP_WIDTH, 50, pyxel.COLOR_LIME
                )
                # show a description of this menu item near the bottom
                pyxel.text(
                    item.description_x,
                    constants.APP_HEIGHT - constants.MENU_DESCRIPTION_OFFSET,
                    item.description_text,
                    pyxel.COLOR_LIME,
                    self.bedstead,
                )
            # show the menu item text
            pyxel.text(item.x, item.y, item.text, item.color, self.bedstead)

    def _draw_search_input_field(self, input_field: constants.SearchElement):

        # year input text
        pyxel.text(
            input_field.x,
            input_field.y,
            input_field.name,
            input_field.colour,
            self.bedstead,
        )

        pyxel.rect(
            input_field.outer_box.x,
            input_field.outer_box.y,
            input_field.outer_box.width,
            input_field.outer_box.height,
            input_field.colour,
        )
        pyxel.rect(
            input_field.inner_box.x,
            input_field.inner_box.y,
            input_field.inner_box.width,
            input_field.inner_box.height,
            pyxel.COLOR_BLACK,
        )
        pyxel.text(
            input_field.inner_box.x + 2,
            input_field.inner_box.y + 2,
            input_field.content,
            input_field.colour,
            self.bedstead,
        )

    def _draw_search_screen(self):
        # title
        self._draw_text(constants.SEARCH_TITLE)

        # year input text
        self._draw_search_input_field(constants.YEAR_INPUT)

        # summary input text
        self._draw_search_input_field(constants.SUMMARY_INPUT)

        pyxel.rect(
            constants.START_SEARCH_BUTTON.outer_box.x,
            constants.START_SEARCH_BUTTON.outer_box.y,
            constants.START_SEARCH_BUTTON.outer_box.width,
            constants.START_SEARCH_BUTTON.outer_box.height,
            constants.START_SEARCH_BUTTON.colour,
        )
        pyxel.rect(
            constants.START_SEARCH_BUTTON.middle_box.x,
            constants.START_SEARCH_BUTTON.middle_box.y,
            constants.START_SEARCH_BUTTON.middle_box.width,
            constants.START_SEARCH_BUTTON.middle_box.height,
            pyxel.COLOR_BLACK,
        )
        pyxel.rect(
            constants.START_SEARCH_BUTTON.inner_box.x,
            constants.START_SEARCH_BUTTON.inner_box.y,
            constants.START_SEARCH_BUTTON.inner_box.width,
            constants.START_SEARCH_BUTTON.inner_box.height,
            constants.START_SEARCH_BUTTON.colour,
        )

        pyxel.text(
            constants.START_SEARCH_BUTTON.text_x,
            constants.START_SEARCH_BUTTON.text_y,
            "START SEARCH",
            pyxel.COLOR_BLACK,
            self.bedstead,
        )

        # show the go back text
        self._draw_text(constants.SEARCH_BACK_TEXT)

    def draw(self):
        # clear screen
        pyxel.cls(pyxel.COLOR_BLACK)

        # draw the centre line
        pyxel.rect(
            constants.HALF_APP_WIDTH - 1,
            0,
            2,
            constants.APP_WIDTH,
            self.vline_col,
        )

        if self._state == constants.State.TITLE:
            self._draw_title_screen()
        elif self._state == constants.State.TERMS_AND_CONDITIONS:
            self._draw_terms_and_conditions()
        elif self._state == constants.State.MAIN_MENU:
            self._draw_main_menu()
        elif self._state == constants.State.THANKS:
            self._draw_info_screen(
                constants.THANKS_TITLE, constants.TEXT_THANKS
            )
        elif self._state == constants.State.WHATS_NEW:
            self._draw_info_screen(
                constants.WHATS_NEW_TITLE, constants.TEXT_WHATS_NEW
            )
        elif self._state == constants.State.HELP:
            self._draw_info_screen(constants.HELP_TITLE, constants.TEXT_HELP)
        elif self._state == constants.State.SEARCH:
            self._draw_search_screen()


parser = argparse.ArgumentParser()
parser.add_argument("-vl", "--vline", action="store_true")
args = parser.parse_args()

App(
    args.vline,
)
