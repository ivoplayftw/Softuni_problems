import re

pattern = '\d+'
line = input()
while line:
    matches = re.findall(pattern, line)
    if matches:
        print(*matches, end=' ')

    line = input()
