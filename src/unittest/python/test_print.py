import pytest
from unittest import TestCase

import telebot

from src.main.python.controller.util import printCurrent
from src.main.python.model import userData


class TestPrint(TestCase):
    data = userData.Data()
    print_curr = None

    def setUp(self):
        self.data.set_country("ua")
        self.data.set_city("kyiv")
        self.print_curr = printCurrent.Print(self.data)

    def test_get_forecast_should_return_correct(self):
        result = self.print_curr.get_forecast()
        assert bool(result) is True

    def test_get_forecast_should_return_incorrect(self):
        self.data.set_city("kyivvvv")
        self.print_curr = printCurrent.Print(self.data)
        result = self.print_curr.get_forecast()
        assert bool(result) is not True

    def test_check_response_should_return_correct(self):
        json_ = self.print_curr.get_forecast()
        result = self.print_curr.check_response(json_['cod'])
        assert result is True

    def test_check_response_should_return_incorrect(self):
        self.data.set_city("kyvvvv")
        result = self.print_curr.get_forecast()
        assert result is not True

    def test_print_forecast_should_return_incorrect(self):
        self.data.set_city("kyvvvv")
        result = self.print_curr.print_forecast(telebot.TeleBot, None)
        expected = False
        assert result is expected
