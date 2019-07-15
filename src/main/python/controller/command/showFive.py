from src.main.python.controller.command.command import Command


class ShowFive(Command):
    def execute(self, bot, message):
        bot.send_message(message.chat.id, 'Show three command!')
