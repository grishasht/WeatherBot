from src.main.python.controller.command.command import Command


class Start(Command):
    def execute(self, bot, message):
       bot.send_message(message.chat.id, 'Start command!')