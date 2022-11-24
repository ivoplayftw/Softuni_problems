import re

furniture_bought = []
money = 0
pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
command = input()
while command != "Purchase":
    match = re.search(pattern, command)
    if match:
        furniture, price, quantity = match.groups()
        furniture_bought.append(furniture)
        money += float(price) * int(quantity)
    command = input()

print("Bought furniture:")
for furniture in furniture_bought:
    print('\n'.join(furniture))
print(f"Total money spend: {money:.2f}")
