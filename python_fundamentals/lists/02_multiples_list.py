factor_num = int(input())
count_num = int(input())
digit_list = []
for number in range(1, count_num + 1):
    digit_list.append(number * factor_num)
print(digit_list)
