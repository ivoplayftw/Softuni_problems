import re
text = input()
regex = r"\=([A-Z][A-Za-z]{2,})\=|\/([A-Z][A-Za-z]{2,})\/"
search = ["".join(ele) for ele in re.findall(regex, text)]
total_points = 0
for destination in search:
    total_points += len(destination)

print(f"Destinations: {', '.join(search)}")
print(f"Travel Points: {total_points}")
