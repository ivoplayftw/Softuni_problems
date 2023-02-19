textiles = list(map(int, input().split()))
medicaments = list(map(int, input().split()))
patch = 30
bandage = 40
medKit = 100
empty = ''
my_dict = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}
while textiles and medicaments:
    first_textile = textiles[0]
    last_med = medicaments[-1]
    sum_of_both = first_textile + last_med

    if sum_of_both == patch:
        my_dict["Patch"] += 1
        textiles.remove(first_textile)
        medicaments.pop()
    elif sum_of_both == bandage:
        my_dict["Bandage"] += 1
        textiles.remove(first_textile)
        medicaments.pop()
    elif sum_of_both == medKit:
        my_dict["MedKit"] += 1
        textiles.remove(first_textile)
        medicaments.pop()
    elif sum_of_both > medKit:
        my_dict["MedKit"] += 1
        textiles.remove(first_textile)
        medicaments.pop()
        sum_of_both -= 100
        medicaments[-1] = medicaments[-1] + sum_of_both
    else:
        textiles.remove(first_textile)
        medicaments[-1] += 10

if len(medicaments) == 0 and len(textiles) == 0:
    empty = "Textiles and medicaments are both empty."
elif len(textiles) == 0:
    empty = "Textiles are empty."
elif len(medicaments) == 0:
    empty = "Medicaments are empty."
print(empty)

sorted_dict = sorted(my_dict, key=lambda x: (-my_dict[x], x))

for key in sorted_dict:
    if int(my_dict[key]) != 0:
        print(f"{key} - {my_dict[key]}")

if len(medicaments) > 0:
    sorted_medicaments = sorted(medicaments, reverse=True)
    print(f"Medicaments left: {', '.join(map(str, sorted_medicaments))}")
if len(textiles) > 0:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
