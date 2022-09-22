number = input()
string_of_number = str(number)
sort_num = sorted(string_of_number, reverse=True)
for d, digit in enumerate(sort_num):
    print(digit, end="")
