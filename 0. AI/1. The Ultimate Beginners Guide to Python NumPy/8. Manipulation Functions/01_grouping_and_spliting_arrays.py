

import numpy as np

array = np.arange(0, 10)
print(array)

array_2d_0 = np.arange(0, 18).reshape(3, 6)
print(array_2d_0)

array_2d_1 = np.arange(18, 36).reshape(3, 6)
print(array_2d_1)

print("---------------concatenate------------------")
# concatenate: combine 2 arrays together
# by default, axis = 0, concatenate by adding new rows
array_2d = np.concatenate([array_2d_0, array_2d_1])
print(array_2d)

print("---------------concatenate axis 1------------------")
# concatenate: combine 2 arrays together with new cols
array_2d = np.concatenate([array_2d_0, array_2d_1], axis = 1)
print(array_2d)

print("---------------concatenate axis 0------------------")
# concatenate: combine 2 arrays together with new rows
array_2d = np.concatenate([array_2d_0, array_2d_1], axis = 0)
print(array_2d)

print("---------------stack------------------")
'''
stack: add new axis, by default = 0
stack along a new dimension at front, then place the arrays inside
in the passed order

result:
[[[ 0  1  2  3  4  5]
  [ 6  7  8  9 10 11]
  [12 13 14 15 16 17]]

 [[18 19 20 21 22 23]
  [24 25 26 27 28 29]
  [30 31 32 33 34 35]]]
'''
stack = np.stack(arrays = [array_2d_0, array_2d_1])
print(stack)
print(stack.shape)

print("---------------stack axis 1------------------")
'''
stack axis = 1 -> Inserts a new dimension at the position specified
original shape: (3, 6)
axis = 1, insert a new dimension at position 1 -> (3, 2, 6)
2 -> number of arrays stacked

result:
[[[ 0  1  2  3  4  5]
  [18 19 20 21 22 23]]

 [[ 6  7  8  9 10 11]
  [24 25 26 27 28 29]]

 [[12 13 14 15 16 17]
  [30 31 32 33 34 35]]]
'''
stack = np.stack(arrays = [array_2d_0, array_2d_1], axis = 1)
print(stack)
print(stack.shape)

print("---------------vstack------------------")
# vstack: vertical stack - (row-wise)
# for 2d arrays: same as np.concatenate([array_2d_0, array_2d_1], axis=0)
# (3, 6) -> keep columns (6), add rows (3 + 3)
vstack = np.vstack(tup = [array_2d_0, array_2d_1])
print(vstack)


print("---------------hstack------------------")
# hstack: Stack arrays horizontally (column-wise)
# for 2d arrays: same as np.concatenate([array_2d_0, array_2d_1], axis=1)
# (3, 6) -> keep rows (3), add columns (6 + 6)
hstack = np.hstack(tup = [array_2d_0, array_2d_1])
print(hstack)

print("---------------split------------------")
# split: Split the array into 2 equal parts along axis=0 (default)
# orginal array size along axis 0 must be divisible by `indices_or_sections`
# return a list of arrays
split = np.split(ary = array, indices_or_sections = 2)
print(split)
print(type(split)) # <class 'list'>

print("---------------split 2d------------------")
# split: Split the array into 2 equal parts along axis=0 (default)
# orginal array size along axis 0 must be divisible by `indices_or_sections`
# return a list of arrays
# array_2d.shape = (3, 6)
split_2d = np.split(ary = array_2d_0, indices_or_sections = 3)
print(split_2d)
print(type(split_2d)) # <class 'list'>

# split array by col
# array_2d.shape = (3, 6) -> 3 rows, 6 cols
# cols split into 3 equal parts -> each_split.shape = (3, 2)
split_2d_axis = np.split(ary = array_2d_0, indices_or_sections = 3, axis = 1)
print(split_2d_axis)
print(type(split_2d_axis)) # <class 'list'>

print("---------------split 2d custom------------------")
# Split at column index 2, and at column index 3
# split: [0, 2), [2, 3), [3:)
split_2d_custom = np.split(ary = array_2d_0, indices_or_sections = [2, 3], axis = 1)
print(split_2d_custom)
print(type(split_2d_custom)) # <class 'list'>

print("---------------vsplit------------------")
'''
vsplit: Vertical split = split along rows
same as: np.split(array_2d_0, 3, axis=0)

Since rows = 3: 3 / 3 = 1 row per chunk

result: (1, 6)
[array([[0, 1, 2, 3, 4, 5]]), array([[ 6,  7,  8,  9, 10, 11]]), array([[12, 13, 14, 15, 16, 17]])]

'''
vsplit = np.vsplit(ary = array_2d_0, indices_or_sections = 3)
print(vsplit)

print("---------------hsplit------------------")
'''
hsplit: Horizontal split = split along columns
same as: np.split(array_2d_0, 3, axis=1)

Columns = 6, 6 / 3 = 2 columns each

result: (3, 2)

[array([[ 0,  1],
       [ 6,  7],
       [12, 13]]), 
array([[ 2,  3],
       [ 8,  9],
       [14, 15]]), 
array([[ 4,  5],
       [10, 11],
       [16, 17]])]
'''
hsplit = np.hsplit(ary = array_2d_0, indices_or_sections = 3)
print(hsplit)

print("------------------------------------------")
'''
custom index splitting, split at column index 2 and column index 3
same as: np.split(array_2d_0, [2,3], axis=1)

slice: [0:2), [2:3), [3:end)
result: (3,2), (3,1), (3,3)

[array([[ 0,  1],
       [ 6,  7],
       [12, 13]]), 
array([[ 2],
       [ 8],
       [14]]), 
array([[ 3,  4,  5],
       [ 9, 10, 11],
       [15, 16, 17]])]
'''
hsplit = np.hsplit(ary = array_2d_0, indices_or_sections = [2, 3])
print(hsplit)