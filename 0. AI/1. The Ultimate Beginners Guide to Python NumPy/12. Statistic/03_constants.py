

import numpy as np

# e: Euler number
e = np.e
print(e) # 2.718281828459045

pi = np.pi
print(pi) # 3.141592653589793

# infinite number -> 1 / 0 = inf
inf = np.inf
print(inf) # inf

# not a number -> log(-1) = nan
nan = np.nan
print(nan) # nan


array = np.array([1, 2, 3])
print(array.shape) # (3,)
# to add a new dimension
# : -> keep all information from original array
# np.newaxis: add a new axis
newarray = array[:, np.newaxis]
'''
[[1]
 [2]
 [3]]
'''
print(newarray)
print(newarray.shape) # (3, 1)

# add new axis at the end
newarray = array[np.newaxis, :]
print(newarray) # [[1 2 3]]
print(newarray.shape) # (1, 3)