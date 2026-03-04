a = 34 
b = "34"
d = 223

print(f"a: {a}")
print(f"type: {type(a)}")

print(f"b: {b}")
print(f"type: {type(b)}")

# Convert b to an integer
c = int(b)
print(f"c: {c}")
print(f"type: {type(c)}")

e = str(d)
print(f"e: {e}")
print(f"type: {type(e)}")

# Convert float to integer
pi = 3.14
pi_int = int(pi)
print(f"pi_int: {pi_int}")
print(f"type: {type(pi_int)}")


x = True
print(type(x) == bool)         # ✅ Works
print(isinstance(x, bool))     # ✅ Better (supports inheritance)


bool(0)         # False
bool(1)         # True
bool("")        # False (empty string)
bool("hello")   # True (non-empty string)
bool([])        # False (empty list)
bool([1, 2])    # True (non-empty list)
bool(None)      # False
bool(3.14)      # True

# Typecasting - converting one data type to another

# int to float
x = 5
y = float(x)     # y = 5.0

# float to int (truncates decimal)
z = int(3.7)     # z = 3

# string to int
s = "42"
n = int(s)       # n = 42

# string to float
f = float("3.14")  # f = 3.14

# number to string
age = 25
text = str(age)  # text = "25"

# list to set
my_list = [1, 2, 3, 1]
my_set = set(my_list)  # {1, 2, 3}

# set to list
unique_list = list(my_set)  # [1, 2, 3]

# Typecasting can fail if the value is not compatible

#int("hello")     #  ValueError
#float("abc123")  #  ValueError

