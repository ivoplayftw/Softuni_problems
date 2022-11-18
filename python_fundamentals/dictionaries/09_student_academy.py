pair_of_rows = int(input())
students_and_grades = {}

for i in range(pair_of_rows):
    student = input()
    grade = float(input())
    if student not in students_and_grades:
        students_and_grades[student] = grade
        grades = [grade]
    else:
        students_and_grades[student] = (students_and_grades[student] + grade) / 2


for key, value in students_and_grades.items():
    if value >= 4.5:
        print(f'{key} -> {value:.2f}')
