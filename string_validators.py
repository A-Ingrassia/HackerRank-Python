# Andrew Ingrassia
# HackerRank
# String Validators


"""
Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical
characters, alphanumeric characters, digits, etc.

Example: 'str.isalnum()'

This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
    - print 'ab123'.isalnum()
        True
    - print 'ab123#'.isalnum()
        False

Example: 'str.isalpha()'

This method checks if all the characters of a string are alphabetical (a-z and A-Z).
    - print 'abcD'.isalpha()
        True
    - print 'abcd1'.isalpha()
        False

Example: 'str.isdigit()'

This method checks if all the characters of a string are digits (0-9).
    - print '1234'.isdigit()
        True
    - print '123edsd'.isdigit()
        False

Example: 'str.islower()'

This method checks if all the characters of a string are lowercase characters (a-z).
    - print 'abcd123#'.islower()
        True
    - print 'Abcd123#'.islower()
        False

Example: 'str.isupper()'

This method checks if all the characters of a string are uppercase characters (A-Z).
    - print 'ABCD123#'.isupper()
        True
    - print 'Abcd123#'.isupper()
        False

TASK:
    You are given a string ('s'). Your task is to find out if the string contains:
        a. alphanumeric characters
        b. alphabetical characters
        c. digits
        d. lowercase characters
        e. uppercase characters

INPUT FORMAT:
    A single line containing a string ('s').

CONSTRAINTS:
    0 < len(s) < 1000

OUTPUT FORMAT:
    a. In the first line, print True if 's' has any alphanumeric characters. Otherwise, print False.
    b. In the second line, print True if 's' has any alphabetical characters. Otherwise, print False.
    c. In the third line, print True if 's' has any digits. Otherwise, print False.
    d. In the fourth line, print True if 's' has any lowercase characters. Otherwise, print False.
    e. In the fifth line, print True if 's' has any uppercase characters. Otherwise, print False.

SAMPLE INPUT:
    qA2

SAMPLE OUTPUT:
    True
    True
    True
    True
    True
"""

# MY ANSWER

s = input()

print(any(element.isalnum() for element in s))    # checks for alphanumeric elements
print(any(element.isalpha() for element in s))    # checks for alphabetical elements
print(any(element.isdigit() for element in s))    # checks for digit elements
print(any(element.islower() for element in s))    # checks for lowercase elements
print(any(element.isupper() for element in s))    # checks for uppercase elements


"""
NOTES: 
    a. The any() function returns True if any item in an iterable are true, otherwise it returns False.
    b. If the iterable object is empty, the any() function will return False.
"""
