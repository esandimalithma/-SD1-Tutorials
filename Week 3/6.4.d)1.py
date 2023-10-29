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
if(op == '+'):
    ans = num1 + num2
elif(op == '-'):
    ans = num1 - num2
elif(op == '*'):
    ans = num1 * num2
elif(op == '/'):
    if num2 == 0:
        print("Cannot divide by zero")
    ans = num1 / num2
else:
    print("Invalid inputs")

print(ans)
           
