quantity_food_kg = float(input())
quantity_hay_kg = float(input())
quantity_cover_kg = float(input())
guinea_pig_weight_kg = float(input())
month = 30
excess_food = 0
excess_hay = 0
excess_cover = 0

for day in range(1, month + 1):
    if excess_food < 0 or excess_hay < 0 or excess_cover < 0:
        break
    quantity_food_kg -= 0.3
    if day % 2 == 0:
        given_hay = quantity_food_kg * 0.05
        quantity_hay_kg -= given_hay
    if day % 3 == 0:
        cover_put = guinea_pig_weight_kg / 3
        quantity_cover_kg -= cover_put

    excess_food = quantity_food_kg
    excess_hay = quantity_hay_kg
    excess_cover = quantity_cover_kg

if excess_food <= 0 or excess_hay <= 0 or excess_cover <= 0:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {excess_food:.2f}, Hay: {excess_hay:.2f}, Cover: {excess_cover:.2f}.")
