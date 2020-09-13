fruit = {
    "orange": "citrus",
    "apple": "cider",
    "lemon": "pirates",
    "grape": "wine",
    "lime": "green lemon"
}

print(fruit)

veg = {
    "cabbage": "meh veg",
    "sprouts": "bitter",
    "spinach": "popeye"
}

# veg.update(fruit)   # combine the two dicts, a new dict/obj is not made
# print(veg)
#
# print()
# print(fruit.update(veg))    # None
# print(fruit)

print()
nice_and_nasty = fruit.copy()   # returns new dict
nice_and_nasty.update(veg)
print(nice_and_nasty)
print()
print(veg)
print(fruit)