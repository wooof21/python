

z = 3
# use `global` keyword to modify the global variable inside a function
print(z)

def sum(a, b):
    print("Sum")
    c = a + b
    global z  # To modify a global variable inside a function, we need to use the 'global' keyword
    z = c # This will refer to global z and not create a local variable
    return c 


print(sum(3, 12))
print(z)