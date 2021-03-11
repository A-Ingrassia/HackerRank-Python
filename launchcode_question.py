# Andrew Ingrassia
# LaunchCode Question
# 3.10.2021


"""
TASK:
    Write a function that returns the index of the highest value(s) in an array.

INPUT:
    An array of integers (ex. [1, 3, 4, 4, 2]).

OUTPUT:
    Index position(s) of highest value within the array.
"""


def highest_val(array):                       # function definition - takes an array as a parameter
    sorted_array = sorted(array)              # sorts the given array
    highest_int = sorted_array[-1]            # determines the highest integer within the given array
    indices = []                              # initializes an empty list representing desired index positions

    for index, element in enumerate(array):   # loops over and assigns an index value to each element in the given array
        if element == highest_int:            # if the given element == highest_int (sorted_array[-1])...
            indices.append(str(index))        # append that value to 'indices' in the form of a string

    return ", ".join(indices)                 # return all elements within 'indices', separated by a comma


print(highest_val([1, 3, 4, 4, 2]))           # example function call (should return index positions 2 & 3)
