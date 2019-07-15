from src.main.python.controller.command.command import Command
import os


class Help(Command):
    def execute(self, bot, message):
        file_path = ""
        file = open(os.path.join(file_path, 'docs', 'help.txt'), 'r')
        bot.send_message(message.chat.id, file.read())
        file.close()
