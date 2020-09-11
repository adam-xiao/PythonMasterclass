a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 76  #example of unpacking
print(x)
print(y)
print(z)

print()

print("Unpacking a Tuple")
data = 1, 2, 76 # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print()

print("Unpacking a list")

data_list = [12, 13, 14]
# data_list.append(15) # will return error

# you can't append items to a tuple, thus they can always be unpacked successfully

p, q, r = data_list
print(p)
print(q)
print(r)