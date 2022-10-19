passangers = int(input())
lift = input().split()
inted_lift = [int(ele) for ele in lift]
equal = False

for elem in range(len(inted_lift)):
    if inted_lift[elem] != 4 and passangers != 0:
        while inted_lift[elem] != 4 and passangers != 0:
            inted_lift[elem] = inted_lift[elem] + 1
            passangers -= 1

for elem in inted_lift:
    if elem == 4:
        equal = True
    else:
        equal = False

if not equal and passangers == 0:
    print("The lift has empty spots!")
    print(*inted_lift)


if equal and passangers != 0:
    print(f"There isn't enough space! {passangers} people in a queue!")
    print(*inted_lift)


if equal and passangers == 0:
    print(*inted_lift)
