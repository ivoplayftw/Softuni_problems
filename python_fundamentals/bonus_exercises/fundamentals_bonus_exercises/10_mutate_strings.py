
first_string = input()
second_string = input()
last_string = first_string
for index in range(len(first_string)):
    left_part = second_string[:index + 1]
    right_part = first_string[index + 1:]
    mutated_string = left_part + right_part
    if mutated_string == last_string:
        continue
    print(mutated_string)
    last_string = mutated_string
