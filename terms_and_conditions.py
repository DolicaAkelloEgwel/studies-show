import pyxel

import constants


class TermsAndConditions:
    def __init__(
        self,
        show_vline: bool,
    ):
        # load retro computer-y font
        self.bedstead = pyxel.Font(constants.FONT_PATH)

        # set colour for vertical centre line
        self.vline_col = constants.get_vline_colour(show_vline)

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

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

        # copyright text
        pyxel.text(
            22,
            constants.COPYRIGHT_TEXT_Y,
            "TERMS AND CONDITIONS",
            pyxel.COLOR_LIME,
            self.bedstead,
        )
