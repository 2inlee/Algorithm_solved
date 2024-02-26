from collections import deque

m, n = map(int, input().split())
a = [list(map(int, input().split())) for i in range(m)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

dq = deque()
dis = [[0] * n for _ in range(m)]
cnt = 0

for i in range(m):
  for j in range(n):
    if a[i][j] == 1:
      dq.append((i, j))
while dq:
  x,y = dq.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < m and 0 <= ny < n and a[nx][ny] == 0:
      a[nx][ny] = 1
      dis[nx][ny] = dis[x][y] + 1
      dq.append((nx, ny))

flag = 1

for i in range(m):
  for j in range(n):
    if a[i][j] == 0:
      flag = 0

res = 0
if flag == 1:
  for i in range(m):
    for j in range(n):
      if dis[i][j] > res:
        res = dis[i][j]
  print(res)
else:
  print(-1)