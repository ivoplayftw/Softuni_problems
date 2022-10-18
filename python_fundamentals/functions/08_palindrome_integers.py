def palindrome_check(numbers):
    numbers_lst = numbers.split(', ')
    for element in numbers_lst:
        if element == element[::-1]:
            result = True
        else:
            result = False
        print(result)


nums = input()
palindrome_check(nums)
