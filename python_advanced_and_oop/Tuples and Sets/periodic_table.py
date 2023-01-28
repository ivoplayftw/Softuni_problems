num_of_inputs = int(input())
periodic_table = set()
for n in range(num_of_inputs):
    elements = input().split()
    for ele in elements:
        periodic_table.add(ele)
print(*periodic_table, sep='\n')