a = 12
b = 3

print(a + b)  #15
print(a - b)  #9
print(a * b)  #36
print(a / b)    #4.0
print(a // b)   #4 (integer division)
print(a % b)    # 0 modulo (the remainder after integer division)

print()

for i in range(1, 4):   #range must provided int values
    print(i)


#you cant have an expression on the left of an assignment (the right however is an expression - see line 1,2)

print(a + b / 3 - 4 * 12)   #PEMDAS - M/D have equal precedence, same with A/S, if on one line, eval from left -> right
print(a + (b / 3) - (4 * 12))
