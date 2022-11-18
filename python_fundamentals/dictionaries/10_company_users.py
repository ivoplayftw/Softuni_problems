companies = {}
while True:
    command = input()
    if command == 'End':
        break
    company, num = command.split(" -> ")

    if company not in companies.keys():
        companies[company] = [num]
    elif company in companies.keys() and num not in companies[company]:
        companies[company].append(num)

for key, value in companies.items():
    print(key)
    for i in range(len(value)):
        print(f'-- {value[i]}')
