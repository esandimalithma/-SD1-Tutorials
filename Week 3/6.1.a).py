try:
    n = int(input('Give me a number over 100: '))
    if n <= 100:
        print(n, 'is not over 100')
except ValueError:
    print("Please enter an integer")
