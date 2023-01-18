parentheses = input()
stack = []
y_n = True
for p in parentheses:
    if p in ["{", "[", "("]:
        stack.append(p)
    elif p == '}':
        if stack and stack[-1] == "{":
            stack.pop()
        else:
            y_n = False
            break
    elif p == ']':
        if stack and stack[-1] == "[":
            stack.pop()
        else:
            y_n = False
            break
    elif p == ')':
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            y_n = False
            break
if y_n:
    print("YES")
else:
    print("NO")