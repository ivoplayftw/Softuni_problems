def minimal(numbers):
    numbers_lst = numbers.split()
    numbers_lst_int = []
    for element in numbers_lst:
        numbers_lst_int.append(int(element))
    min_num = min(numbers_lst_int)
    return min_num


def maximum(numbers):
    numbers_lst = numbers.split()
    numbers_lst_int = []
    for element in numbers_lst:
        numbers_lst_int.append(int(element))
    max_num = max(numbers_lst_int)
    return max_num


def summed(numbers):
    numbers_lst = numbers.split()
    numbers_lst_int = []
    for element in numbers_lst:
        numbers_lst_int.append(int(element))
    summed_nums = sum(numbers_lst_int)
    return summed_nums


nums = input()
print(f"The minimum number is {minimal(nums)}")
print(f"The maximum number is {maximum(nums)}")
print(f"The sum number is: {summed(nums)}")
