options = [1, 2, 3, 4]

menu = '''Please select an option:

1. Option 1
2. Option 2
3. Option 3
4. Option 4
5. Exit Menu'''

choice = -1

while choice not in options:
    choice = int(input("What do you want to do? "))

    if choice == 5:
        print("Exited Menu")
        break
    elif choice in options:
        print(choice)
    else:
        print("Invalid Input")
        print()
        print(menu)

