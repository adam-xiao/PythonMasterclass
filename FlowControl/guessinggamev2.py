import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing

print("Guess a number between 1 and {}. Press 0  to quit".format(highest))
guess = 0

print(5 // 2)   # Side note, int division rounds down

while guess != answer:
    guess = int(input())
    if guess == answer:
        print("You guessed it!")
    elif guess > answer and guess != 0:
        print("Guess lower")
    elif guess < answer and guess != 0:
        print("Guess higher")
    elif guess == 0:
        print("You Quitter!")
        break
