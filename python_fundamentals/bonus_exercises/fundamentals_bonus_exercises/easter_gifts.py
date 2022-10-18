presents = input().split()
command = input().split()

while command[0] != "No" and command[1] != "Money":

    if command[0] == "OutOfStock":
        for i in range(len(presents)):
            if presents[i] == command[1]:
                presents[i] = "None"

    elif command[0] == "Required":
        for i in range(0, len(presents)):
            if i == int(command[-1]):
                presents[i] = command[1]

    elif command[0] == "JustInCase":
        presents[-1] = command[1]
    command = input().split()
while "None" in presents:
    presents.remove("None")
print(*presents, sep=' ')
