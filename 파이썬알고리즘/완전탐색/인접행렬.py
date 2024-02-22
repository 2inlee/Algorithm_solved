n, m = map(int, input().split())
g=[[0]*(n+1) for i in range(n+1)] # 2차 행렬 그래프 (n*1)x(n*1) 배열 선언
for i in range(m):
  a, b, c = map(int, input().split())
  g[a][b]=c
  
for i in range(1, n+1):
  for j in range(1, n+1):
    print(g[i][j], end =' ')
  print()
  