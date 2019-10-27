"""
https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
Ask the user for a number and determine whether the number is prime or not.
"""


def check_prime(val):
    if val == 1:
        return "{} is not prime".format(val)
    elif val == 2:
        return "{} is not prime".format(val)
    else:
        for i in range(2, (val/2)+1):
            if val % i == 0:
                return "{} is not prime".format(val)

    return "{} is prime".format(val)


print(check_prime(int(input("Enter value to determine if prime: "))))
