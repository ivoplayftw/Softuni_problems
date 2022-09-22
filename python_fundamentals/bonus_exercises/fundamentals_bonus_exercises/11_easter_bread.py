budget = float(input())
kg_of_flour_price = float(input())
eggs_price_pack = kg_of_flour_price * 0.75
milk_price_one_kg = kg_of_flour_price * 1.25
one_loaf_price = eggs_price_pack + kg_of_flour_price + (milk_price_one_kg / 4)
loaves_count = 0
coloured_eggs_count = 0
while budget >= one_loaf_price:
    loaves_count += 1
    if loaves_count % 3 == 0:
        coloured_eggs_count -= (loaves_count - 2)
    coloured_eggs_count += 3
    budget -= one_loaf_price
print(f"You made {loaves_count} loaves of Easter bread! "
      f"Now you have {coloured_eggs_count} eggs and {budget:.2f}BGN left.")
