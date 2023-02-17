def pos_vs_neg(*args):

    pos = sum([positive for positive in args if positive > 0])
    neg = sum([negative for negative in args if negative < 0])

    if abs(neg) > abs(pos):
        bigger = "The negatives are stronger than the positives"
    else:
        bigger = "The positives are stronger than the negatives"

    return print(neg), print(pos), print(bigger)


nums = [int(num) for num in input().split()]
pos_vs_neg(*nums)
