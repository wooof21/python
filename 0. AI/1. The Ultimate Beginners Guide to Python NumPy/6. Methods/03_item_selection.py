

import numpy as np

# take: take values from array by index
array_3d = np.arange(1, 25).reshape(2, 4, 3)
print(array_3d)
takes = array_3d.take(indices = [1, 3, 5, 8])
print(takes)
print(type(takes)) # <class 'numpy.ndarray'>
# take value and return in matrxi format by index
takes2 = array_3d.take(indices = [[1, 5], [8, 9]])
print(takes2) # [[ 2  6] [ 9 10]]

print("------------------------")
# put: update value in original array by index
array_3d.put(indices = [1, 5, 9, 10], values = [333, 555, 888, 999])
print(array_3d)

print("------------------------")
# repeat: each item in original array repeast N times and flatten the result
array_repeat = array_3d.repeat(repeats = 2)
print(array_repeat)

print("------------------------")
# repeat with axis 0
# 0 map to orginal shape (2, 4, 3) index 0 -> depth
# repeat depth 2 times
array_3d_rp_2_ax_0 = array_3d.repeat(repeats = 2, axis = 0)
print(array_3d_rp_2_ax_0) # repeat with 2 more depth

# axis = 1
# 1 map to orginal shape (2, 4, 3) index 1 -> row
# this means repeat with each row 2 times
array_3d_rp_2_ax_1 = array_3d.repeat(repeats = 2, axis = 1)
print(array_3d_rp_2_ax_1)

print("------------------------")
# 0 means depth
# first depth -> repeat 1 time
# second depth -> repeat 2 times
array_repeats = array_3d.repeat(repeats = [1, 2], axis = 0)
print(array_repeats)

print("------------------------")
# sort
# 0 -> sort array by row
array_2d = np.array([[10, 3, 7],
                     [8, 2, 9]])
# 10 > 8 -> move 8 to 1st row
# 3 > 2 -> move 2 to 1st row
# 7 < 9 -> does not change
array_2d.sort(axis = 0) #[[ 8  2  7] [10  3  9]]
print(array_2d)

# 1 -> sort arry by col
# apply sort to entire row
array_2d.sort(axis = 1)
print(array_2d) # [[ 2  7  8] [ 3  9 10]]

print("------------------------")
# argsort
# 0 -> sort array by row, and return indices
# [10, 3, 7] -> indices (0, 0, 0)
# [8, 2, 9] -> indices (1, 1, 1)
array_2d = np.array([[10, 3, 7],
                     [8, 2, 9]])

indices = array_2d.argsort(axis = 0)
print(indices) # [[1 1 0] [0 0 1]]

# 1 -> sort arry by col, and return indices
indices = array_2d.argsort(axis = 1)
print(indices) # [[1 2 0] [1 0 2]]

print("------------------------")

array_1d = np.array([10, 3, 7, 8, 2, 9])
indices = array_1d.argsort()
print(indices) # [4 1 2 3 5 0]
array_sorted = array_1d[indices]
print(array_sorted)

print("------------------------")
# searchsorted
# indices                    0  1  2  3  4  5
array_1d_ordered = np.array([2, 3, 7, 8, 9, 10])
# return the indices that the passed array values should be inserted 
# to keep the original array sorted
result = array_1d_ordered.searchsorted([1, 4, 11])
print(result)

print("------------------------")
# diagonal: return values in main diagonal
array_2d = np.array([[10, 3, 7],
                     [8, 2, 9],
                     [11, 4, 1],
                     [5, 8, 9]])

diagonal = array_2d.diagonal()
print(diagonal) # [10  2  1]
