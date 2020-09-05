activity = input("What do you want to do? ")

if "cinema" not in activity.casefold(): #casefold is better than lowercase, in german they have lowercase varations so this swerves that prob
    print("Nah I wanna go to the cinema")
