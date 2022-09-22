number_of_orders = int(input())
total = 0
for order in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    capsule_needed_per_day = int(input())
    if 0.01 > capsule_price or capsule_price > 100.00:
        continue
    if 1 > days or days > 31:
        continue
    if 1 > capsule_needed_per_day or capsule_needed_per_day > 2000:
        continue
    coffee_price = days * capsule_needed_per_day * capsule_price
    print(f"The price for the coffee is: ${coffee_price:.2f}")
    total += coffee_price
print(f"Total: ${total:.2f}")