for i in range(1, 13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i**2, i**3))
print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i**2, i**3))  # field width (width or 2,4, 4 chracters) in rep fields
print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i**2, i**3))
print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i**2, i**3))  # left-aligned, > is right aligned
print()
for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3))  # ^ is centered within field width
print()
print("Pi is approx {0:12}".format(22 / 7))     # default 15 decimals
print("Pi is approx {0:12f}".format(22 / 7))    # when float specified, 6 digits default
print("Pi is approx {0:12.50f}".format(22 / 7))     # field width 12, with 50 digits after decimal, ignore field with since you can't fit 50 in 12, thus width is ignored for precision
print("Pi is approx {0:52.50f}".format(22 / 7))     # max precision in python float is 50 - 53 digits
print("Pi is approx {0:62.50f}".format(22 / 7))
print("Pi is approx {0:72.50f}".format(22 / 7))
print("Pi is approx {0:<72.54f}".format(22 / 7))
print()
for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))   # can still control width w/o field numbers, however cant use value more than once or order where values are used