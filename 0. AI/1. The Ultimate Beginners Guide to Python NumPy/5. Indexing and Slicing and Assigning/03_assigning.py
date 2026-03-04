
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

# access element by index
# same as [1, 1, 0]
print(array_3d[1][1][0])
print(array_3d[1, 1, 0])

# to change the value
array_3d[1][1][0] = 0
print(array_3d)

print("-----------------------")
print(array_3d[:, :2, :1])
array_3d[:, :2, :1] = [[[ 888],
                        [ 888]],

                        [[888],
                        [888]],

                        [[888],
                        [888]]]
print(array_3d)

print("-----------------------")
array_3d[0] = 999
print(array_3d)