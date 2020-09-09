# immutable: int, float, bool (True and False), str (string), tuple, frozenset, bytes

# result = True
# result2 = result
#
# print(id(result))
# print(id(result2))
#
# result = False  # True didnt change to false, result was bound to the new value, False
# print(id(result))

result = "Correct"
result2 = result

print(id(result))
print(id(result2))

result += "ish"
print(id(result))   # as you can see, the id changes, aka its new value not the same value modified
print(id(result2))