

# Decorator is a function that takes a function, 
# it creates a new function inside its body (wrapper). 
# Then it returns that new function

# decorator function: function name does not have to be decorator
def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func() # call the passed function
        print("I have executed this function....")
    return wrapper

# def say_hello():
#     print("Hello!")

# f = decorator(say_hello)
# f()

'''
f will look something like this
def f():
    print("I am about to execute a function....")
    print("Hello!")
    print("I have executed this function....")
'''

# another syntax
# @decorator: match the decorator function name
@decorator
def say_hello():
    print("Hello!")


say_hello()

