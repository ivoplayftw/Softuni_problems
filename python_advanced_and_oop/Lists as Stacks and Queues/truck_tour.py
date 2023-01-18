from collections import deque

petrol_pumps = int(input())
fuels = deque()
kilometers = deque()
printing = False

for _ in range(petrol_pumps):
    command = input().split()
    fuels.append(int(command[0]))
    kilometers.append(int(command[1]))

for idx in range(petrol_pumps):
    if printing:
        break
    fuel_in_tank = 0
    starting_idx = True
    current_fuels = deque()
    current_kilometers = deque()

    for _ in range(petrol_pumps):
        current_fuel = fuels.popleft()
        current_fuels.append(current_fuel)
        current_kilometer = kilometers.popleft()
        current_kilometers.append(current_kilometer)
        fuel_in_tank += current_fuel
        fuel_in_tank -= current_kilometer

        if fuel_in_tank < 0:
            starting_idx = False

    if starting_idx:
        printing = True
        print(idx)

    current_fuel = current_fuels.popleft()
    current_fuels.append(current_fuel)
    current_kilometer = current_kilometers.popleft()
    current_kilometers.append(current_kilometer)
    fuels = current_fuels
    kilometers = current_kilometers
