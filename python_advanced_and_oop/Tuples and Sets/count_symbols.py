text = input()
text = sorted([ele for ele in text])
dict = {}

for ele in text:
    if ele not in dict.keys():
        dict[ele] = 1
    else:
        dict[ele] += 1

for symbol, num in dict.items():
    print(f"{symbol}: {num} time/s", sep='\n')
