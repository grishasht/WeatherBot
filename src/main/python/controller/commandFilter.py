import os

import telebot
from flask import request, Flask

from src.main.python.controller.command \
    import help, start, showToday, chooseLocation, showFive, showMoment

token = "858880474:AAG6FSp0jmrcbdlglJJ9LFCarOtvds7wYF8"
bot = telebot.TeleBot(token)
server = Flask(__name__)
# tkn.get_key('docs/token.txt')

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


@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegram--weather-bot.com/' + token)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
