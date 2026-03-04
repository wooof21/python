

import re

text = "The quick brown fox jumps over the lazy dog. brown"
# https://regexr.com/

# Search for a pattern
# find first occurrence and stop searching
match = re.search("brown", text)
print(match)
if match:
    print("Match found!")
    print("Start index:", match.start())
    print("End index:", match.end())

print("----------------------")

# Find all occurrences of a pattern: only return the list of matches (string)
matches = re.findall("the", text, re.IGNORECASE) # Case-insensitive search
# to return a list of match object:
match_objs = list(re.finditer("the", text, re.IGNORECASE))

print("Matches string: ", matches)
print("Matches obj: ", match_objs)


# replace a pattern: replace all occurrences
new_text = re.sub("brown", "white", text)
print("New text:", new_text)