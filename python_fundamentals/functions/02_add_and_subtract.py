def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(added, num_3):
    return added - num_3


def add_and_subract(num_1, num_2, num_3):
    sum_of_first_two = sum_numbers(num_1, num_2)
    subracted = subtract(sum_of_first_two, num_3)
    return subracted


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())
print(add_and_subract(number_1, number_2, number_3))
