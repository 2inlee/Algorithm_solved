n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

for i in range(len(a)):
  if m == a[i]:
    print(i+1)
    break