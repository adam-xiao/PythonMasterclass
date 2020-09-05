name = input("Name? ")
age = int(input("Age? "))

if 18 <= age <= 30:
    print("Welcome to the booze cruise, {}".format(name))
else:
    print("Sry not for old-timers or kids, only the hip")