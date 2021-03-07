# Andrew Ingrassia
# HackerRank
# Mutations


"""
TASK:
    Read a given string, change the character at a given index and then print the modified string.

INPUT FORMAT:
    a. The first line contains a string, 's'.
    b. The next line contains an integer 'i', denoting the index location and a character 'c' separated by a space.

OUTPUT FORMAT:
    Replace the character at index 'i' with character 'c'.

SAMPLE INPUT:
    abracadabra
    5 k

SAMPLE OUTPUT:
    abrackdabra

NOTE:
    Strings are immutable, so one way to change a specific element within a string is to first convert the string to
    a list, as in the following example:

    string = "abracadabra"
    l = list(string)
    l[5] = 'k'
    string = ''.join(l)
    print(string)
    abrackdabra
"""


def mutate_string(string, position, character):
    listified_string = list(string)                 # converts user's string ('s') to a list of characters
    listified_string[position] = character          # swaps out the character in position 'i' with 'c'
    string = ''.join(listified_string)              # reassembles (joins) the list back into a string
    return string                                   # returns the modified string


if __name__ == '__main__':
    s = input()                                     # user inputs a string ('s')
    i, c = input().split()                          # user inputs related to position ('i')of character to swapped as
                                                    # well as the desired new character ('c')
    s_new = mutate_string(s, int(i), c)             # runs 'mutate_string' function with 's', 'i', and 'c' as parameters
    print(s_new)                                    # prints the result
