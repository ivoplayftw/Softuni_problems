storage = input().split(", ")
phone = 0

while True:
    command = input().split()
    if command[0] == "End":
        break
    elif command[0] == "Add" and command[2] not in storage:
        storage.append(command[2])
    elif command[0] == "Remove" and command[2] in storage:
        storage.remove(command[2])
    elif command[0] == f"Bonus":
        phone_old_new = command[3].split(":")
        if phone_old_new[0] in storage:
            new_phone = phone_old_new[1]
            index_of_old = storage.index(phone_old_new[0])
            storage.insert(index_of_old + 1, new_phone)
    elif command[0] == f"Last" and command[2] in storage:
        storage.remove(command[2])
        storage.append(command[2])

print(", ".join(storage))
