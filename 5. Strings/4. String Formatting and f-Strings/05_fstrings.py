

# String formatting

template = "Dear {}, You are awesome. Take this ${} bag"
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c2 = 300

s1 = template.format(a, a1)
print(s1)

s2 = template.format(b, b1)
print(s2)

s3 = template.format(c, c2)
print(s3)

print(f"{a} you are awesome and take this ${a1} bag")