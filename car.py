from engine import Engine
from battery import Battery


class Car(Engine, Battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def batteryNeedsService(self):
        return self.battery.needsService(self)

    def engineNeedsService(self):
        return self.engine.needsService(self)

    def needsService(self):
        return self.batteryNeedsService or self.engineNeedsService
