# Andrew Ingrassia
# HackerRank
# Finding The Percentage


"""
TASK:
    The provided code stub will read in a dictionary containing key/value pairs of name:[grades] for a list of students.
    Print the average of the grades array for the student name provided, showing 2 places after the decimal.

INPUT FORMAT:
    a. The first line contains the integer 'n', the number of students' records.
    b. The next lines contain the names and grades obtained by a student, each value separated by a space.
    c. The final line contains query_name, the name of a student to query.

CONSTRAINTS:
    a. 2 <= n <= 10
    b. 0 <= grades[i] <= 100
    c. length of grades array = 3

OUTPUT FORMAT:
    Print one line - the average of the grades obtained by the particular student, correct to 2 decimal places.

SAMPLE INPUTS:
    3
    Eva 67 68 69
    Luca 70 98 63
    Ivy 52 56 60
    Ivy

SAMPLE OUTPUT:
    56.00
"""


# MY ANSWER:
n = int(input())
student_grades = {}

grade_sum = 0
grade_average = 0

for _ in range(n):
    name, *score = input().split()
    scores = list(map(float, score))
    student_grades[name] = scores

query_name = input()

for grade in student_grades[query_name]:
    grade_sum += grade

grade_average = grade_sum/len(student_grades[query_name])
print(f"{grade_average: .2f}")


"""
EXPLANATION:
    a. Line 37: number of student records (input)
    b. Line 38: dictionary representing student names/grades (input)
    c. Line 40: initializes sum of student grades to 0
    d. Line 41: initializes avg of students grades to 0
    e. Line 43: for each element in range(n)...
    f. Line 44: splits each student_grades entry into space separated values
    g. Line 45: assembles each student's scores into a list of floats
    h. Line 46: dictionaries created with student name as key and score list as value
    i. Line 48: user indicates the name of one of the students
    j. Lines 50 - 51: adds together the grades of the indicated student
    k. Line 53: divides the sum of grades by the number of grades available
    l. Line 54: prints the grade average, showing 2 places after the decimal
"""
