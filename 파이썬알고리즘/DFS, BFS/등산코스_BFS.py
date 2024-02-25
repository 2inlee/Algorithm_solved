from collections import deque

def BFS():
    q = deque()
    q.append((0, 0))  # 시작점 (0, 0)을 큐에 추가
    cnt = 0  # 경로의 수
    while q:
        x, y = q.popleft()  # 큐에서 하나의 원소를 꺼냄
        if x == n-1 and y == n-1:  # 목적지에 도달했을 경우
            cnt += 1  # 경로 카운트 증가
            continue
        for i in range(4):  # 상하좌우 탐색
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:  # 이동 가능 조건 확인
                q.append((nx, ny))  # 큐에 추가
    return cnt

if __name__ == "__main__":
    n = int(input())  # 지도의 크기 입력
    arr = [list(map(int, input().split())) for _ in range(n)]  # 지도 정보 입력

    dx = [0, 0, -1, 1]  # x 이동 방향 (상하)
    dy = [1, -1, 0, 0]  # y 이동 방향 (좌우)
  
    print(BFS())  # BFS 실행 및 결과 출력
