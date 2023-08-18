from engine import Engine


class Sternman(Engine):
    def __init__(self, warning_light_on):
        super().__init__(warning_light_on)

    def needsService(self):
        return self.warning_light_on
