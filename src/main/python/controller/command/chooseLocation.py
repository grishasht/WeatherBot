from command import Command


class ChooseLocation(Command):
    def execute(self, bot, message):
        bot.send_message(message.chat.id, 'Choose location command!')
