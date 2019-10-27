"""
https://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
"""


# gets user input as string, converts to list, and returns
def get_input():
    raw_str = input("Enter a number: ")
    guess_list = []
    for i in raw_str:
        guess_list.append(int(i))
    return guess_list


# takes guess list and solution list and returns count of cows
def find_cows(g, s):
    count = 0
    for i in range(0, len(g)):
        if g[i] == s[i]:
            # if the guess index matches the solution index inc cow count
            count += 1
    return count


# takes guess list and solution list and returns count of bulls
def find_bulls(g, s):
    count = 0
    for i in range(0, len(g)):
        if g[i] in s:
            if g[i] != s[i]:
                # if the indexed guess is in the solution but not in the right place, inc bull count
                count += 1
    return count


if __name__ == '__main__':
    print("Welcome to the Cows and Bulls Game!")
    cows = 0
    bulls = 0
    solution = [1, 0, 3, 8]
    while cows != 4:
        guess = get_input()
        cows = find_cows(guess, solution)
        bulls = find_bulls(guess, solution)
        print("{} cows, {} bulls".format(cows, bulls))

