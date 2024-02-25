def DFS(x, y, count):
  global answer, n, dx, dy, maze
  if x == n-1 and y == n-1:  # 도착점에 도달했다면
    answer = min(answer, count)
    return
    
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < n and 0 <= ny < n and maze[nx][ny] == 0:
      maze[nx][ny] = 1  # 방문 처리
      DFS(nx, ny, count+1)
      maze[nx][ny] = 0  # 방문 해제

if __name__ == "__main__":
  n = 7  # 격자판 크기
  answer = float('inf')  # 최단 거리를 저장할 변수, 무한대로 초기화
  maze = [[0]*n for _ in range(n)]  # 7x7 격자판 초기화
  dx = [0, 0, -1, 1]
  dy = [1, -1, 0, 0]

  for i in range(n):
    maze[i] = list(map(int, input().split()))

  maze[0][0] = 1  # 시작 지점 방문 처리
  DFS(0, 0, 1)  # 출발점 포함하여 카운트 시작

  # 결과 출력
  print(answer - 1 if answer != float('inf') else -1)  # 도착하지 못했다면 -1 반환
