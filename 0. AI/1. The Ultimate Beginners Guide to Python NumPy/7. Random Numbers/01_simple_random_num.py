
import numpy as np

# install library: pip instanll matplotlib
# used to generate graphs in Python to visualize the data

import matplotlib.pyplot as plt

'''
1. create an Random number generator instance: rng
2. then generate random numbers from rng

seed: initializes the internal state of the generator.

with seed:
    rng1 = np.random.default_rng(seed=1)
    rng2 = np.random.default_rng(seed=1)

then:
    rng1.random() == rng2.random() - always true

Without a seed:
    rng = np.random.default_rng()
get different results every run.

With a seed:
    rng = np.random.default_rng(1)
get the same sequence every time. - Reproducibility

That’s critical for:

    - debugging
    - research papers
    - reproducible experiments
    - production consistency

'''
rng = np.random.default_rng(seed = 1)

ran_num = rng.random() # same num every run
print(ran_num)

print("-----------------------------")

# generate random numbers array in range [0, 1)
ran_nums = rng.random(size = 5)
print(ran_nums)

print("-----------------------------")

# generate random numbers matrix
ran_nums_matrix = rng.random(size = (3, 5))
print(ran_nums_matrix)

print("-----------------------------")

# generate random integers in range [0, 3)
ran_nums_int = rng.integers(3, size = 5)
print(ran_nums_int)

print("-----------------------------")

# generate random integers with range [low, high)
ran_nums_int = rng.integers(low = 3, high = 8, size = 5)
print(ran_nums_int)

print("-----------------------------")

# nums from range [3, 5), [3, 8), [3, 14)
ran_nums_int = rng.integers(low = 3, high = [5, 8, 14])
print(ran_nums_int)

print("-----------------------------")

# select random numbers from an array
array = np.arange(0, 8)
print(array)

print("-----------------------------")

rng_choice = rng.choice(a = array)
print(rng_choice)

print("-----------------------------")

# select 10 nums from array
rng_choice_size = rng.choice(a = array, size = 10)
print(rng_choice_size)

print("-----------------------------")

# without duplicate values, need to becareful with `size`
# Cannot take a larger sample than population when replace is False
rng_choice_size = rng.choice(a = array, size = 8, replace = False)
print(rng_choice_size)

print("-----------------------------")

# with probabilities
array = np.array([1, 2, 3, 4, 5])
# specify the probabilities of each being selected
# sum must be equal to 1
p = np.array([0.2, 0.1, 0.1, 0.1, 0.5])

ran_num_prob = rng.choice(a = array, size = 8, p = p)
print(ran_num_prob)

print("-----------------------------")

array_2d = np.arange(0, 20).reshape(4, 5)
print(array_2d)
# select 2 nums with axis = 0 (rows) - select 2 random rows
ran_choice = rng.choice(a = array_2d, size = 2, axis = 0)
print(ran_choice)

# select 2 random cols
ran_choice = rng.choice(a = array_2d, size = 2, axis = 1)
print(ran_choice)