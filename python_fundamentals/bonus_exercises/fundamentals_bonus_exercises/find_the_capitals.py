inputed_string = input("")
index_of_capital = []
for i in range(len(inputed_string)):
    if inputed_string[i].isupper():
        index_of_capital.append(i)
    else:
        continue

print(index_of_capital)
