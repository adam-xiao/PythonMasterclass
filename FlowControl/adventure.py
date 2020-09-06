available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

while chosen_exit not in available_exits:
    chosen_exit = input("choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("you quitter!")
        break
else:
    print("you escaped!")