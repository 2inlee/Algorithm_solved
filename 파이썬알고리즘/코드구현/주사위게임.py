# 1. 같은 눈이 3개 -> 10000원 + (같은눈)*1000원
# 2. 같은 눈이 2개 -> 1000원 + (같은눈)*100원
# 3. 다른 눈 -> (가장 큰 눈)*100원

n = int(input())

res = 0
for i in range(n):
  a = list(map(int, input().split()))
  tmp = a[i]
  if a.count(a[i]) == 3:
    res = 10000 + a[i]*1000
  elif a.count(a[i]) == 2:
    res = 1000 + a[i]*100
  else:
    if tmp > res:
      res = tmp

print(res)