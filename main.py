import argparse
import math

import pyxel

import constants


class MainMenu:
    def __init__(
        self,
        app_title: str,
        font_path: str,
        app_width: int,
        app_height: int,
        show_vline: bool,
    ):
        pyxel.init(app_width, app_height, title=app_title)

        # load retro computer-y font
        self.bedstead = pyxel.Font(font_path)

        # read the logo text
        with open("./assets/logo", "r") as f:
            logo = f.readlines()
        self._logo = logo + ["", "v8.3.4"]

        if show_vline:
            self.vline_col = pyxel.COLOR_RED
        else:
            self.vline_col = pyxel.COLOR_BLACK

        self.logo_y = constants.text_centre_y(
            constants.length_of_string(self._logo[1])
        )
        self.start_text_y = constants.text_centre_y(
            constants.length_of_string(constants.START_TEXT)
        )
        self.copyright_y = constants.text_centre_y(
            constants.length_of_string(constants.COPYRIGHT_TEXT)
        )

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(
            1024 // 2 - 1, 0, 2, 1024, self.vline_col
        )  # check for alignment
        i = 0
        for line in self._logo:
            pyxel.text(
                self.logo_y,
                41
                + (
                    (i * 20)
                    + math.sin(pyxel.frame_count * 0.125 * 0.25) * 125
                    + 100
                ),
                line,
                pyxel.COLOR_LIME,
                self.bedstead,
            )
            i += 1

        if pyxel.frame_count % 30 < 25:
            pyxel.text(
                self.start_text_y,
                768 - 120,
                constants.START_TEXT,
                pyxel.COLOR_LIME,
                self.bedstead,
            )
        pyxel.text(
            self.copyright_y,
            768 - 60,
            constants.COPYRIGHT_TEXT,
            pyxel.COLOR_LIME,
            self.bedstead,
        )


parser = argparse.ArgumentParser()
parser.add_argument("-vl", "--vline", action="store_true")
args = parser.parse_args()

MainMenu(
    constants.APP_TITLE,
    constants.FONT_PATH,
    constants.APP_WIDTH,
    constants.APP_HEIGHT,
    args.vline,
)
