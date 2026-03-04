

s = {34, 23, 1, 3, 22}

print(s)

s.add(32)
s.add(32)
s.remove(1)
# s.remove(434234) # Throws an error if remove an non-exist element
s.discard(42323) # remove element only if present, no error if not
print(s)

s.pop() # remove an random element