import telebot
import src.main.python.controller.token as tkn

from src.main.python.controller.command \
    import help, start, showToday, showTomorrow, chooseLocation, showThree, showWeek

bot = telebot.TeleBot(tkn.get_token('token.txt'))

commands = {
    '/help': help.Help(),
    '/start': start.Start(),
    '/show_today': showToday.ShowToday(),
    '/show_tomorrow': showTomorrow.ShowTomorrow(),
    '/show_three': showThree.ShowThree(),
    '/show_week': showWeek.ShowWeek(),
    '/choose_location': chooseLocation.ChooseLocation()
}


@bot.message_handler(content_types=['text'])
def handle_messages(message):
    try:
        commands[message.text].execute(bot, message)
    except Exception:
        bot.send_message(message.chat.id, 'Sorry, you entered wrong command!')


bot.polling(none_stop=True, interval=0)
