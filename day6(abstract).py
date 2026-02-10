from abc import ABC, abstractmethod
class Vehicle:
    @abstractmethod
    def start_engine(self):
        pass
class car(Vehicle):
    def start_engine(self):
        print("The car engine is started")
class bike(Vehicle):
    def start_engine(self):
        print("The bike engine is started")
class bus(Vehicle):
    def start_engine(self):
        print("The bus engine is started")

ob1 = car()
ob2 = bike()
ob3 = bus()
ob1.start_engine()
ob2.start_engine()
ob3.start_engine()