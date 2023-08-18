import unittest

from model.engine.sternman import Sternman


class TestSternmanEngine(unittest.TestCase):
    def test_needs_service_true(self):
        warning_light_is_on = True
        engine = Sternman(warning_light_is_on)
        self.assertTrue(engine.needsService())

    def test_needs_service_false(self):
        warning_light_is_on = False
        engine = Sternman(warning_light_is_on)
        self.assertFalse(engine.needsService())
