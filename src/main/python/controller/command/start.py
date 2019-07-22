import telebot

from src.main.python.controller.command.command import Command
from src.main.python.controller.util.printOneDay import Print

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Current', 'Following day')
keyboard1.row('5 days', 'Change location')


class Start(Command):
    printOne = None

    def __init__(self, b):
        super().__init__(b)
        self.printOne = Print(self.data)

    def execute(self, bot, message):
        self.bot.send_message(message.chat.id,
                              "Enter country\nExample: Ukraine or UA",
                              reply_markup=keyboard1)
        self.bot.register_next_step_handler(message, self.get_country)

    def get_country(self, message):
        self.data.set_country(message.text)
        self.bot.send_message(message.chat.id, "Now enter city")
        self.bot.register_next_step_handler(message, self.get_city)

    def get_city(self, message):
        self.data.set_city(message.text)
        is_print = self.printOne.print_forecast(self.bot, message)
        if not is_print:
            self.execute(self.bot, message)
