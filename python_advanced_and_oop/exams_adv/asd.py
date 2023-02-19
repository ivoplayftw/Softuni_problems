recipe = {
    "Patch": 30,
    "Bandage": 40,
    "MedKit": 100
}

textile = list(map(int, input().split()))
medicament = list(map(int, input().split()))

created_items = {}
remaining_resources = []

while textile and medicament:
    textile_value = textile.pop(0)
    medicament_value = medicament.pop()

    total_value = textile_value + medicament_value

    if total_value in recipe.values():
        item_name = list(recipe.keys())[list(recipe.values()).index(total_value)]
        created_items[item_name] = created_items.get(item_name, 0) + 1
    elif total_value >= recipe["MedKit"]:
        created_items["MedKit"] = created_items.get("MedKit", 0) + 1
        remaining_value = total_value - recipe["MedKit"]
        if medicament:
            medicament[0] += remaining_value
        else:
            remaining_resources.append(remaining_value)
    else:
        remaining_resources.append(textile_value)
        medicament.insert(0, medicament_value + 10)

if created_items:
    sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
    for item_name, amount in sorted_items:
        print(f"{item_name} - {amount}")

if textile:
    print(f"Textiles left: ", end="")
    print(*textile, sep=", ")
if medicament:
    print(f"Medicaments left: ", end="")
    print(*medicament, sep=", ")
if remaining_resources:
    print(f"Remaining resources: ", end="")
    print(*remaining_resources, sep=", ")

if not textile and not medicament:
    print("Textiles and medicaments are both empty.")
elif not textile:
    print("Textiles are empty.")
elif not medicament:
    print("Medicaments are empty.")
