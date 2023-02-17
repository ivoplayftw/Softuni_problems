def even_odd(*args):
    listed = [arg for arg in args]

    if listed[-1] == 'even':
        del listed[-1]
        even = [even for even in listed if int(even) % 2 == 0]
        return even
    if listed[-1] == 'odd':
        del listed[-1]
        odd = [odd for odd in listed if int(odd) % 2 != 0]
        return odd

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
