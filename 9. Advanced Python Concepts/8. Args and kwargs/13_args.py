
'''
order matters:

    - func(a, b, *args)
    - func(a, b, *args, **kwargs)
    - func(*args, **kwargs)
    - invalid: func(*args, a)
'''


# nums -> args
def sum(*nums): 
    # args will be a tuple of all the values passed to sum 
    print(nums)
    print(type(nums))
    total = 0
    for item in nums:
        total += item 
    return total


print(sum(342, 2, 7, 9))