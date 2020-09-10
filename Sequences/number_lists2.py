empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

print("---")

sorted_numbers = sorted(numbers)
print(sorted_numbers) # remember sorted returns a new list, sort does function in place
print(numbers)

digits = sorted("123987654")
print(digits)  # creates list strings

print("---")

# more_numbers = list(numbers)
# more_numbers = numbers[:]   # same as above
more_numbers = numbers.copy()   # same as above

print(more_numbers)
print(numbers is more_numbers)  # they are not the same list (False)
print(numbers == more_numbers)  # however, they do contain the same values in the same order (True)