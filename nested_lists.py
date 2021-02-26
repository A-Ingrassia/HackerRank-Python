# Andrew Ingrassia
# HackerRank
# Nested Lists


# Given the names and grades for each student in a class of 'n' students, store them in a nested list (a list of
# smaller lists) and print the name(s) of any student(s) having the second lowest grade.


# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each
# name on a new line.


# EXAMPLE: records = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]
#
# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.0. There are two students with that
# score: "beta" and "alpha". Ordered alphabetically, the names are printed as: "alpha" ----> "beta"


# IMPORT FORMAT:
#   a. The first line contains an integer, n, the number of students.
#   b. The '2n' subsequent lines describe each student over 2 lines.
#       - The first line contains a student's name.
#       - The second line contains their grade.


# CONSTRAINTS:
#   a. 2 <= n <= 5
#   b. There will always be one or more students having the second lowest grade.


# OUTPUT FORMAT: Print the name(s) of any student(s) having the second lowest grade in. If there are multiple
# students, order their names alphabetically and print each one on a new line.


# SAMPLE INPUT:
#   5
#   Harry
#   37.21
#   Berry
#   37.21
#   Tina
#   37.2
#   Bill
#   41
#   Harsh
#   39


# SAMPLE OUTPUT:
#   Berry
#   Harry


# EXPLANATION:
#   There are 5 students in this class whose names and grades are assembled to build the following list:
#
#   python students = [['Tina', 37.2], ['Harry', 37.21], ['Berry', 37.21], ['Harsh', 39], ['Bill', 41]]
#
#   The lowest grade of belongs to Tina. The second lowest grade of belongs to both Harry and Berry, so we order their
#   names alphabetically and print each name on a new line.


# MY ANSWER:

name_score = []
score_only = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    name_score.append([name, score])
    score_only.append(score)

second_highest = sorted(list(set(score_only)))[1]

# Creates a new list that represents a sorted version of 'score_only'
# Eliminates duplicates (by making this list into into a set)
# Chooses the second highest float in the list (in position [1])

for name, score in sorted(name_score):
    if score == second_highest:
        print(name)

# Iterates through a sorted version of the list containing both names and scores
# If the loop finds a score that matches the output of 'second_highest', it prints the associated name
