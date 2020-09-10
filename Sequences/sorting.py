pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram) # sorted always returns a list
print(letters) # spaces, uppercase, then lowercase in that order

numbers = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# difference between sorted and sort?

numbers.sort()
print(numbers)

# sorted returns a new list, sort does its function in place
# sort does not return anything, thus you can not assign it to a new variable
# thats why sorted was assigned to a new variable

# missing_letter = sorted("The quick brown fox jumped over the lazy dog")
# print(missing_letter)

# case-insensitive sorting

missing_letter = sorted("The quick brown fox jumped over the lazy dog", key=str.casefold) #no parentheses
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]

names.sort(key=str.casefold)
print(names)