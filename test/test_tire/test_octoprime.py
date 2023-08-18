import unittest
from model.tire.octoprime import Octoprime


class TestOctoprime(unittest.TestCase):
    def needsServiceTrue(self):
        sensor = [0.7, 0.9, 0.9, 0.8]
        tire = Octoprime(sensor=sensor)
        self.assertTrue(tire.needsService())

    def needsServiceFalse(self):
        sensor = [0.7, 0.9, 0.9, 0.8]
        tire = Octoprime(sensor=sensor)
        self.assertFalse(tire.needsService())
