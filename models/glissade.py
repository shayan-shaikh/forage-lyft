from car import Car
from model.engine.willoughby import Willoughby
from model.battery.spindler import Spindler


class Glissade(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        glissade_engine = Willoughby(current_mileage, last_service_mileage)
        glissade_battery = Spindler(last_service_date)

        super().__init__(glissade_engine, glissade_battery)
        self.engine = glissade_engine
        self.battery = glissade_battery

    def needsService(self):
        return super().needsService()
