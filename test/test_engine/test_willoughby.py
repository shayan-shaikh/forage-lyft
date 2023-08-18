from model.engine.willoughby import Willoughby
import unittest


class TestCapulet(unittest.TestCase):
    def needsServiceTrue(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = Willoughby(current_mileage, last_service_mileage)
        self.assertTrue(engine.needsService())

    def needsServiceFalse(self):
        current_mileage = 60000
        last_service_mileage = 0
        engine = Willoughby(current_mileage, last_service_mileage)
        self.assertFalse(engine.needsService())
