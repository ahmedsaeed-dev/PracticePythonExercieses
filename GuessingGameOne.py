"""
https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

import random

answer = random.randint(1, 9)
count = 1
val = int(input("\nGuess a number between 1 and 9: "))

while True:
    if val == answer:
        break
    elif val < answer:
        print("\nToo low!")
    elif val > answer:
        print("\nToo high!")
    val = int(input("Guess again: "))
    count += 1

print("\nYou got it in {} tries!".format(count))
