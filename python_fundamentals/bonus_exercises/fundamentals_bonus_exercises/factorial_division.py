from math import factorial


def factorial_of_num(num_1, num_2):
    return factorial(num_1) // factorial(num_2)


number_1 = int(input())
number_2 = int(input())
print(f"{factorial_of_num(number_1, number_2):.2f}")
