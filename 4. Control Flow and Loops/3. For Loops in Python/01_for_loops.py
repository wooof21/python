

# for i in range(1, 6): # range function goes from 1 to (6-1) ie 5 in this case
# left - inclusive, right - exclusive
#     print(i)

for i in range(1, 11):
    print(f"5 X {i} = {5*i}")


print("-------List---------")
list = [1, 3, 5, 7, 9]

for num in list:
    print(f"5 X {num} = {5*num}")


print("-------List Slicing---------")
for num in list[0:4]:  # slicing the list to get first 4 elements
    print(f"5 X {num} = {5*num}")


print("-------List Slicing Step---------")
for num in list[0:5:3]:  # slicing the list to get every third element - list[start:stop:step]
    print(f"5 X {num} = {5*num}")

print("-------List Range---------")
# Using range to iterate through a list
for num in range(0, 4):
    print(f"5 X {list[num]} = {5*list[num]}")