# Andrew Ingrassia
# HackerRank (Launch Code Puzzle)
# Change Maker


def ChangeMaker(price, payment):

    price *= 100                                           # Avoids rounding errors (Python like to round down)
    payment *= 100

    total_payment = sum(payment)                           # Adds together all the elements from 'payment' array

    if total_payment >= price:
        change_list = [0, 0, 0, 0]                         # Initializes my outputs
        current_total = total_payment - price

        change_list[3] = int(current_total // 25)
        current_total = current_total % 25

        change_list[2] = int(current_total // 10)
        current_total = current_total % 10

        change_list[1] = int(current_total // 5)
        current_total = current_total % 5

        change_list[0] = int(current_total // 1)

        return change_list

    if total_payment < price:
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
