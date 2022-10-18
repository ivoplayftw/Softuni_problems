words_list = input().split()
new_lst = [word for word in words_list if len(word) % 2 == 0]
print("\n".join(new_lst))
