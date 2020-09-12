def multiply(x: float, y: float) -> float:
    result = x * y
    return result   # you have to explicitly return something, otherwise they will return None


# answer = multiply(10.5, 4) # you should have two blank lines before and after a function as convention
# print(answer)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

def is_palindrome(str1: str) -> bool:   # function annotations, aka shortened docs
    cleanse = str1.casefold()
    return cleanse == cleanse[::-1]


def palindrome_sentence(sent: str) -> bool:
    cleanse_sent = ""

    for char in sent:
        if char.isalnum():
            cleanse_sent += char

    return cleanse_sent.casefold() == cleanse_sent[::-1].casefold()


# word = input("Enter sentence to check: ")
# palincheck = palindrome_sentence(word)
# print(palincheck)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = palindrome_sentence()