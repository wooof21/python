

i = 3

if i == 3:
    # do nothing
    # TODO: implement later
    pass 
print("End of program")


# pass:  is a placeholder — it does nothing when executed.
'''
Use Cases:
1. Empty function or class definitions (to avoid syntax errors)

def my_function():
    pass  # TODO: implement later

class MyClass:
    pass
    
Without pass, you'd get an IndentationError because Python expects an indented block.

2. Stub for if, for, while, etc.

x = 10

if x > 5:
    pass  # Placeholder for future logic
else:
    print("x is 5 or less")

You can't leave control structures empty, so pass avoids syntax errors while allowing the program to run.

3. Used during development as a temporary "to-do"

def login():
    # logic not written yet
    pass
    
4. Used when you want to define a block, but skip its execution

for i in range(5):
    if i == 3:
        pass  # deliberately do nothing when i == 3
    else:
        print(i)

Use	                        Why use pass

Empty blocks	            Avoid syntax errors
Temporary placeholders	    Code not yet written
Skip certain conditions	    No action needed
'''

for i in range(0, 11):
    if i == 5:
        pass # Do nothing, continue the loop
    print(i)