def translate(txt, char, replacement):
    return txt.replace(char, replacement)


def includes(txt, substring):
    if substring in txt:
        return True
    return False


def start(txt, substring):
    if txt.startswith(substring):
        return True
    return False


def lowercase(txt):
    return txt.lower()


def find_index(txt, char):
    lst = [char for char in txt]
    lst.reverse()
    index = lst.index(char)
    return len(lst) - index - 1


def remove(txt, index, count):
    return txt[: index:] + txt[count + index::]


text = input()

while True:
    command = input().split()
    if command[0] == 'End':
        break
    elif command[0] == 'Translate':
        text = translate(text, command[1], command[2])
        print(text)
    elif command[0] == 'Includes':
        print(includes(text, command[1]))
    elif command[0] == 'Start':
        print(start(text, command[1]))
    elif command[0] == 'Lowercase':
        text = lowercase(text)
        print(text)
    elif command[0] == 'FindIndex':
        print(find_index(text, command[1]))
    elif command[0] == 'Remove':
        text = remove(text, int(command[1]), int(command[2]))
        print(text)
