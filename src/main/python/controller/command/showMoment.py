from src.main.python.controller.command.chooseLocation import ChooseLocation
from src.main.python.controller.command.command import Command
from src.main.python.controller.util.printCurrent import Print


class ShowMoment(Command):
    printOne = None

    def __init__(self, b):
        super().__init__(b)
        self.printOne = Print(self.data)

    def execute(self, bot, message):
        if self.data.get_city() != "":
            self.printOne.print_forecast(bot, message)
        else:
            ChooseLocation(bot).execute(bot, message)
            self.printOne.print_forecast(bot, message)
