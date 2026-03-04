
# concatenate strings

# 1. Using + Operator
a = "Hello"
b = "World"
result = a + " " + b
print(result)  # Hello World

# 2. Using f-strings (formatted string literals) — Best for readability (Python 3.6+)
name = "Alice"
greeting = f"Hello, {name}!"
print(greeting)  # Hello, Alice!

# 3. Using join() (Efficient for many strings)
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # Python is awesome

# 4. Using % Operator (Old style)
language = "Python"
print("I love %s!" % language)  # I love Python!

# 5. Using str.format()
framework = "Django"
print("I use {} for web development.".format(framework))

# ** Don't use + in loops for many strings:
# Bad: Inefficient for large concatenations
s = ""
for i in range(1000):
    s += str(i)
# Good: Use join() for better performance
s = "".join(str(i) for i in range(1000)) # ✅ Efficient

"a" + 3  # TypeError: can only concatenate str (not "int") to str
# Python does not automatically convert types when using the + operator for strings. 
# Both operands must be strings.

# To fix, convert the number to a string first
result = "a" + str(3)    # "a3"
print(result)

# With f-string (cleaner way):
result = f"a{3}"         # "a3"