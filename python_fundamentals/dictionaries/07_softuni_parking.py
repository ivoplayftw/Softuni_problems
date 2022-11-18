num = int(input())
registered = {}
for _ in range(num):
    command = input().split()
    if command[0] == "register":
        if command[1] in registered.keys():
            print(f"ERROR: already registered with plate number {registered[command[1]]}")
        else:
            registered[command[1]] = command[2]
            print(f"{command[1]} registered {command[2]} successfully")
    else:
        if command[1] in registered.keys():
            print(f"{command[1]} unregistered successfully")
            del registered[command[1]]

        else:
            print(f"ERROR: user {command[1]} not found")

for key, value in registered.items():
    print(f"{key} => {value}")
