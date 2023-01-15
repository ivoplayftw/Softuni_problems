my_stack = []
num = int(input())
counter = 0
for i in range(num):
    queries = input()
    counter += 1
    if len(queries) > 1:
        splitted = queries.split()
        splitted = [int(ele) for ele in splitted]
        my_stack.append(splitted[1])
    if len(my_stack) > 0:
        if queries == '2':
            my_stack.pop()
        elif queries == '3':
            print(max(my_stack))
        elif queries == '4':
            print(min(my_stack))

my_stack.reverse()
print(*my_stack, sep=', ')
