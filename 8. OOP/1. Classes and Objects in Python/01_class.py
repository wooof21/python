

# Class: Class is a blueprint or a template. 
# Eg. Form for an Exam that contains name, age, electives, father's name etc

# Object: Specific instance created from the template (class.). 
# Eg. Form which contains the data for John Doe

class Employee:
    # Class variable
    # A class attribute, shared by all instances
    # Java equivalent: `static String company = "HP";`
    # if call emp.company = "Apple" -> this just create an instance variable, not changing the class variable value
    company = "HP"

    # NOT a constructor, but initializes the class using __init__
    # emp = Employee("John", 30)
    def __init__(self, name, age):
        # Instance variable
        self.name = name
        self.age = age
    
    '''
        `self` refers to the current object, a way to reference the object of the class which is being created
        It is required as the first parameter
        Python automatically passes it when you call the method

        When call the method:
            - e.get_salary()
        Python internally does:
            - Employee.get_salary(e)
        
        This is why `self` is needed.

        All `Instance method` must have `self` as first parameter

        -----------------------------
        `Static method` do not - 

            class MathUtils:
                @staticmethod
                def add(a, b):
                    return a + b
        
        Usage: MathUtils.add(2, 3)

        Static methods belong to the class, not an instance.

        --------------------------------
        `Class method`, use `cls`, not `self`
            - Class methods operate on the class itself, not instances.
        
        class Employee:
            company = "HP"

            @classmethod
            def get_company(cls):
                return cls.company
        
        Usage: Employee.get_company() # output: HP
            - cls = the class (Employee)
            - Very common for factories and configs
        
        Use when:
            - work with class-level data
            - Factory methods
            - Alternative constructors

        When to Use Classes vs Functions:

            Use classes when:

                - need state
                - model entities
                - build reusable components
                - design systems
            
            Don’t use classes when:

                - Just grouping functions
                - No shared state
                - Script-like code
            
            Python is more functional than Java.
    '''
    def get_salary(self): 
        return 34000


# self = e1
e1 = Employee("John", 35) # An Object of class Employee is created here
print(e1.get_salary()) # Employee e's get salary method is called

# self = e2
e2 = Employee("Jane", 23)
print(e2.get_salary())
print(e2.company)


# Each object stores attributes in: obj.__dict__
# make Python dynamic, can add attributes at runtime

print(e1.__dict__)


# Python is dynamic: can add attributes at runtime
e1.country = "Canada"

print(e1.__dict__)

'''
Normal Python Objects Are Memory Heavy, when create a normal class using __init__,
Each object stores its attributes in a dictionary.
And dictionaries are expensive:
    - Hash table
    - Resizing logic
    - Extra memory overhead
    - Key objects stored separately

To reduce memory, use: __slots__

    - It also prevents dynamic attribute creation.
    - Saves memory
    - Faster attribute access (slightly)
    - Prevents accidental attribute creation
    - Enforces schema

This is useful in:

    - Data modeling
    - ML dataset objects
    - AST trees
    - Graph structures
    - Token representations
    - Financial trading systems

If need dynamic attributes:

    __slots__ = ("name", "age", "__dict__")

But: If subclass does not define __slots__, it will reintroduce __dict__.

Use __slots__ when:

    - Create many small objects
    - Attributes are fixed
    - Memory efficiency matters
    - Performance-critical system
    - Want schema enforcement

Do NOT use when:
    - need dynamic fields
    - use heavy metaprogramming
    - use libraries expecting __dict__
'''

class Emp:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

# NO __dict__ created.
# Instead, Python stores attributes in a fixed, preallocated structure.
emp = Emp("Jack", 55)

# print(emp.__dict__) # AttributeError: 'Emp' object has no attribute '__dict__'.