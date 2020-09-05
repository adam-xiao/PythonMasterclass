parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("{} is not in {}".format(letter, parrot))
# remember its case sensitive so "a" is in "A" is not