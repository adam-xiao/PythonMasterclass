age = 24
print("My age is " + str(age) + " years")
print("My age is {0} years".format(age))    # replacement fields

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6}, and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct, and Dec".format(31))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}".format(28, 30, 31))

# print() empty line

# the line below """ will count as an empty line, in Jan was moved up it would take up the mepty space
print("""
Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
""".format(28, 30, 31)) # just like above comment, this is also a empty line
