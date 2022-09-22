num_of_char = int(input())
for i in range(num_of_char):
    char_i = chr(97 + i)
    for j in range(num_of_char):
        char_j = chr(97 + j)
        for k in range(num_of_char):
            char_k = chr(97 + k)
            print(char_i + char_j + char_k)
            