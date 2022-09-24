from Car import Car
from engine.Engine import Engine, CapuletEngine, WiloughbyEngine, SternmanEngine
from battery.Battery import Battery, SpindlerBattery, NubbinBattery


class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        capulet = CapuletEngine(last_service_mileage, current_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        calliope = Car(capulet, spindler)
        return calliope

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        wiloughby = WiloughbyEngine(last_service_mileage, current_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        glissade = Car(wiloughby, spindler)
        return glissade

    def create_palindrome(self, current_date, last_service_date, warning_lights_on):
        sternman = SternmanEngine(warning_lights_on)
        spindler = SpindlerBattery(last_service_date, current_date)
        palindrome = Car(sternman, spindler)
        return palindrome

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        wiloughby = WiloughbyEngine(last_service_mileage, current_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        rorschach = Car(wiloughby, nubbin)
        return rorschach

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        capulet = CapuletEngine(last_service_mileage, current_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        thovex = Car(capulet, nubbin)
        return thovex
