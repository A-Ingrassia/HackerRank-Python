# Andrew Ingrassia
# HackerRank
# Finding The Percentage


# OVERVIEW:
# The provided code stub will read in a dictionary containing key/value pairs of name:[grades] for a list of students.
# Print the average of the grades array for the student name provided, showing 2 places after the decimal.


# INPUT FORMAT:
#   a. The first line contains the integer 'n', the number of students' records.
#   b. The next lines contain the names and grades obtained by a student, each value separated by a space.
#   c. The final line contains query_name, the name of a student to query.


# CONSTRAINTS:
#   a. 2 <= n <= 10
#   b. 0 <= grades[i] <= 100
#   c. length of grades array = 3


# OUTPUT FORMAT:
# Print one line - the average of the grades obtained by the particular student, correct to 2 decimal places.


# SAMPLE INPUTS:
#   3
#   Eva 67 68 69
#   Luca 70 98 63
#   Ivy 52 56 60
#   Ivy


# SAMPLE OUTPUT: 56.00


# MY ANSWER:

n = int(input())
student_grades = {}
grade_sum = 0
grade_average = 0

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_grades[name] = scores

query_name = input()

for grade in student_grades[query_name]:
    grade_sum += grade

grade_average = grade_sum/len(student_grades[query_name])
print(f"{grade_average: .2f}")
