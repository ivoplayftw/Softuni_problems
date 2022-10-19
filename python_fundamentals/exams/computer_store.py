command = input()
price_no_tax = 0

while True:
    if command == "special" or command == "regular":
        break
    if float(command) < 0:
        print("Invalid price!")
        command = input()
        continue
    price_no_tax += float(command)
    command = input()

taxes = price_no_tax * 0.20
total_price = price_no_tax + taxes
if total_price == 0:
    print("Invalid order!")
else:
    if command == "special":
        total_price *= 0.9
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_no_tax:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
    else:
        print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {price_no_tax:.2f}$\nTaxes: {taxes:.2f}$\n-----------\nTotal price: {total_price:.2f}$")
