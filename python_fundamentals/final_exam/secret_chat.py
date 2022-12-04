def insert_space(message, index):
    msg_as_lst = [char for char in message]
    msg_as_lst.insert(int(index), ' ')
    return ''.join(msg_as_lst)


def reverse(message, substring):
    new_msg = message.replace(substring, '', 1) + substring[::-1]
    return new_msg


def change_all(message, substring, replacement):
    new_msg = message.replace(substring, replacement)
    return new_msg


secret = input()
while True:
    command = input().split(":|:")
    if command[0] == 'Reveal':
        print(f"You have a new text message: {secret}")
        break
    elif command[0] == 'InsertSpace':
        secret = insert_space(secret, command[1])
        print(secret)
    elif command[0] == 'Reverse':
        if command[1] in secret:
            secret = reverse(secret, command[1])
            print(secret)
        else:
            print('error')
    elif command[0] == 'ChangeAll':
        secret = change_all(secret, command[1], command[2])
        print(secret)
