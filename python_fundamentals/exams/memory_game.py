sequence = input().split()
new_sequence = [sequence]
moves = 0

while True:
    command = input()
    splitted = [int(ele) for ele in command.split()]
    if command == "end":
        break
    if splitted[0] == splitted[1] or \
            splitted[0] < 0 or splitted[1] < 0 \
            or splitted[0] > len(new_sequence) \
            or splitted[1] > len(new_sequence):
        moves += 1
        new_ele = str(-moves) + 'a'
        mid_of_seq = len(new_sequence) // 2
        new_sequence.insert(mid_of_seq, new_ele)
        print("Invalid input! Adding additional elements to the board")
