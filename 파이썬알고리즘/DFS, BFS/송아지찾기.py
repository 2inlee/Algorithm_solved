from collections import deque

def bfs(s, e):
    visited = set()  # 방문한 위치를 기록할 집합
    queue = deque([(s, 0)])  # 큐 초기화, (현재 위치, 점프 횟수)
    while queue:
        current, jumps = queue.popleft()
        if current == e:
            return jumps
        for next_step in (current + 1, current - 1, current + 5):  # 가능한 모든 이동
            if next_step not in visited:
                visited.add(next_step)
                queue.append((next_step, jumps + 1))

s, e = map(int, input().split())
print(bfs(s,e))
