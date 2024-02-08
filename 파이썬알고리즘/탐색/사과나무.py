n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

sum = 0
lt = rt = n//2
for i in range(n):
  for j in range(lt, rt+1):
    sum += a[i][j]
  if i < n//2:
    lt -= 1
    rt += 1
  else:
    lt += 1
    rt -= 1
print(sum)
