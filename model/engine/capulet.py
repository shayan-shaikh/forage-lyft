from engine import Engine


class Capulet(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        super().__init__(last_service_mileage, current_mileage)

    def needsService(self):
        return self.current_mileage - self.last_service_mileage > 30000
