

import numpy as np

'''
Linear Algebra:

1. inner products:
    - 2 vectors of the same size
    - result is a scalar

    [1, 2, 3] * [4, 5, 6] = 1 * 4 + 2 * 5 + 3 * 6 = 32

2. external products:
    - 2 vectors of the same size
    - result is a matrix

    [1, 2, 3] . [4, 5, 6] = [[1*4, 1*5, 1*6], [2*4, 2*5, 2*6], [3*4, 3*5, 3*6]] 
                            = [[4, 5, 6], [8, 10, 12], [12, 15, 18]]

3. matrix products:
    - 2 matrix with compatibale format
        * matrxi_1 shape: (a, b)
        * matrix_2 shape: (b, a)
        * result matrix shape: (a, a)
    - result is a matrix

    [[1, 2, 3],      [[7, 8],         [[1*7 + 2*9 + 3*11, 1*8 + 2*10 + 3*12],    [[58, 64],
    [4, 5, 6]]    X   [9, 10],     =   [4*7 + 5*9 + 6*11, 4*8 + 5*10 + 6*12]   =  [139, 154]]
                      [11, 12]]

4. determinant:
    - calculate the inverse of a matrix
    - must be a square matrix
    - result is a scalar

    [[1, 2, 3],      (1*5*9 + 2*6*7 + 3*4*8)
     [4, 5, 6,],  =  - (3*5*7 + 2*4*9 + 1*6*8)    = 0
     [7, 8, 9]]

5. inverse matrix:
    - sqaure matrix
    - result is a matrix

    A * A^-1 = I

    [[1, 2],       [[a, b],      [[1, 0],
     [3, 4]]   *    [c, d]]   =   [0, 1]]

    [[1*a + 2*c, 1*b + 2*d],     [[1, 0],
     [3*a + 4*c, 3*b + 4*d]]  =   [0, 1]]

     ...

    A^-1 = [[-2, 1],
            [3/2, -1/2]]
'''