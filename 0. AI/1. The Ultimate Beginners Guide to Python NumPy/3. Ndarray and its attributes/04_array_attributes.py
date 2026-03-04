

import numpy as np

'''
    size: return number of elements in the array
    ndim: return number of dimensions
    shape: return a vector
        * another way to get dimensions: len(array.shape)
        * get size: (a, b, c) -> a * b * c
    itemsize: return number of bytes each element occupies
    nbytes: return number of bytes - the amount of memory the variable occupies
        * nbytes = size * itemsize
    dtype: reutrn the data type the elements
'''

array_from_list = np.array([1, 2, 3, 4, 5])

print(array_from_list.size)
print(array_from_list.ndim)
print(array_from_list.shape, len(array_from_list.shape))
print(array_from_list.itemsize)
print(array_from_list.nbytes)
print(array_from_list.dtype)

print("--------------2D Array----------------")

array_2d = np.array([[1, 2, 3], 
                    [4, 5, 6], 
                    [7, 8, 9]])
                    

print(array_2d.size)
print(array_2d.ndim)
print(array_2d.shape, len(array_2d.shape))
print(array_2d.itemsize)
print(array_2d.nbytes)
print(array_2d.dtype)

print("--------------3D Array----------------")

array_3d = np.array(
    [
        # first depth
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        # second depth
        [
            [11, 12, 13],
            [14, 15, 16],
            [17, 18, 19]
        ],
        # third depth
        [
            [21, 22, 23],
            [24, 25, 26],
            [27, 28, 29]
        ]
    ]
)

print(array_3d.size)
print(array_3d.ndim)
print(array_3d.shape, len(array_3d.shape))
print(array_3d.itemsize)
print(array_3d.nbytes)
print(array_3d.dtype)


array_32bits = np.array([1, 2, 3], dtype=np.int32)
print(array_32bits)
print(array_32bits.dtype)
print(array_32bits.itemsize) # 1 byte = 8 bits

array_float32 = np.array([11, 12, 13], dtype=np.float32)
print(array_float32)
print(array_float32.dtype)
print(array_float32.itemsize)

array_float64 = np.array([11, 12, 13], dtype=np.float64)
print(array_float64)
print(array_float64.dtype)
print(array_float64.itemsize)

array_str = np.array([21, 22, 23], dtype=np.str_)
print(array_str)
# <U2 -> NumPy Unicode string dtype.
# < → little-endian
# U → Unicode string
# 2 → maximum length = 2 characters -> since all have 2 characters
# NumPy automatically picks the minimum fixed length that fits all values
print(array_str.dtype) 
print(array_str.itemsize) # 8 -> Unicode in NumPy uses 4 bytes per character

array_str1 = np.array([1, 2, 3], dtype=np.str_)
print(array_str1)
print(array_str1.dtype) 
print(array_str1.itemsize) # 4