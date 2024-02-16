n, c = map(int, input().split())
line = []

for _ in range(n):
  line.append(int(input()))
line.sort()

def Count(len):
  cnt = 1
  ep = line[0]
  for i in range(1, n):
    if line[i] - ep >= len:
      cnt += 1
      ep = line[i]
  return cnt

lt = 1
rt = line[n-1]

while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) >= c:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1

print(res)