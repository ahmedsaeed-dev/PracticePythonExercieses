"""
https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""


def get_first_last_list(a):
    return [a[0], a[-1]]


x = [5, 10, 15, 20, 25]
y = get_first_last_list(x)
print(y)

