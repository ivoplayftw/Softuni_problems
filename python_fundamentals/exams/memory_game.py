sequence = input().split()
new_sequence = [sequence]
moves = 0

while True:
    command = input()
    splitted = command.split()
    if command == "end":
        break
    if splitted[0] == splitted[1] or \
            splitted[0] < 0 or splitted[1] < 0 \
            or splitted > len(new_sequence):
        moves += 1
        new_ele = -moves + 'a'
        mid_of_seq = len(new_sequence) // 2
        splitted.insert(mid_of_seq, new_ele)
        print("Invalid input! Adding additional elements to the board")
