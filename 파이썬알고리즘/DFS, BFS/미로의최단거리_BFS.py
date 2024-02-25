from collections import deque

# 7*7 배열이 들어오지만, 인덱스가 0부터 시작하니까 좌표를 맞춰주기 위해 8*8 배열을 미리 선언
arr = [[0]*8 for _ in range(8)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(1, 8):
  arr[i][1:8] = list(map(int, input().split()))

arr[1][1] = 1

q = deque()
q.append(((1,1)))
flag = 0

while flag == 0 and q:
  x, y = q.popleft()

  if x == 7 and y == 7:
    print(arr[x][y] - 1) # 출발점을 1로 설정했으므로, 실제 이동 횟수를 출력하기 위해 1을 뺍니다.
    flag = 1
      
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0<=nx<=7 and 0 <= ny <= 7 and arr[nx][ny] == 0:
      q.append((nx,ny))
      arr[nx][ny] = arr[x][y] + 1

if flag == 0:
  print(-1)
