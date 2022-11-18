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

    for item in range(len(type_of_resource)):
        if type_of_resource[item] in key_materials.keys():
            key_materials[type_of_resource[item]] += quantity[item]
            if type_of_resource[item] == 'fragments' and key_materials[type_of_resource[item]] >= 250:
                print("Valanyr obtained!")
                key_materials[type_of_resource[item]] -= 250
                item_found = True
                break
            if type_of_resource[item] == 'motes' and key_materials[type_of_resource[item]] >= 250:
                print("Dragonwrath obtained!")
                key_materials[type_of_resource[item]] -= 250
                item_found = True
                break
            if type_of_resource[item] == 'shards' and key_materials[type_of_resource[item]] >= 250:
                print("Shadowmourne obtained!")
                key_materials[type_of_resource[item]] -= 250
                item_found = True
                break
        else:
            if type_of_resource[item] in junk:
                junk[type_of_resource[item]] += quantity[item]
            else:
                junk[type_of_resource[item]] = quantity[item]

for key, value in key_materials.items():
    print(f"{key}: {value}")
for key, value in junk.items():
    print(f"{key}: {value}")
