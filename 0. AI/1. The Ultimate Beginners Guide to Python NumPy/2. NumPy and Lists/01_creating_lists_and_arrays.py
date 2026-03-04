
import numpy as np

print(np.__version__)


# NumPy vs Lists

list_a = [1, 2, 3, 4]
print(type(list_a))
print(id(list_a))

list_a.append(5)

print(id(list_a))

# NumPy Arrays
array_a = np.array([1, 2, 3, 4])

print(type(array_a))
print(id(array_a))

array_a = np.append(array_a, [5])
print(array_a)
# after add a new element to NumPy array, it has a new id
# NumPy array has a fixed length
print(id(array_a))