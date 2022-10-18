nums = input().split()
nums_as_ints = [int(x) for x in nums]
average = sum(nums_as_ints) / len(nums)
above_average = []
for element in nums:
    if int(element) > average:
        above_average.append(int(element))
if len(above_average) == 0:
    print("No")
else:
    sorted_nums = sorted(above_average, reverse=True)
    print(*sorted_nums[:5])
