myList = ["a", "b", "c", "d"]

newString = ''
# for c in myList:
#     # newString += c + ", "   # this is ineff
#     newString = ", ".join(myList)   # if using join, you don't need a loop

newString = ", ".join(myList)

print(newString)

locations = {
    0: "At home",
    1: "building",
    2: "hill",
    3: "stream",
    4: "valley",
    5: "forest"
}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         {"N": 5, "Q": 0},
         {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0},
         {"W": 2, "S": 1, "Q": 0}]

loc = 1
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits.upper())
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("Can't go that way")