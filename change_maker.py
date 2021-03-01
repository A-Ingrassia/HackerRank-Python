# Andrew Ingrassia
# HackerRank (Launch Code Puzzle)
# Change Maker


def ChangeMaker(price, payment):

    price *= 100                                           # Avoids rounding errors (Python likes to round down floats)
    payment *= 100

    total_payment = sum(payment)                           # Adds together all the elements from 'payment' array

    if total_payment >= price:                             # What happens if customer has sufficient $
        change_list = [0, 0, 0, 0]                         # Initializes the list representing change (p, n, d, q)
        current_total = total_payment - price              # Total leftover $ after customer buys item

        change_list[3] = int(current_total // 25)          # Determines number of quarters
        current_total = current_total % 25                 # Adjusts change amount after quarters have been counted

        change_list[2] = int(current_total // 10)          # Determines number of dimes
        current_total = current_total % 10                 # Adjusts change amount after dimes have been counted

        change_list[1] = int(current_total // 5)           # Determines number of nickels
        current_total = current_total % 5                  # Adjusts change amount after nickles have been counted

        change_list[0] = int(current_total // 1)           # Determines number of pennies

        return change_list

    if total_payment < price:                              # What happens if customer doesn't have enough $
        change_list = [0, 0, 0, 0]
        current_total = total_payment

        change_list[3] = int(current_total // 25)
        current_total = current_total % 25

        change_list[2] = int(current_total // 10)
        current_total = current_total % 10

        change_list[1] = int(current_total // 5)
        current_total = current_total % 5

        change_list[0] = int(current_total // 1)

        return change_list


# EXAMPLE CALLS:
print(ChangeMaker(1.87, [.25, .25, .25, .25, 1.00]))
print(ChangeMaker(1.87, [.25, .25, .25, .25, .1, .1, .05, .01, .01, .01]))

# EXAMPLE OUTPUTS:
# [3, 0, 1, 0]
# [3, 0, 0, 5]
