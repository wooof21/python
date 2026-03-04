
import numpy as np

list_3d =     [
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

array_3d = np.array(list_3d)

print(array_3d.shape)

print(array_3d[0])
print(array_3d[1])

print(array_3d[1][2])

print(array_3d[1][2][1])

print("------------------------------------")
# : -> access all elements - same as array_3d
print(array_3d[:])

print("------------------------------------")
# access elements from all depth, and row 1 and row 2
print(array_3d[:, [1, 2]])

# access elements from all depth, and row 0 and row 2
print(array_3d[:, [0, 2]])

print("------------------------------------")
# access elements by mask
# first depth and third depth
mask = [True, False, True]
print(array_3d[mask])

print("------------------------------------")
# access only even numbers
mask = array_3d % 2 == 0
print(mask)
print(array_3d[mask])