from battery.battery import battery

class NubbinBattery(Battery):
    def __init__(self,current_date,last_service_date):
        self.current_date=current_date
        self.last_service_date=last_service_date
        self.rubbin_year_need_service=3

    def needs_service(self):
        pass
