shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

for item in shopping_list:
    # print("Buy {}".format(item))
    print("Buy " + item)

print("*" * 50)

# for item in shopping_list:
#     if item == "spam":
#         continue    # skips remainder of block, aka doesnt print spam and returns to top of loop
#
#     print("Buy " + item)

for item in shopping_list:
    if item == "spam":
        break    # ends loop

    print("Buy " + item)