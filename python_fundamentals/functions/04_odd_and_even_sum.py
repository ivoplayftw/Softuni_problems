def odd_and_even(number):
    digits_list = []
    for x in str(number):
        digits_list.append(int(x))
    odds = []
    evens = []

    for element in digits_list:
        if element % 2 == 0:
            evens.append(int(element))
        else:
            odds.append(int(element))

    sum_of_even_digits = sum(evens)
    sum_of_odd_digits = sum(odds)
    result = f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
    return result


numb = int(input())
print(odd_and_even(numb))
