from src.main.python.controller.command.command import Command
from src.main.python.controller.util.printFiveDays import Print


class ShowFive(Command):
    printFive = None

    def __init__(self, b):
        super().__init__(b)
        self.printFive = Print(self.data)

    def execute(self, bot, message):
        bot.send_message(message.chat.id, 'Show three command!')
        self.printFive.print_forecast(bot, message)
