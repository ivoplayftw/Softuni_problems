input_1 = input().split()
input_2 = input().split()
f_nums = set()
s_nums = set()
lines = int(input())

for ele in input_1:
    f_nums.add(int(ele))
for ele in input_2:
    s_nums.add(int(ele))

for line in range(lines):
    command_1, command_2, *command_3 = input().split()
    command = command_1 + ' ' + command_2
    if command == "Add First":
        for ele in command_3:
            if int(ele) not in f_nums:
                f_nums.add(int(ele))
    elif command == "Add Second":
        for ele in command_3:
            if int(ele) not in s_nums:
                s_nums.add(int(ele))
    elif command == "Remove First":
        for ele in command_3:
            if int(ele) in f_nums:
                f_nums.remove(int(ele))
    elif command == "Remove Second":
        for ele in command_3:
            if int(ele) in s_nums:
                s_nums.remove(int(ele))
    elif command == "Check Subset":
        if f_nums > s_nums or s_nums > f_nums:
            print('True')
        else:
            print('False')

f_nums = sorted(f_nums)
s_nums = sorted(s_nums)

print(*f_nums, sep=', ')
print(*s_nums, sep=', ')
