num_of_chars = int(input())
total = 0
for i in range(num_of_chars):
    char = ord(input())
    total += char
print(f"The sum equals: {total}")
