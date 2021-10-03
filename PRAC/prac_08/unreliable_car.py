"""
CP1404/CP5632 Practical
Car class
"""
from prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = 0

    def drive(self, distance):
        random_num = randint(0, 100)
        if random_num > self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven


