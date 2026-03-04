

# Two types of modules in Python: 
# - Built in Modules 
# - External Modules

# List of all the built in Modules: https://docs.python.org/3/py-modindex.html
import math 
import os 
import custom_module as mymodule

# To use external modules, you need to install them using pip
# Example: pip install requests
import requests

print(math.sqrt(16))

mymodule.hello()

r = requests.get("https://www.google.com")
print(r.text)
