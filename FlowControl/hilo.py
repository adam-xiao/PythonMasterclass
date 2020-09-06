low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1

while True:
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if my guess was correct"
                     .format(guess)).casefold()

    if high_low == "h":
        low = guess + 1
        # pass - use as just a block of code to be replaced to make rest of code valid
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        print("I got in in {} guesses!".format(guesses))
    else:
        print("Wrong input. H, c, or l ya dunce")

    guesses += 1
