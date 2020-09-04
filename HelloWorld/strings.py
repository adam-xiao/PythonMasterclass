print("Today is a good day to learn Python")
print('Python is fun')
print('We can include "quotes" in strings')
print("And also the 'other' way")
print("hello" + " world")
greeting = "Hello"
# name = input("Please enter your name: ")
name2 = "Adam"
print(greeting + ' ' + name2)

age = 24
print(age)

print(type(greeting))
print(type(age))

# print("I'm" + age)  #strongly typed, cant cocatenate int is str

# f-strings ONLY IN PYTHON 3.6, no plans to backport them to prev versions
# seems like an in-line/string replacement field


print(name2 + f" is {age} years old")   # notice f
print(type(age))

print(f"Pi is approx {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approx {pi:12.50f}")