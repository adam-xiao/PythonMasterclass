import random


def get_integer(prompt):    # triple quotes in empty line right below function def, press enter in quotes to create stub
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.
    :param prompt: The string that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters
    """
    while True: # no blank line between end of docstring and code
        temp = input(prompt)    # cmd+j for quick info. cmd+click for docs
        if temp.isnumeric():
            return int(temp)
        # else:
        print("Please enter a valid integer: ")


# print(input.__doc__)    # we are referring to attributes here, not calling a function, thus no parentheses
# print("*" * 80)
# print(get_integer.__doc__)
# print("*" * 80)

help(get_integer)

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing

print("Guess a number between 1 and {}. Press 0 to quit".format(highest))
guess = 0

# print(5 // 2)   # Side note, int division rounds down

while guess != answer:
    guess = get_integer(": ")
    if guess == answer:
        print("You guessed it!")
    elif guess > answer and guess != 0:
        print("Guess lower")
    elif guess < answer and guess != 0:
        print("Guess higher")
    elif guess == 0:
        print("You Quitter!")
        break
