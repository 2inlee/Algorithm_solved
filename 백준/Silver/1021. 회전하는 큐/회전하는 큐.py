# 1번 기능 > popleft()
# 2번 기능 > que.append(que.pop(0)) que.rotate(-1)
# 3번 기능 > que.appendleft(que.pop(len(que))) que.roate(1)

from collections import deque

n , m = map(int, input().split())

queue = deque([i for i in range(1, n+1)])

arr = list(map(int, input().split()))

cnt = 0

for i in arr:
    while True:
        if queue[0] == i:
            queue.popleft()
            break
        else:
            if queue.index(i) <= len(queue) // 2:
                queue.rotate(-1)
                cnt += 1
            else:
                queue.rotate(1)
                cnt += 1
print(cnt)