n = int(input())
dp_arr = [[0 for _ in range(n)] for _ in range(n)]
matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

dp_arr[0][0] = matrix[0][0]

for i in range(1, n):
    dp_arr[0][i] = dp_arr[0][i-1] + matrix[0][i]
    dp_arr[i][0] = dp_arr[i-1][0] + matrix[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp_arr[i][j] = min(dp_arr[i-1][j], dp_arr[i][j-1]) + matrix[i][j]
    
print(dp_arr[n-1][n-1])
