from tire import Tire


class Carrigan(Tire):
    def __init__(self, sensor) -> None:
        super().__init__(sensor)

    def needsService(self):
        return any(map(lambda curr: curr >= 0.9, self.tensor))
