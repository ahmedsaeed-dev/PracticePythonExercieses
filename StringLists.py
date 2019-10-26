"""
https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

val = '!!99r!ace!caR@!99'
valSanitized = ''

# for each char in the value where converted to lowercase
for i in val.lower():
    # sanitize by only appending alphanumeric values
    if i.isalnum():
        valSanitized += i

# compare sanitized against reversed sanitized
if valSanitized == valSanitized[::-1]:
    print("palindrome!")
else:
    print("Not palindrome!")
