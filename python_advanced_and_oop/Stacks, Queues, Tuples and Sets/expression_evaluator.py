from functools import reduce
expression = input().split()
stack = []
for ele in range(len(expression)):

    if expression[ele].lstrip('-').isnumeric():
        stack.append(int(expression[ele]))
    elif expression[ele] == '/':
        stack = [reduce(lambda x, y: x // y, stack)]
    elif expression[ele] == '-':
        stack = [reduce(lambda x, y: x - y, stack)]
    elif expression[ele] == '+':
        stack = [reduce(lambda x, y: x + y, stack)]
    elif expression[ele] == '*':
        stack = [reduce(lambda x, y: x * y, stack)]
print(stack[0])
