# Andrew Ingrassia
# HackerRank
# sWAP cASE


"""
TASK:
    You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase
    letters and vice versa.

INPUT FORMAT:
    A single line containing a string S.

OUTPUT FORMAT:
    Print the modified string S.

SAMPLE INPUT:
    HackerRank.com presents "Pythonist 2".

SAMPLE OUTPUT:
    hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""


def swap_case(s):

    modified_string = ""                        # Strings are immutable, so using .upper() and .lower() wouldn't
                                                # actually modify anything. YOU HAVE TO CREATE AN ENTIRELY NEW STRING.

    for char in s:                              # Loops over each character in 's'...
        if char.isupper():                      # If the character is uppercase...
            modified_string += char.lower()     # Adds a lowercase version of that character to 'modified_string'
        elif char.islower():                    # If the character is lowercase...
            modified_string += char.upper()     # Adds an uppercase version of that character to 'modified_string'
        else:                                   # Otherwise (to cover spaces, punctuation, and numbers)...
            modified_string += char             # Adds the character as-is to 'modified_string'

    return modified_string                      # Returns the new, modified version of 's'


s = input()                                     # User's input
result = swap_case(s)                           # Function call
print(result)                                   # Prints the final result


""" 
NOTE: Python has a builtin function that handles case swapping (str.swapcase()), so another version of the same
      code that yields the same result would be as follows...
      
      def swap_case(s):
        return s.swapcase()
        
      s = input()
      result = swap_case(s)
      print(result)
"""
