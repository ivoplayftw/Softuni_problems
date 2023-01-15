from collections import deque
quantity_food = int(input())
order = input().split(' ')
order = [int(ele) for ele in order]
biggest_order = max(order)
print(biggest_order)

while len(order) > 0:
    if quantity_food >= order[0]:
        quantity_food -= order[0]
        deque(order)
    else:
        break

if len(order) > 0:
    print(f"Orders left: {' '.join(map(str, order))}")
else:
    print(f"Orders complete")
