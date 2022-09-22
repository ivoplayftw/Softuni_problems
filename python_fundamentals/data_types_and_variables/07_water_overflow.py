lines = int(input())
capacity_of_tank = 255
liters_in = 0

for i in range(lines):
    liters_to_pour = int(input())
    if liters_in >= capacity_of_tank \
            or liters_in + liters_to_pour > capacity_of_tank:
        print("Insufficient capacity!")
        continue
    liters_in += liters_to_pour
print(liters_in)
