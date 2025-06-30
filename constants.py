import os

APP_TITLE = "ЯECOLLECTOR v8.3.4"
COMMANDS = ("search", "t-and-c", "help", "whats-new", "thanks")
BLOCK_CHARACTER = "█"
FONT_PATH = os.path.join("assets", "bedstead-20.bdf")
LINE_Y_DISTANCE = 20
TOP_LINE_Y = 40

APP_WIDTH = 1024
APP_HEIGHT = 768


def length_of_string(text: str) -> int:
    n = len(text)
    return n * 10 + (n - 1) * 2


def text_centre_x(string_length: int) -> int:
    return APP_WIDTH // 2 - string_length // 2 - 2


START_TEXT = "[PRESS ANY KEY TO START]"
COPYRIGHT_TEXT = "(C) 2025 GRAVE MATTER"
