
import numpy as np

result = np.divide(1, 0)
print(result) # inf -> an infinite number

print("--------------isfinite------------")
isfinite = np.isfinite(result)
print(isfinite) # False

print("--------------isinf------------")
isinf = np.isinf(result)
print(isinf) # True


result = np.divide(-1, 0)
print(result) # -inf

print("--------------isneginf------------")
isneginf = np.isneginf(result)
print(isneginf) # True


print("--------------isnan------------")
result = np.log(-1)
print(result) # nan -> not a number

isnan = np.isnan(result)
print(isnan) # True


print("--------------floor------------")
# round down
floor = np.floor([-3.6, 2.7, 0.4, 7.0])
print(floor) # [-4.  2.  0.  7.]


print("--------------ceil------------")
# round up
ceil = np.ceil([-3.6, 2.7, 0.4, 7.0])
print(ceil) # [-3.  3.  1.  7.]

print("--------------trunc------------")
# truncate the numbers
trunc = np.trunc([-3.6, 2.7, 0.4, 7.0])
print(trunc) # [-3.  2.  0.  7.]