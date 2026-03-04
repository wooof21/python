
'''
Python doesn’t enforce interfaces like Java, but it provides something very close:
    Abstract Base Classes (ABC)

An Abstract Base Class (ABC):
    - Cannot be instantiated directly
    - Defines methods that subclasses MUST implement
    - Enforces a contract
    - Supports polymorphism
    - Enables type checking

Python is duck-typed:

def make_sound(animal):
    animal.speak()

This works without inheritance.

But in large systems (especially backend / AI pipelines):

    - Structure
    - Safety
    - Clear contracts
    - Enforced design

Use ABC when:

    - Building framework
    - Designing plugin system
    - Defining service contracts
    - Building large backend system
    - Building AI pipeline components
    - Want static type checking support
'''
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass

# CANNOT do this: a = Animal()

# Implementing Concrete Classes

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"
    
cat = Cat()
print(cat.speak())

# Abstract Properties
class Shape(ABC):

    @property
    @abstractmethod
    def area(self):
        pass

# Concrete:
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius ** 2

# Registering Virtual Subclasses: can register a class without inheritance.
# This is powerful for plugin systems.
class Bird:
    def speak(self):
        return "Tweet"

Animal.register(Bird)

print(isinstance(Bird(), Animal)) # True
