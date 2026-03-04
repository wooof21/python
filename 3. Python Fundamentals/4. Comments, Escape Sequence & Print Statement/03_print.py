

print('Hello World', "John", 5)
print('Hello World', "John", 5, sep=",")
print('Hello World', "John", 5, sep=", ")

print("Hello World", end=", ")
print("John")
print("Doe")

print('Hello World', end="..")
print('John', end="//")
print("Hello", "World", sep=", ", end="!")

# By default, print() ends with a newline:
# But if override 'end', it changes what gets printed at the end of that line:
# print("John", end="//")  # ends with "//" instead of a newline
# print("Hello", "World", sep=", ", end="!") - out: John//Hello, World!

# Want a newline after both? Use end="\n" explicitly 
# (or omit it, since "\n" is the default):
print("John", end="//\n")
print("Hello", "World", sep=", ", end="!\n")