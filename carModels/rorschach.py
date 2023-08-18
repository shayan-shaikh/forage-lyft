from car import Car
from model.engine.willoughby import Willoughby
from model.battery.nubbin import Nubbin


class Rorschach(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        rorschach_engine = Willoughby(current_mileage, last_service_mileage)
        rorschach_battery = Nubbin(last_service_date)

        super().__init__(rorschach_engine, rorschach_battery)
        self.engine = rorschach_engine
        self.battery = rorschach_battery

    def needsService(self):
        return super().needsService()
