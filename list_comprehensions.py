# Andrew Ingrassia
# HackerRank
# List Comprehensions

"""
TASK:
    Let's learn about list comprehensions! You are given three integers (x, y, and z) representing the dimensions of a
    cuboid along with an integer (n). Print a list of all possible coordinates ([i, j, k]) on a 3D grid where the
    sum of i + j + k is not equal to n. Use list comprehensions rather than multiple loops.

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


# --- OTHER EXAMPLES OF LIST COMPREHENSION ---

"""
EXAMPLE 1:
    a. Without comprehension:
        list_1 = []
        for x in range(10):
            list_1.append(x)

    b. With comprehension:
        list_2 = [x for x in range(10)]

EXAMPLE 2:
    a. Without comprehension:
        list_3 = []
        for x in range(10):
            if x % 3 == 0:
                list_3.append(x)

    b. With comprehension
        list_4 = [x for x in range(10) if x % 3 == 0]


EXAMPLE 3 (MY HACKERRANK ANSWER WITHOUT LIST COMPREHENSION):
    coord = []
    ijk = []
    for x in range(x + 1):
        for y in range(y + 1):
            for z in range(z + 1):
                if x + y + z != n:
                    ijk = [x, y, z]
                    coord.append(ijk)
"""
