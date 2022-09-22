command = input()
while command != "End":
    printed_string = ''
    if command == "SoftUni":
        command = input()
        continue
    for letter in command:
        printed_string += letter*2
    print(f"{printed_string}")
    command = input()
