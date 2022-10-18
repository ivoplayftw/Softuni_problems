def loading_bar(num):
    if num != 100:
        percents = '%' * (num // 10)
        dots = "." * (10 - num // 10)
        return f"{num}% [{percents}{dots}]\nStill loading..."
    else:
        return "100% Complete!\n[%%%%%%%%%%]"


number = int(input())
print(loading_bar(number))
