

import numpy as np

array = np.arange(0, 10)
print(array)

array_2d_0 = np.arange(0, 18).reshape(3, 6)
print(array_2d_0)

print("------------------flip-------------------")
# reverse the order of array elements
# same as: array[::-1]
# `:` -> keep all values from array
# `:-1` -> reverse order
flip = np.flip(array)
print(flip)
print(array[::-1])

print("------------------flip 2d-------------------")
# reverse the order of rows
# and reverse order of elements in each row
flip_2d = np.flip(array_2d_0)
print(flip_2d)

print("------------------flip 2d axis 0-------------------")
# axis = 0, reverse the order of rows
# keep elements order along col
flip_2d = np.flip(array_2d_0, axis = 0)
print(flip_2d)

print("------------------flip 2d axis 1-------------------")
# axis = 1, reverse the order of elements along col
# keep row order
flip_2d = np.flip(array_2d_0, axis = 1)
print(flip_2d)

print("------------------resize-------------------")
# convert the 2d array into 1d array (vector),
# and keep the number of elements by `new_shape`
resize = np.resize(a = array_2d_0, new_shape = 11)
print(resize)

print("------------------resize by tuple-------------------")
# resize 2d array by tuple
# resize to 4 rows and 2 cols
resize = np.resize(a = array_2d_0, new_shape = (4, 2))
print(resize)

# differece with reshape:
# reshape requires the number of values the same
# resize can have a different size

print("------------------resize by more value-------------------")
# resize with more values
# the additional values are repeated from original array
resize = np.resize(a = array_2d_0, new_shape = (8, 4))
print(resize)

print("------------------resize to 3d-------------------")
# resize to 3d array
# the additional values are repeated from original array
resize_3d = np.resize(a = array_2d_0, new_shape = (2, 5, 3))
print(resize_3d)