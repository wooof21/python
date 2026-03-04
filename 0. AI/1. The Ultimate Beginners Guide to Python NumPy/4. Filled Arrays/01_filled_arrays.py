

import numpy as np

# array filled with values

zeros = np.zeros(shape = 3)

print(zeros)
print(zeros.dtype) # default = float64

zero_matrix = np.zeros(shape = (2, 3))
print(zero_matrix)

ones = np.ones(shape = 3)
print(ones)

# fill with custom values
full = np.full(shape = (3, 3), fill_value = 5)
print(full)

array_a = np.array([[1, 2, 3],
                    [4, 5, 6]])
print(array_a.shape)

array_b = np.zeros_like(a = array_a)
# create a new array with same structure as array_a but fill with zeros
print(array_b)

array_c = np.ones_like(a = array_a)
print(array_c)

array_d = np.full_like(a = array_a, fill_value = 5)
print(array_d)

# empty
# values -> memory address
empty = np.empty(shape = (2, 3))
print(empty)

# eye
# create a matrix: 5 rows and 5 cols
# main diagonal of matrix filled with ones
# other cells filled with zeros
eye = np.eye(N = 5)
print(eye)

# specify number of rows and cols
# N -> row, M -> col
e = np.eye(N = 3, M = 5)
print(e)


# identity
# similar to eye, but it only support creating a square identity matrix only
identity = np.identity(n = 5)
print(identity)


# arange
arange = np.arange(stop = 8) 
print(arange) # [0 1 2 3 4 5 6 7]

ar = np.arange(start = 1, stop = 8) 
print(ar) # [1 2 3 4 5 6 7]

ar1 = np.arange(start = 1, stop = 10, step = 3)
print(ar1) # [1 4 7]

ar2 = np.arange(start = 10, stop = 3, step = -1)
print(ar2) # [10  9  8  7  6  5  4]

ar3 = np.arange(start = 3, stop = 5, step = 0.25)
print(ar3) # [3.   3.25 3.5  3.75 4.   4.25 4.5  4.75]

# linspace -> Return evenly spaced numbers over a specified interval.
linspace = np.linspace(start = 1, stop = 8, num = 5)
print(linspace) # [1.   2.75 4.5  6.25 8.  ]

# logspace
# Return numbers spaced evenly on a log scale.
# In linear space, the sequence starts at base ** start (base to the power of start) 
# and ends with base ** stop (see endpoint below).
logspace = np.logspace(start = 1, stop = 4, num = 4)
print(logspace) # [   10.   100.  1000. 10000.]

# geomspace
# Return numbers spaced evenly on a log scale (a geometric progression).
# This is similar to logspace, but with endpoints specified directly. 
# Each output sample is a constant multiple of the previous.
geomspace = np.geomspace(start = 10, stop = 10_000, num = 4)
print(geomspace) # [   10.   100.  1000. 10000.]

# to visulize the scientific notation, conver to integer type
geo = np.geomspace(start = 3, stop = 48_000, num = 6).astype(int)
# start, 3 ^ x = 20, 20 ^ x = 144, 144 ^ x = 999, 999 ^ x = 6924, 6924 ^ x = 48_000
# function itself will calculate x value
print(geo) # [    3    20   144   999  6924 48000]