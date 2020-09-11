t = "a", "b", "c"

# print(t) # see that it prints with parentheses not brackets, since it's a tuple

# paretheses may as well always be used for tuples to avoid trouble

albums =[("Welcome to my Nightmare", "Alice Cooper", 1975),
        ("Bad Company", "Bad Comapny", 1974),
        ("Nightflight", "Budgie", 1981),
        ("More Mayhem", "Emilda May", 2011),
        ("Ride the Light", "Metallica", 1984),
        ]

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))


# for album in albums:
#     name, artist, year = album
#     print("Album: {}, Artist: {}, Year: {}".format(name, artist, year))

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2]) # even though tuples are created with parentheses, they are indexed with brackets

# tuples are immutable, and thus use less than lists
# lists are mutable
# tuples are used to protect integrity of data, due to immutability
# tuples also used when you don't wht values to change

# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)

# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee Table", 200, 100, 75, 34.5)
# print(table[1] * table[2])
# name, length, width, height, price = table
# print(length * width)