from command import Command


class ShowToday(Command):
    def execute(self, bot, message):
        bot.send_message(message.chat.id, 'Show today command!')
