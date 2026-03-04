
import numpy as np

# reshape: conver 1D array to ND array
array_3d = np.arange(1, 25).reshape(2, 4, 3)

# convert a numPy array to a Python list

list_a = array_3d.tolist()
print(list_a)
print(type(list_a))

print("----------------------------")
# item: access array item
# passing a tuple data, with index
item = array_3d.item((1, 0, 2))
print(item)

print("----------------------------")
# view
array_view = array_3d.view()
print(array_view)
array_view[0, 0, 0] = 0
print(array_view) # array_view not a copy of array_3d, both pointing to same variable
print(array_3d) # value also changed in original array_3d


print("----------------------------")
# copy: copy original array into a new variable
# they point to different memory location
array_copy = array_3d.copy()
print(array_copy)
array_copy[0, 0, 0] = 999
print(array_copy)
print(array_3d) # value in original array_3d not changed

print("----------------------------")
# fill: replace all value in array
array_3d.fill(88)
print(array_3d)