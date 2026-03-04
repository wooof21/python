

# try except: try and hanlde the exception
# while True:
#     try: 
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The division is {a / b}")

#     except ValueError:
#         print("Please type a number")
    
#     except ZeroDivisionError:
#         print("Cannot divide by 0")

#     except Exception as e:
#         print("Unknown error occurred!", e)

#raise: throw the exception and let the app stop
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

if b == 0:
    raise ValueError("Please dont divide by 0")

print(f"The division is {a / b}")