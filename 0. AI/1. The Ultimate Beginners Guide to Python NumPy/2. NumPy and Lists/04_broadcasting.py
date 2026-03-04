
import numpy as np

list_a = [1, 2, 3, 4, 5]

# add 8 to each item in list_a
# list_a + 8 # return error

# to add
list_b = []
for e in list_a:
    list_b.append(e + 8)

print(list_b)

print("-----------NumPy---------------")

array_a = np.array(list_a)
array_b = array_a + 8

print(array_b)

array_c = np.array([[5],
                    [8]])

# shape: (num_of_rows, num_of_cols)
print(array_c.shape)

# mathmatical calculation: array_a + array_c
# (2 rows, 4 cols)
array_d = array_a + array_c
print(array_c[0])
# row1: array_a + array_c[0]
# row2: array_a + array_c[1]
print(array_d)
print(array_d[0][2])

'''
The shape of 2 variables must be compatible inorder to perform the calculations:

array_e = np.array([[1, 2],
                    [3, 4]])

array_a + array_e: ValueError - operands could not be broadcast together with shape (5,), (2, 2)
'''

