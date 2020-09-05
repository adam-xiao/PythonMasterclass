answer = 5

print("Please guess a num before 1 - 10: ")
guess = int(input())

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Took ya long enough you unlucky dunce")
#     else:
#         print("No more chances for you!")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Took ya long enough you unlucky dunce")
#     else:
#         print("No more chances for you!")
# else:
#     print("Correct!")

if guess != answer:
    if guess < answer:
        print("guess higher")
    else:
        print("guess lower")
    guess = int(input())
    if guess == answer:
        print("nice! took ya long enough")
    else:
        print("no more guesses, scrub")
else:
    print("you rock, first try!")