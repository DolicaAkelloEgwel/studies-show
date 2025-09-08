import argparse
import math
import time

import pyxel

import constants
import helpers


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
                    constants.reset_main_menu()
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

    def _draw_text(self, text: constants.PaddedCenteredText):
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
            pyxel.text(
                constants.START_TEXT.x,
                constants.START_TEXT.y,
                constants.START_TEXT.text,
                pyxel.COLOR_LIME,
                self.bedstead,
            )

        # copyright text
        pyxel.text(
            constants.COPYRIGHT_TEXT.x,
            constants.COPYRIGHT_TEXT.y,
            constants.COPYRIGHT_TEXT.text,
            pyxel.COLOR_LIME,
            self.bedstead,
        )

    def _draw_terms_and_conditions(self):

        # terms and conditions title
        pyxel.text(
            constants.TERMS_AND_CONDITIONS_TITLE.x,
            constants.TERMS_AND_CONDITIONS_TITLE.y,
            constants.TERMS_AND_CONDITIONS_TITLE.text,
            pyxel.COLOR_LIME,
            self.bedstead,
        )

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
        pyxel.text(
            constants.ACCEPT_OR_DECLINE.x,
            constants.ACCEPT_OR_DECLINE.y,
            constants.ACCEPT_OR_DECLINE.text,
            pyxel.COLOR_LIME,
            self.bedstead,
        )

    def _draw_info_screen(
        self, title: constants.PaddedCenteredText, text_block: list[str]
    ):
        # title
        pyxel.text(
            title.x,
            title.y,
            title.text,
            pyxel.COLOR_LIME,
            self.bedstead,
        )

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

    def _draw_search_screen(self):
        # title
        pyxel.text(
            constants.SEARCH_TITLE.x,
            constants.SEARCH_TITLE.y,
            constants.SEARCH_TITLE.text,
            pyxel.COLOR_LIME,
            self.bedstead,
        )

        # show the go back text
        self._draw_text(constants.BACK_TEXT)

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
