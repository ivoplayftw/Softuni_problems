numbers_list = input().split()
nums_to_remove = int(input())
digits_list = []

for i in range(len(numbers_list)):
    digits_list.append(int(numbers_list[i]))

for i in range(nums_to_remove):
    digits_list.remove(min(digits_list))
print(*digits_list, sep=', ')
