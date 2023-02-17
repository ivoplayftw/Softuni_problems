lines = int(input())
matrix = [[int(ele) for ele in input().split(',')] for _ in range(lines)]
primary = [matrix[r][r] for r in range(lines)]
secondary = [matrix[r][lines - r - 1] for r in range(lines - 1, -1, -1)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary][::-1])}. Sum: {sum(secondary)}")
