"""
https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?
"""
value = int(input("Enter a value: "))
check = int(input("Enter a value to divide {} by: ".format(value)))


if value % check == 0:
    print("\n{} divides equally by {}".format(value, check))
    if value % 4 == 0:
        print("{} is also a multiple of 4!".format(value))
else:
    print("\n{} does not divide equally by {}".format(value, check))
