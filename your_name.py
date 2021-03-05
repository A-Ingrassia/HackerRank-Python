# Andrew Ingrassia
# HackerRank
# What's Your Name?


"""
TASK:
    You are given the first name and last name of a person on two different lines. Your task is to read them and print
    the following:

    "Hello firstname lastname! You just delved into python."

INPUT FORMAT:
    The first line contains the first name, and the second line contains the last name.

CONSTRAINTS:
    The length of the first and last name ≤ 10.

OUTPUT FORMAT:
    Print the output as mentioned above.

SAMPLE INPUT:
    Ross
    Taylor

SAMPLE OUTPUT:
    Hello Ross Taylor! You just delved into python.
"""


def print_full_name(a, b):
    print(f"Hello {a.title()} {b.title()}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


"""
EXPLANATION: 
    'first_name' is parameter 'a', and 'last_name' is parameter 'b', so I simply replaced 'firstname' and 
    'lastname' from the required output string using an f string (and added .title() just in case the user
    didn't use capitalization). 
"""
