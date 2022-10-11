from Car import Car
from engine.Engine import Engine, CapuletEngine, WiloughbyEngine, SternmanEngine
from battery.Battery import Battery, SpindlerBattery, NubbinBattery
from tyres.Tyres import Tyres, CarriganTyres, OctoprimeTyres


class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor_values):
        capulet = CapuletEngine(last_service_mileage, current_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        carrigan = CarriganTyres(wear_sensor_values)
        calliope = Car(capulet, spindler, carrigan)
        return calliope

    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor_values):
        wiloughby = WiloughbyEngine(last_service_mileage, current_mileage)
        spindler = SpindlerBattery(last_service_date, current_date)
        octoprime = OctoprimeTyres(wear_sensor_values)
        glissade = Car(wiloughby, spindler, octoprime)
        return glissade

    def create_palindrome(self, current_date, last_service_date, warning_lights_on, wear_sensor_values):
        sternman = SternmanEngine(warning_lights_on)
        spindler = SpindlerBattery(last_service_date, current_date)
        carrigan = CarriganTyres(wear_sensor_values)
        palindrome = Car(sternman, spindler, carrigan)
        return palindrome

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor_values):
        wiloughby = WiloughbyEngine(last_service_mileage, current_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        octoprime = OctoprimeTyres(wear_sensor_values)
        rorschach = Car(wiloughby, nubbin, octoprime)
        return rorschach

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage, wear_sensor_values):
        capulet = CapuletEngine(last_service_mileage, current_mileage)
        nubbin = NubbinBattery(last_service_date, current_date)
        carrigan = CarriganTyres(wear_sensor_values)
        thovex = Car(capulet, nubbin, carrigan)
        return thovex
