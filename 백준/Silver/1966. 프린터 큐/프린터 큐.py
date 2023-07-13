from collections import deque
import sys

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    que = deque(list(map(int, sys.stdin.readline().split())))
    idx = deque(list(range(n)))
    count = 0
    while que:
        max_value = max(que)
        if que[0] == max_value:
            count += 1
            que.popleft()
            if idx.popleft() == m:
                print(count)
        else:
            que.append(que.popleft())
            idx.append(idx.popleft())