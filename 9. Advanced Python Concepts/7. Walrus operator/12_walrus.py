


'''
walrus operator (:=) 
    - an assignment expression operator
    - assign a value to a variable AND use it in an expression at the same time

Example:

Without walrus:

n = len("hello")
if n > 3:
    print(n)

With walrus:

# Assigns n and Uses it immediately in condition
if (n := len("hello")) > 3:
    print(n)

------------
Without walrus:

line = input()
while line != "quit":
    print(line)
    line = input()

With walrus:

while (line := input()) != "quit":
    print(line)
'''



def very_slow_func():
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    print("Something....")
    return 70

# # a = very_slow_func()
# if((a:=very_slow_func())>10):
#     print(a)

# else:
#     print("Its not greater than 10")

while(data:= input("Enter the value: ") != "q"):
    print(data)