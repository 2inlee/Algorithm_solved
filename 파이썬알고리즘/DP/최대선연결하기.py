n = int(input())
a = list(map(int, input().split()))
dy = [0] * (n+1)
a.insert(0,0)
dy[1] = 1
res = 0
for i in range(2, n+1):
  max = 0
  for j in range(i-1, 0, -1):
    if a[j]<a[i] and dy[j]>max:
      max=dy[j]
  dy[i]=max+1
  if dy[i]>res:
    res=dy[i]

print(res)