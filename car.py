from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.engine = Engine
        self.battery = Battery

    def needs_service(self):
        if self.engine.needs_service() == True or self.battery.needs_service() == True:
            return True
        else:
            return False