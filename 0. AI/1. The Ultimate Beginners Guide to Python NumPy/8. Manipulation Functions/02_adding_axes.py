
import numpy as np

array_2d_0 = np.arange(0, 18).reshape(3, 6)
print(array_2d_0)
print(array_2d_0.ndim) # 2
print(array_2d_0.shape) # (3, 6)

print("----------------add axis 0--------------------")
# add a new axis at beginning
array_2d = np.expand_dims(a = array_2d_0, axis = 0)
print(array_2d)
print(array_2d.ndim) # 3
print(array_2d.shape) # (1, 3, 6)

print("-----------------remove axis------------------")
squeeze = np.squeeze(array_2d)
print(squeeze.shape) # (3, 6)

print("----------------add axis 1--------------------")
# add a new axis at beginning
array_2d = np.expand_dims(a = array_2d_0, axis = 1)
print(array_2d)
print(array_2d.ndim) # 3
print(array_2d.shape) # (3, 1, 6)

print("-----------------remove axis------------------")
squeeze = np.squeeze(array_2d)
print(squeeze.shape) # (3, 6)

print("----------------add axis 2--------------------")
# add a new axis at beginning
array_2d = np.expand_dims(a = array_2d_0, axis = 2)
print(array_2d)
print(array_2d.ndim) # 3
print(array_2d.shape) # (3, 6, 1)

print("-----------------remove axis------------------")
squeeze = np.squeeze(array_2d)
print(squeeze.shape) # (3, 6)

print("-----------------another way 0------------------")
# `:` -> keep all values of the array
array_2d = array_2d_0[np.newaxis, :]
print(array_2d)
print(array_2d.shape) # (1, 3, 6)

print("-----------------another way 1------------------")
# `:` -> keep first part of array, add a new dimentsion in the middle
# then keep all values of last part
# same as: array_2d_0.reshape(3, 1, 6)
array_2d = array_2d_0[:, np.newaxis, :]
print(array_2d)
print(array_2d.shape) # (3, 1, 6)

print("-----------------another way 2------------------")

array_2d = array_2d_0[:, :, np.newaxis]
print(array_2d)
print(array_2d.shape) # (3, 6, 1)
