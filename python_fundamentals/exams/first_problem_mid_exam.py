adventure_days = int(input())
players = int(input())
group_ene = float(input())
water_per_pl = float(input())
food_per_pl = float(input())
total_water = adventure_days * players * water_per_pl
total_food = adventure_days * players * food_per_pl

for day in range(1, adventure_days + 1):
    lost_ene = float(input())
    group_ene -= lost_ene
    if group_ene <= 0:
        break

    if day % 2 == 0 and day % 3 == 0:
        group_ene += group_ene * 0.05
        total_water -= total_water * 0.30
        total_food -= total_food / players
        group_ene += group_ene * 0.10
    elif day % 2 == 0:
        group_ene += group_ene * 0.05
        total_water -= total_water * 0.30
    elif day % 3 == 0:
        total_food -= total_food / players
        group_ene += group_ene * 0.10


if group_ene > 0:
    print(f"You are ready for the quest. You will be left with - {group_ene:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")

