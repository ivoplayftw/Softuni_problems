numbers = input().split(', ')
digit_list = []
for element in numbers:
    digit_list.append(int(element))

beggar_count = int(input())
nums_taken = []
start = 0

while start < beggar_count:
    beggar_sum = 0

    for i in range(start, len(digit_list), beggar_count):
        beggar_sum += digit_list[i]
    nums_taken.append(beggar_sum)
    start += 1
print(nums_taken)
