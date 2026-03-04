
# Python supports several built-in data types:
#     Integers (int): Whole numbers (e.g., 10, -5).
#     Floats (float): Decimal numbers (e.g., 3.14, -0.001).
#     Strings (str): Text data enclosed in quotes (e.g., "Hello", 'Python').
#     Booleans (bool): Represents True or False.
#     Lists: Ordered, mutable collections (e.g., [1, 2, 3]).
#     Tuples: Ordered, immutable collections (e.g., (1, 2, 3)).
#     Sets: Unordered collections of unique elements (e.g., {1, 2, 3}).
#     Dictionaries: Key-value pairs (e.g., {"name": "Alice", "age": 25}).

age = 3 
print(age)
print(type(age))

cgpa = 4.5
print(cgpa)
print(type(cgpa))

name = "John"
print(name)
print(type(name))

name = 123
print(name)
print(type(name))

is_completed = True # can also be False
print(is_completed)
print(type(is_completed))

num_list = [1, 2, 3, 4]
num_list[0] = 10  # Lists are mutable, so this is allowed
print(num_list)

num_tuple = (1, 2, 3)
# num_tuple[1] = 4  # This will raise an error because tuples are immutable
print(num_tuple)

num_set = {1, 2, 3, 4}
num_set.add(4)  
print(num_set)  # Sets automatically handle duplicates

dict = {"name": "Alice", "age": 25, "is_student": False, "gender": "Female"}
dict.get("name")  # Accessing value by key
dict["age"] = 26  # Updating value by key
dict["city"] = "New York"  # Adding a new key-value pair
dict.pop("is_student")  # Removing a key-value pair
dict["hobbies"] = ["reading", "traveling"]  # Adding a list as a value
dict["hobbies"].append("coding")  # Modifying the list within the dictionary
dict["hobbies"].remove("reading")  # Removing an item from the list
dict["hobbies"].sort()  # Sorting the list
dict["hobbies"].reverse()  # Reversing the list
#dict["hobbies"].clear()  # Clearing the list
#dict["hobbies"] = []  # Reinitializing the list
print(dict)
print(dict.get("non_exist_key"))  # out: None - Accessing a non-existent key
print(dict.get("non_exist_key", "default_value"))  # out: default_value - Accessing a non-existent key with default value
print(dict.keys())  # Getting all keys
print(dict.values())  # Getting all values
print(dict.items())  # Getting all key-value pairs

'''
List - Mutable, ordered, allows duplicates.
sort():

    Time complexity: O(n log n)

    Memory: O(1) (in-place)

List Complexity:

Operation	    Time Complexity
Indexing	    O(1)
Append	        O(1) (amortized)
Insert	        O(n)
Delete	        O(n)
Search	        O(n)
Sort	        O(n log n)
'''

'''
Tuple - Immutable, ordered, allows duplicates.

Complexity:

Same indexing/searching performance as lists (O(1) for access, 
O(n) for search), but faster and more memory-efficient due to immutability.

Tuples can't be sorted in place because they're immutable.
'''

'''
Set - Mutable, unordered, no duplicates. & Backed by a hash table.

Set Complexity:

Operation	    Time Complexity
Add	            O(1)
Remove	        O(1)
Search	        O(1)
Sort	        O(n log n)

Note: sorting a set gives a list, not a set.
'''

'''
Dictionary - Mutable, unordered (insertion-ordered as of Python 3.7+), 
keys must be unique and hashable.
Use: Key-value mappings, fast lookup.

Dictionary Complexity:

Operation	        Time Complexity
Get/Set	            O(1)
Delete	            O(1)
Search Key	        O(1)
Sort by keys	    O(n log n)
'''

'''
🧠 Memory Efficiency
Type	        Memory (smallest to largest)
tuple	        ✅ Most efficient
list	        ❗ More overhead (resizable)
set	            ❗❗ Higher (hash table + no order)
dict	        ❗❗❗ Highest (keys + values + hashes)
'''