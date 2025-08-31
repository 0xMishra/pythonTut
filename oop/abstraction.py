"""
hiding complex implementation details from the user
"""
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("car starts with a button")


class Bike(Vehicle):
    def start(self):
        print("bike starts with a key")

car = Car()
bike = Bike()

car.start()
bike.start()
