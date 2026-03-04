


try:
    a = 345/0 # division by zero
    # a = 345/10 # Good Output

except Exception as e:
    print(e)

# Gets executed when there is no error in the try block 
else:
    print("Good Output")



