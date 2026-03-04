
'''
Decorators are a key feature in Python that enable code reusability and cleaner
function modifications. They are commonly used for:

    - Logging: Recording when a function is called and its arguments.
    - Timing: Measuring how long a function takes to execute.
    - Authentication and Authorization: Checking if a user has permission to access
        a function.
    - Caching: Storing the results of a function call so that subsequent calls with the
        same arguments can be returned quickly.
    - Rate Limiting: Controlling how often a function can be called.
    - Input Validation: Checking if the arguments to a function meet certain criteria.
    - Instrumentation: Adding monitoring and profiling to functions.

Frameworks like Flask and Django use decorators extensively for routing,
authentication, and defining middleware
'''

def repeat(n):
    def decorator_func(func):
        def wrapper_func(a):
            for i in range(n):
                func(a)
        return wrapper_func 
    return decorator_func

@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")

'''
It replaces the function say_hello with this:
def decorator(func):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
    return wrapper
'''

say_hello("John")