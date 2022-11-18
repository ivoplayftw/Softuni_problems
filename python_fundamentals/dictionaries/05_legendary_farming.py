key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
item_found = False

while True:
    if item_found:
        break
    gather = input().lower().split()

    gather_item = [ele for ele in gather if ele.isalpha()]
    gather_num = [int(ele) for ele in gather if ele.isdigit()]

    for item in range(len(gather_item)):
        if gather_item[item] in key_materials.keys():
            key_materials[gather_item[item]] += gather_num[item]
            if gather_item[item] == 'fragments' and key_materials[gather_item[item]] >= 250:
                print("Valanyr obtained!")
                key_materials[gather_item[item]] -= 250
                item_found = True
                break
            if gather_item[item] == 'motes' and key_materials[gather_item[item]] >= 250:
                print("Dragonwrath obtained!")
                key_materials[gather_item[item]] -= 250
                item_found = True
                break
            if gather_item[item] == 'shards' and key_materials[gather_item[item]] >= 250:
                print("Shadowmourne obtained!")
                key_materials[gather_item[item]] -= 250
                item_found = True
                break
        else:
            junk[gather_item[item]] = gather_num[item]

for key, value in key_materials.items():
    print(f"{key}: {value}")
for key, value in junk.items():
    print(f"{key}: {value}")