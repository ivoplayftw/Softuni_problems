command = input()
coffee_count = 0
while command != "END":
    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":
        if command.islower():
            coffee_count += 1
        else:
            coffee_count += 2
    command = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
