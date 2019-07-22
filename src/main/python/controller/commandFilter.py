import time

import telebot
import src.main.python.controller.util.keys as tkn
from telegram.ext import Updater, CommandHandler, \
    MessageHandler, Filters, InlineQueryHandler, Dispatcher

from src.main.python.controller.command \
    import help, start, showToday, chooseLocation, showFive, showMoment

bot = telebot.TeleBot(tkn.get_key('docs/token.txt'))

commands = {
    '/help': help.Help(bot),
    '/start': start.Start(bot),
    '/show_curr': showMoment.ShowMoment(bot),
    'Current': showMoment.ShowMoment(bot),
    '/show_today': showToday.ShowToday(bot),
    'Following day': showToday.ShowToday(bot),
    '/show_five': showFive.ShowFive(bot),
    '5 days': showFive.ShowFive(bot),
    '/choose_location': chooseLocation.ChooseLocation(bot),
    'Change location': chooseLocation.ChooseLocation(bot)
}

msg = None


def get_msg():
    return msg


def get_chat_id():
    return msg.chat.id


@bot.message_handler(content_types=['text'])
def handle_messages(message):
    try:
        msg = message
        print(message.chat.id)
        commands[message.text].execute(bot, message)
    except Exception:
        bot.send_message(message.chat.id,
                         'Sorry, you entered wrong command!')


# @bot.add_channel_post_handler()
# dp = Dispatcher(bot)
#
# dp.add_handler(MessageHandler("text"))

# while True:
#     try:
#         bot.polling(none_stop=True, interval=0)
#     except Exception as e:
#         print(e)
#         time.sleep(15)
