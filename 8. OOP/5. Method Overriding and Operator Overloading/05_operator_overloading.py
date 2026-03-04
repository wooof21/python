

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    # passing a Point(p) and return a new Point
    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")

    # overwrite the `__add__` method to support the `+` operation on 2 Points
    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(3, 2)
p2 = Point(6, 3)

# p = p1.sum(p2) # Returns a new point which is sum of p1 and p2
p = p1 + p2 # Overloaded the + Operator by writing __add__ function
p.print_point()

'''
Other overload methods:

__sub__ ( - ), 
__mul__ ( * ), 
__truediv__ ( / ),
 __eq__ ( == ), 
 __ne__( != ), 
 __lt__ ( < ), 
 __gt__ ( > ), 
 __len__ ( len() ), 
 __getitem__ , __setitem__ , __delitem__ (for list/dictionary-like behavior – allowing you
to use [] with your objects)
'''