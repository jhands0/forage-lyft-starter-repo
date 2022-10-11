from abc import ABC, abstractmethod


class Tyres(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class CarriganTyres(Tyres):
    def __init__(self, wear_sensor_values):
        self.wear_sensor_tyres = wear_sensor_values

    def needs_service(self):
        for i in range(0, 3):
            if self.wear_sensor_tyres[i] >= 0.9:
                return True
        return False


class OctoprimeTyres(Tyres):
    def __init__(self, wear_sensor_values):
        self.wear_sensor_values = wear_sensor_values

    def needs_service(self):
        total = self.wear_sensor_values[0] + self.wear_sensor_values[1] + self.wear_sensor_values[2] \
                + self.wear_sensor_values[3]
        if total < 3:
            return False
        return True
