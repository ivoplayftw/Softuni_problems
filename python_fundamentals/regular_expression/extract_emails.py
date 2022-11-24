import re

text = input()
expression = r'\s(([a-z0-9]+[a-z0-9\.\-\_]*)@[a-z\-]+(\.[a-z]+)+)\b'
mails = re.findall(expression, text)
for email in mails:
    print(email[0])

