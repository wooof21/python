
import numpy as np

array = np.arange(0, 10)
print(array)

array_2d_0 = np.arange(0, 18).reshape(3, 6)
print(array_2d_0)

print("-----------------insert 1d--------------------")
# obj: the insertion position
# create a new array
insert = np.insert(arr = array, obj = 5, values = -1)
print(insert)

print("-----------------insert 2d--------------------")
# obj: the insertion position
# axis: 1 -> cols
# insert a new value -1 at col 1 from all rows
insert = np.insert(arr = array_2d_0, obj = 1, values = -1, axis = 1)
print(insert)

print("-----------------insert 2d different values--------------------")
# obj: the insertion position
# axis: 1 -> cols
# insert with different values at each row
insert = np.insert(arr = array_2d_0, obj = 1, values = [-1, -2, -3], axis = 1)
print(insert)

print("-----------------delete 1d--------------------")
# obj: the position to remove
delete = np.delete(arr = array, obj = 4)
print(delete)

print("-----------------delete 2d--------------------")
# obj: the deletion position
# axis: 1 -> cols
# delete the element at col 1 from all rows
delete = np.delete(arr = array_2d_0, obj = 1, axis = 1)
print(delete)

print("-----------------append 1d--------------------")
# append: add new values at the end
append = np.append(arr = array, values = [-1, -2, -3])
print(append)

print("-----------------append 2d row--------------------")
# append: add new row at the end
append_2d = np.append(arr = array_2d_0, values = [[-1, -2, -3, -4, -5, -6]], axis = 0)
print(append_2d)

print("-----------------append 2d col--------------------")
# append: add new col at the end
append_2d = np.append(arr = array_2d_0, values = [[-1], [-2], [-3]], axis = 1)
print(append_2d)

print("-----------------tile 1d--------------------")
# copy the whole array by `reps` and append at the end
# repeating all values by `reps`
tile = np.tile(A = array, reps = 3)
print(tile)

print("-----------------tile tuple--------------------")
# copy the whole array by `reps` and append at the end
# (2, 2) -> 
# col -> copy array 2 times
# append a new row with copied array 2 times
tile_2 = np.tile(A = array, reps = (2, 2))
print(tile_2)

print("-----------------tile 2d--------------------")
# (3, 2) -> 3 - row, 2 - col
# row: copy 3 times
# col: copy 2 times
tile_2d = np.tile(A = array_2d_0, reps = (3, 2))
print(tile_2d)

print("-----------------pad 1d constant--------------------")
'''
pad: extends the array by adding values at the edges.

pad_width → how many values to add before and after the array
    - (1, 2) -> 1 value at start, 2 values at the end

mode='constant' → pad with constant numbers

constant_values=(10,20) → value for before and after
    - (10, 20) -> 10 for start, 20 for end
'''
array_1d = np.array([1, 2, 3])
pad = np.pad(array = array_1d, pad_width = (1, 2), mode = 'constant', constant_values = (10, 20))
print(pad) # [10  1  2  3 20 20]


print("-----------------pad 1d edge--------------------")
# mode = edge: repeat values at edge (begin and end)
pad = np.pad(array = array_1d, pad_width = (1, 2), mode = 'edge')
print(pad) # [1 1 2 3 3 3]

print("-----------------pad 1d minimum--------------------")
# mode = minimum: repeat minimum value at edge (begin and end)
pad = np.pad(array = array_1d, pad_width = (1, 2), mode = 'minimum')
print(pad) # [1 1 2 3 1 1]

print("-----------------pad 1d maximum--------------------")
# mode = maximum: repeat minimum value at edge (begin and end)
pad = np.pad(array = array_1d, pad_width = (1, 2), mode = 'maximum')
print(pad) # [3 1 2 3 3 3]

print("-----------------pad 1d mean--------------------")
# mode = mean: repeat mean value at edge (begin and end)
# mean = total_sum_of_all_values / quantity_of_values
pad = np.pad(array = array_1d, pad_width = (1, 2), mode = 'mean')
print(pad) # [2 1 2 3 2 2]

print("-----------------pad 2d--------------------")
'''
mode='reflect' → mirror the array values at the edges

pad_width=(before, after) → default applies to all axes if only a tuple of 2 numbers is given.
Since array_2d_1 is 2D, pad_width=(1,2) is applied to both axes, meaning:
    - 1 row and 1 col added at beginning, and 2 rows and 2 cols added at the end
    - 1 row above, 2 rows below
    - 1 column left, 2 columns right

Pad vertically (rows):
    - Row before → mirror the first row → [3,4]
    - Row after → mirror last rows → [3,4] and [1,2]

Pad horizontally (columns):
    - Column before → mirror first column
    - Column after → mirror last column
'''
array_2d_1 = np.array([[1, 2], [3, 4]])
pad_2d = np.pad(array = array_2d_1, pad_width = (1, 2), mode = 'reflect')
print(pad_2d)


print("-----------------trim_zeros--------------------")
# trim: remove zeros from beginning and the end of array only
array_with_zeros = np.array([0, 0, 1, 2, 3, 0, 5, 0, 0, 0])
trim = np.trim_zeros(filt = array_with_zeros)
print(trim) # [1 2 3 0 5]

print("-----------------trim_zeros front--------------------")
# trim = 'f: remove zeros from beginning
array_with_zeros = np.array([0, 0, 1, 2, 3, 0, 5, 0, 0, 0])
trim = np.trim_zeros(filt = array_with_zeros, trim = 'f')
print(trim) # [1 2 3 0 5 0 0 0]

print("-----------------trim_zeros back--------------------")
# trim = 'b: remove zeros from back
array_with_zeros = np.array([0, 0, 1, 2, 3, 0, 5, 0, 0, 0])
trim = np.trim_zeros(filt = array_with_zeros, trim = 'b')
print(trim) # [0 0 1 2 3 0 5]