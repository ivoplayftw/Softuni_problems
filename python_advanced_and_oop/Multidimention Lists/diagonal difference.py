lines = int(input())

matrix = [[int(ele) for ele in input().split()] for _ in range(lines)]
primary = [matrix[r][r] for r in range(lines)]
secondary = [matrix[r][lines - r - 1] for r in range(lines - 1, -1, -1)]
difference = sum(primary) - sum(secondary)
print(f"{abs(difference)}")
