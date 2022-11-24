import re
sentence = input().lower()
word = input().lower()
expression = fr'\b{word}\b'
find = re.findall(expression, sentence)
print(len(find))
