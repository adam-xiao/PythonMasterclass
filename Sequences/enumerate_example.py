# for index, character in enumerate("abcdefgh"):   # provides efficient way to get index
#     print(index, character)

# for t in enumerate("abcdefgh"):
#     print(t)

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

# index, character = (0, 'a')
# print(index)
# print(character)