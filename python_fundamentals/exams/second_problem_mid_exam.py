travel_route = input()
starting_fuel = int(input())
ammo = int(input())
travel_route_lst = travel_route.split("||")

for ele in travel_route_lst:
    command_and_num = ele.split()

    if command_and_num[0] == "Travel":
        if starting_fuel - int(command_and_num[1]) >= 0:
            starting_fuel -= int(command_and_num[1])
            print(f"The spaceship travelled {command_and_num[1]} light-years.")
        elif starting_fuel - int(command_and_num[1]) < 0:
            print("Mission failed.")
            break

    if command_and_num[0] == "Enemy":
        if ammo >= int(command_and_num[1]):
            ammo -= int(command_and_num[1])
            print(f"An enemy with {command_and_num[1]} armour is defeated.")
        elif ammo <= int(command_and_num[1]) and starting_fuel >= int(command_and_num[1]) * 2:
            print(f"An enemy with {command_and_num[1]} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break

    if command_and_num[0] == "Repair":
        fuel_add = int(command_and_num[1])
        ammo_to_add = int(command_and_num[1]) * 2
        starting_fuel += fuel_add
        ammo += ammo_to_add
        print(f"Ammunitions added: {ammo_to_add}.")
        print(f"Fuel added: {fuel_add}.")

    if command_and_num[0] == "Titan":
        print("You have reached Titan, all passengers are safe.")
        break
