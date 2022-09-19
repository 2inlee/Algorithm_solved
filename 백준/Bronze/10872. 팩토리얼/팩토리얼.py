def rec(n):
  global res
  if (n == 0):
    print(res)
    return
  res = res * n
  rec(n-1)

n = int(input())
res = 1
rec(n)