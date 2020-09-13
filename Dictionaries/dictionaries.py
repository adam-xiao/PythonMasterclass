fruit = {
    "orange": "citrus",
    "apple": "cider",
    "lemon": "pirates",
    "grape": "wine",
    "lime": "green lemon"
}   # note that as of python 3.6, the order of keys is preserved, of course it's
# best to code as if it wasn't just to be safe
# you can do this be creating a list from the dict keys and then iterating over the list

# sorted(fruit.keys())
ordered_keys = list(fruit.keys())   # you can also use .values, but keys is more eff
ordered_keys.sort()
# for f in ordered_keys:
#     print(f)

print(fruit)
print(fruit["lemon"])

fruit["pear"] = "a yellow apple"
print(fruit)
fruit["pear"] = "still a yellow apple"  # replacing the value of of key-value pair
print(fruit)

# del fruit["grape"]    # if no key provided, will delete whole dictionary, careful
# print(fruit)
# fruit.clear()     # keeps fruit dictionary, but empties it
# print(fruit)

# print(fruit["tomato"])  # cant do anything if key doesnt exist

# while True:
#     dict_key = input("Please enter a fruit : ")
#     if dict_key == "quit":
#         break
#     description = fruit.get(dict_key, "We don't have a " + dict_key)
#     print(description)
#     # if dict_key in fruit :
#     #     description = fruit.get(dict_key)
#     #     print(description)
#     # else:
#    #     print("We don't have a" + dict_key)


fruit_keys = fruit.keys()
print(fruit_keys)
fruit["tomato"] = "ketchup"
print(fruit_keys)   # fruit keys will update with tomato, aka its dynamic


print(fruit)
print(fruit.items())     # list of tuples
f_tuple = tuple(fruit.items())
print(f_tuple)      #tuple of tuples
# you can also turn tuples to dicts