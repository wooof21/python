

import numpy as np

array_2d = np.array([[4, 2, 12],
                     [10, 5, 6],
                     [1, 11, 9],
                     [7, 8 ,3]])

# max
# axis = 0 -> get max value by row, compare col direction
max = array_2d.max(axis = 0)
print(max) # [10 11 12]
# axis = 1 -> get max value by col, compare row direction
max = array_2d.max(axis = 1)
print(max) # [12 10 11  8]
# keepdims = True -> keep original dimensions
max = array_2d.max(axis = 1, keepdims = True)
print(max) # [[12][10][11][8]] - matrix
# get max value from whole array
max = array_2d.max()
print(max) # 12

print("---------------------------")
# argmax - return indices instead of the value itself
argmax = array_2d.argmax(axis = 0)
print(argmax) # [1 2 0]
argmax = array_2d.argmax(axis = 1)
print(argmax) # [2 0 1 1]
argmax = array_2d.argmax() 
print(argmax) # 2

print("---------------------------")
# min
min = array_2d.min() 
print(min) # 1
min = array_2d.min(axis = 0)
print(min) # [1 2 3]
min = array_2d.min(axis = 1)
print(min) # [2 5 1 3]


print("---------------------------")
# argmin: return indices instead of the value itself
argmin = array_2d.argmin() 
print(argmin) # 6
argmin = array_2d.argmin(axis = 0)
print(argmin) # [2 0 3]
argmin = array_2d.argmin(axis = 1)
print(argmin) # [1 1 0 2]

print("---------------------------")
# ptp (peak to peak): compute max(array) - min(array)
ptp = np.ptp(array_2d)
print(ptp) # 11

print("---------------------------")
# clip 
# set all values lower than min to min
# set all values greater than max to max
array_2d_1 = np.arange(1, 13).reshape(4, 3)
print(array_2d_1)
clip = array_2d_1.clip(min = 3, max = 9)
print(clip) # [[3 3 3][4 5 6][7 8 9][9 9 9]]

print("---------------------------")
# round
array_2d_lin = np.linspace(0, 1, 12).reshape(4, 3)
'''
[[0.         0.09090909 0.18181818]
 [0.27272727 0.36363636 0.45454545]
 [0.54545455 0.63636364 0.72727273]
 [0.81818182 0.90909091 1.        ]]

 round each array item with decimal points:
 [[0.   0.09 0.18]
 [0.27 0.36 0.45]
 [0.55 0.64 0.73]
 [0.82 0.91 1.  ]]
'''
print(array_2d_lin)
round = array_2d_lin.round(decimals = 2)
print(round)

print("---------------------------")
print(array_2d_1)
# sum
# axis = 0 -> sum all values by row, from col direction
# axis = 1 -> sum all values by col, from row direction
sum = array_2d_1.sum(axis = 0)
print(sum) # [22 26 30]
sum = array_2d_1.sum(axis = 1)
print(sum) # [ 6 15 24 33]
# sum all numbers in the whole array
sum = array_2d_1.sum()
print(sum) # 78

print("---------------------------")
print(array_2d_1)
# cumsum
'''
array_2d_1:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

 cumsum, axis = 0: cumulative sum by row, from col direction
[[ 1  2  3]
 [ 5  7  9]
 [12 15 18]
 [22 26 30]]

 cumsum, axis = 1: cumulative sum by col, from row direction
[[ 1  3  6]
 [ 4  9 15]
 [ 7 15 24]
 [10 21 33]]

 with axis: flat ND array and do cumulative sum
 [ 1  3  6 10 15 21 28 36 45 55 66 78]
'''
cumsum = array_2d_1.cumsum(axis = 0)
print(cumsum)
cumsum = array_2d_1.cumsum(axis = 1)
print(cumsum)
cumsum = array_2d_1.cumsum()
print(cumsum) # [ 1  3  6 10 15 21 28 36 45 55 66 78]

print("---------------------------")
# mean: sum_of_total_num / total_num_count
# axis = 0 -> col direction
# axis = 1 -> row direction
mean = array_2d_1.mean(axis = 0)
print(mean) # [5.5 6.5 7.5]
mean = array_2d_1.mean(axis = 1)
print(mean) # [ 2.  5.  8. 11.]
mean = array_2d_1.mean()
print(mean) # 6.5

print("---------------------------")
# var: variance -> how much the values vary from the mean
# statistics concept
variance = array_2d_1.var(axis = 0)
print(variance) # [11.25 11.25 11.25]
variance = array_2d_1.var(axis = 1)
print(variance) # [0.66666667 0.66666667 0.66666667 0.66666667]
variance = array_2d_1.var()
print(variance) # 11.916666666666666


print("---------------------------")
# std: standard deviation
# statistics concept
std = array_2d_1.std(axis = 0)
print(std) # [3.35410197 3.35410197 3.35410197]
std = array_2d_1.std(axis = 1)
print(std) # [0.81649658 0.81649658 0.81649658 0.81649658]
# in average, the data is far from the mean by 3.45 standard deviations
std = array_2d_1.std()
print(std) # 3.452052529534663

print("---------------------------")
print(array_2d_1)
# prod
'''
similar to sum: prod calculate product of numbers
'''
prod = array_2d_1.prod(axis = 0)
print(prod) # [ 280  880 1944]
prod = array_2d_1.prod(axis = 1)
print(prod) # [   6  120  504 1320]
# sum all numbers in the whole array
prod = array_2d_1.prod()
print(prod) # 479001600

print("---------------------------")
# cumprod
print(array_2d_1)
'''
array_2d_1:
[[ 1  2  3]
 [ 4  5  6]
 [ 7  8  9]
 [10 11 12]]

 axis = 0:
 [[   1    2    3]
 [   4   10   18]
 [  28   80  162]
 [ 280  880 1944]]

 axis = 1:
 [[   1    2    6]
 [   4   20  120]
 [   7   56  504]
 [  10  110 1320]]

 withour axis:
 [        1         2         6        24       120       720      5040
     40320    362880   3628800  39916800 479001600]
'''
cumprod = array_2d_1.cumprod(axis = 0)
print(cumprod)
cumprod = array_2d_1.cumprod(axis = 1)
print(cumprod)
cumprod = array_2d_1.cumprod()
print(cumprod)

print("---------------------------")
# all
print(array_2d_1)
array_2d_gt_0 = array_2d_1 > 0
'''
array_2d_gt_0: return an array comparing each value if > 0, set to True or False

[[ True  True  True]
 [ True  True  True]
 [ True  True  True]
 [ True  True  True]]

array_2d_gt_5: 

 [[False False False]
 [False False  True]
 [ True  True  True]
 [ True  True  True]]

'''
print(array_2d_gt_0)
# check all values in array, retrun True if all True
print(array_2d_gt_0.all()) # True

print(array_2d_gt_0.all(axis = 0)) # [ True  True  True]
print(array_2d_gt_0.all(axis = 1)) # [ True  True  True  True]

array_2d_gt_5 = array_2d_1 > 5
print(array_2d_gt_5)

print(array_2d_gt_5.all()) # False

print(array_2d_gt_5.all(axis = 0)) # [False False False]
print(array_2d_gt_5.all(axis = 1)) # [False False  True  True]


print("---------------------------")
# any
# check if any value in array, retrun True if any value is True
print(array_2d_gt_5.any()) # True
print(array_2d_gt_5.any(axis = 0)) # [ True  True  True]
print(array_2d_gt_5.any(axis = 1)) # [False  True  True  True]


