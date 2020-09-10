data = [4, 5, 100, 105, 120, 160, 400, 500]

# del data[0:2]
# print(data)
# del data[4:]
# print(data)

min_valid = 100
max_valid = 200

# for index, value in enumerate(data):    # be careful when changing size of list, this wont work as intended
#     if (value < min_valid) or (value > max_valid):
#         del data[index]
#
# print(data)

# process the low values in the list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break

print(stop)
del data[:stop]
print(data)

# process the high values form the list
start = 0
for index in range(len(data) - 1,  -1, -1):
    if data[index] <= max_valid:
        # we need to change the index from last item to keep, to first item to delete
        start = index + 1
        break

print(start)
del data[start:]
print(data)