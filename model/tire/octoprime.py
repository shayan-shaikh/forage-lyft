from tire import Tire


class Octoprime(Tire):
    def __init__(self, sensor) -> None:
        super().__init__(sensor)

    def needsService(self):
        return sum(self.tensor >= 3)
