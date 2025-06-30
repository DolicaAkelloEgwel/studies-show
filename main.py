import argparse
import math

import pyxel

import constants


class App:
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
        self._text = logo + ["", "v8.3.4"]

        if show_vline:
            self.vline_col = 8
        else:
            self.vline_col = 0

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
        for line in self._text:
            pyxel.text(
                55,
                41
                + (
                    (i * 20)
                    + math.sin(pyxel.frame_count * 0.125 * 0.25) * 125
                    + 100
                ),
                line,
                11,
                self.bedstead,
            )

            i += 1
        if pyxel.frame_count % 30 < 25:
            pyxel.text(
                constants.text_centre_y(
                    constants.length_of_string(constants.START_TEXT)
                ),
                768 - 120,
                constants.START_TEXT,
                11,
                self.bedstead,
            )
        pyxel.text(
            constants.text_centre_y(
                constants.length_of_string(constants.COPYRIGHT_TEXT)
            ),
            768 - 60,
            constants.COPYRIGHT_TEXT,
            11,
            self.bedstead,
        )


parser = argparse.ArgumentParser()
parser.add_argument("-vl", "--vline", action="store_true")
args = parser.parse_args()

App(
    constants.APP_TITLE,
    constants.FONT_PATH,
    constants.APP_WIDTH,
    constants.APP_HEIGHT,
    args.vline,
)
