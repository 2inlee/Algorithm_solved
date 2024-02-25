from collections import deque

def solution(maps):
    n = len(maps)       # 행의 수
    m = len(maps[0])    # 열의 수

    # 방향 벡터 설정: 동, 서, 남, 북
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    # 예외 처리: 목적지 바로 앞의 두 칸이 모두 벽인 경우
    if maps[n-2][m-1] == 0 and maps[n-1][m-2] == 0:
        return -1

    # BFS를 위한 큐 초기화 및 시작 위치 설정
    queue = deque([(0, 0)])
    # 시작 위치부터 각 위치까지의 거리 저장 (시작 위치는 1로 초기화)
    maps[0][0] = 1

    # BFS 실행
    while queue:
        x, y = queue.popleft()

        # 목적지에 도착한 경우
        if x == n-1 and y == m-1:
            return maps[x][y]

        # 현재 위치에서 4가지 방향으로의 탐색 실행
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위를 벗어나지 않고, 갈 수 있는 길인 경우
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                queue.append((nx, ny))
                # 시작 위치부터 nx, ny 위치까지의 거리 업데이트
                maps[nx][ny] = maps[x][y] + 1

    # 모든 위치를 탐색했으나 목적지에 도달하지 못한 경우
    return -1
