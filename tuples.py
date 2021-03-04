# Andrew Ingrassia
# HackerRank
# Tuples

"""
TASK:
    You are given an integer, 'n', on a single line. The next line contains 'n' space-separated integers. Create a
    tuple, 't', of those 'n' integers, then compute and print the result of hash(t).

NOTE:
    hash() is one of the functions in the __builtins__ module.

INPUT FORMAT:
    a. The first line contains an integer, n (the number of elements in the tuple).
    b. The second line contains n space-separated integers describing t.

OUTPUT FORMAT:
    Print the result of hash(t).

SAMPLE INPUT:
    2
    1 2

SAMPLE OUTPUT:
    3713081631934410656
"""


# MY ANSWER:
n = int(input())                                 # number of space-separated integers
integer_list = map(int, input().split())         # assembles 'n' integers into a list

t = tuple(integer_list)                          # creates a tuple and populates it with the contents of integer_list
print(hash(t))                                   # prints result of hash(t)
