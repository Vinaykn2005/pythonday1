from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    def sleep():
        print("All animal are sleep")
class Dog(Animal):
    def sound(self):
        print("Barking sound made by dog")
class Cat(Animal):
    def sound(self):
        print("Meow sound is made by cat")
class Cow(Animal):
    def sound(self):
        print("Moo sound is made by cow")
ob1 = Dog()
ob2 = Cat()
ob1.sound()
ob2.sound()