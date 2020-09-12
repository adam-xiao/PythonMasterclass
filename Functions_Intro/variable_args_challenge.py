def sum_numbers(*nums: float) -> float: # use float not int, as is convention
    """
    Sums up provided integer/s `nums`

    :param nums: Integer/s
    :return: An Integer
    """
    result = 0
    for num in nums:
        result += num
    return result


print(sum_numbers(1, 2, 3))