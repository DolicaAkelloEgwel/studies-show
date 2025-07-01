import argparse

import pyxel

import constants
from start_screen import StartScreen


class App:
    def __init__(self, vline: bool):

        pyxel.init(
            constants.APP_WIDTH,
            constants.APP_HEIGHT,
            title=constants.APP_TITLE,
        )

        self.start_screen = StartScreen(vline)
        self.terms_and_conditions = None

    def update(self):
        pass

    def draw(self):
        if self._show_start_screen:
            self.start_screen.draw()


parser = argparse.ArgumentParser()
parser.add_argument("-vl", "--vline", action="store_true")
args = parser.parse_args()

App(
    args.vline,
)
