text = input().split()
my_dict = {}
symbols = ''.join(text)
for symbol in symbols:
    if symbol not in my_dict.keys():
        my_dict[symbol] = 0
    my_dict[symbol] += 1

for char, num in my_dict.items():
    print(f"{char} -> {num}")