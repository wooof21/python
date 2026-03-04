

'''
Suppose a dataset that contains the age of 20 people:

15 - 16: 1          16 - 17: 1          18 - 19: 3 
20 - 21: 2          21 - 22: 3          22 - 23: 5
23 - 24: 1          25 - 26: 2          26 - 27: 1
27 - 28: 1

1. Percentile/quantile: value that delimits a percentage or a fraction of the data.

15 - 17: 2 -> 2 / 20 = 10% = 0.1
           -> percentile = 10 
           -> quantile = 0.1
    -> given: percentile = 25 / quantile = 0.25 
    -> x / 20 = 0.25 
    -> x = 5
    -> select the 5 elements from dataset

    -> given: percentile = 50 / quantile = 0.5 -> Median
    -> x / 20 = 0.5 
    -> x = 10
    -> select the 10 elements from dataset+

2. Variance and standard deviation: measure the dispersion of the data in relation to the mean

3. Covariance: relates the variance between 2 variables

4. Pearson coefficient: another measure of covariance between 2 variables

'''