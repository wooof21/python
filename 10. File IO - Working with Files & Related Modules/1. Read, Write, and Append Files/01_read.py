

'''
r: read mode, by default, in text mode
rb: read in binary mode (binary file)
rt: read in text mode
'''

f = open("test.txt", "r")

content = f.read()

print(content)

f.close()