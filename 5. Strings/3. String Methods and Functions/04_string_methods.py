

s = "hello world" # Strings are immutable

# s[0] = "R" # You cannot do this

'''
You can reassign the variable, but not modify the string in place
reassign a new string in a new memory location
Any "change" to a string results in a new string object being created in memory.

s = "new string" 

1. "hello world" is created in memory.
2. s points to "hello world".
3. Then reassign s = "new string":
    - "new string" is created in memory.
    - s now points to "new string".
    - The reference to "hello world" is removed.
4. The original "hello world" string remains unchanged in memory until garbage collected.
'''


a = len(s)
print(a)
print(s.upper(), s) # Output: "HELLO WORLD hello world" - s.upper() + original string (not changed)
print(s.lower()) # Output: "hello world" - all characters lowercased
print(s.capitalize()) # Output: "Hello world" - first letter capitalized, rest lowercased
print(s.title()) # Output: "Hello World" - first letter of each word capitalized

print("---------Strip----------")

text = " \nhello world "
print(text.strip()) # Output: "hello world" - removes leading and trailing whitespace
print(text.lstrip()) # Output: "hello world " - removes leading whitespace
print(text.rstrip()) # Output: " \nhello world" - removes trailing whitespace


print("---------Find----------")

text = "Python is fun and fun and fun"
print(text.find("is")) # Output: 7 - index of first occurrence of "is"
# Output: "Python is awesome and awesome and awesome" - replaces all occurrences of "fun" with "awesome"
print(text.replace("fun", "awesome")) 

text = "Apples,Bananas,Pineapples"
text_list = text.split(",") # Output: ['Apples', 'Bananas', 'Pineapples'] - splits string into a list at commas
print(text_list)
# Output: "Apples,Bananas,Pineapples" - joins list elements into a string with commas
print(",".join(text_list)) 

print("---------Is----------")
text = "Python123"
print(text.isalpha()) # Output: False - contains digits
# isdigit() - checks if all characters are decimal digits + some other digit characters 
# (e.g., superscripts, Unicode digits).
print(text.isdigit()) # Output: False - contains letters
# isdecimal() - checks if all characters are decimal digits(0-9)
print(text.isdecimal()) # Output: False - contains letters, not just digits
print(text.isspace())
print(text.isalnum()) # Output: True - check if string is alphanumeric, contains only alphabets and numbericals
'''
str.isnumeric()
Returns True for:
    - All decimal digits (0–9)
    - Unicode digits (e.g., Arabic, Devanagari)
    - Superscripts (², ³)
    - Fractions (½, ⅓)
    - Roman numerals (Ⅻ)
    - Full-width numbers used in East Asian typography
Note: "四".isnumeric() - False, because it is a Chinese character for "four" but not a digit.
'''
print(text.isnumeric)

# Output: True - 
# Checks The first character of each word is uppercase, and
# All other characters are lowercase (except non-letter characters, which are ignored).
print(text.istitle()) 
text1 = "Python123Java"
print(f"text1: {text1.istitle()}") # Output: True - "Python123" and "Java" are both title-cased
print(text.isalnum()) # Output: True - contains letters and digits
print(text.isspace()) # Output: False - contains letters and digits
print(text.islower()) # Output: False - contains uppercase letters
print(text.isupper()) # Output: False - contains lowercase letters
print(text.isprintable()) # Output: True - all characters are printable
# Output: True - valid Python identifier - ie. valid variable name
# text = "def", it would return False - "def" is a reserved keyword in Python
print(text.isidentifier()) 
print(text.startswith("Python")) # Output: True - starts with "Python"
print(text.endswith("123")) # Output: True - ends with "123"
print(text.count("o")) # Output: 1 - counts occurrences of "o"
print(text.count("fun")) # Output: 0 - counts occurrences of "fun" (not present in text)
print(text.count("P")) # Output: 1 - counts occurrences of "P"

text = "Python is fun"
print(text.isalnum()) # Output: False - contains spaces

# Encoding and decoding
print([ord(c) for c in "ABC"]) # Output: [65, 66, 67] - Unicode code points for "A", "B", "C"
print(ord("a")) # Output: 97 - Unicode code point for "a"
print(chr(65)) # Output: "A" - character for Unicode code point 65
print(chr(97)) # Output: "a" - character for Unicode code point 97
print(''.join(chr(n) for n in [65, 66, 67])) # Output: "ABC" - characters for Unicode code points 65, 66, 67