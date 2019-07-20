from src.main.python.controller.util import keys
from src.main.python.model.userData import Data


class Command:
    bot = None
    data = Data()

    def __init__(self, b):
        self.bot = b

    def execute(self, bot, message):
        pass
