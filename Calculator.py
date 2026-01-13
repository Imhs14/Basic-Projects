def calculator():
    while True: #ask for user to choose from following operations
        print("enter the operation you want to perform:")
        print("""1: Addition
      2: subtraction
      3: multiplication
      4: division
      5: modulus
      6: exponential
      7: Floor division""")
        #get the useer inputs
        operation = input("choose the operation you want to perform 1-7:")
        a = float(input("enter first number:"))
        b = float(input("enter the second number"))
        if operation == '1':
            print(f"The addition of {a} and {b} is {a + b}")
        elif operation == '2':
            print(f"The subtraction of {a} and {b} is {a - b}")
        elif operation == '3':
            print(f"The multiplication of {a} and {b} is {a * b}")
        elif operation == '4':
            print(f"The division of {a} and {b} is {a / b}")
        elif operation == '5':
            print(f"The modulus of {a} and {b} is {a % b}")
        elif operation == '6':
            print(f"The exponential of {a} and {b} is {a ** b}")
        elif operation == '7':
            print(f"The Floor division of {a} and {b} is {a // b}")
        else:
            print("Invalid operation selected.") #handles to invalid inputs
        
        user_input = input("do you want to continue (yes/no):").lower() #asks if the user wants to continue the operations
        if user_input != 'yes':
            print("operations terminated:")
            break
        
calculator()    #function call to start the calculator