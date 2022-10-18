numbers = input().split(', ')
group = 10
while len(numbers) > 0:
    group_list = [int(num) for num in numbers if 0 < int(num) <= group]
    print(f"Group of {group}'s: {group_list}", sep='\n')
    group += 10
    for ele in group_list:
        numbers.remove(str(ele))
