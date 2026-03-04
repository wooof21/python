

import numpy as np


# reshape: reshape() does NOT modify the array in-place.
# It returns a new view (or new array), and need to store it.
# ** (a, b, c) -> a * b * c == array.size
array_3d = np.arange(1, 25).reshape(2, 4, 3)
print(array_3d)
array_reshape = array_3d.reshape(4, 3, 2)
print(array_reshape)
# when do not know the value of one reshaping index, use -1
# numPy will take care the calculation
array_reshape_unknow = array_3d.reshape(6, 2, -1) # (-1, 1, 12)
print(array_reshape_unknow)

print("----------------------------")
# transpose: pass a tuple (a, b, c)
# (a, b, c) map to original shape (2, 4, 3) index
# when transpose, 
# a = 1 means -> new shape of index 0 (depth) = 4 (value at index 0 of original shape)
# b = 0 means -> new shape of index 1 (row) = 2 (value at index 1 of original shape)
# c = 2 means -> new shape of index 2 (col) = 3 (value at index 2 of original shape)
print(array_3d.shape) # (2, 4, 3)
# reshape: keep the original order
# transpose: rotate the data as if it was a Rubik's Cube
array_transpose = array_3d.transpose((1, 0 ,2))
print(array_transpose.shape) # (4, 2, 3)
print(array_transpose)

print("----------------------------")
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])
print(array_2d)
print(array_2d.shape)
array_transpose2 = array_2d.transpose((1, 0))
print(array_transpose2.shape)
print(array_transpose2)
array_reshape2 = array_2d.reshape((3, 2))
print(array_reshape2)

print("----------------------------")
# swapaxes
# orginal array_3d shape = (2, 4, 3)
# 1 map to index 1 of original array_3d shape -> 4 depth
# 0 map to index 0 of orginal array_3d shape -> 2 rows
# same as transpose((1, 0, 2)) -> both data was rotated
array_swapaxes = array_3d.swapaxes(1, 0)
print(array_swapaxes)


print("----------------------------")
# flatten: flat a ND array to 1D array, copy into a new array
# Safe to modify without affecting original
# More memory usage
array_flat = array_3d.flatten()
print(array_flat)


print("----------------------------")
# ravel: return a view if possbile, if not return a copy
# More memory efficient and faster
array_ravel = array_3d.ravel()
print(array_ravel)
array_ravel[0] = 888 # the value in original array_3d also change, they share memory
print(array_ravel)
print(array_3d)

print("----------------------------")
# squeeze: remove a dimension if possible, if that dimension value is 1
array_axis_size_1 = array_3d.reshape(8, 1, 3)
print(array_axis_size_1)
array_squeeze = array_axis_size_1.squeeze()
print(array_squeeze)
print(array_squeeze.shape) # (8, 3)
