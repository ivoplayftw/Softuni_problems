lines = int(input())
count = 0
for i in range(lines):
    some_input = input()
    if some_input == "(":
        count += 1
    if count > 1 or count < 0:
        print("UNBALANCED")
        break
    if some_input == ")":
        count -= 1

if count == 0:
    print("BALANCED")
