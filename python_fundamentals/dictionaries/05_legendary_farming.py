key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_found = False

while True:
    if item_found:
        break
    resources = input().lower().split()
    quantity = []
    type_of_resource = []
    for ele in resources:
        if ele.isdigit():
            quantity.append(int(ele))
        else:
            type_of_resource.append(ele)
    for item, num in resources, quantity:
        if item in key_materials.keys():
            key_materials[item] += quantity[num]
            if item == 'fragments' and key_materials[item] >= 250:
                print("Valanyr obtained!")
                key_materials[item] -= 250
                item_found = True
                break
            if item == 'motes' and key_materials[item] >= 250:
                print("Dragonwrath obtained!")
                key_materials[item] -= 250
                item_found = True
                break
            if item == 'shards' and key_materials[item] >= 250:
                print("Shadowmourne obtained!")
                key_materials[item] -= 250
                item_found = True
                break
        else:
            if item in junk:
                junk[item] += num
            else:
                junk[item] = num

for key, value in key_materials.items():
    print(f"{key}: {value}")
for key, value in junk.items():
    print(f"{key}: {value}")
