def reception(one, two, three, count):
    hours_worked = 0
    while count > 0:
        count -= one + two + three
        hours_worked += 1
        if hours_worked % 4 == 0:
            hours_worked += 1
    return f"Time needed: {hours_worked}h."


first_empl_cap_per_hour = int(input())
second_empl_cap_per_hour = int(input())
third_empl_cap_per_hour = int(input())
students = int(input())
print(reception(first_empl_cap_per_hour,
                second_empl_cap_per_hour,
                third_empl_cap_per_hour, students))
