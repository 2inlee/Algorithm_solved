from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, 1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ch = [[0] * n for _ in range(n)]
sum = 0
q = deque()

ch[n//2][n//2] = 1
sum += ch[n//2][n//2]
q.append(([n//2][n//2]))
L = 0 
while True:
  if L == n // 2:
    break
  size = len(q)
  for i in range(size):
    tmp = q.popleft()
    for j in range(4):
      x = tmp[0] + dx[j]
      y = tmp[1] + dy[j]
      if ch[x][y] == 0:
        sum += a[x][y]
        ch[x][y] = 1
        q.append((x,y))
  L += 1
  
print(sum)