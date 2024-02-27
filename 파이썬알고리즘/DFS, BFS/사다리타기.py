from collections import deque

def find_exit_ladder(a):
    # 좌, 우 방향 설정
    dx = [0, 0]
    dy = [-1, 1]

    # 시작 위치 찾기
    start = 0
    for i in range(10):
        if a[9][i] == 2:
            start = i

    # BFS 시작
    dq = deque([(9, start)])
    while dq:
        x, y = dq.popleft()

        # 최상단에 도달한 경우
        if x == 0:
            return y  # 최종 위치 반환

        a[x][y] = 0  # 방문 표시

        # 좌우 탐색 후 위로 이동
        for i in range(2):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < 10 and 0 <= ny < 10 and a[nx][ny] == 1:
                dq.append((nx, ny))
                break
        else:  # 좌우 이동이 없는 경우, 위로 이동
            dq.append((x-1, y))

if __name__ == "__main__":
    # 10x10 배열 입력 받기
    a = [list(map(int, input().split())) for _ in range(10)]
    
    # 최종 결과 출력
    print(find_exit_ladder(a))
