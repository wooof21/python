
import numpy as np

rng = np.random.default_rng(seed = 2)

array_1 = rng.integers(low = -10, high = 10, size = 20).reshape(4, 5)

array_2 = rng.integers(low = -10, high = 10, size = 20).reshape(4, 5)

print(array_1)
print(array_2)

# np.add, np.subtract, np.multiply, np.divide
# same using Python operator: array_1 + array_2
array = np.add(array_1, array_2)
print(array)

# array_1 - array_2
array = np.subtract(array_1, array_2)
print(array)

# array_1 * array_2
array = np.multiply(array_1, array_2)
print(array)

# array_1 / array_2
array = np.divide(array_1, array_2)
print(array)

array = np.add(array_1, 100)
print(array)

print("------------------mod--------------------")
# array_1 % 2
array = np.mod(array_1, 2)
print(array)

print("------------------divmod--------------------")
# (div_result, mod_result)
array = np.divmod(array_1, 2)
print(type(array)) # <class 'tuple'>
print(array)


print("------------------absolute--------------------")
array = np.absolute(array_1)
print(array)

print("------------------diff--------------------")
'''
array_1:
[[ 6 -5 -8 -5 -2]
 [ 6 -1 -9 -4  2]
 [ 6  4  9 -7  7]
 [-9  1 -5 -6  3]]

array diff:
[[-11  -3   3   3]
 [ -7  -8   5   6]
 [ -2   5 -16  14]
 [ 10  -6  -1   9]]

-11 = -5 - (6), -3 = -8 - (-5)

difference of each adjecent cell - default col direction

axis = 0:
[[  0   4  -1   1   4]
 [  0   5  18  -3   5]
 [-15  -3 -14   1  -4]]

difference on col direction

n = 2:
[[  8   6   0]
 [ -1  13   1]
 [  7 -21  30]
 [-16   5  10]]

difference of difference
'''
array = np.diff(a = array_1)
print(array)

array = np.diff(a = array_1, axis = 0)
print(array)

# same: array = np.diff(a = array_1)
array = np.diff(a = array_1, n = 1)
print(array)

# n = 2, difference of difference
array = np.diff(a = array_1, n = 2)
print(array)

print("------------------power--------------------")
array = np.power(array_1, 2) # power of 2
'''
[[36 25 64 25  4]
 [36  1 81 16  4]
 [36 16 81 49 49]
 [81  1 25 36  9]]

same as array_1 ** 2
'''
print(array)

'''
[[  36   25   64   25    4]
 [  36    1   81   16    4]
 [ 216   64  729 -343  343]
 [-729    1 -125 -216   27]]

first 2 rows: power of 2
last 2 rows: power of 3
'''
array = np.power(array_1, [[2], [2], [3], [3]])
print(array)

'''
[[  36   25 -512 -125   -8]
 [  36    1 -729  -64    8]
 [  36   16  729 -343  343]
 [  81    1 -125 -216   27]]

power on col direction: 
first 2 cols: power of 2
last 3 cols: power of 3
'''
array = np.power(array_1, [2, 2, 3, 3, 3])
print(array)

print("------------------exp--------------------")
'''
[[4.03428793e+02 6.73794700e-03 3.35462628e-04 6.73794700e-03
  1.35335283e-01]
 [4.03428793e+02 3.67879441e-01 1.23409804e-04 1.83156389e-02
  7.38905610e+00]
 [4.03428793e+02 5.45981500e+01 8.10308393e+03 9.11881966e-04
  1.09663316e+03]
 [1.23409804e-04 2.71828183e+00 6.73794700e-03 2.47875218e-03
  2.00855369e+01]]
'''
e = np.e
print(e) # 2.718281828459045
array = np.exp(array_1) # calculate e**value
print(array)

print("------------------log--------------------")
'''
[[1.79175947        nan        nan        nan        nan]
 [1.79175947        nan        nan        nan 0.69314718]
 [1.79175947 1.38629436 2.19722458        nan 1.94591015]
 [       nan 0.                nan        nan 1.09861229]]

logarithm
'''
array = np.log(array_1)
print(array)

print("------------------reciprocal--------------------")
array = np.reciprocal(array_1)
# converting numbers to integer
'''
[[ 0  0  0  0  0]
 [ 0 -1  0  0  0]
 [ 0  0  0  0  0]
 [ 0  1  0  0  0]]
'''
print(array)

'''
[[ 0.16666667 -0.2        -0.125      -0.2        -0.5       ]
 [ 0.16666667 -1.         -0.11111111 -0.25        0.5       ]
 [ 0.16666667  0.25        0.11111111 -0.14285714  0.14285714]
 [-0.11111111  1.         -0.2        -0.16666667  0.33333333]]
'''
# convert to float
# same as: 1 / array_1
array = np.reciprocal(array_1.astype(float))
print(array)

print("------------------sqrt--------------------")
# square root
array = np.sqrt(array_1)
print(array)

print("------------------cbrt--------------------")
# cubic root
array = np.cbrt(array_1)
print(array)

print("------------------gcd--------------------")
'''
greatest common divisor:

[[2 1 1 1 2]
 [2 1 3 4 2]
 [6 2 1 1 7]
 [3 1 1 2 1]]
'''
array = np.gcd(array_1, array_2)
print(array)

print("------------------lcm--------------------")

'''
lowest common multiple:

[[12  5 40 35  4]
 [ 6  3  9  8  2]
 [ 6  4 72 63  7]
 [ 9  3 15 30 21]]
'''
array = np.lcm(array_1, array_2)
print(array)