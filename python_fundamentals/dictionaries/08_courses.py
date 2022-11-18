course_and_count = {}
students = {}
while True:
    command = input().split(" : ")
    if command[0] == 'end':
        break

    if command[0] in course_and_count.keys():
        course_and_count[command[0]] += 1
        students[command[1]] = command[0]
    else:
        course_and_count[command[0]] = 1
        students[command[1]] = command[0]

for key, value in course_and_count.items():
    print(f'{key}: {value}')
    for k, v in students.items():
        if v == key:
            print(f'-- {k}')
