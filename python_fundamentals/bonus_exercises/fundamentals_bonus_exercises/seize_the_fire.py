fire_str_cell = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells_lst = []
cells_puted_out = []

for ele in fire_str_cell:  # appending all elements as lists in list.
    cells_lst.append([ele])
# Going through all the lists in the initial list splitting into "Strenght" and "Value".
for cell in range(0, len(cells_lst)):
    strenght = cells_lst[cell][0].split(' = ')[0]
    # Inting the value to subtract it from the water and calculate the effort.
    value = int(cells_lst[cell][0].split(' = ')[1])

    if strenght == "High" and 81 <= value <= 125 \
            or strenght == "Medium" and 51 <= value <= 80 \
            or strenght == "Low" and 1 <= value <= 50:  # Checking if the cells are valid.
        if water < value:  # Checking if I have enough water.
            continue  # if I don't have enough water continue to next cell to check if I can put it out.
        water -= value
        effort += value * 0.25
        cells_puted_out.append(value)  # adding cell values to different list to print out in the end.
        total_fire += value
    else:
        continue  # if cell is invalid continue to next cell.

print("Cells:")
for j in range(len(cells_puted_out)):
    print(f" - {cells_puted_out[j]}")  # printing out all the saved cells.
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
