
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(seed = 1)

# statistical distributions

# generate 10 numbers by beta distribution
beta1 = rng.beta(a = 1, b = 100, size = 10)
print(beta1)

# the lower value with b, the higher numbers will be generated
beta2 = rng.beta(a = 1, b = 10, size = 10)
print(beta2)

'''
plot a histogram to show the distribution of the numbers
larger numbers are positioned on the left
smaller numbers are positioned on the right
bins: plot the graph with 100 intervals to better visualize the data

plt.show():
    Open a separate GUI window and render the figure.
    to show the number distributions
'''
# plt.hist(rng.beta(a = 1, b = 100, size = 100_000), bins = 100)
# plt.show()

print("--------------------------------")
# binomial: generated 8 numbers from range [0, 10] - upper bound inclusive
# with the probabilities of 25% for each number being selected
# only integer numbers are being generated
binomial = rng.binomial(n = 10, p = 0.25, size = 8)
print(binomial)

# plt.hist(rng.binomial(n = 10, p = 0.25, size = 100_000), bins = 100)
# plt.show()

print("--------------------------------")
# chisquare: generates 10 random numbers from a Chi-square distribution
# df = 5 → degrees of freedom
# A Chi-square distribution with k degrees of freedom is:
# The sum of squares of k independent standard normal random variables.
chisquare = rng.chisquare(df = 5, size = 10)
print(chisquare)

# plt.hist(rng.chisquare(df = 5, size = 100_000), bins = 100)
# plt.show()

print("--------------------------------")
# exponential: generates 10 random samples from an Exponential distribution with
# scale = 5
'''
Exponential distribution models:
    1. Waiting time between events
        * Examples:
            - Time until next customer arrives
            - Time until server fails
            - Time between radioactive decay events
    If events occur randomly at constant rate → exponential.

'''
exp = rng.exponential(scale = 5, size = 10)
print(exp)

# plt.hist(rng.exponential(scale = 5, size = 100_000), bins = 100)
# plt.show()


print("--------------------------------")
# gamma: Generates 10 samples from a Gamma distribution
# Gamma is: The sum of k independent exponential random variables (if shape is integer)
gamma = rng.gamma(shape = 5, scale = 2, size = 10)
print(gamma)

# plt.hist(rng.gamma(shape = 5, scale = 2, size = 100_000), bins = 100)
# plt.show()

print("--------------------------------")
# logistic: Generates 10 samples from a Logistic distribution
# loc = 2, positive and negative numbers
# loc = 100, higher lock value, cannot visualize negative value
logistic = rng.logistic(loc = 2, scale = 5, size = 10)
print(logistic)

# plt.hist(rng.logistic(loc = 2, scale = 5, size = 100_000), bins = 100)
# plt.show()

print("--------------------------------")
# normal: Generates 10 samples from a Normal (Gaussian) distribution

normal = rng.normal(loc = 0, scale = 1, size = 10)
print(normal)

# plt.hist(rng.normal(loc = 0, scale = 1, size = 100_000), bins = 100)
# plt.show()

print("--------------------------------")
# uniform: Generates 10 random numbers from a continuous uniform distribution between
# low = 10 → minimum value
# high = 50 → maximum value
# All numbers are equally likely anywhere in [10, 50).

uniform = rng.uniform(low = 10, high = 50, size = 10)
print(uniform)

plt.hist(rng.uniform(low = 10, high = 50, size = 100_000), bins = 100)
plt.show()