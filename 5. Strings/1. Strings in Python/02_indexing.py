

name = "John" 
# name = "J   o   h  n"
#         0   1   2  3
#        -4  -3  -2 -1

# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4]) # This will raise an IndexError: string index out of range

# reversed indexing
print(name[-1]) # len + (-1) = 4 - 1 = 3
print(name[-2])
print(name[-3])
print(name[-4]) # name[-4+4] name[0]

######################################
print("string leghth: ", len(name))

print(len(""))                 # 0 (empty string)
print(len("123\n456"))         # 7 (newline counts as 1 character)
print(len("😊👍") )            # 2 (each emoji is one character)

# to count words, we can split the string by spaces
text = "Python is fun and powerful"
# splits by spaces
# When call split() without any arguments in Python:
# means: splitting on any amount of whitespace (spaces, tabs, newlines) 
# and ignoring extra spaces. This is by design.
words = text.split()
word_count = len(words)
print(word_count)           # Output: 5

# tabs and newlines
text2 = "One\ttwo\nthree"        
print(len(text2.split()))        # 3

# split() tells Python: “Split on any whitespace and ignore extra whitespace between words.”
text3 = "  Python   is\tawesome\nindeed  "
words = text3.split()

print(words)  # ['Python', 'is', 'awesome', 'indeed']

# split by comma (or any custom delimiter)
text4 = "Python,,is,,fun"
words = text4.split(",")
print(words)  # ['Python', '', 'is', '', 'fun']

text5 = "  Python   is\tawesome\nindeed  "
words = text5.split(" ")
print(words)  # ['','Python','','','','is','awesome','indeed','',''] (extra spaces are not ignored)

