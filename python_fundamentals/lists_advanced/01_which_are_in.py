first_sequence = input().split(", ")
second_sequence = input().split(", ")
new_list = []
for ele in first_sequence:
    for elem in second_sequence:
        if ele in elem and ele not in new_list:
            new_list.append(ele)

print(new_list)
