"""
https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

value = int(input("Enter a number to find all it's divisors: "))
x = []

# for each value from 1 to the user inputted value, find all results that = 0 mod
for i in range(1, value+1):
    if value % i == 0:
        x.append(i)
print(x)
