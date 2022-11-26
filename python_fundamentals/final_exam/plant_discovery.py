import re

n = int(input())
plants_list = {}
for i in range(n):
    plant, rarity = input().split("<->")
    rarity = int(rarity)
    if plant in plants_list:
        plants_list[plant]['RARITY'] += rarity
        plants_list[plant]['RATING'] = []
    else:
        plants_list[plant] = {'RARITY': rarity, 'RATING': []}

data = input()

while data != "Exhibition":
    matches = re.split(r": | - ", data)
    if matches[0] == "Rate":
        plant, rating = matches[1:]
        rating = int(rating)
        if plant in plants_list:
            plants_list[plant]['RATING'].append(rating)
        else:
            print("error")
    elif matches[0] == "Update":
        plant, new_rarity = matches[1:]
        new_rarity = int(new_rarity)
        if plant in plants_list:
            plants_list[plant]['RARITY'] = new_rarity
        else:
            print("error")

    elif matches[0] == "Reset":
        plant = matches[1]
        if plant in plants_list:
            plants_list[plant]['RATING'] = []
        else:
            print("error")
    data = input()

for k, v in plants_list.items():
    if not plants_list[k]['RATING']:
        plants_list[k]['RATING'] = 0
    else:
        plants_list[k]['RATING'] = sum(plants_list[k]['RATING']) / len(plants_list[k]['RATING'])

sorted_plants = sorted(plants_list.items(), key=lambda kvpt: (kvpt[1]["RARITY"], kvpt[1]["RATING"]), reverse=True)
print("Plants for the exhibition:")
for name, value in sorted_plants:
    print(f"- {name}; Rarity: {value['RARITY']}; Rating: {value['RATING']:.2f}")