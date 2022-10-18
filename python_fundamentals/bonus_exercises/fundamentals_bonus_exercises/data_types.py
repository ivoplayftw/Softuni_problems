def data_type(first, second):
    if first == "real":
        return f"{float(second )* 1.5:.2f}"
    elif first == "int":
        return f"{int(second) * 2}"
    elif first == "string":
        return f"${second}$"


type_of_data = input()
text_or_num = input()
print(data_type(type_of_data, text_or_num))
