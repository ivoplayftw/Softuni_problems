number_of_strings = int(input())
for string in range(number_of_strings):
    inputed_string = input()
    if "," in inputed_string or "." in inputed_string or "_" in inputed_string:
        print(f"{inputed_string} is not pure!")
    else:
        print(f"{inputed_string} is pure.")