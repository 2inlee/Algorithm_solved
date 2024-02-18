# 환자가 접수한 순서대로 목록에서 제일 앞에 있는 환자목록을 꺼낸다.
# 나머지 대기 모골겡서 꺼낸 환자 보다 위험도가 높은 환자가 존재하면 대기목록 제일 뒤로 다시 넣는다.
# 그렇지 않으면 꺼낸 환자를 진료한다.

from collections import deque

n,m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q = deque(Q)
cnt = 0
while True:
  cur = Q.popleft()
  if any(cur[1] < x[1] for x in Q):
    Q.append(cur)
  else:
    cnt += 1
    if cur[0] == m:
      break
print(cnt)
