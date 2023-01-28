f_nums = list(map(int, input().split()))
s_nums = list(map(int, input().split()))
lines = int(input())

for line in range(lines):
    command_1, command_2, *nums_to_add = input().split()
    command = command_1 + ' ' + command_2
    nums_to_add = list(map(int, nums_to_add))
    if command == "Add First":
        f_nums.append(nums_to_add)
    elif command == "Add Second":
        s_nums.append(nums_to_add)
    elif command == "Remove First":
        f_nums.remove(nums_to_add)
    elif command == "Remove Second":
        s_nums.remove(nums_to_add)
    elif command == "Check Subset":
        print(f_nums < s_nums)
