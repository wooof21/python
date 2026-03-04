

import numpy as np

# nonzero
array_2d = np.array([[1, 0, 0],
                     [0, 2, 0],
                     [3, 4, 0]])
indices = np.nonzero(array_2d)
print(type(indices)) # <class 'tuple'>
# return a tuple of (row, col) position where nonzero elements in array_2d
print(indices) # (array([0, 1, 2, 2]), array([0, 1, 0, 1]))

# construct the array with nonzero elements
array_nonzero = array_2d[indices]
print(array_nonzero) # [1 2 3 4]

array = np.array([1, 0, 0, 2, 0, 3, 4, 0, 0, 0])
indices = np.nonzero(array)
print(type(indices)) # <class 'tuple'>
# return a tuple of (row,) position where nonzero elements in array
print(indices) # (array([0, 3, 5, 6]),)


print("---------------where-------------------")
# where
array_1d = np.arange(10)
print(array_1d)

# passing a filter condition
array = np.where(array_1d < 5)
print(type(array)) # <class 'tuple'>
print(array) # (array([0, 1, 2, 3, 4]),)

# 0 -> replace the values to 0 when condition is True
# 1 -> replace the values to 1 when condition is False
array = np.where(array_1d < 5, 0, 1)
print(type(array)) # <class 'numpy.ndarray'>
print(array) # [0 0 0 0 0 1 1 1 1 1]

# array_1d -> keep the original values when condition is True
# array_1d + 5 -> add 5 to each value when condition is False
array = np.where(array_1d < 5, array_1d, array_1d + 5)
print(type(array)) # <class 'numpy.ndarray'>
print(array) # [ 0  1  2  3  4 10 11 12 13 14]

# use the values from another array when condition is False
# use the values from the same index from other array
array_new = np.arange(50, 60)
array = np.where(array_1d < 5, array_1d, array_new)
print(type(array)) # <class 'numpy.ndarray'>
print(array) # [ 0  1  2  3  4 55 56 57 58 59]


print("---------------where 2d-------------------")
array_2d = np.arange(0, 20).reshape(4, 5)
print(array_2d)

# when condition is True, keep the orginal value
# when condition is False, replace the values with -1
array = np.where(array_2d % 2 == 0, array_2d, -1)
print(type(array)) # <class 'numpy.ndarray'>
'''
[[ 0 -1  2 -1  4]
 [-1  6 -1  8 -1]
 [10 -1 12 -1 14]
 [-1 16 -1 18 -1]]
'''
print(array) 


print("---------------argwhere-------------------")
# argwhere
array = np.argwhere(array_2d % 2 == 0)
print(type(array)) # <class 'numpy.ndarray'>
'''
arghwere: only extract the indexes
return a matrix of (row, col) pairs where condition is True
[[0 0] 
 [0 2]
 [0 4]
 [1 1]
 [1 3]
 [2 0]
 [2 2]
 [2 4]
 [3 1]
 [3 3]]
'''
print(array)

print("---------------select-------------------")
# select
print(array_1d)
'''
condlist -> condition list
    -> select values that > 5 and < 8
choicelist -> if value < 5, then add 10
           -> if value > 8, then add 20
default -> if all conditions False, replace values with -1
'''
array = np.select(condlist = [array_1d < 5, array_1d > 8], 
                  choicelist = [array_1d + 10, array_1d + 20], default = -1)

print(array) # [10 11 12 13 14 -1 -1 -1 -1 29]

print("---------------unravel_index-------------------")
# unravel_index
shape = (4, 5)
array_2d = np.arange(20).reshape(shape)
print(array_2d)

'''
array_2d:
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]

tuple: If there is a flattened array of shape (4,5),
where would the flat index 14 be located in 2D coordinates?
    -> it is doing mathematical index conversion
    -> it does not search a value index in an array

given a 2d array with shape (4, 5), if flattened:
[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
-> Index 14 is the 15th element.

unravel_index is just: Converting a flat index into multi-dimensional coordinates.
    -> inverse of `ravel_multi_index`

(np.int64(2), np.int64(4)): row = 2, col = 4
'''
tuple = np.unravel_index(indices = 14, shape = shape)
print(type(tuple)) # <class 'tuple'>
print(tuple) # (np.int64(2), np.int64(4))


print("---------------diag_indexes-------------------")
# diag_indexes
# a 2 dimension 3 X 3 matrix
indices = np.diag_indices(n = 3, ndim = 2)
print(type(indices)) # <class 'tuple'>
print(indices) # (array([0, 1, 2]), array([0, 1, 2]))

'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]

then using the `indices` to access the diagonal of the matrix
'''
array_2d_1 = np.arange(9).reshape(3, 3)
print(array_2d_1)
print(array_2d_1[indices]) # [0 4 8]

print("---------------tril_indexes-------------------")
# tril_indexes
# access the lower triangle
indices = np.tril_indices(n = 3, m = 3)
print(type(indices)) # <class 'tuple'>
print(indices) # (array([0, 1, 1, 2, 2, 2]), array([0, 0, 1, 0, 1, 2]))

'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]

then using the `indices` to access the lower triangle of the matrix
    -> [0 3 4 6 7 8]
'''
# the elements from lower triangle
print(array_2d_1[indices]) # [0 3 4 6 7 8]

print("---------------triu_indexes-------------------")
# triu_indexes
# access the upper triangle
indices = np.triu_indices(n = 3, m = 3)
print(type(indices)) # <class 'tuple'>
print(indices) # (array([0, 0, 0, 1, 1, 2]), array([0, 1, 2, 1, 2, 2]))

'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]

then using the `indices` to access the upper triangle of the matrix
    -> [0 1 2 4 5 8]
'''
# the elements from upper triangle
print(array_2d_1[indices]) # [0 1 2 4 5 8]

print("---------------diag_indexes_from-------------------")
# diag_indexes_from
tuple = np.diag_indices_from(array_2d_1)

# indices of the main diagonal of the matrix
# (row, col)
print(tuple) # (array([0, 1, 2]), array([0, 1, 2]))

print("---------------tril_indexes_from-------------------")
# tril_indexes_from

# indices of lower traingle (row, col)
tuple = np.tril_indices_from(array_2d_1)
print(tuple) # (array([0, 1, 1, 2, 2, 2]), array([0, 0, 1, 0, 1, 2]))

print("---------------triu_indexes_from-------------------")
# triu_indexes_from

# indices of upper traingle (row, col)
tuple = np.triu_indices_from(array_2d_1)
print(tuple) # (array([0, 0, 0, 1, 1, 2]), array([0, 1, 2, 1, 2, 2]))