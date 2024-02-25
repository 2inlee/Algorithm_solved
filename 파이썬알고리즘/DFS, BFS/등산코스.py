def DFS(x, y):
  global cnt
  
  if x == n-1 and y == n-1:
    cnt += 1
    return
  
  else:
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:
        DFS(nx, ny)

if __name__ == "__main__":
  n = int(input())
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]
  cnt = 0
  arr = []
  
  for i in range(n):
    arr.append(list(map(int,input().split())))
  
  DFS(0, 0)
  print(cnt)
