
'''
Multiple inheritance is valid when parents are independent.

Python multiple inheritance works best with:

    - Mixins
    - Small behavior-only classes
    - No shared state
'''

class Flyable:
    def fly(self):
        print("Flying")
    
    # both parents have same method
    def color(self):
        print("Brown")

class Swimmable:
    def swim(self):
        print("Swimming")
    
    def color(self):
        print("Black")

class Duck(Flyable, Swimmable):
    pass

d = Duck()

d.fly()
d.swim()

# MRO (Method Resolution Order)
d.color() # Brown

print(Duck.__mro__)

# MRO determines how Python searches parent classes.
# Order: Current class -> Left parent -> Right parent -> Continue recursively
