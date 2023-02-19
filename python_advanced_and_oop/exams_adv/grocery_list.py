def shop_from_grocery_list(budget, grocery_list, *products_and_prices):
    products_purchased = []

    for tup in products_and_prices:
        product, price = tup

        if product in products_purchased:
            continue

        if product in grocery_list and product not in products_purchased:
            if budget >= price:
                budget -= price
                products_purchased.append(product)
            else:
                grocery_list = [ele for ele in grocery_list if ele not in products_purchased]
                return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

    grocery_list = [ele for ele in grocery_list if ele not in products_purchased]
    if len(grocery_list) == 0:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))

print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
