
import numpy as np

rng = np.random.default_rng(seed = 2)

array_1 = rng.integers(low = -10, high = 10, size = 20).reshape(4, 5)

array_2 = rng.integers(low = -10, high = 10, size = 20).reshape(4, 5)

print(array_1)
print(array_2)

print("----------------maximum--------------------")
'''
[[ 6  1 -5 -5  4]
 [ 6  3  3  8  2]
 [ 6  4  9  9  7]
 [ 3  1 -3 -6  3]]

return the maximum value of 2 arrays in each position
'''
array = np.maximum(array_1, array_2)
print(array)


print("----------------minimum--------------------")
'''
[[ -4  -5  -8  -7  -2]
 [ -2  -1  -9  -4  -2]
 [ -6   2   8  -7   7]
 [ -9  -3  -5 -10  -7]]
'''
array = np.minimum(array_1, array_2)
print(array)

print("----------------greater--------------------")
'''
[[ True False False  True False]
 [ True False False False  True]
 [ True  True  True False False]
 [False  True False  True  True]]

compare values of 2 array at each position, return True or False
same as: array_1 > array_2
'''
array = np.greater(array_1, array_2)
print(array)

print("----------------less_equal--------------------")
'''
[[False  True  True False  True]
 [False  True  True  True False]
 [False False False  True False]
 [ True False  True False False]]

 same as: array_1 <= array_2
'''
array = np.less_equal(array_1, array_2)
print(array)

print("----------------equal--------------------")
'''
[[False False False False False]
 [False False False False False]
 [False False False False  True]
 [False False False False False]]

same as: array_1 == array_2
'''
array = np.equal(array_1, array_2)
print(array)

print("----------------logical_and--------------------")
comparision_1 = array_1 > 0 # all positive values
print(comparision_1)
comparision_2 = np.mod(array_2, 2) == 0 # all even values
print(comparision_2)
'''
comparision_1:

[[ True False False False False]
 [ True False False False  True]
 [ True  True  True False  True]
 [False  True False False  True]]

 comparision_2:

[[ True False False False  True]
 [ True False False  True  True]
 [ True  True  True False False]
 [False False False  True False]]

array:
[[ True False False False False]
 [ True False False False  True]
 [ True  True  True False False]
 [False False False False False]]
'''
# True only if BOTH are True: all positive values AND all even values
# same as: comparision_1 & comparision_2
array = np.logical_and(comparision_1, comparision_2)
print(array)
print("----------------logical_or--------------------")
'''
[[False  True  True  True  True]
 [False  True  True  True False]
 [False False False  True False]
 [ True False  True  True False]]
'''
# True if at least one is True: all positive values OR all even values
# same as: comparision_1 | comparision_2
array = np.logical_or(comparision_1, comparision_2)
print(array)

print("----------------logical_xor--------------------")
'''
[[False False False False  True]
 [False False False  True False]
 [False False False False  True]
 [False  True False  True  True]]

Truth table:

A	B	XOR
T	T	F
T	F	T
F	T	T
F	F	F
'''
# True if exactly one is True
# same as: comparision_1 ^ comparision_2
array = np.logical_xor(comparision_1, comparision_2)
print(array)


print("----------------logical_not--------------------")
'''
[[False  True  True  True False]
 [False  True  True False False]
 [False False False  True  True]
 [ True  True  True False  True]]
'''
# Negates boolean array: all NOT even (odd) values
# same as: ~comparision_2
array = np.logical_not(comparision_2)
print(array)


print("----------------isclose--------------------")
# 2 similar arrays
array1 = np.array([-1.1558, 0.8994, 3.2894])
array2 = np.array([-1.1557, 0.8993, 3.2895])

# compare each value at same position, check if both values are same
isclose = np.isclose(a = array1, b = array2)
print(isclose) # [False False False]

# atol -> tolerance
# values are within the tolerance margin
isclose = np.isclose(a = array1, b = array2, atol = 0.0001)
print(isclose) # [ True  True  True]

isclose = np.isclose(a = array1, b = array2, atol = 0.001)
print(isclose) # [ True  True  True]

# difference are out of tolerance margin
isclose = np.isclose(a = array1, b = array2, atol = 0.00001)
print(isclose) # [False False False]

print("----------------allclose--------------------")

# checks all values
allclose = np.allclose(a = array1, b = array2)
print(allclose) # False

# same as np.isclose(a = array1, b = array2, atol = 0.00001).all()
allclose = np.allclose(a = array1, b = array2, atol = 0.0001)
print(allclose) # True


print("----------------array_equal--------------------")
array_1 = np.arange(20).reshape(4, 5)
array_2 = np.arange(20).reshape(4, 5)
print(array_1)
print(array_2)

equal = np.array_equal(array_1, array_2)
print(equal) # True