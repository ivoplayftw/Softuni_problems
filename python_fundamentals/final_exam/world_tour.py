def add_stop(index, stop, text):
    splitted = [char for char in text]
    splitted.insert(index, stop)
    return ''.join(splitted)


def remove_stop(start, end, text):
    splitted = [char for char in text]
    del splitted[start:end +1]
    return ''.join(splitted)


def switch(old_str, new_str, text):
    new_text = text.replace(old_str, new_str)
    return new_text


text = input()
while True:
    command = input().split(':')

    if command[0] == "Travel":
        break
    elif command[0] == "Add Stop":
        index = int(command[1])
        stop = command[2]
        if 0 <= index < len(text):
            text = add_stop(index, stop, text)
        print(text)

    elif command[0] == "Remove Stop":
        first_ind = int(command[1])
        second_ind = int(command[2])
        if 0 <= second_ind < len(text) and 0 <= first_ind < len(text):
            text = remove_stop(first_ind, second_ind, text)
        print(text)

    elif command[0] == "Switch":
        old = command[1]
        new = command[2]
        if old in text:
            text = switch(old, new, text)
        print(text)

print(f"Ready for world tour! Planned stops: {text}")