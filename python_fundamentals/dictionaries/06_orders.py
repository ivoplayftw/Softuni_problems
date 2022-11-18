command = input()
products_and_price = {}
products_quantity = {}
products_full_price = {}
quantity = []
while command != 'buy':
    splitted = command.split()
    if splitted[0] in products_and_price and splitted[0] in products_quantity:
        products_and_price[splitted[0]] = float(splitted[1])
        products_quantity[splitted[0]] += int(splitted[2])
        products_full_price[splitted[0]] = products_quantity[splitted[0]] * float(splitted[1])
    else:
        products_and_price[splitted[0]] = float(splitted[1])
        products_quantity[splitted[0]] = int(splitted[2])
        products_full_price[splitted[0]] = int(splitted[2]) * float(splitted[1])

    command = input()

for key, value in products_full_price.items():
    print(f"{key} -> {value:.2f}")
