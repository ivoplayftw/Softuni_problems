import re
text = input()
pattern = r"@([a-zA-Z]{3,})@@([a-zA-Z]{3,})@|#([a-zA-Z]{3,})##([a-zA-Z]{3,})#"
mirror_words = []
pairs = []
search = re.findall(pattern, text)
words = [tuple(comp for comp in a if comp) for a in search]
print(words)
