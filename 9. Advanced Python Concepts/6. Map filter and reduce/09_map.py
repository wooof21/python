
'''
map, filter, reduce: higher-order functions, they operate on iterables (list, tuple, set ...)
'''



numbers = [1, 2, 3, 45, 4, 21]


new = list(map(lambda x: x*x, numbers))
print(new)

# same as:
# def square(x):
#     return x * x 
# new = list(map(square, numbers))
