day = "Friday"
temp = 30
raining = False

if (day == "Saturday" and temp > 27) or not raining:    # "and" has higher precedence than "or", use parentheses when and/or in same statement
    print("swim")
else:
    print("python")

# None and False are False
# 0 of any numeric type is False (int, float, fraction, etc)
# empty sequences and collections are False

if 0:
    print("True")
else:
    print("False")

name = input("Name? ")
# if name:
if name != "":      # more explicit version of above
    print("Hello, {}".format(name))
else:
    print("Okay no-name")