lines = int(input())
longest = []
intersec = []
for line in range(lines):
    first, second = input().split("-")
    first_split = first.split(",")
    second_split = second.split(",")
    set_1 = set()
    set_2 = set()

    for i in range(int(first_split[0]), int(first_split[1]) + 1):
        set_1.add(i)
    for j in range(int(second_split[0]), int(second_split[1]) + 1):
        set_2.add(j)

    intersection = set_1 & set_2
    if len(intersection) > len(intersec):
        intersec = intersection
    else:
        continue
print_list = [ele for ele in intersec]
print(f"Longest intersection is {print_list} with length {len(intersec)}")