

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

print(array_3d[1]) # second depth

print("-------------------------------")
# access array from depth 0 (inclusive) to depth 1 (exclusive)
# same as array_3d[:1]
print(array_3d[0:1])

print("-------------------------------")
# access elements from all depths, and row 1 and row 2
print(array_3d[:, 1:3])

print("-------------------------------")
# access elements from all depths, and row 1 and row 2, and col 0 and col 1
# same as - [:, 1:3, :2]
print(array_3d[:, 1:3, 0:2])

print("-------------------------------")
# access elements from all depths, and row 1 and row 2
# skip (2-1) rows
# same as [:, 1::2]
print(array_3d[:, 1:3:2])
print(array_3d[:, 1::2])

print("-------------------------------")
# access elements from first depth and all rows, and skip (2-1) row
print(array_3d[0, ::2])
# in reverse order
print(array_3d[0, ::-2])

print("-------------------------------")
# access elements from first depth and all rows, and skip (1-1) row in reverse order
print(array_3d[0, ::-1])