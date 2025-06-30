import argparse
import math

import pyxel

import constants


class MainMenu:
    def __init__(
        self,
        show_vline: bool,
    ):
        pyxel.init(
            constants.APP_WIDTH,
            constants.APP_HEIGHT,
            title=constants.APP_TITLE,
        )

        # load retro computer-y font
        self.bedstead = pyxel.Font(constants.FONT_PATH)

        # set colour for vertical centre line
        self.vline_col = constants.get_vline_colour(show_vline)

        # determine x-values for text
        self.logo_x = constants.text_centre_x(
            constants.length_of_string(constants.LOGO[1])
        )
        self.start_text_x = constants.text_centre_x(
            constants.length_of_string(constants.START_TEXT)
        )
        self.copyright_x = constants.text_centre_x(
            constants.length_of_string(constants.COPYRIGHT_TEXT)
        )

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)

        # draw the centre line
        pyxel.rect(511, 0, 2, constants.APP_WIDTH, self.vline_col)

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
        if pyxel.frame_count % 30 < 25:
            pyxel.text(
                self.start_text_x,
                768 - 120,
                constants.START_TEXT,
                pyxel.COLOR_LIME,
                self.bedstead,
            )

        # copyright text
        pyxel.text(
            self.copyright_x,
            768 - 60,
            constants.COPYRIGHT_TEXT,
            pyxel.COLOR_LIME,
            self.bedstead,
        )


parser = argparse.ArgumentParser()
parser.add_argument("-vl", "--vline", action="store_true")
args = parser.parse_args()

MainMenu(
    args.vline,
)
