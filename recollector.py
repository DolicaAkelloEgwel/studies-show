import pyxel


class App:
    def __init__(self, app_title: str, font_path: str):
        pyxel.init(800, 600, title=app_title)
        self.bedstead = pyxel.Font(font_path)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "ЯECOLLECTOЯ v 8.3.4", 11, self.bedstead)
        pyxel.text(55, 81, "[rec@cth] ENTER PASSWORD:", 11, self.bedstead)
