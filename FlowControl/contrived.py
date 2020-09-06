numbers = [1, 45, 32, 12, 60]

# if any number is divisible by 8, we don't want it
for number in numbers:
    if number % 8 == 0:
        print("The numbers are unacceptable")
        break
else:   # pay attention to indent, the else is for "for" not "if"
    # used to do something if loop wasnt broken out of and runs its course
    # aka when loop terminates normally
    print("All those numbers are fine")