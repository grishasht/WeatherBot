import requests

from src.main.python.controller.util import keys, printCurrent
from datetime import datetime


class Print:
    data = None
    # api_key = keys.get_key('docs/api_key.txt')
    api_key = "08e3367a0319ad170280b418c668700f"

    def __init__(self, data):
        self.data = data

    def get_forecast(self):
        r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=' +
                         self.data.get_city() + ',' + self.data.get_country() +
                         '&APPID=' + self.api_key)
        json_file = r.json()
        is_correct = self.check_response(json_file['cod'])
        if is_correct:
            return json_file
        else:
            return False

    def check_response(self, code):
        return True if '200' == code else False

    def print_forecast(self, bot, message):
        json = self.get_forecast()
        if json:
            i = 0
            list_ = json['list']
            timezone = json['city']['timezone']
            local_time, _time = self.utc_to_local(list_[i]['dt'], timezone)
            curr = printCurrent.Print(self.data)
            curr.print_forecast(bot, message)
            while i < len(list_):
                local_time, _time = self.utc_to_local(list_[i]['dt'], timezone)
                out = "Date: " + local_time.strftime("%d.%d; %H:%M") + '\n'
                out += "Date (local): " + \
                       _time.strftime("%d.%d; %H:%M") + '\n\n'
                weather = list_[i]['weather'][0]
                out += "Weather: " + weather['description'] + '\n'
                main_ = list_[i]['main']
                out += "Current temperature: " + \
                       str(round(main_['temp'] - 273.15)) + ', \u2103\n'
                main_ = list_[i]['main']
                out += "Min temperature: " + \
                       str(round(main_['temp_min'] - 273.15)) + ', \u2103\n'
                main_ = list_[i]['main']
                out += "Max temperature: " + \
                       str(round(main_['temp_max'] - 273.15)) + ', \u2103\n'
                wind = list_[i]['wind']
                out += "Speed of wind: " + str(wind['speed']) + ', m/sec'
                bot.send_message(message.chat.id, out)

                i = i + 1
            return True
        else:
            bot.send_message(message.chat.id,
                             'Country or city name is incorrect!'
                             '\nTry again')
            return False

    def utc_to_local(self, utc_datetime, timezone):
        local_time = datetime.utcfromtimestamp(utc_datetime + timezone)
        _time = datetime.fromtimestamp(utc_datetime)
        return _time, local_time
