# Andrew Ingrassia
# HackerRank
# List Comprehensions

"""
TASK:
    You are given three integers (x, y, and z) representing the dimensions of a cuboid along with an integer (n).
    Print a list of all possible coordinates ([i, j, k]) on a 3D grid where the sum of i + j + k is not equal to n.
    Use list comprehensions rather than multiple loops.

INPUT FORMAT:
    Four integers (x, y, z, and n), each on a separate line.

OUTPUT FORMAT:
    Printed list in lexicographic increasing order.

EXAMPLE INPUT:
    x = 1
    y = 1
    z = 1
    n = 2

EXAMPLE OUTPUT:
    [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""

# MY ANSWER:
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
print(coordinates)


# EXPLANATION (same result without list comprehension):

coord = []                                      # empty coordinates list
ijk = []                                        # empty list for possible grid coordinates
for x in range(x + 1):                          # for every position along dimension 'x'...
    for y in range(y + 1):                      # and every position along dimension 'y'...
        for z in range(z + 1):                  # and every position along dimension 'z'...
            if x + y + z != n:                  # as long as the sum of x+y+z is not equal to 'n'...
                ijk = [x, y, z]                 # a given coordinate equals [x, y, z]
                coord.append(ijk)               # append to 'coord' list every coordinate that passes muster

                                                # NOTE: +1 to each dimension because Python lists are zero based
