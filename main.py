from constants import APP_TITLE, FONT_PATH
from recollector import App


class Presenter:

    def __init__(self):
        self.view = App(APP_TITLE, FONT_PATH, self)
        self.view._set_text([APP_TITLE, ">"])


Presenter()
