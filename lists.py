# Andrew Ingrassia
# HackerRank
# Lists


# Consider a list (list = []). You can perform the following commands:
#   a. insert i e: Insert integer e at position i.
#   b. print: Print the list.
#   c. remove e: Delete the first occurrence of integer e.
#   d. append e: Insert integer e at the end of the list.
#   e. sort: Sort the list.
#   f. pop: Pop the last element from the list.
#   g. reverse: Reverse the list.

# Initialize your list and read in the value of 'n' followed by 'n' lines of commands where each command will be of the
# types listed above. Iterate through each command in order and perform the corresponding operation on your list.


# INPUT FORMAT:
#   a. The first line contains an integer, 'n', denoting the number of commands.
#   b. Each subsequent line contains one of the commands described above.


# OUTPUT FORMAT: For each command of type print, print the list on a new line.


# SAMPLE INPUT:
#   12
#   insert 0 5
#   insert 1 10
#   insert 0 6
#   print
#   remove 6
#   append 9
#   append 1
#   sort
#   print
#   pop
#   reverse
#   print


# SAMPLE OUTPUT:
#   [6, 5, 10]
#   [1, 5, 9, 10]
#   [9, 5, 1]


# MY ANSWER:

# Initialize my list (the one that will be manipulated and printed):
my_list = []

# User inputs number of subsequent commands:
n = int(input())

# For each command (in range(n)), perform the indicated action:
for x in range(n):

    command_list = input().split()   # Splits the command's components into a list

    command = command_list[0]        # The first element in the newly split list will indicate which command to execute

    if command == "insert":
        my_list.insert(int(command_list[1]), int(command_list[2]))

    if command == "print":
        print(my_list)

    if command == "remove":
        my_list.remove(int(command_list[1]))

    if command == "append":
        my_list.append(int(command_list[1]))

    if command == "sort":
        my_list.sort()

    if command == "pop":
        my_list.pop()

    if command == "reverse":
        my_list.reverse()
