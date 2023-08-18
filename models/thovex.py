from car import Car
from model.engine.capulet import Capulet
from model.battery.nubbin import Nubbin


class Thovex(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        thovex_engine = Capulet(current_mileage, last_service_mileage)
        thovex_battery = Nubbin(last_service_date)

        super().__init__(thovex_engine, thovex_battery)
        self.engine = thovex_engine
        self.battery = thovex_battery

    def needsService(self):
        return super().needsService()
