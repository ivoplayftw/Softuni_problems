n, m = list(map(int, input().split()))
matrix = []
value_temp = 0
moves = 0
found_people = 0

for row in range(n):
    rows = input().split()
    matrix.append(rows)
    try:
        start_row = matrix[row].index("B")
    except ValueError:
        start_row = -1
    if start_row != -1:
        start_pos = start_row
        my_place = [value_temp, start_pos]
    value_temp += 1

while True:
    command = input()

    try:
        if command == "Finish" or found_people == 3:
            break
        if command == "up":
            my_place[0] = my_place[0] - 1
            moves += 1
        elif command == 'down':
            my_place[0] = my_place[0] + 1
            moves += 1
        elif command == 'right':
            my_place[1] = my_place[1] + 1
            moves += 1
        elif command == 'left':
            my_place[1] = my_place[1] - 1
            moves += 1
    except RuntimeError:
        continue

    if matrix[my_place[0]][my_place[1]] == 'O':
        moves -= 1
        matrix[my_place[0]][my_place[1]] = '-'

    if matrix[my_place[0]][my_place[1]] == 'P':
        found_people += 1
        matrix[my_place[0]][my_place[1]] = '-'

print(f"Game over!")
print(f"Touched opponents: {found_people} Moves made: {moves}")