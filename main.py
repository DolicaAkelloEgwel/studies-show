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
            constants.APP_WIDTH, constants.APP_HEIGHT, constants.APP_TITLE
        )

        # load retro computer-y font
        self.bedstead = pyxel.Font(constants.FONT_PATH)

        # set colour for vertical centre line
        self.vline_col = constants.get_vline_colour(show_vline)

        # determine x-values for text
        self.logo_x = constants.text_centre_x(constants.LOGO[1])
        self.start_text_x = constants.text_centre_x(constants.START_TEXT)
        self.copyright_x = constants.text_centre_x(constants.COPYRIGHT_TEXT)
        self.t_and_c_title_x = constants.text_centre_x(
            constants.TERMS_AND_CONDITIONS_TITLE
        )

        self._state = State.TITLE

        pyxel.run(self.update, self.draw)

    def _update_title(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self._state = State.TERMS_AND_CONDITIONS

    def _update_terms_and_conditions(self):
        pass

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
                    (i * constants.LINE_Y_DISTANCE)
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
                self.start_text_x,
                constants.START_TEXT_Y,
                constants.START_TEXT,
                pyxel.COLOR_LIME,
                self.bedstead,
            )

        # copyright text
        pyxel.text(
            self.copyright_x,
            constants.COPYRIGHT_TEXT_Y,
            constants.COPYRIGHT_TEXT,
            pyxel.COLOR_LIME,
            self.bedstead,
        )

    def _draw_terms_and_conditions(self):

        # terms and conditions title
        pyxel.text(
            self.t_and_c_title_x,
            20,
            constants.TERMS_AND_CONDITIONS_TITLE,
            pyxel.COLOR_LIME,
            self.bedstead,
        )

        for i, line in enumerate(constants.TERMS_AND_CONDITIONS_TEXT):
            pyxel.text(
                20,
                60 + i * constants.LINE_Y_DISTANCE,
                line,
                pyxel.COLOR_LIME,
                self.bedstead,
            )

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
