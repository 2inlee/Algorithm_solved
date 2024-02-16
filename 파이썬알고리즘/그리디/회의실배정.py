n = int(input())
meeting = []
for i in range(n):
  s, e = map(int, input().split())
  meeting.append((s, e))
  meeting.sort(key=lambda x: (x[1], x[0])) #그리디 문제는 정렬이 중요한데, 어떤 것을 기준으로 정렬할 지 람다식으로 풀 수 있다.

et = 0
cnt = 0

for x, y in meeting:
  if x >= et:
    et = y
    cnt += 1
print(cnt)
