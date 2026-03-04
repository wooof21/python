


# f = open("John Doe.txt", "r")
# content = f.read()
# print(content)
# f.close()


'''
    with: automatically closes the file
    similar to Java: try-with-resources
'''

with open("John Doe.txt", "r") as f: # context manager
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using with synax


# read all lines
with open("John Doe.txt") as f:
    lines = [line.strip() for line in f]
    print(lines)