records = {}

while True:
    command = input().split(": ")
    if command[0] == "Log out":
        break
    elif command[0] == "New follower":
        if command[1] in records.keys():
            continue
        else:
            records[command[1]] = [0, 0]
    elif command[0] == "Like":
        if command[1] in records.keys():
            records[command[1]][0] += int(command[2])
        else:
            records[command[1]] = [int(command[2]), 0]
    elif command[0] == "Comment":
        if command[1] in records.keys():
            records[command[1]][1] += 1
        else:
            records[command[1]] = [0, 1]
    elif command[0] == "Blocked":
        if command[1] in records.keys():
            del records[command[1]]
        else:
            print(f"{command[1]} doesn't exist.")

print(f"{len(records.keys())} followers")
for key, value in records.items():
    print(f"{key}: {sum(value)}")
