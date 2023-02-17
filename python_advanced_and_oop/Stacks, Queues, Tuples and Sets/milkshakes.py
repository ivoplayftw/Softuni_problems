from collections import deque

chocs = deque(int(x) for x in input().split(', '))
cups_of_milk = deque(int(x) for x in input().split(', '))

milkshakes = 0

while milkshakes != 5 and chocs and cups_of_milk:
    choco = chocs.pop()
    cup_of_milk = cups_of_milk.popleft()

    if choco <= 0 and cup_of_milk <= 0:
        continue
    elif choco <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocs.append(choco)
        continue

    if choco == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocs.append(choco - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if len(chocs) > 0:
    print(f"Chocolate: {', '.join(map(str, chocs))}")
else:
    print(f"Chocolate: empty")

if len(cups_of_milk) > 0:
    print(f"Milk: {', '.join(map(str, cups_of_milk))}")
else:
    print(f"Milk: empty")

