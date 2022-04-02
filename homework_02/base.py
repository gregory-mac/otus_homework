from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 1500
    fuel = 1000
    fuel_consumption = 10
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError

    def move(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if fuel_needed > self.fuel:
            raise NotEnoughFuel
        self.fuel = self.fuel - fuel_needed
