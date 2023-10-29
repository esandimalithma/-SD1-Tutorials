conversion = input("""Enter '1' to convert from Celsius to Fahrenheit
Enter '2' to convert from Fahrenheit to Celsius
: """)

if conversion == '1':
    c = float(input("Enter a temperature in the correct unit: "))
    f = (c * 1.8) + 32
    print(c,"Centigrades is",f,"Fahrenheits")
elif conversion == '2':
    f = float(input("Enter a temperature in the correct unit: "))
    c = (f - 32) / 1.8
    print(f,"Fahrenheits is",c,"Centigrades")

else:
    print("Invalid option entered")


