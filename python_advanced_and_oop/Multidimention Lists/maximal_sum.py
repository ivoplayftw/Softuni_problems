import sys

rows, columns = list(map(int, input().split()))

matrix = [
    [int(num) for num in input().split()]
    for row in range(rows)
]

maximal_sum_matrix = []
maximal_sum = -sys.maxsize

end_of_matrix = False

for row in range(rows):

    for col in range(columns):
        if row+2 < rows and col+2 < columns:
            check_matrix = [
                [
                    matrix[row][col], matrix[row][col+1], matrix[row][col+2]
                ],
                [
                    matrix[row+1][col], matrix[row+1][col+1], matrix[row+1][col+2]
                ],
                [
                    matrix[row+2][col], matrix[row+2][col+1], matrix[row+2][col+2]
                ]
            ]
            sum_check_matrix = sum(check_matrix[0]) + sum(check_matrix[1]) + sum(check_matrix[2])
            if sum_check_matrix > maximal_sum:
                maximal_sum_matrix = check_matrix
                maximal_sum = sum_check_matrix

print(f"Sum = {maximal_sum}")
[print(' '.join([str(num) for num in row])) for row in maximal_sum_matrix]