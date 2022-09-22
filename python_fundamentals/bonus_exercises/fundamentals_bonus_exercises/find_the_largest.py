number = int(input())


def print_max_num(num):
    hashed = []
    for i in range(0, 10):
        hashed.append(0)
    if num < 0:
        n = num * -1
    else:
        n = num
    ans = 0
    while n != 0:
        hashed[int(n % 10)] = hashed[int(n % 10)] + 1
        n = n // 10
    if num > 0:
        for i in range(9, -1, -1):
            for _ in range(0, hashed[i]):
                ans = ans * 10 + i
    else:
        if hashed[0] > 0:
            for i in range(1, 10):
                if hashed[i] > 0:
                    ans = i
                    hashed[i] = hashed[i] - 1
                    break
        for i in range(0, 10):
            for _ in range(0, hashed[i]):
                ans = ans * 10 + i
        ans = ans * -1
    return ans


print(print_max_num(number))
