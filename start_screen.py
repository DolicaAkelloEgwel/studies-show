import math

import pyxel

import constants


class StartScreen:
    def __init__(
        self,
        show_vline: bool,
    ):
        # load retro computer-y font
        self.bedstead = pyxel.Font(constants.FONT_PATH)

        # set colour for vertical centre line
        self.vline_col = constants.get_vline_colour(show_vline)

        # determine x-values for text
        self.logo_x = constants.text_centre_x(constants.LOGO[1])
        self.start_text_x = constants.text_centre_x(constants.START_TEXT)
        self.copyright_x = constants.text_centre_x(constants.COPYRIGHT_TEXT)

        pyxel.run(self.update, self.draw)

    def update(self):
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
        if constants.show_25_frames(pyxel.frame_count):
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
