import unittest
from datetime import date

from model.battery.spindler import Spindler


class TestSpindlerBattery(unittest.TestCase):
    def test_needs_service_true(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2018-01-25")
        battery = Spindler(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2020-05-15")
        last_service_date = date.fromisoformat("2019-03-10")
        battery = Spindler(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
