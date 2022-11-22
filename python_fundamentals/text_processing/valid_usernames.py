def length_check(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def char_check(name):
    for char in name:
        if not (char.isalnum() or char == "-" or char == '_'):
            return False
    return True


def redundant_check(name):
    if ' ' in name:
        return False
    return True


usernames = input().split(', ')

for user in usernames:
    if length_check(user) and char_check(user) and redundant_check(user):
        print(user)
