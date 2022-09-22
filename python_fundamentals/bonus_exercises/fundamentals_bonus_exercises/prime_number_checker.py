num = int(input())
is_prime = False

for i in range(2, int(num / 2) + 1):
    if num % i == 0:
        print(is_prime)
        break
else:
    is_prime = True
    print(is_prime)
