

import os 


# list all directories and files in the directory "dir"
# a = os.listdir("dir")
# print(a)

# get current directory
print(os.getcwd())

# check if a directory exist
print(os.path.exists("8. OOP"))

# delete a file, cannot remove a directory
os.remove("John Doe.txt")

# delete a directory: only remove an empty directory
# os.rmdir("dir")