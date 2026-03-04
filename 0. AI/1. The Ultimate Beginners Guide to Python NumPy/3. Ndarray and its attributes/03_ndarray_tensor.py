

import numpy as np

# An array with 3 or more demensions is called a TENSOR

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

print(array_3d)
# (depth, rows, cols)
print(array_3d.shape)
print(type(array_3d))

print(array_3d[1][1][1]) # 15