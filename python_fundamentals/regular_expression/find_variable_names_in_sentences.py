import re
sentence = input()
expression = r"\b_([a-zA-Z0-9]+)\b"
find = re.findall(expression, sentence)
print(",".join(find))