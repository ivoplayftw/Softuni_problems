text = input()
new_text = ''
strength = 0
for i in range(len(text)):
    if strength > 0 and text[i] != '>':
        strength -= 1
    elif text[i] == '>':
        new_text += text[i]
        strength += int(text[i + 1])
    else:
        new_text += text[i]
print(new_text)