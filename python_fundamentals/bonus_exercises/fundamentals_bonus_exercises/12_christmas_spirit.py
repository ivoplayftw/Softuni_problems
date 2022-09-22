quantity_decors_needed = int(input())
days_left_to_christmas = int(input())
ornaments_price = 2
tree_skirt = 5
tree_garland = 3
tree_lights = 15
spirit_points = 0
current_day = 0
total = 0
while current_day != days_left_to_christmas:
    current_day += 1
    if current_day % 11 == 0:
        quantity_decors_needed += 2
    if current_day % 2 == 0:
        total += ornaments_price * quantity_decors_needed
        spirit_points += 5
    if current_day % 3 == 0:
        total += (tree_skirt + tree_garland) * quantity_decors_needed
        spirit_points += 13
    if current_day % 5 == 0:
        total += tree_lights * quantity_decors_needed
        spirit_points += 17
    if current_day % 3 == 0 and current_day % 5 == 0:
        spirit_points += 30
    if current_day % 10 == 0:
        spirit_points -= 20
        total += tree_skirt + tree_garland + tree_lights
last_day = current_day
if last_day % 10 == 0:
    spirit_points -= 30
print(f"Total cost: {total}")
print(f"Total spirit: {spirit_points}")
