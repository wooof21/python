


class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary

    # Instance method (default)
    def print_info(self):
        info = f"The name is {self.name} and the salary is {self.salary}"
        print(info)

    # Static Method: no need to pass `self` to the method
    # useful when create an utility class
    # the method belong to the class, not the object calling the method
    @staticmethod
    def sum(a, b):
        return a+b
    
    # Class Methods 
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company



e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 34355)
# print(Employee.company)
# print(Employee.name) # this will throw an error
# e1.print_info()
# e2.print_info()

print(e2.sum(5, 23))
e2.print_company()
# changes the class attribute value
e1.change_company("Acer")
e1.print_company()

e3 = Employee("Jane", 12345)
e3.print_company()