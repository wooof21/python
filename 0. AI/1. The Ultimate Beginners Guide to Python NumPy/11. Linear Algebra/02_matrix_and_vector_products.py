
import numpy as np

rng = np.random.default_rng(seed = 2)

vector_1 = rng.integers(low = -10, high = 10, size = 4)
vector_2 = rng.integers(low = -10, high = 10, size = 4)

matrix_1 = rng.integers(low = -10, high = 10, size = 12).reshape(4, 3)
matrix_2 = rng.integers(low = -10, high = 10, size = 12).reshape(3, 4)
matrix_3 = rng.integers(low = -10, high = 10, size = 12).reshape(4, 3)
matrix_4 = rng.integers(low = -10, high = 10, size = 9).reshape(3, 3)
print(vector_1)
print(vector_2)
print(matrix_1)
print(matrix_2)
print(matrix_3)
print(matrix_4)
'''
vector_1:
[ 6 -5 -8 -5]

vector_2:
[-2  6 -1 -9]

matrix_1:
[[-4  2  6]
 [ 4  9 -7]
 [ 7 -9  1]
 [-5 -6  3]]

matrix_2:
[[-4  1 -5 -7]
 [ 4 -2  3  3]
 [ 8 -2 -6  2]]

matrix_3:
[[  8   9   7]
 [  3  -3  -3]
 [-10  -7  -4]
 [ -4   1   0]]

matrix_4:
[[ 3  7  7]
 [ 5  9 -4]
 [ 8  8 -6]]
'''


print("-------------------dot vector-------------------")
# inner product
dot = np.dot(a = vector_1, b = vector_2)
print(dot) # 11

print("-------------------dot matrix-------------------")
# matrix product
'''
[[ 72 -20 -10  46]
 [-36   0  49 -15]
 [-56  23 -68 -74]
 [ 20   1 -11  23]]
'''
mdot = np.dot(a = matrix_1, b = matrix_2)
print(mdot)

print("-------------------dot matrix with vector-------------------")
mvdot = np.dot(a = matrix_2, b = vector_1)
print(mvdot) # [46 -5 96]

# mvdot = np.dot(a = matrix_1, b = vector_1)
# print(mvdot) # ValueError: shapes (4,3) and (4,) not aligned: 3 (dim 1) != 4 (dim 0)

print("-------------------vdot-------------------")
# inner product: same as dot
vdot = np.vdot(vector_1, vector_2)
print(vdot) # 11


print("-------------------inner-------------------")
# inner product: same as dot
inner = np.inner(vector_1, vector_2)
print(inner) # 11

print("-------------------inner matrix-------------------")
'''
[[ 28 -36   2  18]
 [ 64   6 -75  -7]
 [-18  45 -11 -37]
 [-73  -6  80  14]]
'''
minner = np.inner(matrix_1, matrix_3)
print(minner)


print("-------------------outer-------------------")
'''
[[-12  36  -6 -54]
 [ 10 -30   5  45]
 [ 16 -48   8  72]
 [ 10 -30   5  45]]
'''
# external/outer product
outer = np.outer(vector_1, vector_2)
print(outer)


print("-------------------matmul-------------------")
# multiplcation of matrix
# same as: dot
matmul = np.matmul(vector_1, vector_2)
print(matmul) # 11

print("-------------------matmul matrix-------------------")
'''
[[ 72 -20 -10  46]
 [-36   0  49 -15]
 [-56  23 -68 -74]
 [ 20   1 -11  23]]
'''
mmatmul = np.matmul(matrix_1, matrix_2)
print(mmatmul)


print("-------------------linalg.det-------------------")
# matrix determinate
det = np.linalg.det(matrix_4)
print(det) # -304.00000000000006


print("-------------------linalg.inv-------------------")
'''
[[ 0.07236842 -0.32236842  0.29934211]
 [ 0.00657895  0.24342105 -0.15460526]
 [ 0.10526316 -0.10526316  0.02631579]]
'''
# inverse of matrix
inv = np.linalg.inv(matrix_4)
print(inv)