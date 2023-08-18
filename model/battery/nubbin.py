from battery import Battery
from datetime import datetime, timedelta


class Nubbin(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needsService(self):
        thresholdDate = self.last_service_Date + timedelta(days=4 * 365)

        if thresholdDate <= datetime.today():
            return True
        else:
            return False
