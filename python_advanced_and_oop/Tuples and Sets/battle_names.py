lines = int(input())
set_odd = set()
set_even = set()

for line in range(lines):
    name = input()
    name = [char for char in name]
    summed = 0

    for char in name:
        value = ord(char)
        summed += value
    summed //= line + 1

    if summed % 2 == 0:
        set_even.add(summed)
    else:
        set_odd.add(summed)

summed_one = sum(set_even)
summed_two = sum(set_odd)

if summed_one == summed_two:
    union = set_odd | set_even
    print(', '.join(map(str, union)))
elif summed_one < summed_two:
    diff = set_odd - set_even
    print(', '.join(map(str, diff)))
elif summed_one > summed_two:
    symmetric = set_odd ^ set_even
    print(', '.join(map(str, symmetric)))
