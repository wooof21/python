

from collections import Counter
import string


text = "Hello, world! Hello again... world?"

'''
string.punctuation — list of all punctuation

str.translate() — to remove punctuation

split() — to break text into words

set() — to get unique words
'''

# Step 1: Remove punctuation
print(string.punctuation) #list of all punctuation characters: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
'''

Using str.translate() to remove punctuation
str.maketrans() creates a translation table that maps each punctuation character to None

str.maketrans() is a built-in function that returns a translation map — a special dictionary that
 can be used with .translate() to:

Replace characters
Delete characters

Syntax:
str.maketrans(from_str, to_str, delete_str)

Parameter	        Meaning

from_str	        Characters to replace
to_str	            What to replace them with
delete_str	        Characters to remove completely

str.maketrans("", "", string.punctuation)
 means:
    Don't replace anything (from_str and to_str are empty).
    Delete all punctuation characters listed in string.punctuation.
 build a delete map
Then: 
    .translate(...) → apply it to remove punctuation fast and cleanly
'''
print(str.maketrans("", "", string.punctuation)) # Output: {33: None, 34: None, 35: None, ...}
text_clean = text.translate(str.maketrans("", "", string.punctuation))
print(f"text_clean: {text_clean}")

# Step 2: Convert to lowercase (optional for case-insensitive match)
text_clean = text_clean.lower()

# Step 3: Split into words
words = text_clean.split()

# Step 4: Count word frequencies
word_freq = Counter(words)

# Step 5: Count unique words
unique_words = set(words)

print("Word frequencies:", word_freq) # Counter({'hello': 2, 'world': 2, 'again': 1})
print("All words:", words) # ['hello', 'world', 'hello', 'again', 'world']
print("Unique words:", unique_words) # {'hello', 'world', 'again'}
print("Unique word count:", len(unique_words)) # Output: 3


'''
str.translate(mapping)
returns a copy of the string where characters are mapped using a translation table (created by str.maketrans()).

str.maketrans(from_str, to_str, delete_str)
"from_str" and "to_str" are strings of equal length, where each character in "from_str" is 
replaced by the corresponding character in "to_str".

str.translate() just needs a translation table, which is a dictionary-like object mapping 
character Unicode ordinals (integers) to:

    - a new character (string),

    - None (to delete it),

    - or another ordinal.
Could also create a translation table using a dictionary:
'''
print("##################################")
text = "hello world"
table = str.maketrans("aeiou", "12345")
result = text.translate(table)
print(result)  # h2ll4 w4rld

print("##################################")
text = "a+b=c; a=b!"
table = str.maketrans({"+": " plus ", "=": " equals ", ";": None, "!": None})
print(text.translate(table))

print("##################################")
table = {
    ord("a"): "A",
    ord("b"): "B",
    ord("!"): None  # remove "!"
}
print("abc!".translate(table))  # ABc