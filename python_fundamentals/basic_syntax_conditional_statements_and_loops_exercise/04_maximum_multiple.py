divisor = int(input())
boundary = int(input())
for number in range(boundary, divisor, - 1):
    if number % divisor == 0 and number <= boundary:
        print(number)
        break
