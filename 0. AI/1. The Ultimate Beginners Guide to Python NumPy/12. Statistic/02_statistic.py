

import numpy as np

rng = np.random.default_rng(seed = 5)

vector_1 = rng.integers(low = -10, high = 10, size = 4)
matrix_1 = rng.integers(low = -10, high = 10, size = 12).reshape(4, 3)

print(vector_1)
print(matrix_1)

print("---------------percentile---------------")
# q -> 10% of the data
percentile = np.percentile(a = vector_1, q = 10)
print(percentile) # -6.1

percentile = np.percentile(a = vector_1, q = 50) # median
print(percentile) # 4.5

mpercentile = np.percentile(a = matrix_1, q = 10)
print(mpercentile) # -8.9

mpercentile = np.percentile(a = matrix_1, q = 50) # median
print(mpercentile) # -2.5

print("---------------quantile---------------")
quantile = np.quantile(a = vector_1, q = 0.1) # 10% of the data
print(quantile) # -6.1

quantile = np.quantile(a = vector_1, q = 0.5) # median
print(quantile) # 4.5

mquantile = np.quantile(a = matrix_1, q = 0.1)
print(mquantile) # -8.9

mquantile = np.quantile(a = matrix_1, q = 0.1, axis = 1)
print(mquantile) # [-0.8 -8.2 -4.6 -9.6]

mquantile = np.quantile(a = matrix_1, q = 0.5) # median
print(mquantile) # -2.5

# quantile of each rows
mquantile = np.quantile(a = matrix_1, q = 0.5, axis = 1) # median
print(mquantile) # [ 0. -5. -3. -8.]

print("---------------median---------------")
# same as: quantile = np.quantile(a = vector_1, q = 0.5)
# and: percentile = np.percentile(a = vector_1, q = 50)
median = np.median(a = vector_1)
print(median) # 4.5

# median of each row
mmedian = np.median(a = matrix_1, axis = 1)
print(mmedian) # [ 0. -5. -3. -8.]

print("---------------mean---------------")
# mean: total sum of all values / total count 
# (3 + 6 + (-10) + 6) / 4 = 1.25
mean = np.mean(a = vector_1)
print(mean) # 1.25

# mean of each row
mmean = np.mean(a = matrix_1, axis = 1)
print(mmean) # [ 0.33333333 -1.66666667 -2.33333333 -6.66666667]

print("---------------average---------------")
# calculate the mean and apply the weights to each value
# weights sum MUST BE equal to 1
average = np.average(a = vector_1, weights = [0.15, 0.25, 0.4, 0.2])
print(average) # -0.8499999999999996

# same as: np.mean(a = vector_1)
average = np.average(a = vector_1)
print(average) # 1.25

print("---------------std---------------")
# standard deviation: in average, the values from the arrays are far away from the mean (1.25)
# 6.6 Standard Deviation units
std = np.std(a = vector_1)
print(std) # 6.609652033201143

# standard deviation of each row
mstd = np.std(a = matrix_1, axis = 1)
print(mstd) # [1.24721913 7.7172246  2.49443826 3.39934634]

print("---------------var---------------")
# standard deviation = sqrt(variance)
var = np.var(a = vector_1)
print(var) # 43.6875

# variance of each row
mvar = np.var(a = matrix_1, axis = 1)
print(mvar) # [ 1.55555556 59.55555556  6.22222222 11.55555556]

print("---------------cov---------------")
# covariance of the variable itself
cov = np.cov(m = vector_1)
print(cov) # 58.25

vector_2 = vector_1 * 3

cov = np.cov(m = vector_2)
print(cov) # 524.25

'''
[[ 58.25 174.75]
 [174.75 524.25]]
'''
# covariance of 2 variables
cov = np.cov(m = vector_1, y = vector_2)
print(cov)
 
print("---------------corrcoef---------------")
'''
[[1. 1.]
 [1. 1.]]
'''
# Pearson correlation: calculate the similarity between variables
# correlation with itself
corrcoef = np.corrcoef(x = vector_1, y = vector_1)
print(corrcoef)

'''
[[1. 1.]
 [1. 1.]]
'''
# same result: since vector_2 is created by vector_1 * 3
corrcoef = np.corrcoef(x = vector_1, y = vector_2)
print(corrcoef)


print("---------------histogram---------------")
# histogram: calculate the distribution of the data
vector_3 = rng.integers(low = -10, high = 10, size = 100)
print(vector_3)

'''
hist: quantity of the data
bin_edge: intervals

28 data in interval (-10, -5.25)
24 data in interval (-5.25, -0.5) ...
'''

hist, bin_edge = np.histogram(a = vector_3, bins = 4)
print(hist) # [28 24 19 29]
print(bin_edge) # [-10.    -5.25  -0.5    4.25   9.  ]

print("---------------bincount---------------")

vector_4 = np.arange(6)
print(vector_4)

bincount = np.bincount(vector_4)
print(bincount) # [1 1 1 1 1 1]

vector_5 = rng.integers(low = 0, high = 10, size = 6)
print(vector_5)

bincount = np.bincount(vector_5)
print(bincount) # [0 1 0 1 0 0 2 1 0 1]