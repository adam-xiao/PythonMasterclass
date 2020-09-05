for i in range(10):
    print(i)

print("**********")

i = 0   # while loops need init value initialized
# also needs some stop condition and a way to reach it, otherwise infinite loop
# while loops are usually not used for known range-esque tasks
while i < 10:
    print(i)
    i += 1