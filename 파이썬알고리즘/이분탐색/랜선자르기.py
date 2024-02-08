k,n = map(int, input().split())
res = 0
Line = []
max_n = 0

def Count(len):
  cnt = 0
  for x in Line:
    cnt += (x // len)
  return cnt

for i in range(k):
  tmp = int(input())
  Line.append(tmp)
  max_n = max(max_n, tmp)

lt = 1
rt = max_n
while lt <= rt:
  mid = (lt + rt) // 2
  if Count(mid) >= n:
    res = mid
    lt = mid + 1
  else:
    rt = mid - 1

print(res)