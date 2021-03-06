even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]


# print(min(even))
# print(max(even))
# print(min(odd))
# print(max(odd))
#
# print()
#
# print(len(even))
# print(len(odd))
#
# print()
#
# print("mississippi".count("s"))
# print("mississippi".count("iss"))
# print("mississippi".count("issi")) # the count is not 2 since letters are reused, aka middle "i"

# method is the same as function, except its bound to an object

even.extend(odd) # adds the items in odd to even
print(even)

even.sort()
print(even)
another_even = even
print(even)
even.sort(reverse=True)  # Does not create a new list
print(even)
print(another_even) # even is same as another_even