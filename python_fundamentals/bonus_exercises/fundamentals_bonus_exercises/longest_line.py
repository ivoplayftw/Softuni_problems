def longest_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4):
    squared_1 = (x_1 ** 2) + (y_1 ** 2)
    squared_2 = (x_2 ** 2) + (y_2 ** 2)
    squared_3 = (x_3 ** 2) + (y_3 ** 2)
    squared_4 = (x_4 ** 2) + (y_4 ** 2)

    line_1 = squared_1 + squared_2
    line_2 = squared_3 + squared_4

    if line_1 < line_2:
        if squared_3 <= squared_4:
            return f"({int(x_3 // 1)}, {int(y_3 // 1)})({int(x_4 // 1)}, {int(y_4 // 1)})"
        else:
            return f"({int(x_4 // 1)}, {int(y_4 // 1)})({int(x_3 // 1)}, {int(y_3 // 1)})"
    else:
        if squared_1 <= squared_2:
            return f"({int(x_1//1)}, {int(y_1)})({int(x_2//1)}, {int(y_2//1)})"
        else:
            return f"({int(x_2 // 1)}, {int(y_2 // 1)})({int(x_1 // 1)}, {int(y_1)})"


first_x = float(input())
first_y = float(input())
second_x = float(input())
second_y = float(input())
third_x = float(input())
third_y = float(input())
fourth_x = float(input())
fourth_y = float(input())

print(longest_line(first_x, first_y, second_x, second_y, third_x, third_y, fourth_x, fourth_y))