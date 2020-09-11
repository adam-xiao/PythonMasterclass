def multiply(x, y):
    result = x * y
    return result


# answer = multiply(10.5, 4) # you should have two blank lines before and after a function as convention
# print(answer)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

def is_palindrome(str1):
    return str1 == str1[::-1]


word = input("Enter word to check: ")
palincheck = is_palindrome(word)
print(palincheck)