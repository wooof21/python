
# Python is Dynamically Typed Language, no need to explicitly specify the data type of a variable
# Python automatically figures out the type
age = 20
name = "John" # string
cgpa = 4.55 # float

# Rule of defining a variable in Python: 
    # Variable names must start with a letter (a-z, A-Z) or an underscore (_).
    # They can contain letters, numbers, and underscores (no other special characters).
    # Variable names are case-sensitive (age and Age are different).
    # Avoid using Python keywords (e.g., if, for, while) as variable names.



# Python also support define variables with explicit type - type hint
gender: str = "Male" # string with type hint
is_student: bool = True # boolean with type hint

# Dictionary with string keys and int values
student_ages: dict[str, int] = {"Alice": 20, "Bob": 22}
# Optional values (e.g. might be None)
# Use Optional from the typing module:
from typing import Optional
nickname: Optional[str] = None

# But be aware: Python will not enforce types at runtime — 
# it’s only for static analysis tools like mypy, IDEs, or documentation purposes.

#Even if you declare a variable with a specific type, 
# Python won’t stop you from assigning a value of a different type to it 
# when the code runs. - Python is a dynamically typed language - 
# types are flexible unless you use special tools or frameworks to enforce them.
age: int = 25
age = "twenty" # Python allows this without error at runtime
# If you want Python to enforce types during execution, you’d need to:
# Use libraries like pydantic, enforce, or typeguard
# Or write manual checks like:
def set_age(age: int):
    if not isinstance(age, int):
        raise TypeError("age must be an int")
    
# set_age("33") # Raises TypeError: age must be an int

# Tools That Do Check Types (Statically):
# mypy – Static type checker for Python:
# bash: mypy <file_name>.py



# get user input
text = input("Enter text: ")
# convert to uppercase
text = text.upper()
# print the result  
print("Uppercase text:", text)