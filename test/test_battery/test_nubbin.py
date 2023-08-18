import unittest
from datetime import date

from model.battery.nubbin import Nubbin


class TestNubbin(unittest.TestCase):
    def testNeedsServiceTrue(self):
        current_date = date.fromisoformat("2023-11-21")
        last_service_date = date.fromisoformat("2017-08-12")
        battery = Nubbin(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date.fromisoformat("2023-01-15")
        last_service_date = date.fromisoformat("2022-04-10")
        battery = Nubbin(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
