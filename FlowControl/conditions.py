age = int(input("How old are you? "))

if 16 <= age <= 65:  # simplified chain comparison (most efficient of the 3)
# if age >= 16 and age <= 65:
    print("Have fun at work!")
else:
    print("enjoy the break")

print("*" * 80)

if age < 16 or age > 65:
    print("enjoy the break")
else:
    print("Have fun at work!")

print("*" * 80)

if age in range(16, 66):
    print("Have fun at work!")
else:
    print("enjoy the break")
