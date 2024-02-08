n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0

# 상하좌우에 0을 추가하기 위해 n+2 x n+2 크기의 2차원 리스트를 생성하고 0으로 초기화
expanded = [[0 for _ in range(n+2)] for _ in range(n+2)]

# 원래의 2차원 리스트를 새로운 리스트의 중앙에 복사
for i in range(n):
    for j in range(n):
        expanded[i+1][j+1] = a[i][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if expanded[i][j] > expanded[i-1][j] and expanded[i][j] > expanded[i][j-1] and expanded[i][j] > expanded[i+1][j] and expanded[i][j] > expanded[i][j+1]:
          res += 1
# 결과 출력
print(res)