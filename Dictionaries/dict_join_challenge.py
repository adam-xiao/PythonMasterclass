myList = ["a", "b", "c", "d"]

# newString = ''
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

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

vocab = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W"
}

print(locations[0].split())
print(locations[3].split(","))
print(' '.join(locations[0].split()))

loc = 1
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits).upper()
    print()

    if len(direction) > 1:
        # for word in vocab:
        #     if word in direction:
        #         direction = vocab[word]
        words = direction.split()
        for word in words:
            if word in vocab:
                direction = vocab[word]
                break

    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("Can't go that way")