resources = {}
counter = 0
while True:
    command = input()
    if command == "stop":
        break
    counter += 1
    if counter % 2 != 0:
        resources[command] = 0
    elif counter % 2 == 0:
        for keys in resources.keys():
            if resources[keys] == 0:
                resources[keys] = command

    last_command = command
for key, value in resources.items():
    print(f"{key} -> {value}")
