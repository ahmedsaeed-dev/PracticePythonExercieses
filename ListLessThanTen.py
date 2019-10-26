"""
https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
Take a list, say for example this one: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

value = int(input("Enter number to search for values in list less than it: "))
print([b for b in a if b < value])
