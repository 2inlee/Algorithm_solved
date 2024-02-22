# 고려해야 되는 값이 정사각형의 넓이와 무게이며, 높이 = score라고 생각하고 접근
# 고려해야 되는 값이 여러개일경우 하나를 기준으로 먼저 정렬 후 다른 값만 비교해가면서 dp로 누적해서 풀자

n=int(input())
bricks = []
for i in range(n):
  a, b, c = map(int, input().split())
  bricks.append((a, b, c))
bricks.sort(reverse=True)
dy=[0]*n
dy[0]=bricks[0][1]
res=bricks[0][1]

for i in range(1, n):
  max_h = 0
  for j in range(i-1, -1, -1):
    if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
      max_h = dy[j]
  dy[i] = max_h + bricks[i][1]
  res = max(res, dy[i])

print(res)