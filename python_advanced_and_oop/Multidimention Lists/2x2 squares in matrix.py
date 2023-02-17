rows, columns = list(map(int, input().split()))

matrix = [input().split() for _ in range(rows)]

squares = 0

for row in range(rows):

    for col in range(columns):
        if row+1 < rows and col+1 < columns:
            symbol = matrix[row][col]
            if matrix[row][col+1] == symbol and matrix[row+1][col] == symbol and matrix[row+1][col+1] == symbol:
                squares += 1

print(squares)
