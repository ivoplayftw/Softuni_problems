def chars_between(char_1, char_2):
    chars = []
    for i in range(ord(char_1) + 1, ord(char_2)):
        chars.append(chr(i))
    return chars


character_1 = input()
character_2 = input()
print(*chars_between(character_1, character_2))
