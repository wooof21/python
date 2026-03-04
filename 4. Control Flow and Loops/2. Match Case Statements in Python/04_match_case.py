
# match-case: introduced in Python 3.10 as new feature, it allows for pattern matching
# similar to switch-case in Java

a = int(input("Enter a number between 1 and 10: "))

match a: # match (complex_expression):
    case 3:
        print("You won a charger")
    case 5:
        print("You won $5")
    case 8:
        print("You won a camera")
    case _: # default case
        print("Better luck next time")
    
