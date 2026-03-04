

import numpy as np


array_from_list = np.array([1, 2, 3, 4, 5])
print(type(array_from_list))

# Tuple
tuple_a = (1, 2, 3)
print(type(tuple_a))

array_from_tuple = np.array(tuple_a)
print(array_from_tuple)
print(type(array_from_tuple))
print(array_from_tuple.dtype) # int64


set_a = {1, 2, 3, 4, 5, 5, 5}
print(set_a)
print(type(set_a))

array_from_set = np.array(set_a)
print(array_from_set)
print(type(array_from_set))
print(array_from_set.dtype) # object

'''
array_a = array_from_set + 5 # TypeError: unsupported operand type(s) for +: 'set' and 'int'
print(array_a)

array_from_set is a numpy.ndarray

But NumPy arrays have two layers:

    1. The container → ndarray
    2. The dtype → what kind of elements it holds

For set, dtype=object
NumPy cannot guarantee order from a set, so it often falls back to: dtype=object
Each element is a Python object, not a NumPy numeric type.

NumPy vectorized math only works when elements are numeric dtypes (int32, float64, etc).

With dtype=object, NumPy does Python-level addition:
    element + 5
If element is not a pure numeric type (or NumPy can’t safely infer it), then get:
    TypeError: unsupported operand type(s) for +: 'set' and 'int'

Do:

array_from_set = np.array(sorted(set_a))
array_a = array_from_set + 5

If NumPy math behaves weirdly, always check .dtype first.
'''


dict_a = {1: 'a', 2: 'b'}
print(dict_a)
print(type(dict_a))

array_from_dict = np.array(dict_a)
print(array_from_dict)
print(type(array_from_dict))
print(array_from_dict.dtype) # object

