from src.main.python.controller.util import keys


class Data:
    country = ""
    city = ""

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city
