from src.main.python.controller.command.command import Command


class Help(Command):
    def execute(self, bot, message):
        bot.send_message(message.chat.id, 'Help command!')
