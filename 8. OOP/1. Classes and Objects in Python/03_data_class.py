

# instead of:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# use:
# Auto-generates:
    # __init__
    # __repr__
    # __eq__
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int