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
        presenter,
    ):
        pyxel.init(app_width, app_height, title=app_title)
        self.bedstead = pyxel.Font(font_path)
        self.presenter = presenter
        with open("./logo", "r") as f:
            logo = f.readlines()
        self._text = logo + ["", "v8.3.4"]
        pyxel.run(self.update, self.draw)

    def _set_text(self, display_text: list[str]):
        self._text = display_text

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
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
            pyxel.text(0, 768 - 120, constants.CENTERED_START, 11, self.bedstead)
        pyxel.text(0, 768 - 60, constants.CENTERED_COPYRIGHT, 11, self.bedstead)
