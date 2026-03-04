

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("...")

class Dog(Animal):

    # if parent has __init__, child must call it explicitly.

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        # call parent
        super().speak()
        print("Woof")

'''
Composition vs Inheritance

Inheritance:
    Dog is an Animal

Composition:
    Car has an Engine

-------------------------
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()

Modern design (including in large Python systems like Django) prefers:
    Composition over inheritance
'''
