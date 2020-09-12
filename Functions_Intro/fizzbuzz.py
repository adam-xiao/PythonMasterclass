def fizz_buzz(n: int) -> str:
    """
    Returns a different string depending on the divisiblity of `n`
    3: fizz
    5: buzz
    3 & 5: fizz buzz
    :param n: A positive integer `n`
    :return: A string
    """
    if (n % 3 == 0) and (n % 5 == 0):
        return "fizz buzz"
    elif n % 5 == 0:
        return "buzz"
    elif n % 3 == 0:
        return "fizz"
    else:
        return str(n)


# for i in range(1, 101):
#     print(fizz_buzz(i))

input("Play Fizz buzz? Press Enter to start")
print()

next_num = 0
while next_num < 99:
    next_num += 1
    print(fizz_buzz(next_num))
    next_num += 1
    correct_answer = fizz_buzz(next_num)
    player_answer = input("Your turn: ")
    # player_answer = correct_answer
    if player_answer != correct_answer:
        print("LOSER, the correct answer was {}".format(correct_answer))
        break
else:
    print("You don't suck, you reached {}.".format(next_num))