num_of_names = int(input())
set_of_names = set()
for n in range(num_of_names):
    name = input()
    set_of_names.add(name)
print(*set_of_names, sep='\n')
