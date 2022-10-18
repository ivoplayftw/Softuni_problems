def closest_to_center(x_1, y_1, x_2, y_2):
    squared_1 = (x_1 ** 2) + (y_1 ** 2)
    squared_2 = (x_2 ** 2) + (y_2 ** 2)

    if squared_1 <= squared_2:
        return f"({int(x_1//1)}, {int(y_1//1)})"
    return f"({int(x_2//1)}, {int(y_2//1)})"


first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())

print(closest_to_center(first_x, first_y, second_x, second_y))
