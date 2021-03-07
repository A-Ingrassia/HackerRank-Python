# Andrew Ingrassia
# HackerRank
# Find a String


"""
TASK:
    In this challenge, the user enters a string and a substring. You have to print the number of times that the
    substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE:
    String letters are case-sensitive.

INPUT FORMAT:
    a. The first line of input contains the original string.
    b. The next line contains the substring.

CONSTRAINTS:
    a. 1 <= len(string) <= 200
    b. Each character in the string is an ascii character.

OUTPUT FORMAT:
    Output the integer number indicating the total number of occurrences of the substring in the original string.

SAMPLE INPUT:
    ABCDCDC
    CDC

SAMPLE OUTPUT:
    2
"""


def count_substring(s, sub_s):
    num_occurrences = 0                # initialize sub_s occurrence count to 0
    for i in range(len(s)):            # for every element in range(0, len(s))...
        if s[i:].startswith(sub_s):    # traverses string from left to right, looking for occurrences of 'sub_s'
            num_occurrences += 1       # each time an occurrence is located, 'num_occurrences' increases by 1
    return num_occurrences             # returns the final 'num_occurrences' count


if __name__ == '__main__':
    string = input().strip()                         # strips 'string' into a list of characters
    sub_string = input().strip()                     # strips 'sub_string' into a list of characters
    count = count_substring(string, sub_string)      # runs the 'count_substring' function
    print(count)                                     # prints the result
