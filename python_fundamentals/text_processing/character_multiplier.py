str_one, str_two = input().split()
total_sum = 0

if len(str_one) > len(str_two):
    for i in range(len(str_two)):
        total_sum += ord(str_one[i]) * ord(str_two[i])
    for j in range(len(str_two), len(str_one)):
        total_sum += ord(str_one[j])

elif len(str_two) > len(str_one):
    for i in range(len(str_one)):
        total_sum += ord(str_one[i]) * ord(str_two[i])
    for j in range(len(str_one), len(str_two)):
        total_sum += ord(str_two[j])
else:
    for i in range(len(str_one)):
        total_sum += ord(str_one[i]) * ord(str_two[i])

print(total_sum)
