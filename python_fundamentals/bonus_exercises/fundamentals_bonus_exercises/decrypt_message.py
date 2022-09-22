key = int(input())
lines = int(input())
message = ''
for i in range(lines):
    chars = ord(input())
    number_char = key + chars
    message += chr(number_char)
print(message)
