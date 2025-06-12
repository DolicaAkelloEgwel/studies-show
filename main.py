from constants import APP_HEIGHT, APP_TITLE, APP_WIDTH, FONT_PATH
from recollector import App


class Presenter:

    def __init__(self):
        self.view = App(APP_TITLE, FONT_PATH, APP_WIDTH, APP_HEIGHT, self)


Presenter()
