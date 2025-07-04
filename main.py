import argparse
import math
from enum import Enum

import pyxel

import constants
import helpers


class State(Enum):
    TITLE = 1
    TERMS_AND_CONDITIONS = 2
    TERMINAL = 3


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
        self._state = State.TITLE

        pyxel.run(self.update, self.draw)

    def _update_title(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self._state = State.TERMS_AND_CONDITIONS

    def _update_terms_and_conditions(self):
        if pyxel.btnp(pyxel.KEY_A):
            self._state = State.TERMINAL
        if pyxel.btnp(pyxel.KEY_D):
            self._state = State.TITLE

    def _update_terminal(self):
        pass

    def update(self):
        if self._state == State.TITLE:
            self._update_title()
        elif self._state == State.TERMS_AND_CONDITIONS:
            self._update_terms_and_conditions()
        elif self._state == State.TERMINAL:
            self._update_terminal()

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
                constants.BORDER_TERMS_AND_CONDITIONS,
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

    def _draw_recollector_terminal(self):
        pass

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

        if self._state == State.TITLE:
            self._draw_title_screen()
        elif self._state == State.TERMS_AND_CONDITIONS:
            self._draw_terms_and_conditions()
        elif self._state == State.TERMINAL:
            self._draw_recollector_terminal()


parser = argparse.ArgumentParser()
parser.add_argument("-vl", "--vline", action="store_true")
args = parser.parse_args()

App(
    args.vline,
)
