

import numpy as np

# 1-D array: [1, 2, 3] -> Vector
# 2-D array: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] -> Matrix
# An array with 3 or more demensions is called a -> TENSOR

array_2d = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])

print(array_2d)
print(type(array_2d))
print(array_2d.dtype)

print(array_2d[1]) # [4, 5, 6]
print(array_2d[1][1]) # 5

'''
The number of cols must be same:

array_2d = np.array([
                    [1, 2, 3],
                    [4, 5],
                    [6, 7, 8, 9],
                    [10]
                    ])

ValueError: setting an array element with a sequence. 
The requested array has an inhomogeneous shape after 1 dimensions. 
The detected shape was (4,) + inhomogeneous part.

'''


