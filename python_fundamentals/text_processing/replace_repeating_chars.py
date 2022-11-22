text = input()
sorted_text = ''
last_char = ''
for char in text:
    if char != last_char:
        last_char = char
        sorted_text += char
print(sorted_text)