shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"
found_at = None     #constant that represents nothing

# for index in range(len(shopping_list)):     # len = length, basically for range(6)
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

# print(found_at)


if item_to_find in shopping_list:       # cleaner way to write above
    found_at = shopping_list.index(item_to_find)


if found_at is not None:
    print(found_at)
else:
    print("not found")