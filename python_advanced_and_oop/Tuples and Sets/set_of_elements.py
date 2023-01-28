n, m = input().split()
first_set = set()
second_set = set()

for set1 in range(int(n)):
    first_set.add(int(input()))
for set2 in range(int(m)):
    second_set.add(int(input()))

print(*first_set & second_set, sep='\n')
