import unittest
from model.tire.carrigan import Carrigan


class CarriganTest(unittest.TestCase):
    def needsServiceTrue(self):
        sensor = [0.1, 0.9, 0.3, 0.4]
        tire = Carrigan(sensor=sensor)
        self.assertTrue(tire.needsService())

    def needsServiceFalse(self):
        sensor = [0.1, 0.6, 0.8, 0.3]
        tire = Carrigan(sensor=sensor)
        self.assertFalse(tire.needsService())
