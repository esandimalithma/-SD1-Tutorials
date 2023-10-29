choice = input("Do you like Python?(yes/no): ")
choice = choice.lower()
if choice == 'yes' or choice == 'y':
    print("You are on the right course")
elif choice == 'no' or choice == 'n':
    print("You might change your mind")
else:
    print("I did not understand")
