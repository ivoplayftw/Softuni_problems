import re

lines = int(input())

for _ in range(lines):
    boss_name_and_title = input()
    expression = r"\|([A-Z]{4,})\|:#([a-zA-Z]+ [a-zA-Z]+)#"
    name_and_title = re.findall(expression, boss_name_and_title)
    if len(name_and_title) < 1:
        print("Access denied!")
    else:
        name, title = name_and_title[0]
        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")
