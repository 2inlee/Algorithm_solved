n = int(input())

cnt = 0

def isPrime(n):  
  i = 2
  if n == 1:
    return False
  while i * i <= n:
    if n % i == 0:
      return False
    i += 1
  return True

for i in range(1, n+1):
  if isPrime(i):
    cnt += 1

print(cnt)