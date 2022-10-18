def sort_numbers(numbers):
    num_list = numbers.split()
    nums_as_ints = []
    for element in num_list:
        nums_as_ints.append(int(element))

    return sorted(nums_as_ints)


nums = str(input())
print(sort_numbers(nums))