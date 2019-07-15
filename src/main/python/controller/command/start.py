import requests

from src.main.python.controller.command.command import Command


class Start(Command):

    def __init__(self, b):
        super().__init__(b)

    def execute(self, bot, message):
        self.bot.send_message(message.chat.id, "Enter country\nExample: Ukraine or UA")
        self.bot.register_next_step_handler(message, self.get_country)

    def get_country(self, message):
        self.country = message.text
        self.bot.send_message(message.chat.id, "Now enter city")
        self.bot.register_next_step_handler(message, self.get_city)

    def get_city(self, message):
        self.city = message.text
        is_temp = self.get_forecast()
        if is_temp:
            self.bot.send_message(message.chat.id, is_temp)
        else:
            self.bot.send_message(message.chat.id, 'Country or city name is incorrect!'
                                                   '\nTry again')
            self.execute(self.bot, message)

    def get_forecast(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='
                         + self.city + ',' + self.country + '&APPID='
                         + self.api_key)
        json_file = r.json()
        is_correct = self.check_response(json_file['cod'])
        if is_correct:
            temp___ = json_file['main']['temp'] - 273.15
            return round(temp___)
        else:
            return False

    def check_response(self, code):
        return True if 200 == code else False
