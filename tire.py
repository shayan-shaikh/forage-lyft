from abc import ABC, abstractmethod


class Tire(ABC):
    def __init__(self, sensor) -> None:
        super().__init__()
        self.sensor = sensor

    @abstractmethod
    def needsService(self):
        pass
