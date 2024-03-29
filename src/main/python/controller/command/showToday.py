from src.main.python.controller.command.command import Command
from src.main.python.controller.util.printOneDay import Print


class ShowToday(Command):

    printOne = None

    def __init__(self, b):
        super().__init__(b)
        self.printOne = Print(self.data)

    def execute(self, bot, message):
        bot.send_message(message.chat.id, 'Today\'s forecast')
        self.printOne.print_forecast(bot, message)
