from Serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, Engine, Battery, Tyres):
        self.engine = Engine
        self.battery = Battery
        self.tyres = Tyres

    def needs_service(self):
        if self.engine.needs_service() == True or self.battery.needs_service() == True or self.tyres.needs_service():
            return True
        else:
            return False