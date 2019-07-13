from src.main.python.controller.command.command import Command


class ShowThree(Command):
    def execute(self, bot, message):
        bot.send_message(message.chat.id, 'Show three command!')
