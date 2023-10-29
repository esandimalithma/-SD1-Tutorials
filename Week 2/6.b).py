n = int(input("Enter a number: "))
d = int(input("Enter the dividend: "))
try:
    q = n/d
    print(q)
except ZeroDivisionError:
    print("Cannot divide by zero")
