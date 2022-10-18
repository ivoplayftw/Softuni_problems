nums_array = input().split()
while True:
    command = input().split()
    if command[0] == 'end':
        break
    elif command[0] == 'swap':
        nums_array[int(command[1])], nums_array[int(command[2])] = nums_array[int(command[2])], nums_array[int(command[1])]
    elif command[0] == 'multiply':
        nums_array[int(command[1])] = int(nums_array[int(command[1])]) * int(nums_array[int(command[2])])
    elif command[0] == 'decrease':
        nums_array = [int(ele) - 1 for ele in nums_array]

print(*nums_array, sep=', ')
