def factorial(n: int) -> int:
    """
    Returns the factorial of `n`!

    :param n: A positive integer `n` or 0
    :return: A positive integer
    """
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i

    return result


for i in range(0, 36):
    print(factorial(i))