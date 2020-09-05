# not names range.py otherise confusion with Python range Class

# up to bt not including, just like slice
for i in range(0, 10):
    print("i is now {}".format(i))

print("*" * 80)

for i in range(10): # same as above, assume initial value of 0
    print("i is now {}".format(i))

print("*" * 80)

for i in range(0, 10, 2):   # have to provide initial value when using steps
    print("i is now {}".format(i))

print("*" * 80)


for i in range(10, 0, -2):
    print("i is now {}".format(i))