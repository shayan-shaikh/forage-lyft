from abc import abstractmethod, ABC


class Battery(ABC):
    def __init__(self, last_service_date):
        self.last_service_Date = last_service_date

    @abstractmethod
    def needsService(self):
        pass
