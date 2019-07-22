from datetime import datetime

import requests

from src.main.python.controller.util import keys


class Print():
    data = None
    api_key = keys.get_key(
        '/home/hs/PycharmProjects/WeatherBot/docs/api_key.txt')

    def __init__(self, data):
        self.data = data

    def get_forecast(self):
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' \
              + self.data.get_city() + ',' + \
              self.data.get_country() + '&APPID=' + self.api_key
        r = requests.get(url)
        print(url)
        json_file = r.json()
        is_correct = self.check_response(json_file['cod'])
        if is_correct:
            return json_file
        else:
            return False

    def check_response(self, code):
        return True if 200 == code else False

    def print_forecast(self, bot, message):
        json = self.get_forecast()
        if json:
            weather = json['weather'][0]
            main = json['main']
            wind = json['wind']
            _time, local_time = self.utc_to_local(json['dt'], json)
            out = json['sys']['country'] + ", " + json['name'] + "\n"
            bot.send_message(message.chat.id, out)
            out = "Weather for the current moment\n"
            out += "Time: " + str(local_time.hour) \
                   + ":" + str(local_time.minute) + '\n'
            out += "Time (local): " + str(_time.hour) \
                   + ":" + str(_time.minute) + '\n\n'
            out += "Weather: " + weather['description'] + '\n'
            out += "Current temperature: " + \
                   str(round(main['temp'] - 273.15)) + ', \u2103\n'
            out += "Min temperature: " + \
                   str(round(main['temp_min'] - 273.15)) + ', \u2103\n'
            out += "Max temperature: " + \
                   str(round(main['temp_max'] - 273.15)) + ', \u2103\n'
            out += "Speed of wind: " + str(wind['speed']) + ', m/sec'
            bot.send_message(message.chat.id, out)

            return True
        else:
            if message is not None:
                bot.send_message(message.chat.id,
                                 'The city name is incorrect!'
                                 '\nTry again')
            return False

    def utc_to_local(self, utc_datetime, json):
        local_time = datetime.utcfromtimestamp(utc_datetime + json['timezone'])
        _time = datetime.fromtimestamp(utc_datetime)
        return _time, local_time
