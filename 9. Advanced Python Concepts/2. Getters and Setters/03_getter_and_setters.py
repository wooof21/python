

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    # @property decorator: make first_name a property
    # - Defines a getter
    # - Allows to access `first_name`like a field, not a method
    @property
    def first_name(self):
        l = self.name.split(" ") 
        return l[0]
    
    # def set_first_name(self, first):
    #     l = self.name.split(" ")
    #     new_name = f"{first} {l[1]}" 
    #     self.name = new_name
    
    # @first_name.setter: make a setter method on property
    @first_name.setter
    def first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}" 
        self.name = new_name

e = Employee("Jane Doe", 34555)
# print(e.first_name())
# e.set_first_name("John")
# print(e.name)

print(e.first_name)
e.first_name = "John"
print(e.name)