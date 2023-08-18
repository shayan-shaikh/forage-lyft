from car import Car
from model.engine.capulet import Capulet
from model.battery.spindler import Spindler


class Calliope(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        calliope_engine = Capulet(current_mileage, last_service_mileage)
        calliope_battery = Spindler(last_service_date)

        super().__init__(calliope_engine, calliope_battery)
        self.engine = calliope_engine
        self.battery = calliope_battery

    def needsService(self):
        return super().needsService()
