text = input()
encrypted = []
for char in text:
    ascii_num = ord(char)
    new_char = chr(int(ascii_num) + 3)
    encrypted.append(new_char)

print(''.join(encrypted))
