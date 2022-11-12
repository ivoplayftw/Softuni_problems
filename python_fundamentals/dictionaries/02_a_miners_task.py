resources = {}
counter = 0
last_resource = ''
while True:
    command = input()
    if command == "stop":
        break

    counter += 1

    if counter % 2 != 0:
        if command in resources.keys():
            last_resource = command
            continue
        resources[command] = 0

    elif counter % 2 == 0:
        for keys in resources.keys():
            if resources[keys] == 0:
                resources[keys] = int(command)
        if last_resource in resources.keys():
            resources[last_resource] += int(command)

for key, value in resources.items():
    print(f"{key} -> {value}")
