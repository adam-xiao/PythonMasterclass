# a set is unordered and contains no duplicates
# items aren't accessed by keys
#
# animals = {"sheep", "cow", "hen"}
# print(animals)
#
# # if you want to create an empty set, you have to use set(), just using braces will create an empty dictionary
# animals2 = set(["lion", "tiger", "panther"])
# print(animals2)
#
# animals.add("horse")
# animals2.add("horse")

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# print()
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares)) # union are all elements that are in either sets
# print(len(even.union(squares)))
# print(squares.union(even))
#
# print()
# print(even.intersection(squares)) # intersection are elements that are in both sets
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

print()     # subtracting set b FROM set a removes any item that exists in set b from set a
even = set(range(0, 40, 2))
print(sorted(even))
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(sorted(squares))

# print("even minus squares")
# print(sorted(even.difference(squares))) # use differences since it is more intentional
# print(sorted(even - squares))
#
# print("squares minus even")
# print(sorted(squares.difference(even)))      # difference returns a new set
# print(squares - even)
#
# print()
# print(sorted(even))
# print(squares)
# even.difference_update(squares) # difference in place, no new set
# print(sorted(even))

# print()
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))   # symmetric_diff basically the opposite of intersection
# # a set with all values except for the ones in both sets
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))
# there is also symmetric_difference_update - in place

# also discard and remove
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
# squares.remove(8)   # remove will throw error if item to be removed does not exist
# # you want to use remove if you want an error to be thrown

if squares.issubset(even):
    print("squares is a subset of even")    # all ements needed to be superset/subset

if even.issuperset(squares):
    print("even is a superset of even")

# frozen set
# an immutable set, can be used as dict key or as member of a set

even = frozenset(range(0, 100, 2))
print(even)

