

import numpy as np

array = np.array([7, 8, 8, 6, 8, 7, 7])

# return an array with unique values
unique = np.unique(ar = array)
print(unique) # [6 7 8]

print("------------------return_index----------------------")
# retuen a tuple (A, B)
# A -> unique array
# B -> first index of each unique value appears in original array
unique = np.unique(ar = array, return_index = True)
print(unique) # (array([6, 7, 8]), array([3, 0, 1]))
print(type(unique)) # <class 'tuple'>

print("------------------return_invserse----------------------")
# indices -> for each element in the original array, which position in unique_values it corresponds to
unique_values, indices = np.unique(ar = array, return_inverse = True)
print(unique_values, indices) # [6 7 8] [1 2 2 0 2 1 1]

print("------------------reconstruct from indicies----------------------")
# reconsrcut original array from indices
orginal = unique_values[indices]
print(orginal) # [7 8 8 6 8 7 7]

print("------------------return_counts----------------------")
# indices -> for each element in the original array, which position in unique_values it corresponds to
# return unique value with counts
# value 6 appear once, value 7 & 8 appear 3 times each
counts = np.unique(ar = array, return_counts = True)
print(counts) # (array([6, 7, 8]), array([1, 3, 3]))

print("------------------unique 2d----------------------")
array_2d = np.array([[0, 1, 2],
                     [3, 4, 5],
                     [0, 1, 2]])
unique_2d = np.unique(ar = array_2d, return_counts = True)
# return 1d array
print(unique_2d) # (array([0, 1, 2, 3, 4, 5]), array([2, 2, 2, 1, 1, 1]))

print("------------------unique 2d count axis 0----------------------")
# axis = 0, count by unqiue row 
# first row apears twice, 2nd row apear once
unqiue_count_row = np.unique(ar = array_2d, return_counts = True, axis = 0)
print(unqiue_count_row) # (array([[0, 1, 2],[3, 4, 5]]), array([2, 1]))