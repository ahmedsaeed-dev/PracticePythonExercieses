"""
https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
Remember the rules:
    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""
import random

# list for bot's random repo
enum = ['Rock', 'Paper', 'Scissors']

choice = ''
while 'n' != choice.lower():
    print("""
    Rock:       R or r
    Paper:      P or p
    Scissors:   S or s
    """)
    player1 = str(input("Selection: "))

    # grabs random selection from enum list
    player2 = random.choice(enum)

    print("Bot: {}\n".format(player2))
    if 'r' == player1.lower() and 's' == player2[0].lower():
        print("\tYou win!")
    elif 's' == player1.lower() and 'p' == player2[0].lower():
        print("\tYou win!")
    elif 'p' == player1.lower() and 'r' == player2[0].lower():
        print("\tYou win!")
    elif player1.lower() == player2[0].lower():
        print("\tIt's a tie!!")
    else:
        print("You lose!")

    choice = str(input('\nPlay again? Y/N: '))

print("\nGoodbye...")