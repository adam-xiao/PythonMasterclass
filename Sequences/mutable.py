# mutable objects: list, dict, set, Bytearray

shopping_list = ["milk",
                 "pasta",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list

print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list)) # the id remains the same, can add item to list without creating new list
print(another_list) # this list also includes cookies

a = b = c = d = e = f = another_list # more lists haven't been created, the same list just has multiple names

print("Adding cream")
b.append("cream")
print(c)
print(d)