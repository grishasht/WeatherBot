from command import Command


class ShowTomorrow(Command):
    def execute(self, bot, message):
        bot.send_message(message.chat.id, 'Show tomorrow command!')
