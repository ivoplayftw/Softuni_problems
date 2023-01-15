box = input().split()
single_rack_cap = int(input())

racks = 1
current_rack = single_rack_cap

while box:
    cloth = int(box.pop())

    if current_rack - cloth >= 0:
        current_rack -= cloth
    else:
        racks += 1
        current_rack = single_rack_cap - cloth
print(racks)
