nums = input().split(" ")
my_stack = []
while len(nums) > 0:
    last_num = nums.pop(-1)
    my_stack.append(last_num)
print(*my_stack)
