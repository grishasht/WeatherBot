import telebot
import src.main.python.controller.util.keys as tkn

from src.main.python.controller.command \
    import help, start, showToday, chooseLocation, showFive

bot = telebot.TeleBot(tkn.get_key('docs/token.txt'))

commands = {
    '/help': help.Help(bot),
    '/start': start.Start(bot),
    '/show_today': showToday.ShowToday(),
    '/show_five': showFive.ShowFive(bot),
    '/choose_location': chooseLocation.ChooseLocation()
}


@bot.message_handler(content_types=['text'])
def handle_messages(message):
    try:
        commands[message.text].execute(bot, message)
    except Exception:
        bot.send_message(message.chat.id, 'Sorry, you entered wrong command!')


bot.polling(none_stop=True, interval=0)
