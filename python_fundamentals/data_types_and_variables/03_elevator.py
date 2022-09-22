people = int(input())
capacity = int(input())
courses = 0
while people > 0:
    people -= capacity
    courses += 1
print(courses)
