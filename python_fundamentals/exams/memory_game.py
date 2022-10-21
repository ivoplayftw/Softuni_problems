sequence = input().split()
moves = 0
while True:
    command = input().split()

    if command[0] == "end":
        if len(sequence) > 0:
            print("Sorry you lose :(")
            print(*sequence)
            break
        break
    splitted = [int(num) for num in command]
    if splitted[0] == splitted[1] or \
            splitted[0] < 0 or splitted[1] < 0 \
            or splitted[0] > len(sequence) - 1 \
            or splitted[1] > len(sequence) - 1:
        moves += 1
        new_ele = f"-{moves}a"
        mid_of_seq = len(sequence) // 2
        sequence.insert(mid_of_seq, new_ele)
        sequence.insert(mid_of_seq, new_ele)
        print("Invalid input! Adding additional elements to the board")
        continue
    if sequence[splitted[0]] == sequence[splitted[1]]:
        moves += 1
        found_ele = sequence[splitted[0]]
        for ele in range(len(sequence)):
            if found_ele in sequence:
                sequence.remove(found_ele)
        print(f"Congrats! You have found matching elements - {found_ele}!")
    elif sequence[splitted[0]] != sequence[splitted[1]]:
        moves += 1
        print("Try again!")
    if len(sequence) == 0 and command[0] != 'end':
        print(f"You have won in {moves} turns!")
        break
