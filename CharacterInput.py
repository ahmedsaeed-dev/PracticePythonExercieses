"""
https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""


name = str(input("Enter name: "))
age = int(input("Enter age: "))
year = (2019 - age) + 100

print("{} will be 100 in the year {}!".format(name, year))
