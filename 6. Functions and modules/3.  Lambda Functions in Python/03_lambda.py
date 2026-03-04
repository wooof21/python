


'''
A lambda function in Python is a small, anonymous (unnamed) function defined using the lambda keyword.

Syntax:

lambda arguments: expression

Used with map(), filter(), sorted()

1. map() with lambda

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)  # [1, 4, 9, 16]

2. filter() with lambda

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2, 4]

3. sorted() with lambda (custom sort)

words = ['banana', 'apple', 'cherry']
sorted_by_len = sorted(words, key=lambda x: len(x))
print(sorted_by_len)  # ['apple', 'banana', 'cherry']

4. Inline use

print((lambda x: x ** 3)(4))  # 64

When to Use (and Not Use)

Use lambda when:

    - The function is simple
    - It's used once or in a short scope (like in map, filter, etc.)

Avoid lambda when:

    - The function is complex
    - It needs more readability/debugging
'''


square = lambda x: x*x 
'''
As good as writing
def square(x):
    return x*x
'''
sum = lambda x, y: x+y
'''
As good as writing
def sum(x, y):
    return x + y
'''

print(square(3))
print(sum(3, 62))

# Sorting a list of tuples by second value:

pairs = [(1, 5), (2, 3), (4, 1)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # [(4, 1), (2, 3), (1, 5)]