from src.main.python.controller.util import keys


class Command:
    bot = None
    api_key = keys.get_key('docs/api_key.txt')

    def __init__(self, b):
        self.bot = b

    def execute(self, bot, message):
        pass
