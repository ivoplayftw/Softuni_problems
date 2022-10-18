cards = input().split()
shuffles_to_do = int(input())

for i in range(shuffles_to_do):
    shuffled = []
    half_deck = len(cards) // 2
    left_part_shuffled = cards[0: half_deck]
    right_part_shuffled = cards[half_deck::]

    for card in range(len(left_part_shuffled)):
        shuffled.append(left_part_shuffled[card])
        shuffled.append(right_part_shuffled[card])
        cards = shuffled
print(cards)
