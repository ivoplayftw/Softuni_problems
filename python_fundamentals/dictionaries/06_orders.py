command = input()
products_and_price = {}
quantity = []
while command != 'buy':
    splitted = command.split()
    for i in range(0, len(splitted), 2):
        quantity.append[splitted[i]]
    if splitted[0] in products_and_price:
        products_and_price[splitted[0]] = float(splitted[1])
    else:
        products_and_price[splitted[0]] = float(splitted[1])

    command = input()

for product, price in products_and_price.items():
