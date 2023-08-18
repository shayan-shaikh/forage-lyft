from datetime import datetime, timedelta
from battery import Battery


class Spindler(Battery):
    def __init__(self, last_service_date):
        super().__init__(last_service_date)

    def needsService(self):
        thresholdDate = self.last_service_Date + timedelta(days=2 * 365)

        if thresholdDate <= datetime.today():
            return True
        else:
            return False
