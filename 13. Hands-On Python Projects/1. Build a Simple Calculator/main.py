
while True:

    try: 
        a = int(input("Enter the first number: "))

        b = int(input("Enter the second number: "))

        msg = '''
            what kind of operation do you want to perform. 
            Press + for addition
            Press - for subtraction
            Press / for division
            press * for multiplication
            '''

        print(msg)

        o = input("Enter Operation: ")
        match o:
            case "+":
                print(f"The result is: {a + b}")
            case "-":
                print(f"The result is: {a - b}")
            case "*":
                print(f"The result is: {a * b}")
            case "/":
                print(f"The result is: {a / b}")
            case default: 
                print(f"There was an error")

    except Exception as e:
        print("Enter a valid value of a and b")

    key = input("\nPress Q to quit, or Enter to continue: ").lower()
    if key == "q":
        break
print("Goodbye 👋")
