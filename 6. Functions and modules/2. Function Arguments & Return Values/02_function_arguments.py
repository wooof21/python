


# plus: default argument
def add(a, b, plus=1):
    x = a + b + plus
    return x

# overwrite the defaul argument - pass value 2
c = add(3, 5, 2)
print(c)


# Using keyword arguments
# The order of arguments does not matter
c1 = add(b=5, a=3)
print(c1)

c2 = add(2, 4)
print(c2)

# function return tuple
def divide(a, b):
    return a / b, a % b, a // b

c3 = divide(b=5, a=3)
print(c3)
print(type(c3)) # <class 'tuple'>

# tuple unpacking
c4, c5, c6 = divide(5, 3)
print(c4, c5, c6)

# partially unpack: only care some values

c7, c8, _ = divide(5, 3) # ignore the third value

c9, *rest = divide(5, 3) #c9 = first value, rest = [remainder, total]

print(c9, rest)