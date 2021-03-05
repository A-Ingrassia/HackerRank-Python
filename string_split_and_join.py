# Andrew Ingrassia
# HackerRank
# String Split and Join


"""
In Python, a string can be split on a delimiter.

EXAMPLE:
    a = "this is a string"
    a = a.split(" ") ('a' is converted to a list of strings.)
    print(a)

    ['this', 'is', 'a', 'string']

Joining a string is simple:
    a = "-".join(a)
    print(a)

    this-is-a-string

TASK:
    You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

INPUT FORMAT:
    The first line contains a string consisting of space separated words.

OUTPUT FORMAT:
    Print the formatted string as explained above.
"""


def split_and_join(line):
    split_line = line.split()                   # Splits the user's input into a list of strings
    joined_line = "-".join(split_line)          # Reassembles the list into a hyphen-separated string
    return joined_line                          # Returns the result


if __name__ == '__main__':
    line = input()                              # User's input
    result = split_and_join(line)               # Function call
    print(result)                               # Prints the result
