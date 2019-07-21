from src.main.python.controller.command.command import Command


class ChooseLocation(Command):

    def __init__(self, b):
        super().__init__(b)

    def execute(self, bot, message):
        self.bot.send_message(message.chat.id, "Enter country\nExample: Ukraine or UA")
        self.bot.register_next_step_handler(message, self.get_country)

    def get_country(self, message):
        self.data.set_country(message.text)
        self.bot.send_message(message.chat.id, "Now enter city")
        self.bot.register_next_step_handler(message, self.get_city)

    def get_city(self, message):
        self.data.set_city(message.text)
        self.bot.send_message(message.chat.id, "New location chosen!")
