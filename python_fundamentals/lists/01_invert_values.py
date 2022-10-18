nums = input().split()
listed = []
for number in range(len(nums)):
        digit_opposite = -int(nums[number])
        listed.append(digit_opposite)
print(listed)
