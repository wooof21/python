
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 1)

array = np.arange(10)
print(array)

# *** shuffle - modify the original array

# shuffle - randomly change the order of the elements
rng.shuffle(array)
print(array)

print("-----------------------------")
# shuffle with matrix
array_2d = np.arange(20).reshape(4, 5)
print(array_2d)

# shuffle only on rows, keep col nums
rng.shuffle(array_2d, axis = 0)
print(array_2d)

print("-----------------------------")
array_2d = np.arange(20).reshape(4, 5)
print(array_2d)

# shuffle on cols
rng.shuffle(array_2d, axis = 1)
print(array_2d)

print("-----------------------------")
# permutation
# *** permutation - do not modify the original array, it returns a new copy

perm = rng.permutation(10)
print(perm)

print("-----------------------------")
array_2d = np.arange(20).reshape(4, 5)
print(array_2d)

# permutation on rows
array_2d_perm_row = rng.permutation(array_2d, axis = 0)
print(array_2d_perm_row)

# permutation on cols
array_2d_perm_col = rng.permutation(array_2d, axis = 1)
print(array_2d_perm_col)

print("-----------------------------")
'''
array_2d:
    [[ 0  1  2  3  4]
    [ 5  6  7  8  9]
    [10 11 12 13 14]
    [15 16 17 18 19]]

permuted rows: axis = 0 - Each column is shuffled independently down the rows.
    [[ 5  1  2 18  9]
    [10 11 17 13 19]
    [15  6 12  3  4]
    [ 0 16  7  8 14]]

permuted cols: axis = 1 - Each row is independently shuffled, row order stays the same
    [[ 0  2  3  1  4]
    [ 9  5  6  7  8]
    [14 12 13 10 11]
    [19 15 17 18 16]]
'''
array_2d = np.arange(20).reshape(4, 5)
print(array_2d)

# permuted - independently permute slices along the given axis
# permutes along rows - Each column is shuffled independently down the rows.
array_2d_permuted_row = rng.permuted(array_2d, axis = 0)
print(array_2d_permuted_row)

# permuted - change the elements order of each row, but keep row order
array_2d_permuted_col = rng.permuted(array_2d, axis = 1)
print(array_2d_permuted_col)