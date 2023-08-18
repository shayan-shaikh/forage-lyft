from car import Car
from model.engine.sternman import Sternman
from model.battery.spindler import Spindler


class Palindrome(Car):
    def __init__(self, current_mileage, last_service_mileage, last_service_date):
        palindrome_engine = Sternman(current_mileage, last_service_mileage)
        palindrome_battery = Spindler(last_service_date)

        super().__init__(palindrome_engine, palindrome_battery)
        self.engine = palindrome_engine
        self.battery = palindrome_battery

    def needsService(self):
        return super().needsService()
