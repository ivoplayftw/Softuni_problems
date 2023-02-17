size_of_matrix = int(input())
matrix = []
destroyed_ships = 0
hits = 0
start_pos = -1
value_temp = 0
ship_place = []

for row in range(size_of_matrix):
    rows = list(input())
    matrix.append(rows)
    try:
        start_row = matrix[row].index("S")
    except ValueError:
        start_row = -1
    if start_row != -1:
        start_pos = start_row
        ship_place = [value_temp, start_pos]
    value_temp += 1

while True:

    command = input()
    matrix[ship_place[0]][ship_place[1]] = "-"
    if hits == 3 or destroyed_ships == 3:
        break

    if command == "up":
        ship_place[0] = ship_place[0] - 1
    elif command == 'down':
        ship_place[0] = ship_place[0] + 1
    elif command == 'right':
        ship_place[1] = ship_place[1] + 1
    elif command == 'left':
        ship_place[1] = ship_place[1] - 1

    if matrix[ship_place[0]][ship_place[1]] == '*':
        hits += 1
        matrix[ship_place[0]][ship_place[1]] = '-'

    if matrix[ship_place[0]][ship_place[1]] == 'C':
        destroyed_ships += 1
        matrix[ship_place[0]][ship_place[1]] = '-'

if hits == 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates [{ship_place[0]}, {ship_place[1]}]!")
elif destroyed_ships == 3:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

matrix[ship_place[0]][ship_place[1]] = "S"
for row in matrix:
    print("".join(row), end="\n")
