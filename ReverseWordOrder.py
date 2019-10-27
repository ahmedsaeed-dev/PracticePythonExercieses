"""
https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.
"""
# ' '.join() joins the list and separates them with a space. if it was '-'.join() it would be this-is-a-list
# reversed() reverses a list
# split splits the string based on the character parameter declared

print(' '.join(reversed(input('Enter a string: ').split(' '))))
