


table_of_5 = {i: 5*i for i in range(1, 11)}

print(table_of_5)

# Adding a condition (filter)
table_even = {i : 5*i for i in range(1, 11) if i % 2 == 0}
print(table_even)

# Transforming an existing dictionary
prices = {"apple": 2, "banana": 3, "orange": 1}

# Apply a 10% discount
discounted = {k: v*0.9 for k, v in prices.items()}
print(discounted)