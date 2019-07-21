import unittest
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
        self.assertEqual(True, bool(result))

    def test_get_forecast_should_return_incorrect(self):
        self.data.set_city("kyivvvv")
        self.print_curr = printCurrent.Print(self.data)
        result = self.print_curr.get_forecast()
        self.assertNotEqual(True, bool(result))

    def test_check_response_should_return_correct(self):
        json_ = self.print_curr.get_forecast()
        result = self.print_curr.check_response(json_['cod'])
        self.assertEqual(True, result)

    def test_check_response_should_return_incorrect(self):
        self.data.set_city("kyvvvv")
        result = self.print_curr.get_forecast()
        self.assertNotEqual(True, result)

    @unittest.expectedFailure
    def test_print_forecast_should_return_incorrect(self):
        result = self.print_curr.print_forecast(telebot.AsyncTeleBot, None)
        self.assertEqual(Exception, result)
