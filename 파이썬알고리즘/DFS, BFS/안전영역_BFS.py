def DFS(x,y,h):
  ch[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny <= n and ch[nx][ny] == 0 and a[nx][ny] > h:
      DFS(nx, ny, h)


if __name__ == "__main__":
  n = int(input())
  a = [list(map(int, input().split())) for _ in range(n)]
  # 상하좌우
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]
  cnt = 0

  for h in range(max(a)):
    ch = [[0] * n for _ in range(n)]
    for i in range(n):
      for j in range(n):
        if ch[i][j] == 0 and a[i][j] > h:
          cnt += 1
          DFS(i, j, h)

    res = max(res, cnt)
    if cnt == 0:
      break
