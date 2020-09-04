parrot = "Norwegian Blue"
winner = "we win"

print(parrot)   #index starts at 0
# print(parrot[3])
# print(parrot[4])
# print(parrot[9])
# print(parrot[3])
# print(parrot[6])
# print(parrot[8])

# print(winner[0])
# print(winner[1])
# print(winner[2])
# print(winner[3])
# print(winner[4])
# print(winner[5])
#
# print(parrot[-11])
# print(parrot[-10])
# print(parrot[-5])
# print(parrot[-11])
# print(parrot[-8])
# print(parrot[-6])   #you can get te negative index by (positive index - str length), -11
#
# print(parrot[0:6])  #the final value is not included, aka up to but not including, also happens in range, etc
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])   #same as line 28
# print(parrot[10:14])
# print(parrot[10:])
# print(parrot[:])
#
# print(parrot[-4:2]) #nothing, you cant wrap around
# print(parrot[-4:-2])
# print(parrot[-4:12])

print(parrot[0:6:2])    #Nre - slice starts at index 0 goes up to but not including 6, and the step thorugh seq in steps of 2
print(parrot[0:6:3])    #Nw

num = "9,223;372:036,854"
print(num[1::4])
separators = num[1::4]
print(separators)

values = "".join(char if char not in separators else " " for char in num).split()
print([int(val) for val in values])

