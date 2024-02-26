from collections import deque

if __name__ == "__main__":
  n = int(input())
  a = [list(map(int, input().split())) for _ in range(n)]
  dq = deque()
  # 상하좌우
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]
  cnt = 0
  for i in range(n):
    for j in range(n):
      if a[i][j] == 1:
        dq.append((i, j))
        a[i][j] = 0  # 현재 위치를 방문했다고 표시
        while dq:
          x, y = dq.popleft()
          for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and a[nx][ny] == 1:
              dq.append((nx, ny))
              a[nx][ny] = 0  # 새 위치를 방문했다고 표시
        cnt += 1
  print(cnt)
