from model.engine.capulet import Capulet
import unittest


class TestCapulet(unittest.TestCase):
    def needsServiceTrue(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = Capulet(current_mileage, last_service_mileage)
        self.assertTrue(engine.needsService())

    def needsServiceFalse(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = Capulet(current_mileage, last_service_mileage)
        self.assertFalse(engine.needsService())
