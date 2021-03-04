# Andrew Ingrassia
# HackerRank
# Runner-Up Score

"""
TASK:
    Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
    You are given scores. Store them in a list and find the score of the runner-up.

INPUT FORMAT:
    The first line contains 'n'. The second line contains an array A[] of 'n' integers each separated by a space.

CONSTRAINTS:
    a. 2 <= n <= 10
    b. -100 <= A[i] <= 100

OUTPUT FORMAT:
    Print the runner-up score.

SAMPLE INPUT:
    5
    2 3 6 6 5

SAMPLE OUTPUT:
    5

EXPLANATION:
    a. Given list is [2, 3, 6, 6, 5]
    b. Max score = 6
    c. Second max = 5
    d. Hence, we print '5' as the runner-up score
"""

# MY ANSWER:
n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])


"""
EXPLANATION:
    Line 1: number of integers within the given array ('n')
    Line 2: array of 'n' integers, 'split' into comma separated elements (made into a list)
    Line 3:
        a. transforms list into a set, eliminating duplicates
        b. sorts the integers within the set - lowest to highest (by default)
        c. prints the second highest element (second from the end of the set = [-2])
"""
