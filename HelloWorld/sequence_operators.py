str1 = "he's "
str2 = "probably "
str3 = "pining "
str4 = "for the "
str5 = "fjords"

print(str1 + str2 + str3 +str4 + str5)
print("he's " "probably " "pining " "for the " "fjords")    # + not necessary for cocatenating string literals in python

print("Hello " * 5) # prints hello 5 times

# print("Hello " * 5 + 4) # will get error

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today)   # true
print("fri" in today)   # true
print("thur" in today)  # false
print("parrot" in "fjord")  # false
