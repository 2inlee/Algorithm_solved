def DFS(x, y):
  global cnt
  cnt += 1
  a[x][y] = 0
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]

    if 0<=nx<n and 0<=ny<n and a[nx][ny] == 1:
      DFS(nx, ny)
  if x == n-1 and y == n-1:
    return cnt

if __name__ == "__main__":
  n = int(input())
  a = [list(map(int, input())) for _ in range(n)]
  res = []
  
# 상하좌우
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]

  for i in range(n):
    for j in range(n):
      if a[i][j] == 1:
        cnt = 0
        DFS(i, j)
        res.append(cnt)


  res.sort()
  for x in res:
    print(x)
