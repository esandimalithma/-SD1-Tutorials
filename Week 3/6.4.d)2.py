# Simple Calculator
print("------- SIMPLE CALCULATOR -------")

# Initializing variables
num1 = 0
num2 = 0
op = ""

# Getting the user input
num1 = int(input("Enter first value:"))
op = input("Enter operator (+,-,*,/):")
num2 = int(input("Enter second value:"))

# Performing the calculation
try:
    if(op == '+'):
        ans = num1 + num2
    elif(op == '-'):
        ans = num1 - num2
    elif(op == '*'):
        ans = num1 * num2
    elif(op == '/'):
        ans = num1 / num2
    else:
        print("Invalid inputs")

    print(ans)
except ZeroDivisionError:
    print("Cannot divide by zero")
           
