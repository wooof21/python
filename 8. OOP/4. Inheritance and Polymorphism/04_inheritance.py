

class Animal: # Parent class (superclass)
    location = "Australia"
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("Generic Animal sound")


# class `Dog` inherit from `Animal`
class Dog(Animal): # This is how inheritance is done in Python
    def speak(self):
        # extend the behavior of parent method, instead of complete replace it
        super().speak() # Using the speak function of the parent class
        print("Woof!")


a = Animal("Dog")
a.speak()


d = Dog("Bruno")
d.speak()
print(d.location)