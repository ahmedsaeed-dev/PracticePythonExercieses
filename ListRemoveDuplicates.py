"""
https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
"""


def remove_duplicates(x):
    y = []
    [y.append(i) for i in x if i not in y]
    return y


a = [0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 9, 9, 9, 9, 10]
print(remove_duplicates(a))
