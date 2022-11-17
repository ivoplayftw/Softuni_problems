countries = input().split(", ")
capitals = input().split(", ")
my_dict = zip(countries, capitals)
for keys, value in my_dict:
    print(f"{keys} -> {value}")


