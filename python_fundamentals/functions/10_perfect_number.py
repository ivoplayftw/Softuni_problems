def perfect_check(number):
    checked_divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            checked_divisors.append(i)
    summed = sum(checked_divisors)
    if summed // 2 == number:
        return True
    return False


num = int(input())

if perfect_check(num):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
