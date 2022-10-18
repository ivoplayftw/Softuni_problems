def even_nums(number):
    if number % 2 == 0:
        return True
    return False


num = input().split()
num_lst_as_ints = map(int, num)

filtered = filter(even_nums, num_lst_as_ints)
even_numbers = list(filtered)

print(even_numbers)
